#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import json
import logging
import re
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.ERROR, datefmt='%Y-%m-%d %H:%M:%S')

class vvx():

    """
    Class for VVX based on UCS 6.1.0 REST APIs.
    INPUTS for instance creation:
        - ipaddr = IP address of phone
        - auth = username and password in tuple
    Attributes:
        .ipaddr
        .auth_credentials
        .use_https
        .verify_secure
        .model
        .firmware
        .macaddress
        .baseprofile
    
    Methods:
       .getDeviceInfoV2() - calls "/api/v2/mgmt/device/info"
       .getNetwork() - calls "/api/v1/mgmt/network/info"
       .getLineInfoV2() - calls "/api/v2/mgmt/lineInfo"
       .getCallStatusV2() - calls "/api/v2/webCallControl/callStatus"
       .getRunningConfig() - calls "/api/v1/mgmt/device/runningConfig"
       .getDeviceStats() - calls "/api/v1/mgmt/device/stats"
       .getNetworkStats() - calls "/api/v1/mgmt/network/stats"
       .getSessionStats() - calls "/api/v1/mgmt/media/sessionStats"
       .callDial() - "/api/v1/callctrl/dial"
       .callEnd() - "/api/v1/callctrl/endCall"
       .getConfig() - calls "/api/v1/mgmt/config/get"
       .setConfig() - calls "/api/v1/mgmt/config/set"
    """

    
    __qpaths_dict={

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
            "callresume" : "/api/v1/callctrl/resumeCall",
            "devicestats" : "/api/v1/mgmt/device/stats",
            "networkstats" : "/api/v1/mgmt/network/stats",
            "sessionStats" : "/api/v1/mgmt/media/sessionStats"
        
    }
    
    __valid_versions = ("6.1.0",)
    
        
    def __init__(self, ipaddr, auth_credentials, use_https=True, verify_secure=False):
        self.ipaddr = ipaddr
        self.auth_credentials = auth_credentials
        self.use_https = use_https
        self.verify_secure = verify_secure
        self.__session = requests.Session()
        
        # initiates requests.Session()
        vvx_adapter = requests.adapters.HTTPAdapter(max_retries=3)
        
        if self.use_https:
            self.__session.mount(f"https://{self.ipaddr}", vvx_adapter)
        else:
            self.__session.mount(f"http://{self.ipaddr}", vvx_adapter)

        # Extracts attributes' values for model, firmware, macaddress and __swVer
        dev = self.getDeviceInfoV2()
        if dev != None:
            self.model = dev["data"]["ModelNumber"]
            self.firmware = dev["data"]["Firmware"]["Application"]
            self.macaddress = dev["data"]["MACAddress"]
            
            for item in self.__valid_versions:
                if self.firmware.startswith(item):
                    self.__swVer = item
                else:
                    self.__swVer = None
        else:
            self.model = None
            self.firmware = None
            self.macaddress = None            
        
        # Extracts attribute's value for baseprofile
        dev = self.getConfig({ "data" : [ "device.baseProfile" ] })
        if dev != None:
            self.baseprofile = dev["data"]["device.baseProfile"]["Value"]
        else:
            self.baseprofile = None
        
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

            
    def __httpRequest(self, qpath, rtype="GET", rdata={}, ctype="application/json"):
        """
        Method makes HTTP request using requests. 
        INPUTS: *qpath as string (*qpath is key value taken from qpaths_dict),
            rtype as string(GET,POST,DELETE,UPDATE, etc), ctype as string(Content-Type),
            rdata as dict(body)
        OUTPUT: Response JSON object from requests.get()
        """
        
        s = self.__session
               
        if self.use_https:
            target_url = f"https://{self.ipaddr}{self.__qpaths_dict[qpath]}"
        else:
            target_url = f"http://{self.ipaddr}{self.__qpaths_dict[qpath]}"
        
        
        try:    

            if rtype == "GET":
                r = s.get(target_url, auth=self.auth_credentials, verify=self.verify_secure, timeout=(1, 1))
                r.raise_for_status()
                return r

            elif rtype == "POST":
                headers = { "Content-Type" : ctype }
                r = s.post(url=target_url, data=json.dumps(rdata), headers=headers, 
                                  auth=self.auth_credentials, verify=self.verify_secure, timeout=(1, 1))
                r.raise_for_status()
                return r

        except requests.exceptions.HTTPError as http_err:
            logging.error( f"HTTP Error: <{http_err}>")
        except requests.exceptions.ConnectionError as connect_err:
            logging.error(f"Connection Error: <{connect_err}>")
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Timeout Error: <{timeout_err}>")
        except requests.exceptions.RequestException as err:
            logging.error(f"Request Error: <{err}>")

            
    def getDeviceInfoV2(self):
        """
        Method calls internal httpRequest to GET "deviceinfov2" : "/api/v2/mgmt/device/info".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """     
        dev = self.__httpRequest("deviceinfov2")
        if dev != None:
            return dev.json()
        
  
    def getNetwork(self):
        """
        Method calls internal httpRequest to GET "network" : "/api/v1/mgmt/network/info".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """ 
        dev = self.__httpRequest("network")
        if dev != None:
            return dev.json()
        
    
    def getLineInfoV2(self):
        """
        Method calls internal httpRequest to GET "lineinfov2" : "/api/v2/mgmt/lineInfo".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("lineinfov2")
        if dev != None:
            return dev.json()

            
    def getCallStatusV2(self):
        """
        Method calls internal httpRequest to GET "callstatusv2" : "/api/v2/webCallControl/callStatus".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("callstatusv2")
        if dev != None:
            return dev.json()


    def getRunningConfig(self):
        """
        Method calls internal httpRequest to GET "runningConfig" : "/api/v1/mgmt/device/runningConfig".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("runningConfig")
        if dev != None:
            return dev.json()

    
    def getDeviceStats(self):
        """
        Method calls internal httpRequest to GET "devicestats" : "/api/v1/mgmt/device/stats".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("devicestats")
        if dev != None:
            return dev.json()

    def getNetworkStats(self):
        """
        Method calls internal httpRequest to GET "networkstats" : "/api/v1/mgmt/network/stats".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("networkstats")
        if dev != None:
            return dev.json()

    def getSessionStats(self):
        """
        Method calls internal httpRequest to GET "sessionStats" : "/api/v1/mgmt/media/sessionStats".
        INPUTS: none
        OUTPUT: Returns response body as dict.
        """
        dev = self.__httpRequest("sessionStats")
        if dev != None:
            return dev.json()


    def getConfig(self, rdata, ctype="application/json"):
        """
        Method calls internal httpRequest to POST "getconfig" : "/api/v1/mgmt/config/get".
        INPUTS: ctype as string(Content-Type), rdata as dict(body)
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        # validate rdata for right structure and not empty, rdata = { "data": [...] }
        if isinstance(rdata, dict) is False:
            return logging.error("<JSON Body Error: boby passed is not a dictionary...>")
        elif "data" not in rdata:
            return logging.error("<JSON Body Error: 'data' is key missing...>")
        elif isinstance(rdata["data"], list) is False:
            return logging.error("<JSON Body Error: 'data' value is not a list...>")
        elif not rdata["data"]:
            return logging.error("<JSON Body Error: 'data' is empty...>")
        else:
            logging.debug(f"Body passed: {rdata}")
            dev = self.__httpRequest(qpath="getconfig", rtype="POST", ctype=ctype, rdata=rdata)
            if dev != None:
                return dev.json()

            
    def setConfig(self, rdata, ctype="application/json", chunk_size=20):
        """
        Method calls internal httpRequest to POST "setconfig" : "/api/v1/mgmt/config/set".
        INPUTS: ctype as string(Content-Type), rdata as dict(body)
        OUTPUT: Returns response body as list.
        """
        
        response = []
        
        # setConfig API has limit of 20 parameters in each request. 
               
        # validate rdata for right structure and not empty, rdata = { "data": {...} }
        if isinstance(rdata, dict) is False:
            return logging.error("<JSON Body Error: boby passed is not a dictionary...>")
        elif "data" not in rdata:
            return logging.error("<JSON Body Error: 'data' is key missing...>")
        elif isinstance(rdata["data"], dict) is False:
            return logging.error("<JSON Body Error: 'data' value is not a dictionary...>")
        elif not rdata["data"]:
            return logging.error("<JSON Body Error: 'data' is empty...>")
        else:
            params = rdata["data"]
            params_count = len(params)
           
        chunk_dict = {}
        body_dict = {}

        if params_count <= chunk_size:
            # parameters count is 20 or less, make http request directly
            logging.debug(f"Body passed: {rdata}")
            dev = self.__httpRequest(qpath="setconfig", rtype="POST", ctype=ctype, rdata=rdata)
            if dev != None:
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
                    
                    logging.debug(f"Body passed: {body_dict}")
                    dev = self.__httpRequest(qpath="setconfig", rtype="POST", ctype=ctype, rdata=body_dict)
                    if dev != None:
                        response.append(dev.json())
                    
                    chunk_dict.clear()
                    body_dict.clear()

            if params_count%chunk_size != 0:
                # last chunk containing all remainder, send for http request
                body_dict["data"] = chunk_dict
                logging.debug(f"Body passed: {body_dict}")
                dev = self.__httpRequest(qpath="setconfig", rtype="POST", ctype=ctype, rdata=body_dict)
                if dev != None:
                    response.append(dev.json())
            
        return response

    
    def callDial(self, dest, line=1, linetype="Tel", duration=0, ctype="application/json"):
        """
        Method calls internal httpRequest to POST "calldial" : "/api/v1/callctrl/dial". Auto-disconnect is supported for a 
        singe line(1) dialout scenario only.
        INPUTS: 
            dest as string (either in TEL, eg. 3002 or SIP URI format, eg. 3002@apbeta.internal),
            line as int (defaults to line 1), 
            linestype as string (SIP, H323 or TEL, should match dest string format),
                duration as int (in seconds - defaults to zero meaning no auto-disconnect, 
                when value is 1s or more (on line1 only), method will track duration and 
                auto-disconnect after duration lapsed.),
            ctype as string(Content-Type).
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        params = {
                    "data" : { 
                                "Dest" : dest,
                                "Line" : line,
                                "Type" : linetype
                             }
                }
        
        logging.debug(f"Body passed: {params}") 
        
        # validates duration as integer
        if not isinstance(duration, int):
            return logging.error("Invalid type for duration, expects Int only")
            
        dev = self.__httpRequest(qpath="calldial", rtype="POST", ctype=ctype, rdata=params)
        if dev != None:
            logging.info(f"Placing call out to '{dest}'...")
            print(f"Placing call out to '{dest}'...")
        
            loop = True
            
            while loop:

                call = self.getCallStatusV2()   
                
                if call != None:
                    if ( len(call["data"] ) == 0):
                        logging.info(f"Call to '{dest}' has ended.")
                        print(f"Call to '{dest}' has ended.")
                        loop = False

                    if( len(call["data"] ) == 1): 
                        # Validates one active connection

                        session_RemotePartyNumber = re.sub( "^sip:", "", call["data"][0]["RemotePartyNumber"] )
                        # Removes 'sip:' from RemotePartyNumber if present.

                        callstate = call["data"][0]["CallState"]

                        logging.info(f"CallState to '{dest}' is currently '{callstate}'.")
                        print(f"CallState to '{dest}' is currently '{callstate}'.")

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
                
            return dev.json()

        
    def callEnd(self, callhandle=None, ctype="application/json"):
        """
        Method calls internal httpRequest to POST "callend" : "/api/v1/callctrl/endCall".
        INPUTS: callHandle as string (should be a valid callHandle from 'getCallStatusV2()'), 
                ctype as string(Content-Type)
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        params = {
                    "data" : { 
                                "Ref" : callhandle
                             }
                }
        
        logging.debug(f"Body passed: {params}")
        dev = self.__httpRequest(qpath="callend", rtype="POST", ctype=ctype, rdata=params)
        if dev != None:
            return dev.json()

        
    def simulateKeyEvent(self, key, ctype="application/json"):
        """
        Method calls internal httpRequest to POST "simulateKeyEvent" : "/api/v1/mgmt/simulateKeyEvent".
        INPUTS: key as string (should be a valid KeyName), 
                ctype as string(Content-Type)
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        params = {
                    "data" : { 
                                "Type" : "Tap",
                                "KeyName" : key
                             }
                }

        dev = self.__httpRequest(qpath="simulateKeyEvent", rtype="POST", ctype=ctype, rdata=params)
        if dev != None:
            return dev.json()

        
    def simulateTextInput(self, textinput, replacetext="true", ctype="application/json"):
        """
        Method calls internal httpRequest to POST "callend" : "/api/v1/callctrl/endCall".
        INPUTS: textinput as string, 
                replacetext as string ('true' or 'false', if set to true, it replaces any existing text in phone UI’s text field 
                with the value provided.),
                ctype as string(Content-Type)
        OUTPUT: Returns response body as dict when successful, None when unsuccessful.
        """
        params = {
                    "data" : { 
                                "Value" : textinput,
                                "ReplaceText" : replacetext
                             }
                }
        
        logging.debug(f"Body passed: {params}")
        dev = self.__httpRequest(qpath="simulateTextInput", rtype="POST", ctype=ctype, rdata=params)
        if dev != None:
            return dev.json()


# In[ ]:

