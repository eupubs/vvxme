#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vvxme import menu
import time


# In[ ]:


def quick_configuration_submenu(dev):
    """
    Method - Quick Configuration Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()
    
    while loop:
        
        print("Quick Configuration Menu")
        print("========================")        
        print("1. Acoustic Fence Menu")
        print("2. Active Call Screen")
        print("3. Font Size Customization")
        print("4. Headset Configuration Menu")
        print("5. Message Waiting Indicator(LED)")
        print("6. Pagination")
        print("7. Remote Packet Capture")
        print("8. Screen Capture")
        print("9. SIP Autoanswer")
        print("10. SIP Debug & USB Logging")
        print("0. Exit")  
        choice = input("Enter your choice[0-10]: ")
        
        if choice == "1":
            # Calls acousticfencemenu_submenu
            menu.clear()
            acousticfencemenu_submenu(dev)
            menu.clear()
        elif choice == "2":
            # Calls activecallscreen_submenu
            menu.clear()
            activecallscreen_submenu(dev)
            menu.clear()
        elif choice == "3":
            # Calls fontsizecustomization_submenu
            menu.clear()
            fontsizecustomization_submenu(dev)
            menu.clear()
        elif choice == "4":
            # Calls headsetconfiguration_submenu
            menu.clear()
            headsetconfiguration_submenu(dev)
            menu.clear()
        elif choice == "5":
            # Calls messagewaitingindicator_submenu
            menu.clear()
            messagewaitingindicator_submenu(dev)
            menu.clear()
        elif choice == "6":
            # Calls pagination_submenu
            menu.clear()
            pagination_submenu(dev)
            menu.clear()   
        elif choice == "7":
            # Calls remotepacketcapture_submenu
            menu.clear()
            remotepacketcapture_submenu(dev)
            menu.clear()
        elif choice == "8":
            # Calls screencapture_submenu
            menu.clear()
            screencapture_submenu(dev)
            menu.clear()
        elif choice == "9":
            # Calls sipautoanswer_submenu
            menu.clear()
            sipautoanswer_submenu(dev)
            menu.clear()
        elif choice == "10":
            # Calls sipdebugusblogging_submenu
            menu.clear()
            sipdebugusblogging_submenu(dev)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-10].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def acousticfencemenu_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["feature.acousticFenceUI.enabled"] }
    body_dict = { "data" : {} }
    loop = True
        
    while loop:
        
        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Acoustic Fence Menu")
        print("2. Disable Acoustic Fence Menu")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["feature.acousticFenceUI.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["feature.acousticFenceUI.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def activecallscreen_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["up.LineViewCallStatus.enabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Active Call Screen")
        print("2. Disable Active Call Screen")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["up.LineViewCallStatus.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["up.LineViewCallStatus.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def fontsizecustomization_submenu(dev):
   
    menu.clear()
    valid_models = ("VVX 250", "VVX 350", "VVX 450")
    query_dict = { "data" : ["device.font.size"] }
    body_dict = { "data" : {} }
    loop = True
    
    if dev.model not in valid_models:
        print(f"This device {dev.model} doesn't support this setting. Supported models are {valid_models}")
        input("Press Enter to continue...")
        return
    
    if not dev._swVer:
        print(f"This firmware {dev.firmware} doesn't support this setting. Supported versions are {dev._valid_versions}")
        input("Press Enter to continue...")
        return
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("***NOTE: Changing this value will cause device to reboot!***")
        print("")
        print("1. Normal Font Size")
        print("2. Large Font Size")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.font.size"] = "Normal"
            body_dict["data"]["device.font.size.set"] = "1"
            print(dev.setConfig(body_dict))
            print("Device is rebooting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.font.size"] = "Large"
            body_dict["data"]["device.font.size.set"] = "1"
            print(dev.setConfig(body_dict))
            print("Device is rebooting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def headsetconfiguration_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["usb.headset.config.enabled"] }
    body_dict = { "data" : {} }
    loop = True

    if not dev._swVer:
        print(f"This firmware {dev.firmware} doesn't support this setting. Supported versions are {dev._valid_versions}")
        input("Press Enter to continue...")
        return
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Headset Configuration Menu")
        print("2. Disable Headset Configuration Menu")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["usb.headset.config.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["usb.headset.config.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def messagewaitingindicator_submenu(dev, line=1):
   
    menu.clear()
    body_dict = { "data" : {} }
    loop = True

    while loop:

        print("Current Value:")
        print("==============")
        for i in range (dev.linescount):
            query_dict = { "data" : [f"msg.mwi.{i+1}.led"] }
            menu.display_dict(dev.getConfig(query_dict)["data"])
        print("***NOTE: Changing this value will cause device to restart!***")
        print("")
        print("1. Enable Message Waiting Indicator(LED)")
        print("2. Disable Message Waiting Indicator(LED)")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            line = menu.getline_input()
            body_dict["data"][f"msg.mwi.{line}.led"] = "1"
            print(dev.setConfig(body_dict))
            print("Device is restarting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return
        elif choice == "2":
            line = menu.getline_input()
            body_dict["data"][f"msg.mwi.{line}.led"] = "0"
            print(dev.setConfig(body_dict))
            print("Device is restarting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def pagination_submenu(dev):
   
    menu.clear()
    invalid_models = ("VVX 101", "VVX 201", "VVX 150")
    query_dict = { "data" : ["up.Pagination.enabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    if dev.model in invalid_models:
        print(f"This device {dev.model} doesn't support this setting. Unsupported models are {invalid_models}")
        input("Press Enter to continue...")
        return

    if not dev._swVer:
        print(f"This firmware {dev.firmware} doesn't support this setting. Supported versions are {dev._valid_versions}")
        input("Press Enter to continue...")
        return
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Pagination")
        print("2. Disable Pagination")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["up.Pagination.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["up.Pagination.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def remotepacketcapture_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["diags.pcap.enabled", "diags.pcap.remote.enabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Remote Packet Capture")
        print("2. Disable Remote Packet Capture")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["diags.pcap.enabled"] = "1"
            body_dict["data"]["diags.pcap.remote.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["diags.pcap.enabled"] = "0"
            body_dict["data"]["diags.pcap.remote.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def screencapture_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["up.screenCapture.enabled", "up.screenCapture.value"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable Screen Capture")
        print("2. Disable Screen Capture")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["up.screenCapture.enabled"] = "1"
            body_dict["data"]["up.screenCapture.value"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["up.screenCapture.enabled"] = "0"
            body_dict["data"]["up.screenCapture.value"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def sipautoanswer_submenu(dev):
    
    menu.clear()
    query_dict = { "data" : ["call.autoAnswer.SIP"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable SIP Autoanswer")
        print("2. Disable SIP Autoanswer")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["call.autoAnswer.SIP"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["call.autoAnswer.SIP"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def sipdebugusblogging_submenu(dev):
   
    menu.clear()
    invalid_models = ("VVX 101", "VVX 201", "VVX 301", "VVX 311", "VVX 150")
    query_dict = { "data" : ["log.level.change.sip", "log.render.level", "log.render.file.size", "feature.usbLogging.enabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    if dev.model in invalid_models:
        print(f"This device {dev.model} doesn't support USB. Unsupported models are {invalid_models}")
        input("Press Enter to continue...")
        return
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable SIP Debug & USB Logging")
        print("2. Disable SIP Debug & USB Logging")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["log.render.level"] = "0"
            body_dict["data"]["log.render.file.size"] = "1"
            body_dict["data"]["log.level.change.sip"] = "0"
            body_dict["data"]["feature.usbLogging.enabled"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["log.render.level"] = "4"
            body_dict["data"]["log.render.file.size"] = "32"
            body_dict["data"]["log.level.change.sip"] = "4"
            body_dict["data"]["feature.usbLogging.enabled"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def networkcdp_submenu(dev):
    # not in use...

    menu.clear()
    query_dict = { "data" : ["device.net.cdpEnabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable CDP")
        print("2. Disable CDP")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.net.cdpEnabled"] = "1"
            body_dict["data"]["device.net.cdpEnabled.set"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.net.cdpEnabled"] = "0"
            body_dict["data"]["device.net.cdpEnabled.set"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def networklldp_submenu(dev):
    # not in use...
   
    menu.clear()
    query_dict = { "data" : ["device.net.lldpEnabled"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable LLDP")
        print("2. Disable LLDP")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.net.lldpEnabled"] = "1"
            body_dict["data"]["device.net.lldpEnabled.set"] = "1"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.net.lldpEnabled"] = "0"
            body_dict["data"]["device.net.lldpEnabled.set"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            


# In[ ]:


def phonetheme_submenu(dev):
    # not in use...
   
    menu.clear()
    invalid_models = ("VVX 101", "VVX 201", "VVX 150")
    query_dict = { "data" : ["device.theme"] }
    body_dict = { "data" : {} }
    loop = True
    
    if dev.model in invalid_models:
        print(f"This device {dev.model} doesn't support this setting. Unsupported models are {invalid_models}")
        input("Press Enter to continue...")
        return
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("***NOTE: Changing this value will cause device to reboot!***")
        print("")
        print("1. Classic Theme")
        print("2. BroadSoft Theme")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.theme"] = "Classic"
            body_dict["data"]["device.theme.set"] = "1"
            print(dev.setConfig(body_dict))
            print("Device is rebooting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["device.set"] = "1"
            body_dict["data"]["device.theme"] = "BroadSoft"
            body_dict["data"]["device.theme.set"] = "1"
            print(dev.setConfig(body_dict))
            print("Device is rebooting, pausing for 30sec...")
            time.sleep(30)
            #input("Press Enter to continue...")
            return              
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()
            

