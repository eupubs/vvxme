#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vvxme import menu
import time


# In[ ]:


def device_infomation_submenu(dev, pdmssp=False):  
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
            print(f"Device Info - {dev._qpaths_dict['deviceinfov2']}")
            print("======================================")
            res = dev.getDeviceInfoV2(pdmssp)
            print("")                  
            if res != None:     
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "2":
            # Show device stats
            menu.clear()
            print(f"Device Stats - {dev._qpaths_dict['devicestats']}")
            print("========================================")
            res = dev.getDeviceStats(pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "3":
            # Show network info
            menu.clear()
            print(f"Network Info - {dev._qpaths_dict['network']}")
            print("========================================")
            res = dev.getNetwork(pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "4":
            # Show network stats
            menu.clear()
            print(f"Network Stats - {dev._qpaths_dict['networkstats']}")
            print("==========================================")
            res = dev.getNetworkStats(pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "5":
            # Show line info
            menu.clear()
            print(f"Line Info - {dev._qpaths_dict['lineinfov2']}")
            print("=================================")            
            res = dev.getLineInfoV2(pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()        
        elif choice == "6":
            # Show Running info
            menu.clear()
            print(f"Running Config - {dev._qpaths_dict['runningConfig']}")
            print("==================================================")            
            res = dev.getRunningConfig(pdmssp)
            print("")
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "7":
            # Show session stats
            menu.clear()
            print(f"Session Stats - {dev._qpaths_dict['sessionStats']}")
            print("===============================================")            
            res = dev.getSessionStats(pdmssp)
            print("")
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()        
        elif choice == "8":
            # Show call logs 
            menu.clear()      
            calllogs_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-7].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def calllogs_submenu(dev, pdmssp=False):  
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
            print(f"Missed Calls - {dev._qpaths_dict['callLogs_missed']}")
            print("===========================================")
            res = dev.getCallLogs("missed", pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "2":
            # Show received calls
            menu.clear()
            print(f"Received Calls - {dev._qpaths_dict['callLogs_received']}")
            print("===============================================")
            res = dev.getCallLogs("received", pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "3":
            # Show placed calls
            menu.clear()
            print(f"Placed Calls - {dev._qpaths_dict['callLogs_placed']}")
            print("===========================================")
            res = dev.getCallLogs("placed", pdmssp)
            print("")                  
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-3].")
            time.sleep(1)
            menu.clear()

