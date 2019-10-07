#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import menu
import time


# In[ ]:


def selection_menu(dev):
    """
    Method is the main selection menu, after successful connectivity to device.
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()
       
    while loop:
        
        print(f"Connected to device {dev.model} with MAC {dev.macaddress} running on build {dev.firmware} in {dev.baseprofile} mode.")
        
        for i in range(dev.linescount):
            print(f">> Line {i+1} configured as {dev.lines[i+1]} in [{dev.linestates[dev.lines[i+1]]}] state")
        
        print("")
        print("Main Selection Menu")
        print("===================")
        print("1. Show Device Information Menu")
        print("2. Quick Configuration Menu")
        print("3. Web Call Controls Menu")
        print("4. Simulate Key Events Menu")
        #print("5. Import Configuration")
        print("0. Exit")  
        choice = input("Enter your choice[0-5]: ")
        
        if choice == "1":
            # Calls device_info_submenu
            menu.clear()
            menu.device_infomation_submenu(dev)
            menu.clear()
        elif choice == "2":
            # Calls quick_configuration_submenu
            menu.clear()
            menu.quick_configuration_submenu(dev)
            menu.clear()
        elif choice == "3":
            # Calls web_call_controls_submenu
            menu.clear()
            menu.web_call_controls_submenu(dev)
            menu.clear()
        elif choice == "4":
            # Calls simulate_key_events_submenu
            menu.clear()
            menu.simulate_key_events_submenu(dev)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-2].")
            time.sleep(1)
            menu.clear()

