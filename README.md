# vvxme
version: 1.1.0.post1

Manages your Poly VVX powered by RESTAPIs based on (UCS>=6.1) directly or now via PDMS-SP!, with CLI Menu or simply use the available VVX class to develop your own applications.

1.1.0.post1 Updates:
  - Bug fix to handle multiple lines.
  - General error handling improvements on vvx class and main.    

What's new on this build:
  - Connect now to your VVX on PDMS-SP! 
  - New menu options in **bold**.
  - Re-worked Call Dial method for improved resiliency, especially over PDMS-SP.
  - General updates to support PDMS-SP connectivity.
  - Logging level added into VVX class (INFO as default). PDMS-SP connectivity has INFO logging in console to show live API status. Direct phone connectivity requires DEBUG level to print the same on console.  

Notes on this build:
  - As of this build, APIs getConfig/setConfig are not working well on PDMS-SP yet. Therefore, certain menu options are not available on PDMS-SP connectivity.
  - PDMS-SP API calls take a little more time, so please be patience!


Prerequisites:
  - Recommends install python 3.5 or above
  - Install the project:  'pip install vvxme'
  - Full features tested on VVX (non-touch screen) models running UCS 6.1. Earlier version will exibit some API errors.
  - Environment variable 'HOME' has to be defined containing a valid directory/folder, to hold configuraiton file (pdmssp.cfg) containing PDMS-SP credentials- client_id, client_secret and org_id. Sample pdmssp.cfg is included in package under data folder.

#### Sample pdmssp.cfg.example:
    [API_KEY]
    client_id = xxxxx
    client_secret = xxxxx

    [ORG]
    org_id = xxxxx

OS security notes:  
  - For Windows users: May have to run the console in Administrator mode to use VVX class in interactive mode.  
  - For Mac users: Requires sudo mode to run CLI Menu - 'sudo python -m vvxme'  

## Using the inbuilt CLI Menu
To invoke the CLI Menu, simply open a console and type command: 'python -m vvxme' 

### Available menus in this version:
Main Selection Menu:
  1. Device Information Menu *__(Useful information of your VVX)__*
      - Show Device Info
      - Show Device Stats
      - Show Network Info
      - Show Network Stats
      - Show Line Info
      - Show Running Config
      - Show Call Logs
      - Show Session Stats
  2. Device Management Menu *__(Useful VVX management options)__*
      - Import from cfg (xml/json)
      - Reset Configuration
      - Update Configuration
      - Restart Device
      - Reboot Device
      - Factory Reset
  3. Quick Configuration Menu *__(Quick fix to enable/disable specific features on your VVX)__*
      - Acoustic Fence Menu
      - Active Call Screen
      - Font Size Customization
      - Headset Configuration Menu
      - Message Waiting Indicator (LED)
      - Pagination
      - Remote Packet Capture
      - Screen Capture
      - SIP Autoanswer
      - SIP Debug & USB Logging
  4. Web Call Controls Menu *__(Remote dial-out using either TEL/SIP dialstrings from specified Line with specified duration)__*
      - **Check Call Status**
      - Call Dial 
      - **Call Answer**
      - **Call Reject**
      - **Call Ignore**
      - **Call Hold**
      - **Call Resume**
      - **Call End**
  5. Simulate Key Events Menu *__(Drive the VVX using your keyboard)__*
      - Simulate Keys 
  

## Using the VVX Class 

Direct Example:  
\# **python**  
\>>> **import vvxme**  
\>>> **dev = vvxme.vvx( '192.168.1.120', ('Polycom', '789') )**  
\>>> **dev.getDeviceInfoV2()**  
{'data': {'DeviceType': 'HardwareEndpoint', 'IPv6ULAAddress': '::', 'AttachedHardware': {'EM': []}, 'DeviceVendor': 'Polycom', 'CanApplyShutdownRequest': 'True', 'Firmware': {'Application': '5.9.3.2857 02-Jul-19 06:14', 'Updater': '5.9.7.26508', 'BootBlock': '3.0.6.0098 (48830-001)'}, 'ReadyToUse': 'True', 'IPStack': 'IPv4 Only', 'ModelNumber': 'VVX 350', 'UpTime': {'Seconds': '1', 'Days': '0', 'Minutes': '3', 'Hours': '1'}, 'IPAddress': '192.168.1.120', 'PreferredNetwork': 'IPv6', 'IPv6Address': '::', 'IntendToShutdown': 'False', 'IPv6LinkAddress': '::', 'AppState': 'AppStateCall', 'MACAddress': '64167f3959ca'}, 'Status': '2000'}  
  
PDMS-SP Example:  
\# **python**  
\>>> **import vvxme**  
\>>> **dev = vvxme.vvx(pdmssp=True, macaddr='64167F0945F4', pdmssp_credentials={'client_id':'xxxxx', 'client_secret':'xxxxx', 'org_id'='xxxxx'})**  
\>>>   
2019-10-31 10:29:52 INFO     Request -->> https://pcs-api-na.obitalk.com/api/v2/oauth/client_credential/accesstoken, Body: {}  
2019-10-31 10:29:52 INFO     Response <<-- <200>  
2019-10-31 10:29:55 INFO     Request -->> https://pcs-api-na.obitalk.com/api/v2/domain/xxxxx/devices, Body: {}  
2019-10-31 10:29:55 INFO     Response <<-- <200>  
2019-10-31 10:29:57 INFO     Request -->> https://pcs-api-na.obitalk.com/api/v2/domain/xxxxx/devices/xxxxx/ucsapi, Body: {'method': \'GET', 'apiurl': '/v2/mgmt/device/info'}  
2019-10-31 10:29:57 INFO     Response <<-- <201>  
2019-10-31 10:30:01 INFO     Request -->> https://pcs-api-na.obitalk.com/api/v2/domain/xxxxx/devices/xxxxx/ucsapi, Body: {'method': \'GET', 'apiurl': '/v2/mgmt/lineInfo'}  
\>>>    
\>>> **dev.getDeviceInfoV2(True)**  
2019-10-31 10:30:36 INFO     Request -->> https://pcs-api-na.obitalk.com/api/v2/domain/xxxxx/devices/xxxxx/ucsapi, Body: {'method': 'GET', 'apiurl': '/v2/mgmt/device/info'}  
2019-10-31 10:30:36 INFO     Response <<-- <201>  
{'data': {'httpStatus': 200, 'body': {'uploadTime': '2019-10-31T10:30:38+0800', 'data': {'DeviceType': 'HardwareEndpoint', 'ModelNumber': 'VVX 501', 'Firmware': {'BootBlock': '3.0.5.0131 (48500-001)', 'Application': '6.1.0.6189 31-Jul-19 02:54', 'Updater': '6.1.0.6163'}, 'MACAddress': '64167f0945f4', 'IPAddress': '10.250.150.93', 'DeviceVendor': 'Polycom', 'ReadyToUse': 'True', 'AttachedHardware': {'EM': [], 'Camera': 'yes'}, 'UpTime': {'Minutes': '13', 'Seconds': '7', 'Hours': '20', 'Days': '12'}, 'IPStack': 'IPv4 Only', 'PreferredNetwork': 'IPv6', 'IPv6Address': '::', 'IPv6LinkAddress': '::', 'IPv6ULAAddress': '::', 'AppState': 'AppStateCall', 'CanApplyShutdownRequest': 'True', 'IntendToShutdown': 'False'}, 'versionInfo': '1.0', 'Status': '2000', 'eventMonotonicTime': '357h:10m:15s:203ms'}}}  


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
       .callMute() - "/api/v1/callctrl/mute"
       .sendDTMF() - "/api/v1/callctrl/sendDTMF"
       .callAnswer() - "/api/v1/callctrl/answerCall"
       .callIgnore() - "/api/v1/callctrl/ignoreCall"
       .callReject() - "/api/v1/callctrl/rejectCall"
       .callHold() - "/api/v1/callctrl/holdCall"
       .callResume() - "/api/v1/callctrl/resumeCall"
       .simulateKeyEvent() - calls "/api/v1/mgmt/simulateKeyEvent"
       .simulateTextInput() - calls "/api/v1/mgmt/simulateTextInput"
       .safeRestart() - calls "/api/v1/mgmt/safeRestart"
       .safeReboot() - calls "/api/v1/mgmt/safeReboot"
       .factoryReset() - calls "/api/v1/mgmt/factoryReset"
       .updateConfig() - calls "/api/v1/mgmt/updateConfiguration"
       .resetConfig() - calls "/api/v1/mgmt/configReset"
    """
