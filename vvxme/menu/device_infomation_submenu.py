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
        print("Show Device Information Menu")
        print("============================")
        print("1. Show Device Info")
        print("2. Show Device Stats")
        print("3. Show Network Info")
        print("4. Show Network Stats")
        print("5. Show Line Info")
        print("6. Show Session Stats")
        print("0. Exit")
        choice = input("Enter your choice[0-6]: ")

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
            # Show session stats
            menu.clear()
            print("Session Stats - /api/v1/mgmt/media/sessionStats")
            print("===============================================")            
            menu.display_dict(dev.getSessionStats()["data"])
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-6].")
            time.sleep(1)
            menu.clear()

