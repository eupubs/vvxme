#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import menu
import time


# In[ ]:


def device_infomation_submenu(dev):  
    """
    Method - Show Device Information Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()

    while loop:
        print("Device Information Menu")
        print("=======================")
        print("1. Show Device Info")
        print("2. Show Device Stats")
        print("3. Show Network Info")
        print("4. Show Network Stats")
        print("5. Show Line Info")
        print("6. Show Running Config")
        print("7. Show Session Stats")
        print("8. Show Call Logs")
        print("0. Exit")
        choice = input("Enter your choice[0-7]: ")

        if choice == "1":
            ## Show device info
            menu.clear()
            print("Device Info - /api/v2/mgmt/device/info")
            print("======================================")
            menu.display_dict(dev.getDeviceInfoV2()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "2":
            # Show device stats
            menu.clear()
            print("Device Stats - /api/v1/mgmt/device/stats")
            print("========================================")
            menu.display_dict(dev.getDeviceStats()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "3":
            # Show network info
            menu.clear()
            print("Network Info - /api/v1/mgmt/network/info")
            print("========================================")
            menu.display_dict(dev.getNetwork()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "4":
            # Show network stats
            menu.clear()
            print("Network Stats - /api/v1/mgmt/network/stats")
            print("==========================================")
            menu.display_dict(dev.getNetworkStats()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "5":
            # Show line info
            menu.clear()
            print("Line Info - /api/v2/mgmt/lineInfo")
            print("=================================")            
            menu.display_dict(dev.getLineInfoV2()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()        
        elif choice == "6":
            # Show Running info
            menu.clear()
            print("Running Config - /api/v1/mgmt/device/runningConfig")
            print("=================================")            
            menu.display_dict(dev.getRunningConfig()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "7":
            # Show session stats
            menu.clear()
            print("Session Stats - /api/v1/mgmt/media/sessionStats")
            print("===============================================")            
            menu.display_dict(dev.getSessionStats()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()        
        elif choice == "8":
            # Show call logs 
            menu.clear()      
            calllogs_submenu(dev)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-7].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def calllogs_submenu(dev):  
    """
    Method - Show Call Logs Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()

    while loop:
        print("Call Logs Menu")
        print("==============")
        print("1. Show Missed Calls")
        print("2. Show Received Calls")
        print("3. Show Placed Calls")
        print("0. Exit")
        choice = input("Enter your choice[0-3]: ")

        if choice == "1":
            ## Show missed calls
            menu.clear()
            print("Call Logs - /api/v1/mgmt/callLogs/missed")
            print("========================================")
            menu.display_dict(dev.getCallLogs("missed")["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "2":
            # Show received calls
            menu.clear()
            print("Call Logs - /api/v1/mgmt/callLogs/received")
            print("==========================================")
            menu.display_dict(dev.getCallLogs("received")["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "3":
            # Show placed calls
            menu.clear()
            print("Call Logs - /api/v1/mgmt/callLogs/placed")
            print("========================================")
            menu.display_dict(dev.getCallLogs("placed")["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-3].")
            time.sleep(1)
            menu.clear()

