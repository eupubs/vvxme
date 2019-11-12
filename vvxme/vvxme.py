#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def validate_getConfig_body(rdata):
    """
    Method validate getConfig's body for right structure and not empty, rdata = { "data": [...] }
    INPUTS: rdata as dict(body)
    OUTPUT: Returns boolean, True when structure is valid, False when structure is invalid.
    """     
    if isinstance(rdata, dict) is False:
        logging.error("<JSON Body Error: boby passed is not a dictionary...>")
        return False
    elif "data" not in rdata:
        logging.error("<JSON Body Error: 'data' key is missing...>")
        return False
    elif isinstance(rdata["data"], list) is False:
        logging.error("<JSON Body Error: 'data' value is not a list...>")
        return False
    elif not rdata["data"]:
        logging.error("<JSON Body Error: 'data' is empty...>")
        return False
    else:
        return True


# In[ ]:


def validate_setConfig_body(rdata):
    """
    Method validate setConfig's body for right structure and not empty, rdata = { "data": {...} }
    INPUTS: rdata as dict(body)
    OUTPUT: Returns boolean, True when structure is valid, False when structure is invalid.
    """     
    if isinstance(rdata, dict) is False:
        logging.error("<JSON Body Error: boby passed is not a dictionary...>")
        return False
    elif "data" not in rdata:
        logging.error("<JSON Body Error: 'data' key is missing...>")
        return False
    elif isinstance(rdata["data"], dict) is False:
        logging.error("<JSON Body Error: 'data' value is not a dictionary...>")
        return False
    elif not rdata["data"]:
        logging.error("<JSON Body Error: 'data' is empty...>")
        return False
    else:
        return True


# In[ ]:


def getCallConnectionInfo(call, dest, pdmssp=False):
    """
    Method expects call dict input from output from getCallStatusV2() method. Extract call info - RemotePartyNumber, 
        CallState, CallHandle and LineID, from call if dest matches.
    INPUTS: call as dict(body), dest as string
    OUTPUT: Returns response body as dict when dest match successful, None when match unsuccessful.
    """     
    body_dict = {}
    
    if not pdmssp:
        for i in range(len(call["data"])):
            # Removes 'sip:' from RemotePartyNumber if present.
            body_dict["RemotePartyNumber"] = re.sub( "^sip:", "", call["data"][i]["RemotePartyNumber"] )
            if body_dict["RemotePartyNumber"] == dest:
                body_dict["CallState"] = call["data"][i]["CallState"]
                body_dict["CallHandle"] = call["data"][i]["CallHandle"]
                body_dict["LineID"] = call["data"][i]["LineID"]

    elif pdmssp:
        for i in range(len(call["data"]["body"]["data"])):
            # Removes 'sip:' from RemotePartyNumber if present.
            body_dict["RemotePartyNumber"] = re.sub( "^sip:", "", call["data"]["body"]["data"][i]["RemotePartyNumber"] )
            if body_dict["RemotePartyNumber"] == dest:
                body_dict["CallState"] = call["data"]["body"]["data"][i]["CallState"]
                body_dict["CallHandle"] = call["data"]["body"]["data"][i]["CallHandle"]
                body_dict["LineID"] = call["data"]["body"]["data"][i]["LineID"]
    
    return body_dict


# In[ ]:


import datetime
import json
import logging
import re
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class vvx():

    """
    Class for VVX based on UCS 6.1.0 REST APIs.
    INPUTS for instance creation:
        - ipaddr = IP address of phone, auth = username and password in tuple
        OR
        - pdmssp = True, macaddr = mac address of phone, pdmssp_credentials = { 'client_id', 'client_secret', 'org_id'}
    Attributes:
        .ipaddr
        .phone_credentials
        .use_https
        .verify_secure
        .model
        .firmware
        .macaddress
        .lines
        .linescount
        .linestates
    Additional PDMS-SP Attributes:
        .client_id
        .client_secret
        .org_id
        .token
        .device_id
        .obi_number
    
    Methods:
       .pdmssp_getToken() - calls PDMS-SP to generate & retrieve authorization access_token
       .pdmssp_getDeviceId() - calls PDMS-SP to retrieve DeviceID of device on PDMS-SP
       .getDeviceInfoV2() - calls "/api/v2/mgmt/device/info"
       .getNetwork() - calls "/api/v1/mgmt/network/info"
       .getLineInfoV2() - calls "/api/v2/mgmt/lineInfo"
       .getCallStatusV2() - calls "/api/v2/webCallControl/callStatus"
       .getRunningConfig() - calls "/api/v1/mgmt/device/runningConfig"
       .getDeviceStats() - calls "/api/v1/mgmt/device/stats"
       .getNetworkStats() - calls "/api/v1/mgmt/network/stats"
       .getSessionStats() - calls "/api/v1/mgmt/media/sessionStats"
       .getCallLogs() - calls "/api/v1/mgmt/callLogs"
       .getConfig() - calls "/api/v1/mgmt/config/get"
       .setConfig() - calls "/api/v1/mgmt/config/set"
       .callDial() - "/api/v1/callctrl/dial"
       .callEnd() - "/api/v1/callctrl/endCall"
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes
       .callMute() - "/api/v1/callctrl/mute"
       .sendDTMF() - "/api/v1/callctrl/sendDTMF"
       .callAnswer() - "/api/v1/callctrl/answerCall"
       .callIgnore() - "/api/v1/callctrl/ignoreCall"
       .callReject() - "/api/v1/callctrl/rejectCall"
       .callHold() - "/api/v1/callctrl/holdCall"
       .callResume() - "/api/v1/callctrl/resumeCall"
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
       .simulateKeyEvent() - calls "/api/v1/mgmt/simulateKeyEvent"
       .simulateTextInput() - calls "/api/v1/mgmt/simulateTextInput"
       .safeRestart() - calls "/api/v1/mgmt/safeRestart"
       .safeReboot() - calls "/api/v1/mgmt/safeReboot"
       .factoryReset() - calls "/api/v1/mgmt/factoryReset"
       .updateConfig() - calls "/api/v1/mgmt/updateConfiguration"
       .resetConfig() - calls "/api/v1/mgmt/configReset"
    """

    
    _qpaths_dict={
<<<<<<< Updated upstream
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            "sipStatus" : "/api/v1/webCallControl/sipStatus",
            "network" : "/api/v1/mgmt/network/info", 
            "deviceinfov2" : "/api/v2/mgmt/device/info",
            "lineinfov2" : "/api/v2/mgmt/lineInfo",
            "runningConfig" : "/api/v1/mgmt/device/runningConfig",
            "getconfig" : "/api/v1/mgmt/config/get",
            "setconfig" : "/api/v1/mgmt/config/set",
            "simulateTextInput" : "/api/v1/mgmt/simulateTextInput",
            "simulateKeyEvent" : "/api/v1/mgmt/simulateKeyEvent",
            "callstatusv2" : "/api/v2/webCallControl/callStatus",
            "calldial" : "/api/v1/callctrl/dial",
            "callend" : "/api/v1/callctrl/endCall",
            "callmute" : "/api/v1/callctrl/mute",
            "sendDTMF" : "/api/v1/callctrl/sendDTMF",
            "callresume" : "/api/v1/callctrl/resumeCall",
            "callanswer" : "/api/v1/callctrl/answerCall",
            "callignore" : "/api/v1/callctrl/ignoreCall",
            "callreject" : "/api/v1/callctrl/rejectCall",
            "callhold" : "/api/v1/callctrl/holdCall",
            "callresume" : "/api/v1/callctrl/resumeCall",
            "devicestats" : "/api/v1/mgmt/device/stats",
            "networkstats" : "/api/v1/mgmt/network/stats",
            "sessionStats" : "/api/v1/mgmt/media/sessionStats",
            "callLogs" : "/api/v1/mgmt/callLogs",
            "callLogs_missed" : "/api/v1/mgmt/callLogs/missed",
            "callLogs_received" : "/api/v1/mgmt/callLogs/received",
            "callLogs_placed" : "/api/v1/mgmt/callLogs/placed",
            "safeRestart" : "/api/v1/mgmt/safeRestart",
            "safeReboot" : "/api/v1/mgmt/safeReboot",
            "factoryReset" : "/api/v1/mgmt/factoryReset",
            "updateConfig" : "/api/v1/mgmt/updateConfiguration",
            "resetConfig" : "/api/v1/mgmt/configReset",
            "resetConfig_cloud" : "/api/v1/mgmt/configReset/cloud",
            "resetConfig_local" : "/api/v1/mgmt/configReset/local",
            "resetConfig_web" : "/api/v1/mgmt/configReset/web",
            "resetConfig_device" : "/api/v1/mgmt/configReset/device"
    }
    
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
    _pdmssp_baseurl="https://pcs-api-na.obitalk.com"
    _access_token_path = "/api/v2/oauth/client_credential/accesstoken"
    _domain_path = "/api/v2/domain/"
    
>>>>>>> Stashed changes
    _valid_versions = ("6.0.0", "6.1.0",)
    
=======
    _pdmssp_baseurl="https://pcs-api-na.obitalk.com"
    _access_token_path = "/api/v2/oauth/client_credential/accesstoken"
    _domain_path = "/api/v2/domain/"
    
    _valid_versions = ("6.0.0", "6.1.0",)
    
>>>>>>> Stashed changes
    def __init__(self, ipaddr="", phone_credentials=(), use_https=True, verify_secure=False, 
                                         pdmssp=False, pdmssp_credentials={}, macaddr="", loglevel="INFO"):
        
        logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        level = logging.getLevelName(loglevel)
        logger = logging.getLogger()
        logger.setLevel(level)
        
        # initiates requests.Session()
        vvx_adapter = requests.adapters.HTTPAdapter(max_retries=3)
        self.__session = requests.Session()
        
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        if self.use_https:
            self.__session.mount(f"https://{self.ipaddr}", vvx_adapter)
        else:
            self.__session.mount(f"http://{self.ipaddr}", vvx_adapter)

        # Extracts attributes' values for model, firmware, macaddress and _swVer
        dev = self.getDeviceInfoV2()
        if dev != None:
            self.model = dev["data"]["ModelNumber"]
            self.firmware = dev["data"]["Firmware"]["Application"]
            self.macaddress = dev["data"]["MACAddress"]
            
            for item in self._valid_versions:
                if self.firmware.startswith(item):
                    self._swVer = item
                else:
                    self._swVer = None
        else:
=======
        if not pdmssp:
            # direct phone query scenario
            
            self.ipaddr = ipaddr
            self.phone_credentials = phone_credentials
            self.use_https = use_https
            self.verify_secure = verify_secure
            
            self.macaddress = macaddr
>>>>>>> Stashed changes
            self.model = None
            self.firmware = None
            self._swVer = None
            self.lines = {}
            self.linestates = {}
            self.linescount = None

            if self.use_https:
                # apply HTTPAdapter settings to url
                self.__session.mount(f"https://{self.ipaddr}", vvx_adapter)
            else:
                # apply HTTPAdapter settings to url
                self.__session.mount(f"http://{self.ipaddr}", vvx_adapter)

            try:
                # Extracts attributes' values for model, firmware, macaddress and _swVer
                dev = self.getDeviceInfoV2()
                if dev:
                    self.model = dev["data"]["ModelNumber"]
                    self.firmware = dev["data"]["Firmware"]["Application"]
                    self.macaddress = dev["data"]["MACAddress"]

                    for item in self._valid_versions:
                        if self.firmware.startswith(item):
                            self._swVer = item

                # *** setConfig/getConfig not working on PDMSSP, skipping altogther ***                
                # Extracts attribute's value for baseprofile
                #dev = self.getConfig({ "data" : [ "device.baseProfile" ] })
                #if dev != None:
                #    self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
                #else:
                #    self.baseprofile = None

                # Extracts information about lines, count and state.
                dev = self.getLineInfoV2()
                if dev:
                    self.linescount = len(dev["data"])
                    for i in range(self.linescount):
                        if dev["data"][i]["CallServers"]:
                            p = i
                            self.lines[i+1] = dev["data"][i]["Label"]
                            self.linestates[dev["data"][i]["Label"]] = dev["data"][i]["RegistrationStatus"]
                        else:
                            self.lines[i+1] = dev["data"][p]["Label"]
                            self.linestates[dev["data"][p]["Label"]] = dev["data"][i]["RegistrationStatus"]

            except Exception:
                pass
                            
            logging.debug(f"Device ip-address: {self.ipaddr}")
            logging.debug(f"Device model: {self.model}")
            logging.debug(f"Device firmware: {self.firmware}")
            logging.debug(f"Device mac address: {self.macaddress}")
            # *** setConfig/getConfig not working on PDMSSP***
            #logging.debug(f"Device base profile: {self.baseprofile}")
            logging.debug(f"Device lines: {self.lines}")
            logging.debug(f"Device lines count: {self.linescount}")
            logging.debug(f"Device lines states: {self.linestates}")

        
<<<<<<< Updated upstream
        # Extracts attribute's value for baseprofile
        dev = self.getConfig({ "data" : [ "device.baseProfile" ] })
        if dev != None:
            self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
        else:
            self.baseprofile = None
=======
        if not pdmssp:
            # direct phone query scenario
            
            self.ipaddr = ipaddr
            self.phone_credentials = phone_credentials
            self.use_https = use_https
            self.verify_secure = verify_secure

            if self.use_https:
                # apply HTTPAdapter settings to url
                self.__session.mount(f"https://{self.ipaddr}", vvx_adapter)
            else:
                # apply HTTPAdapter settings to url
                self.__session.mount(f"http://{self.ipaddr}", vvx_adapter)

            # Extracts attributes' values for model, firmware, macaddress and _swVer
            dev = self.getDeviceInfoV2()
            if dev != None:
                self.model = dev["data"]["ModelNumber"]
                self.firmware = dev["data"]["Firmware"]["Application"]
                self.macaddress = dev["data"]["MACAddress"]

                for item in self._valid_versions:
                    if self.firmware.startswith(item):
                        self._swVer = item
                    else:
                        self._swVer = None
            else:
                self.model = None
                self.firmware = None
                self.macaddress = None            

            # *** setConfig/getConfig not working on PDMSSP, skipping altogther ***                
            # Extracts attribute's value for baseprofile
            #dev = self.getConfig({ "data" : [ "device.baseProfile" ] })
            #if dev != None:
            #    self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
            #else:
            #    self.baseprofile = None

            # Extracts information about lines, count and state.
            self.lines = {}
            self.linestates = {}
            dev = self.getLineInfoV2()
            if dev != None:
                self.linescount = len(dev["data"])
                for i in range(self.linescount):
                    self.lines[i+1] = dev["data"][i]["Label"]
                    self.linestates[dev["data"][i]["Label"]] = dev["data"][i]["RegistrationStatus"]
            else:
                self.linescount = None
>>>>>>> Stashed changes
        
            logging.debug(f"Device ip-address: {self.ipaddr}")
            logging.debug(f"Device model: {self.model}")
            logging.debug(f"Device firmware: {self.firmware}")
            logging.debug(f"Device mac address: {self.macaddress}")
            # *** setConfig/getConfig not working on PDMSSP***
            #logging.debug(f"Device base profile: {self.baseprofile}")
            logging.debug(f"Device lines: {self.lines}")
            logging.debug(f"Device lines count: {self.linescount}")
            logging.debug(f"Device lines states: {self.linestates}")

        
        elif pdmssp:
            # pdmssp query scenario
            
            # apply HTTPAdapter settings to url
            self.__session.mount(self._pdmssp_baseurl, vvx_adapter)
            
            self.macaddress = macaddr
            self.client_id = pdmssp_credentials["client_id"]
            self.client_secret = pdmssp_credentials["client_secret"]
            self.org_id = pdmssp_credentials["org_id"]
            
            # get access_token from pdmssp using Org's client_id & client_secret.
            dev = self.pdmssp_getToken()
            if dev != None:
                self.token = dev["access_token"]
                
                # get device_id from pdmssp using access_token, org_id & macaddr
                dev = self.pdmssp_getDeviceId()
                if dev != None:
                    self.device_id = dev["data"][0]["id"]
                    self.obi_number = dev["data"][0]["obiNumber"]
                               
                    dev = self.getDeviceInfoV2(True)
                    if dev != None:
                        self.model = dev["data"]["body"]["data"]["ModelNumber"]
                        self.firmware = dev["data"]["body"]["data"]["Firmware"]["Application"]
                        #self.macaddress = dev["data"]["body"]["data"]["MACAddress"]
                        
                        for item in self._valid_versions:
                            if self.firmware.startswith(item):
                                self._swVer = item
                            else:
                                self._swVer = None
                    else:
                        self.model = None
                        self.firmware = None
                        #self.macaddress = None  
                    
                    # *** setConfig/getConfig not working on PDMSSP, skipping altogther ***
                    # Extracts attribute's value for baseprofile
                    #dev = self.getConfig({ "data" : [ "device.baseProfile" ] }, True)
                    #if dev != None:
                    #    self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
                    #else:
                    #    self.baseprofile = None
                   
                    # Extracts information about lines, count and state.
                    self.lines = {}
                    self.linestates = {}
                    dev = self.getLineInfoV2(True)
                    if dev != None:
                        self.linescount = len(dev["data"]["body"]["data"])
                        for i in range(self.linescount):
                            self.lines[i+1] = dev["data"]["body"]["data"][i]["Label"]
                            self.linestates[dev["data"]["body"]["data"][i]["Label"]] = dev["data"]["body"]["data"][i]["RegistrationStatus"]
                    else:
                        self.linescount = None
                
                    logging.debug(f"Device id of device on PDMS-SP: {self.device_id}")
                    logging.debug(f"Device obi-number of device on PDMS-SP: {self.obi_number}")
                    logging.debug(f"Device model on PDMS-SP: {self.model}")
                    logging.debug(f"Device firmware on PDMS-SP: {self.firmware}")
                    logging.debug(f"Device mac address on PDMS-SP: {self.macaddress}")
                    # *** setConfig/getConfig not working on PDMSSP***
                    #logging.debug(f"Device base profile: {self.baseprofile}")
                    logging.debug(f"Device lines: {self.lines}")
                    logging.debug(f"Device lines count: {self.linescount}")
                    logging.debug(f"Device lines states: {self.linestates}")
=======
        elif pdmssp:            
            # pdmssp query scenario
        
            self.ipaddr = ipaddr
            self.phone_credentials = phone_credentials
            self.use_https = use_https
            self.verify_secure = verify_secure
            
            self.macaddress = macaddr
            self.model = None
            self.firmware = None
            self._swVer = None
            self.lines = {}
            self.linestates = {}
            self.linescount = None

            self.token = None
            self.device_id = None
            self.obi_number = None
            self.client_id = pdmssp_credentials["client_id"]
            self.client_secret = pdmssp_credentials["client_secret"]
            self.org_id = pdmssp_credentials["org_id"]

            # apply HTTPAdapter settings to url
            self.__session.mount(self._pdmssp_baseurl, vvx_adapter)
            
            try:
                # get access_token from pdmssp using Org's client_id & client_secret.
                dev = self.pdmssp_getToken()
                if dev:
                    self.token = dev["access_token"]

                    # get device_id from pdmssp using access_token, org_id & macaddr
                    dev = self.pdmssp_getDeviceId()
                    if dev["data"]:
                        self.device_id = dev["data"][0]["id"]
                        self.obi_number = dev["data"][0]["obiNumber"]

                        dev = self.getDeviceInfoV2(True)
                        if dev["data"]:
                            self.model = dev["data"]["body"]["data"]["ModelNumber"]
                            self.firmware = dev["data"]["body"]["data"]["Firmware"]["Application"]

                            for item in self._valid_versions:
                                if self.firmware.startswith(item):
                                    self._swVer = item

                        # *** setConfig/getConfig not working on PDMSSP, skipping altogther ***
                        # Extracts attribute's value for baseprofile
                        #dev = self.getConfig({ "data" : [ "device.baseProfile" ] }, True)
                        #if dev != None:
                        #    self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
                        #else:
                        #    self.baseprofile = None

                        # Extracts information about lines, count and state.
                        dev = self.getLineInfoV2(True)
                        if dev["data"]:
                            self.linescount = len(dev["data"]["body"]["data"])
                            for i in range(self.linescount):
                                if dev["data"]["body"]["data"][i]["CallServers"]:
                                    p = i
                                    self.lines[i+1] = dev["data"]["body"]["data"][i]["Label"]
                                    self.linestates[dev["data"]["body"]["data"][i]["Label"]] = dev["data"]["body"]["data"][i]["RegistrationStatus"]
                                else:
                                    self.lines[i+1] = dev["data"]["body"]["data"][p]["Label"]
                                    self.linestates[dev["data"]["body"]["data"][p]["Label"]] = dev["data"]["body"]["data"][i]["RegistrationStatus"]
            
            except Exception:
                pass
            
            logging.debug(f"Device id of device on PDMS-SP: {self.device_id}")
            logging.debug(f"Device obi-number of device on PDMS-SP: {self.obi_number}")
            logging.debug(f"Device model on PDMS-SP: {self.model}")
            logging.debug(f"Device firmware on PDMS-SP: {self.firmware}")
            logging.debug(f"Device mac address on PDMS-SP: {self.macaddress}")
            # *** setConfig/getConfig not working on PDMSSP***
            #logging.debug(f"Device base profile: {self.baseprofile}")
            logging.debug(f"Device lines: {self.lines}")
            logging.debug(f"Device lines count: {self.linescount}")
            logging.debug(f"Device lines states: {self.linestates}")
>>>>>>> Stashed changes

        
    def __httpRequest(self, qpath="", rtype="GET", params={}, headers={}, rdata={}, pdmssp=False, pdmssp_url=""):
        """
        Method makes HTTP request using requests. 
        INPUTS: qpath as string (qpath is key value taken from qpaths_dict, meant for direct phone api call),
            rtype as string(supported - GET, POST), params as dict, headers as dict,
            rdata as dict, pdmssp as boolean, pdmssp_url as str
        OUTPUT: Response JSON object from requests.get() when successful, None when unsuccessful.
        """
        s = self.__session
               
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        if self.use_https:
            target_url = f"https://{self.ipaddr}{self._qpaths_dict[qpath]}"
        else:
            target_url = f"http://{self.ipaddr}{self._qpaths_dict[qpath]}"
=======
=======
>>>>>>> Stashed changes
        if not pdmssp:  
            if self.use_https:
                target_url = f"https://{self.ipaddr}{self._qpaths_dict[qpath]}"
            else:
                target_url = f"http://{self.ipaddr}{self._qpaths_dict[qpath]}"
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        
        
        try:    

            if not pdmssp:         
                if rtype == "GET":
                    r = s.get(url=target_url, auth=self.phone_credentials, verify=self.verify_secure, timeout=(3, 3))
                    r.raise_for_status()

<<<<<<< Updated upstream
<<<<<<< Updated upstream
            elif rtype == "POST":
                headers = { "Content-Type" : ctype }
                r = s.post(url=target_url, data=json.dumps(rdata), headers=headers, 
                                  auth=self.auth_credentials, verify=self.verify_secure, timeout=(3, 3))
                r.raise_for_status()
=======
=======
>>>>>>> Stashed changes
                elif rtype == "POST":
                    r = s.post(url=target_url, params=params, headers=headers, data=json.dumps(rdata),
                                   auth=self.phone_credentials, verify=self.verify_secure, timeout=(3, 3))
                    r.raise_for_status()
                
                logging.debug(f"Request -->> {target_url}, Body: {rdata}")
                logging.debug(f"Headers -->> {headers}, Pramas: {params}, Body: {rdata}, verify: {self.verify_secure}")
                logging.debug(f"Response <<-- <{r.status_code}>")
                logging.debug(f"Response <<-- {r.text}")
                
                return r
            
            elif pdmssp:
                if rtype == "GET":
                    r = s.get(url=pdmssp_url, params=params, headers=headers, data=json.dumps(rdata), 
                              verify=True, timeout=(10, 10))
                    r.raise_for_status()
                    
                elif rtype == "POST":
                    r = s.post(url=pdmssp_url, params=params, headers=headers, data=json.dumps(rdata), 
                              verify=True, timeout=(10, 10))
                    r.raise_for_status()
                
                logging.info(f"Request -->> {pdmssp_url}, Body: {rdata}")
                logging.debug(f"Headers -->> {headers}, Pramas: {params}, Body: {rdata}, verify: True")
                logging.info(f"Response <<-- <{r.status_code}>")
                logging.debug(f"Response <<-- {r.text}")
                
<<<<<<< Updated upstream
>>>>>>> Stashed changes
                return r

        except requests.exceptions.HTTPError as http_err:
            logging.error( f"HTTP Error: <{http_err}>")
<<<<<<< Updated upstream
            time.sleep(3)
=======
            time.sleep(2)
>>>>>>> Stashed changes
=======
                return r

        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP Error: <{http_err}>")
            time.sleep(2)
>>>>>>> Stashed changes
        except requests.exceptions.ConnectionError as connect_err:
            logging.error(f"Connection Error: <{connect_err}>")
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Timeout Error: <{timeout_err}>")
        except requests.exceptions.RequestException as err:
            logging.error(f"Request Error: <{err}>")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            time.sleep(3)
=======
            time.sleep(2)
>>>>>>> Stashed changes
=======
            time.sleep(2)
>>>>>>> Stashed changes

            
    def pdmssp_getToken(self):
        """
        Method calls pdmssp api, "/api/v2/oauth/client_credential/accesstoken", to retrieve authorization access_token.
        INPUTS: None
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        import base64

        pdmssp_url = ""
        pdmssp_headers = {}
        pdmssp_params = {}
        
        pdmssp_url = self._pdmssp_baseurl + self._access_token_path

        credentials = self.client_id + ":" + self.client_secret       
        encoded_bytes = base64.b64encode(credentials.encode("utf-8")) 
        encoded_str = str(encoded_bytes, "utf-8")

        pdmssp_params["grant_type"] = "client_credentials"

        pdmssp_headers["Authorization"] = f"Basic {encoded_str}"
        pdmssp_headers["Content-Type"] = "application/json"
        pdmssp_headers["Content-Length"] = "0"

        dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, headers=pdmssp_headers)
<<<<<<< Updated upstream
        if dev != None:
            return dev.json()
       

    def pdmssp_getDeviceId(self):
        """
        Method calls pdmssp api, "/api/v2/domain/{org_id}/devices", to retrieve device info such as device_id, obi_number, etc.
        INPUTS: None
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        pdmssp_url = ""
        pdmssp_headers = {}
        pdmssp_params = {}
        
        resource_path = self._domain_path + self.org_id + "/devices" 
        pdmssp_url = self._pdmssp_baseurl + resource_path

        pdmssp_params["macAddress"] = self.macaddress

        pdmssp_headers["Authorization"] = f"Bearer {self.token}"
        pdmssp_headers["Content-Type"] = "application/json"
        pdmssp_headers["Content-Length"] = "0"
        
        dev = self.__httpRequest(rtype="GET", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, headers=pdmssp_headers)
        if dev != None:
            return dev.json()
 

    def getDeviceInfoV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "deviceinfov2" : "/api/v2/mgmt/device/info", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            #logging.debug("getDeviceInfoV2 Method <GET>")
            dev = self.__httpRequest(qpath="deviceinfov2")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["deviceinfov2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
            
            
    def getNetwork(self, pdmssp=False):
        """
        Method calls ucs api, GET "network" : "/api/v1/mgmt/network/info", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            #logging.debug("getNetwork Method <GET>")
            dev = self.__httpRequest(qpath="network")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["network"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
            

    def getLineInfoV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "lineinfov2" : "/api/v2/mgmt/lineInfo", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            dev = self.__httpRequest(qpath="lineinfov2")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["lineinfov2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()


    def getCallStatusV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "callstatusv2" : "/api/v2/webCallControl/callStatus", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp: 
            dev = self.__httpRequest(qpath="callstatusv2")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["callstatusv2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()


    def getRunningConfig(self, pdmssp=False):
        """
        Method calls ucs api, GET "runningConfig" : "/api/v1/mgmt/device/runningConfig", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp: 
            dev = self.__httpRequest(qpath="runningConfig")
=======
        if dev != None:
            return dev.json()
       

    def pdmssp_getDeviceId(self):
        """
        Method calls pdmssp api, "/api/v2/domain/{org_id}/devices", to retrieve device info such as device_id, obi_number, etc.
        INPUTS: None
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        pdmssp_url = ""
        pdmssp_headers = {}
        pdmssp_params = {}
        
        resource_path = self._domain_path + self.org_id + "/devices" 
        pdmssp_url = self._pdmssp_baseurl + resource_path

        pdmssp_params["macAddress"] = self.macaddress

        pdmssp_headers["Authorization"] = f"Bearer {self.token}"
        pdmssp_headers["Content-Type"] = "application/json"
        pdmssp_headers["Content-Length"] = "0"
        
        dev = self.__httpRequest(rtype="GET", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, headers=pdmssp_headers)
        if dev != None:
            return dev.json()
 

    def getDeviceInfoV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "deviceinfov2" : "/api/v2/mgmt/device/info", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            #logging.debug("getDeviceInfoV2 Method <GET>")
            dev = self.__httpRequest(qpath="deviceinfov2")
>>>>>>> Stashed changes
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
<<<<<<< Updated upstream
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["runningConfig"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
           

    def getDeviceStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "devicestats" : "/api/v1/mgmt/device/stats", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:       
            dev = self.__httpRequest(qpath="devicestats")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["devicestats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()


    def getNetworkStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "networkstats" : "/api/v1/mgmt/network/stats", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:    
            dev = self.__httpRequest(qpath="networkstats")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["networkstats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
          

    def getSessionStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "sessionStats" : "/api/v1/mgmt/media/sessionStats", either to phone or pdmssp, determined by pdmssp
=======
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["deviceinfov2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
            
            
    def getNetwork(self, pdmssp=False):
        """
        Method calls ucs api, GET "network" : "/api/v1/mgmt/network/info", either to phone or pdmssp, determined by pdmssp
>>>>>>> Stashed changes
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
<<<<<<< Updated upstream
            dev = self.__httpRequest(qpath="sessionStats")
=======
            #logging.debug("getNetwork Method <GET>")
            dev = self.__httpRequest(qpath="network")
>>>>>>> Stashed changes
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
<<<<<<< Updated upstream
            pdmssp_body["apiurl"] = self._qpaths_dict["sessionStats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()


    def getCallLogs(self, logtype="all", pdmssp=False):
        """
        Method calls ucs api, GET "callLogs" : "/api/v1/mgmt/callLogs", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
                logtype as str. Valid strings are "all", "missed", "received", "placed".
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:    
            if logtype == "missed":
                dev = self.__httpRequest(qpath="callLogs_missed")
            elif logtype == "received":
                dev = self.__httpRequest(qpath="callLogs_received")
            elif logtype == "placed":
                dev = self.__httpRequest(qpath="callLogs_placed")
            elif logtype == "all":
                dev = self.__httpRequest(qpath="callLogs")
            else:
                return logging.error(f"<Invalid input [logtype]: '{logtype}'>")

            if dev != None:
                return dev.json()        
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            
            if logtype == "missed":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_missed"][4:]
            elif logtype == "received":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_received"][4:]
            elif logtype == "placed":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_placed"][4:]
            elif logtype == "all":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs"][4:]
            else:
                return logging.error(f"<Invalid input [logtype]: '{logtype}'>")
=======
            pdmssp_body["apiurl"] = self._qpaths_dict["network"][4:]
>>>>>>> Stashed changes
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
<<<<<<< Updated upstream
                return dev.json()        
            

    def safeRestart(self, pdmssp=False):
        """
        Method calls ucs api, POST "safeRestart" : "/api/v1/mgmt/safeRestart", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="safeRestart", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["safeRestart"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
            
 
    def safeReboot(self, pdmssp=False):
        """
<<<<<<< Updated upstream
        dev = self.__httpRequest("sessionStats")
        if dev != None:
            return dev.json()
=======
                return dev.json()
            

    def getLineInfoV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "lineinfov2" : "/api/v2/mgmt/lineInfo", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            dev = self.__httpRequest(qpath="lineinfov2")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["lineinfov2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
>>>>>>> Stashed changes

    def getCallLogs(self, logtype="all"):
        """
        Method calls internal httpRequest to GET "callLogs" : "/api/v1/mgmt/callLogs".
        INPUTS: logtype as str. Valid strings are "all", "missed", "received", "placed".
        OUTPUT: Returns response body as dict.
        """        
        if logtype == "missed":
            dev = self.__httpRequest("callLogs_missed")
        elif logtype == "received":
            dev = self.__httpRequest("callLogs_received")
        elif logtype == "placed":
            dev = self.__httpRequest("callLogs_placed")
        elif logtype == "all":
            dev = self.__httpRequest("callLogs")
        else:
            return logging.error(f"<Invalid input [logtype]: '{logtype}'>")
            
        if dev != None:
            return dev.json()        

<<<<<<< Updated upstream
        
    def safeRestart(self):
        """
        Method calls internal httpRequest to POST "safeRestart" : "/api/v1/mgmt/safeRestart".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest(qpath="safeRestart", rtype="POST")
        if dev != None:
            return dev.json()

        
    def safeReboot(self):
        """
        Method calls internal httpRequest to POST "safeReboot" : "/api/v1/mgmt/safeReboot".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest(qpath="safeReboot", rtype="POST")
        if dev != None:
            return dev.json()

        
    def factoryReset(self):
        """
        Method calls internal httpRequest to POST "factoryReset" : "/api/v1/mgmt/factoryReset".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest(qpath="factoryReset", rtype="POST")
        if dev != None:
            return dev.json()


    def updateConfig(self):
        """
        Method calls internal httpRequest to POST "updateConfig" : "/api/v1/mgmt/updateConfiguration".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest(qpath="updateConfig", rtype="POST")
        if dev != None:
            return dev.json()

    
    def resetConfig(self, configtype="all"):
        """
        Method calls internal httpRequest to POST "resetConfig" : "/api/v1/mgmt/configReset".
        INPUTS: configtype as str. Valid strings are "all", "cloud", "local", "web", "device".
        OUTPUT: Returns response body as dict.
        """        
        if configtype == "cloud":
            dev = self.__httpRequest(qpath="resetConfig_cloud", rtype="POST")
        elif configtype == "local":
            dev = self.__httpRequest(qpath="resetConfig_local", rtype="POST")
        elif configtype == "web":
            dev = self.__httpRequest(qpath="resetConfig_web", rtype="POST")
        elif configtype == "device":
            dev = self.__httpRequest(qpath="resetConfig_device", rtype="POST")
        elif configtype == "all":
            dev = self.__httpRequest(qpath="resetConfig", rtype="POST")
        else:
            return logging.error(f"<Invalid input [configtype]: '{configtype}'>")
            
        if dev != None:
            return dev.json()        
    
=======
        Method calls ucs api, POST "safeReboot" : "/api/v1/mgmt/safeReboot", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:   
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="safeReboot", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
=======
    def getCallStatusV2(self, pdmssp=False):
        """
        Method calls ucs api, GET "callstatusv2" : "/api/v2/webCallControl/callStatus", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp: 
            dev = self.__httpRequest(qpath="callstatusv2")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["callstatusv2"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()


    def getRunningConfig(self, pdmssp=False):
        """
        Method calls ucs api, GET "runningConfig" : "/api/v1/mgmt/device/runningConfig", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp: 
            dev = self.__httpRequest(qpath="runningConfig")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["runningConfig"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
           

    def getDeviceStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "devicestats" : "/api/v1/mgmt/device/stats", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:       
            dev = self.__httpRequest(qpath="devicestats")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["devicestats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()


    def getNetworkStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "networkstats" : "/api/v1/mgmt/network/stats", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:    
            dev = self.__httpRequest(qpath="networkstats")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["networkstats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()
          

    def getSessionStats(self, pdmssp=False):
        """
        Method calls ucs api, GET "sessionStats" : "/api/v1/mgmt/media/sessionStats", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            dev = self.__httpRequest(qpath="sessionStats")
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            pdmssp_body["apiurl"] = self._qpaths_dict["sessionStats"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()


    def getCallLogs(self, logtype="all", pdmssp=False):
        """
        Method calls ucs api, GET "callLogs" : "/api/v1/mgmt/callLogs", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
                logtype as str. Valid strings are "all", "missed", "received", "placed".
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:    
            if logtype == "missed":
                dev = self.__httpRequest(qpath="callLogs_missed")
            elif logtype == "received":
                dev = self.__httpRequest(qpath="callLogs_received")
            elif logtype == "placed":
                dev = self.__httpRequest(qpath="callLogs_placed")
            elif logtype == "all":
                dev = self.__httpRequest(qpath="callLogs")
            else:
                return logging.error(f"<Invalid input [logtype]: '{logtype}'>")

            if dev != None:
                return dev.json()        
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "GET"
            
            if logtype == "missed":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_missed"][4:]
            elif logtype == "received":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_received"][4:]
            elif logtype == "placed":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs_placed"][4:]
            elif logtype == "all":
                pdmssp_body["apiurl"] = self._qpaths_dict["callLogs"][4:]
            else:
                return logging.error(f"<Invalid input [logtype]: '{logtype}'>")
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)
            if dev != None:
                return dev.json()        
            

    def safeRestart(self, pdmssp=False):
        """
        Method calls ucs api, POST "safeRestart" : "/api/v1/mgmt/safeRestart", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="safeRestart", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["safeRestart"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
            
 
    def safeReboot(self, pdmssp=False):
        """
        Method calls ucs api, POST "safeReboot" : "/api/v1/mgmt/safeReboot", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:   
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="safeReboot", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["safeReboot"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()

 
    def factoryReset(self, pdmssp=False):
        """
        Method calls ucs api, POST "factoryReset" : "/api/v1/mgmt/factoryReset", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:   
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="factoryReset", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["factoryReset"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()

            
    def updateConfig(self, pdmssp=False):
        """
        Method calls ucs api, POST "updateConfig" : "/api/v1/mgmt/updateConfiguration", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="updateConfig", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["updateConfig"][4:]

            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
            
            
    def resetConfig(self, configtype="all", pdmssp=False):
        """
        Method calls ucs api, POST "resetConfig" : "/api/v1/mgmt/configReset", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
                configtype as str. Valid strings are "cloud", "local", "web", "device", "all".
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            if configtype == "cloud":
                dev = self.__httpRequest(qpath="resetConfig_cloud", rtype="POST", headers=headers)
            elif configtype == "local":
                dev = self.__httpRequest(qpath="resetConfig_local", rtype="POST", headers=headers)
            elif configtype == "web":
                dev = self.__httpRequest(qpath="resetConfig_web", rtype="POST", headers=headers)
            elif configtype == "device":
                dev = self.__httpRequest(qpath="resetConfig_device", rtype="POST", headers=headers)
            elif configtype == "all":
                dev = self.__httpRequest(qpath="resetConfig", rtype="POST", headers=headers)
            else:
                return logging.error(f"<Invalid input [configtype]: '{configtype}'>")
            
            if dev != None:
                return dev.json()        
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            
            if configtype == "cloud":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_cloud"][4:]
            elif configtype == "local":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_local"][4:]
            elif configtype == "web":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_web"][4:]
            elif configtype == "device":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_device"][4:]
            elif configtype == "all":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig"][4:]
            else:
                return logging.error(f"<Invalid input [configtype]: '{configtype}'>")
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)   
            if dev != None:
                return dev.json()
 

    def getConfig(self, rdata, pdmssp=False):
        """
        Method calls ucs api, POST "getconfig" : "/api/v1/mgmt/config/get", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean, rdata as dict(body)
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        
        res = validate_getConfig_body(rdata)
        if not res:
            return
            
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="getconfig", rtype="POST", headers=headers, rdata=rdata)
            if dev != None:
                return dev.json()

>>>>>>> Stashed changes
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
<<<<<<< Updated upstream
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["safeReboot"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
>>>>>>> Stashed changes

 
    def factoryReset(self, pdmssp=False):
        """
        Method calls ucs api, POST "factoryReset" : "/api/v1/mgmt/factoryReset", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:   
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="factoryReset", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["factoryReset"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()

            
    def updateConfig(self, pdmssp=False):
        """
        Method calls ucs api, POST "updateConfig" : "/api/v1/mgmt/updateConfiguration", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="updateConfig", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["updateConfig"][4:]

            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
            
            
    def resetConfig(self, configtype="all", pdmssp=False):
        """
        Method calls ucs api, POST "resetConfig" : "/api/v1/mgmt/configReset", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean,
                configtype as str. Valid strings are "cloud", "local", "web", "device", "all".
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            if configtype == "cloud":
                dev = self.__httpRequest(qpath="resetConfig_cloud", rtype="POST", headers=headers)
            elif configtype == "local":
                dev = self.__httpRequest(qpath="resetConfig_local", rtype="POST", headers=headers)
            elif configtype == "web":
                dev = self.__httpRequest(qpath="resetConfig_web", rtype="POST", headers=headers)
            elif configtype == "device":
                dev = self.__httpRequest(qpath="resetConfig_device", rtype="POST", headers=headers)
            elif configtype == "all":
                dev = self.__httpRequest(qpath="resetConfig", rtype="POST", headers=headers)
            else:
                return logging.error(f"<Invalid input [configtype]: '{configtype}'>")
            
            if dev != None:
                return dev.json()        
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            
            if configtype == "cloud":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_cloud"][4:]
            elif configtype == "local":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_local"][4:]
            elif configtype == "web":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_web"][4:]
            elif configtype == "device":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig_device"][4:]
            elif configtype == "all":
                pdmssp_body["apiurl"] = self._qpaths_dict["resetConfig"][4:]
            else:
                return logging.error(f"<Invalid input [configtype]: '{configtype}'>")
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)   
            if dev != None:
                return dev.json()
 

    def getConfig(self, rdata, pdmssp=False):
        """
        Method calls ucs api, POST "getconfig" : "/api/v1/mgmt/config/get", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean, rdata as dict(body)
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        
        res = validate_getConfig_body(rdata)
        if not res:
            return
            
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="getconfig", rtype="POST", headers=headers, rdata=rdata)
            if dev != None:
                return dev.json()

        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}

            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path

            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"

            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["getconfig"][4:]
            pdmssp_body["body"] = rdata

            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body) 
            if dev != None:
                return dev.json()

                
    def setConfig(self, rdata, chunk_size=20, pdmssp=False):
        """
        Method calls ucs api, POST "setconfig" : "/api/v1/mgmt/config/set", either to phone or pdmssp, determined by pdmssp
        *Note: setConfig API has limit of 20 parameters in each request. This method will break body and send requests
            in chunk size.
        INPUTS: pdmssp as boolean, rdata as dict(body)
        OUTPUT: Returns response body as list when api call is successful, None when unsuccessful.
        """     
        
        res = validate_setConfig_body(rdata)
        if not res:
            return
            
        response = []   
        chunk_dict = {}
        body_dict = {}

        params = rdata["data"]
        params_count = len(params)

        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"

        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}

            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path

            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"

            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["setconfig"][4:]
            pdmssp_body["body"] = rdata

        if params_count <= chunk_size:
            # parameters count is 20 or less, make http request directly
            if not pdmssp:
                dev = self.__httpRequest(qpath="setconfig", rtype="POST", headers=headers, rdata=rdata)
            elif pdmssp:
                dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)

            if dev != None:
=======

            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path

            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"

            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["getconfig"][4:]
            pdmssp_body["body"] = rdata

            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body) 
            if dev != None:
                return dev.json()

                
    def setConfig(self, rdata, chunk_size=20, pdmssp=False):
        """
        Method calls ucs api, POST "setconfig" : "/api/v1/mgmt/config/set", either to phone or pdmssp, determined by pdmssp
        *Note: setConfig API has limit of 20 parameters in each request. This method will break body and send requests
            in chunk size.
        INPUTS: pdmssp as boolean, rdata as dict(body)
        OUTPUT: Returns response body as list when api call is successful, None when unsuccessful.
        """     
        
        res = validate_setConfig_body(rdata)
        if not res:
            return
            
        response = []   
        chunk_dict = {}
        body_dict = {}

        params = rdata["data"]
        params_count = len(params)

        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"

        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}

            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path

            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"

            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["setconfig"][4:]
            pdmssp_body["body"] = rdata

        if params_count <= chunk_size:
            # parameters count is 20 or less, make http request directly
            if not pdmssp:
                dev = self.__httpRequest(qpath="setconfig", rtype="POST", headers=headers, rdata=rdata)
            elif pdmssp:
                dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)

            if dev != None:
>>>>>>> Stashed changes
                response.append(dev.json())

        else:
            # need to slice body into chunks of 20 parameters and make http requests by chunks
            item_count = 0
            loop_count = 0

            for k,v in params.items():
                chunk_dict[k] = v
                item_count += 1

                if item_count > chunk_size-1:
                    # chunk collection is full, send for http request, then empty chunk_dict & body_dict
                    item_count = 0
                    loop_count += 1
                    body_dict["data"] = chunk_dict

                    if not pdmssp:
                        dev = self.__httpRequest(qpath="setconfig", rtype="POST", headers=headers, rdata=body_dict)
                    elif pdmssp:
                        dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)

                    if dev != None:
                        response.append(dev.json())

                    chunk_dict.clear()
                    body_dict.clear()

            if params_count%chunk_size != 0:
                # last chunk containing all remainder, send for http request
                body_dict["data"] = chunk_dict
                
                if not pdmssp:
                    dev = self.__httpRequest(qpath="setconfig", rtype="POST", headers=headers, rdata=body_dict)
                elif pdmssp:
                    dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)

                if dev != None:
                    response.append(dev.json())

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    
    def callDial(self, dest, line=1, linetype="Tel", duration=10, ctype="application/json"):
=======
=======
>>>>>>> Stashed changes
        return response
                
 
    def callDial(self, dest, line=1, linetype="Tel", duration=10, pdmssp=False):
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        """
        Method calls ucs api, POST "calldial" : "/api/v1/callctrl/dial", either to phone or pdmssp, determined by pdmssp
        *Note: Auto-disconnect is supported for a singe line(1) dialout scenario only.
        INPUTS: 
            dest as string (either in TEL, eg. 3002 or SIP URI format, eg. 3002@apbeta.internal),
            line as int (defaults to line 1), 
            linestype as string (SIP, H323 or TEL, should match dest string format),
                duration as int (in seconds - defaults to 10S,when value is 1s or more (on line1 only), 
                method will track duration and auto-disconnect after duration lapsed.), 0s means no auto-disconnect.
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            ctype as string(Content-Type).
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        body_dict = {
                    "data" : { 
                                "Dest" : dest,
                                "Line" : line,
                                "Type" : linetype
                             }
                }
                
        # validates duration as integer
        if not isinstance(duration, int):
            logging.error("Invalid type for duration, expects Int only")
            return
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
                
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}

            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path

            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"

            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["calldial"][4:]
            pdmssp_body["body"] = body_dict
        
        
        if not pdmssp:
            call = self.getCallStatusV2()
            
            if call != None:
                # validates if active session exists before placing call.
                if len(call["data"]) >= 1:
                    print("Active call exists - call dial method will not proceed.")
                    return 
                else:
                    # proceed with call dial
                    dev = self.__httpRequest(qpath="calldial", rtype="POST", headers=headers, rdata=body_dict)
<<<<<<< Updated upstream
            
            else:
                print("Could not query status of the phone. Exiting now.")
                return call
                
        elif pdmssp:
            call = self.getCallStatusV2(pdmssp=True)
            
=======
            
            else:
                print("Could not query status of the phone. Exiting now.")
                return call
                
        elif pdmssp:
            call = self.getCallStatusV2(pdmssp=True)
            
>>>>>>> Stashed changes
            if call != None:
                # validates if active session exists before placing call.
                if len(call["data"]["body"]["data"]) >= 1:
                    print("Active call exists - call dial method will not proceed.")
                    return
                else:
                    # proceed with call dial
                    dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                         headers=pdmssp_headers, rdata=pdmssp_body)
            
            else:
                print("Could not query status of the phone. Exiting now.")
                return call

        if dev != None:
            logging.info(f"Placing call out to '{dest}'...")
            print(f"Placing call out to '{dest}'...")
            
            # gives some time for callDial to take effect.
            time.sleep(1)
        
            if duration <= 0:
                # duration is <=0, does not attempt auto-disconnect, exit method instead.
                print(f"Call Dial to {dest} is done. \nDuration '{duration}' is less than or equal to 0 >> Auto-disconnect is Disabled. \nNo more actions taken.")
                return dev.json()
            
            loop = True
            timelapsed = False
            call_dict = {}
           
            while loop:
                
                # query interval 
                time.sleep(3)
                
                # query callstatus from phone 
                if not pdmssp:
                    call = self.getCallStatusV2()
                    
                    if call != None:
                        if not call["data"]:
                            print("No more calls detected on phone: Exiting now.")
                            loop = False
                        else:
                            call_dict = getCallConnectionInfo(call, dest)
                    
                    else:
                        print("Could not query status of the phone. Exiting now.")
                        return call
                        
                elif pdmssp:
                    call = self.getCallStatusV2(True)
                    
                    if call != None:
                        if not call["data"]["body"]["data"]:
                            print("No more calls detected on phone: Exiting now.")
                            loop = False
                        else:
                            call_dict = getCallConnectionInfo(call, dest, True)

                    else:
                        print("Could not query status of the phone. Exiting now.")
                        return call
                    
                            
                if not call_dict:
                    # active call has no match to dest, and so exit loop.
                    print(f"Call to {dest} not found! Exiting now.")
                    loop = False
                    
                else:
                    # active call has match to dest, and so continue...
                    print(f"CallHandle[{call_dict['CallHandle']}]: CallState to '{dest}' is currently '{call_dict['CallState']}'.")

                    if ( call_dict['CallState'] == "Connected" ) & ( timelapsed == False ):
                        # detects that call has connected for the first time.
                        print(f"CallHandle[{call_dict['CallHandle']}]: Waiting for {duration}s now... ")
                        # sleep for specified duration
                        time.sleep(duration)
                        print(f"CallHandle[{call_dict['CallHandle']}]: {duration}s has now lapsed. ")
                        timelapsed = True

<<<<<<< Updated upstream
<<<<<<< Updated upstream
                        if duration > 0:                       
                            if ( dest == session_RemotePartyNumber ) & ( callstate == "Connected" ):
                                # Validates called party number and connected state before executing callEnd.
                                logging.info(f"Call is now connected to '{dest}'...")
                                print(f"Call is now connected to '{dest}'...")

                                callHandle = call["data"][0]["CallHandle"]
                                time.sleep(duration)
                                logging.info(f"Duration {duration}s has lapsed, attempting to disconnect call now.")
                                print(f"Duration {duration}s has lapsed, attempting to disconnect call now.")

                                res = self.callEnd(callHandle)
                                if res != None:
                                    logging.info(f"Call to '{dest}' has ended.")
                                    print(f"Call to '{dest}' has ended.")
                                else:
                                    logging.info(f"Disconnection attempt to '{dest}' at '{callHandle}' failed. \nPlease check device physically to end the session.")
                                    print(f"Disconnection attempt to '{dest}' at '{callHandle}' failed. \nPlease check device physically to end the session.")

                                return res            
                
                time.sleep(3)
                
=======
                    elif ( call_dict['CallState'] == "Connected" ) & ( timelapsed == True ):
                        # detects that call has connected and duration lapsed, and so attempt to end call.
                        print(f"CallHandle[{call_dict['CallHandle']}]: Attempt to end call now...")
                              
                        if not pdmssp:
                            end = self.callEnd(call_dict['CallHandle'])
                        elif pdmssp:
                            end = self.callEnd(call_dict['CallHandle'], True)

                        if end != None:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Call to '{dest}' has ended.")
                            return end
                        else:
                            # call end attempt failure, and so exit loop.
                            print(f"CallHandle[{call_dict['CallHandle']}]: End call attempt to '{dest}'failed. \nPlease try end the session using Call End method.")
                            loop = False          
                    
                    elif ( call_dict['CallState'] == "Hold" ):
                        # detects that call has been put on hold, and so attempt to resume call.
                        print(f"CallHandle[{call_dict['CallHandle']}]: Attempt to resume call now...")
                              
                        if not pdmssp:
                            resume = self.callResume()
                        elif pdmssp:
                            resume = self.callResume(True)

                        if resume != None:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Resume call successful.")
                        else:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Resume attempt to '{dest}'failed. \nPlease try end the session using Call End method.")
                            loop = False

=======
                    elif ( call_dict['CallState'] == "Connected" ) & ( timelapsed == True ):
                        # detects that call has connected and duration lapsed, and so attempt to end call.
                        print(f"CallHandle[{call_dict['CallHandle']}]: Attempt to end call now...")
                              
                        if not pdmssp:
                            end = self.callEnd(call_dict['CallHandle'])
                        elif pdmssp:
                            end = self.callEnd(call_dict['CallHandle'], True)

                        if end != None:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Call to '{dest}' has ended.")
                            return end
                        else:
                            # call end attempt failure, and so exit loop.
                            print(f"CallHandle[{call_dict['CallHandle']}]: End call attempt to '{dest}'failed. \nPlease try end the session using Call End method.")
                            loop = False          
                    
                    elif ( call_dict['CallState'] == "Hold" ):
                        # detects that call has been put on hold, and so attempt to resume call.
                        print(f"CallHandle[{call_dict['CallHandle']}]: Attempt to resume call now...")
                              
                        if not pdmssp:
                            resume = self.callResume()
                        elif pdmssp:
                            resume = self.callResume(True)

                        if resume != None:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Resume call successful.")
                        else:
                            print(f"CallHandle[{call_dict['CallHandle']}]: Resume attempt to '{dest}'failed. \nPlease try end the session using Call End method.")
                            loop = False

>>>>>>> Stashed changes
                    elif ( call_dict['CallState'] == "Disconnected" ):
                        # detects that call dial has failed and disconnected, and so exit loop.
                        print(f"CallHandle[{call_dict['CallHandle']}]: No more calls detected on phone. Exiting now.")
                        loop = False
                              
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
            return dev.json()
        

    def callEnd(self, callhandle="", pdmssp=False):
        """
        Method calls ucs api, POST "callend" : "/api/v1/callctrl/endCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: callHandle as string (should be a valid callHandle from 'getCallStatusV2()'), pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        body_dict = {
                    "data" : { 
                                "Ref" : callhandle
                             }
                }
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callend", rtype="POST", headers=headers, rdata=body_dict)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callend"][4:]
            pdmssp_body["body"] = body_dict
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()

            
    def callMute(self, mute="1", pdmssp=False):
        """
        Method calls ucs api, POST "callmute" : "/api/v1/callctrl/mute", either to phone or pdmssp, determined by pdmssp
        INPUTS: mute as str ("1" to mute, "0" to unmute), pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        body_dict = {
                    "data" : { 
                                "state" : mute
                             }
                }
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callmute", rtype="POST", headers=headers, rdata=body_dict)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callmute"][4:]
            pdmssp_body["body"] = body_dict
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()

            
    def sendDTMF(self, digits, pdmssp=False):
        """
        Method calls ucs api, POST "sendDTMF" : "/api/v1/callctrl/sendDTMF", either to phone or pdmssp, determined by pdmssp
        INPUTS: digits as str (expecting 0-9,*,#), pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        body_dict = {
                    "data" : { 
                                "Digits" : digits
                             }
                }
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="sendDTMF", rtype="POST", headers=headers, rdata=body_dict)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["sendDTMF"][4:]
            pdmssp_body["body"] = body_dict
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
           
 
    def callAnswer(self, pdmssp=False):
        """
        Method calls ucs api, POST "callanswer" : "/api/v1/callctrl/answerCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callanswer", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callanswer"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()
<<<<<<< Updated upstream


=======


>>>>>>> Stashed changes
    def callIgnore(self, pdmssp=False):
        """
        Method calls ucs api, POST "callignore" : "/api/v1/callctrl/ignoreCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callignore", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callignore"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()            

            
    def callReject(self, pdmssp=False):
        """
        Method calls ucs api, POST "callreject" : "/api/v1/callctrl/rejectCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callreject", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callreject"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()            
            

    def callHold(self, pdmssp=False):
        """
        Method calls ucs api, POST "callhold" : "/api/v1/callctrl/holdCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callhold", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callhold"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()            

            
    def callResume(self, pdmssp=False):
        """
        Method calls ucs api, POST "callresume" : "/api/v1/callctrl/resumeCall", either to phone or pdmssp, determined by pdmssp
        INPUTS: pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="callresume", rtype="POST", headers=headers)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["callresume"][4:]
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()                        
            
            
    def simulateKeyEvent(self, key, pdmssp=False):
        """
        Method calls ucs api, POST "simulateKeyEvent" : "/api/v1/mgmt/simulateKeyEvent", either to phone or pdmssp, determined by pdmssp
        INPUTS: key as string (should be a valid KeyName), pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        body_dict = {
                    "data" : { 
                                "Type" : "Tap",
                                "KeyName" : key
                             }
                }
        
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="simulateKeyEvent", rtype="POST", headers=headers, rdata=body_dict)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["simulateKeyEvent"][4:]
            pdmssp_body["body"] = body_dict
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)           
            if dev != None:
                return dev.json()


<<<<<<< Updated upstream
<<<<<<< Updated upstream
        
    def simulateTextInput(self, textinput, replacetext="true", ctype="application/json"):
        """
        Method calls internal httpRequest to POST "simulateTextInput" : "/api/v1/mgmt/simulateTextInput".
        INPUTS: textinput as string, 
                replacetext as string ('true' or 'false', if set to true, it replaces any existing text in phone UI’s text field 
                with the value provided.),
                ctype as string(Content-Type)
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
=======
    def simulateTextInput(self, textinput, replacetext="true", pdmssp=False):
>>>>>>> Stashed changes
=======
    def simulateTextInput(self, textinput, replacetext="true", pdmssp=False):
>>>>>>> Stashed changes
        """
        Method calls ucs api, POST "simulateTextInput" : "/api/v1/mgmt/simulateTextInput", either to phone or pdmssp, determined by pdmssp
        INPUTS: textinput as string, replacetext as string ('true' or 'false', if set to true, it replaces any existing text in phone UI’s text field 
                with the value provided.), pdmssp as boolean
        OUTPUT: Returns response body as dict when api call is successful, None when unsuccessful.
        """     
        body_dict = {
                    "data" : { 
                                "Value" : textinput,
                                "ReplaceText" : replacetext
                             }
                }
                
        if not pdmssp:
            headers = {}
            headers["Content-Type"] = "application/json"
            
            dev = self.__httpRequest(qpath="simulateTextInput", rtype="POST", headers=headers, rdata=body_dict)
            if dev != None:
                return dev.json()
        
        elif pdmssp:
            pdmssp_headers = {}
            pdmssp_body = {}
            pdmssp_params = {}
            
            resource_path = self._domain_path + self.org_id + "/devices/" + self.device_id + "/ucsapi"
            pdmssp_url = self._pdmssp_baseurl + resource_path
            
            pdmssp_headers["Authorization"] = f"Bearer {self.token}"
            pdmssp_headers["Content-Type"] = "application/json"
            
            pdmssp_body["method"] = "POST"
            pdmssp_body["apiurl"] = self._qpaths_dict["simulateTextInput"][4:]
            pdmssp_body["body"] = body_dict
            
            dev = self.__httpRequest(rtype="POST", pdmssp=True, pdmssp_url=pdmssp_url, params=pdmssp_params, 
                                     headers=pdmssp_headers, rdata=pdmssp_body)  
            if dev != None:
                return dev.json()
        
        
    


# In[ ]:




