# vvxme
version: 1.0.0.post6

Manages your Poly VVX powered by RESTAPIs based on (UCS>=6.1), with CLI Menu or simply use the available VVX class to develope your own applications.

Prerequisites:
  - Recommends install python 3.5 or above
  - Install the project:  'pip install vvxme'
  - Full features tested on VVX (non-touch screen) models running UCS 6.1. Earlier version will exibit some API errors.

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
      - ~~Network Discovery - CDP~~ 
      - ~~Network Discovery - LLDP~~ 
  4. Web Call Controls Menu *__(Remote dial-out using either TEL/SIP dialstrings from specified Line with specified duration)__*
      - Call Dial 
  5. Simulate Key Events Menu *__(Drive the VVX using your keyboard)__*
      - Simulate Keys 
  

## Using the VVX Class 

Example:  
\# python  
\>>> import vvxme  
\>>> dev = vvxme.vvx( '192.168.1.120', ('Polycom', '789') )  
\>>> dev.getDeviceInfoV2()  
{'data': {'DeviceType': 'HardwareEndpoint', 'IPv6ULAAddress': '::', 'AttachedHardware': {'EM': []}, 'DeviceVendor': 'Polycom', 'CanApplyShutdownRequest': 'True', 'Firmware': {'Application': '5.9.3.2857 02-Jul-19 06:14', 'Updater': '5.9.7.26508', 'BootBlock': '3.0.6.0098 (48830-001)'}, 'ReadyToUse': 'True', 'IPStack': 'IPv4 Only', 'ModelNumber': 'VVX 350', 'UpTime': {'Seconds': '1', 'Days': '0', 'Minutes': '3', 'Hours': '1'}, 'IPAddress': '192.168.1.120', 'PreferredNetwork': 'IPv6', 'IPv6Address': '::', 'IntendToShutdown': 'False', 'IPv6LinkAddress': '::', 'AppState': 'AppStateCall', 'MACAddress': '64167f3959ca'}, 'Status': '2000'}


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
       .getCallLogs() - calls "/api/v1/mgmt/callLogs"
       .getConfig() - calls "/api/v1/mgmt/config/get"
       .setConfig() - calls "/api/v1/mgmt/config/set"
       .callDial() - "/api/v1/callctrl/dial"
       .callEnd() - "/api/v1/callctrl/endCall"
       .simulateKeyEvent() - calls "/api/v1/mgmt/simulateKeyEvent"
       .simulateTextInput() - calls "/api/v1/mgmt/simulateTextInput"
       .safeRestart() - calls "/api/v1/mgmt/safeRestart"
       .safeReboot() - calls "/api/v1/mgmt/safeReboot"
       .factoryReset() - calls "/api/v1/mgmt/factoryReset"
       .updateConfig() - calls "/api/v1/mgmt/updateConfiguration"
       .resetConfig() - calls "/api/v1/mgmt/configReset"
    """

