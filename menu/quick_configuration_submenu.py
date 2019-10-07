#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import menu
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
        print("2. Headset Configuration Menu")
        #print("x. DNS Cache?")
        print("3. Message Waiting Indicator(LED)")
        print("4. Network Discovery - CDP")
        print("5. Network Discovery - LLDP")
        print("6. Remote Packet Capture")
        print("7. Screen Capture")
        print("8. SIP Autoanswer")
        print("9. SIP Debug & Logging")
        print("0. Exit")  
        choice = input("Enter your choice[0-8]: ")
        
        if choice == "1":
            # Calls acousticfencemenu_submenu
            menu.clear()
            acousticfencemenu_submenu(dev)
            menu.clear()
        elif choice == "2":
            # Calls headsetconfiguration_submenu
            menu.clear()
            headsetconfiguration_submenu(dev)
            menu.clear()
        elif choice == "3":
            # Calls messagewaitingindicator_submenu
            menu.clear()
            messagewaitingindicator_submenu(dev)
            menu.clear()
        elif choice == "4":
            # Calls networkcdp_submenu
            menu.clear()
            networkcdp_submenu(dev)
            menu.clear()
        elif choice == "5":
            # Calls networklldp_submenu
            menu.clear()
            networklldp_submenu(dev)
            menu.clear()
        elif choice == "6":
            # Calls remotepacketcapture_submenu
            menu.clear()
            remotepacketcapture_submenu(dev)
            menu.clear()
        elif choice == "7":
            # Calls screencapture_submenu
            menu.clear()
            screencapture_submenu(dev)
            menu.clear()
        elif choice == "8":
            # Calls sipautoanswer_submenu
            menu.clear()
            sipautoanswer_submenu(dev)
            menu.clear()
        elif choice == "9":
            # Calls sipdebuglogging_submenu
            menu.clear()
            sipdebuglogging_submenu(dev)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-1].")
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


def headsetconfiguration_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["usb.headset.config.enabled"] }
    body_dict = { "data" : {} }
    loop = True
    
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
            print("Device is restarting, pausing for 20sec...")
            time.sleep(20)
            #input("Press Enter to continue...")
            return
        elif choice == "2":
            line = menu.getline_input()
            body_dict["data"][f"msg.mwi.{line}.led"] = "0"
            print(dev.setConfig(body_dict))
            print("Device is restarting, pausing for 20sec...")
            time.sleep(20)
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


def networkcdp_submenu(dev):

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


def sipdebuglogging_submenu(dev):
   
    menu.clear()
    query_dict = { "data" : ["log.level.change.sip", "log.render.level", "log.render.file.size"] }
    body_dict = { "data" : {} }
    loop = True
    
    while loop:

        print("Current Value:")
        print("==============")
        menu.display_dict(dev.getConfig(query_dict)["data"])
        print("")
        print("1. Enable SIP Debug & Logging")
        print("2. Disable SIP Debug & Logging")
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            # Calls setConfig using body_dict
            body_dict["data"]["log.render.level"] = "0"
            body_dict["data"]["log.render.file.size"] = "1000"
            body_dict["data"]["log.level.change.sip"] = "0"
            print(dev.setConfig(body_dict))
            input("Press Enter to continue...")
            return
        elif choice == "2":
            # Calls setConfig using body_dict
            body_dict["data"]["log.render.level"] = "4"
            body_dict["data"]["log.render.file.size"] = "32"
            body_dict["data"]["log.level.change.sip"] = "4"
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

