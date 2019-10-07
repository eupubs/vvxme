# vvxme
version: 1.0.0

Manages your Poly VVX powered by RESTAPIs based on (UCS>=6.1), with CLI Menu or simply use the available VVX class to develope your own applications.

Prerequisite:
  - Install python 3.7 or above
  - Install the project:  'pip install vvxme==1.0.0'

## Using the inbuilt CLI Menu
To invoke the CLI Menu, simply open a console and type command: 'python vvxme' or 'python -m vvxme'

### Available menus in this version:
Main Selection Menu:
  1. Show Device Information Menu
      - Show Device Info
      - Show Device Stats
      - Show Network Info
      - Show Network Stats
      - Show Line Info
      - Show Session Stats
  2. Quick Configuration Menu
      - Acoustic Fence Menu
      - Headset Configuration Menu
      - Message Waiting Indicator (LED)
      - Network Discovery - CDP
      - Network Discovery - LLDP
      - Remote Packet Capture
      - Screen Capture
      - SIP Autoanswer
      - SIP Debug & Logging
  3. Web Call Controls Menu
      - Call Dial __(Remote dial-out call to TEL/SIP dialstrings from specified Line with specified duation)__
  4. Simulate Key Events Menu
      - Simulate Keys __(Drives the VVX using your keyboard)__
  

