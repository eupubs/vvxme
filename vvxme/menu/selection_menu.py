#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vvxme import menu
import time


# In[ ]:


def selection_menu(dev, pdmssp=False):
    """
    Method is the main selection menu, after successful connectivity to device.
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()
       
    while loop:
        
        #print(f"Connected to device {dev.model} with MAC {dev.macaddress} running on build {dev.firmware} in {dev.baseprofile} mode.")
        print(f"Connected to device {dev.model} with MAC {dev.macaddress} running on build {dev.firmware}.")
        
        for i in range(dev.linescount):
            print(f">> Line {i+1} configured as {dev.lines[i+1]} in [{dev.linestates[dev.lines[i+1]]}] state")
        
        print("")
        print("Main Selection Menu")
        print("===================")
        print("1. Device Information Menu")
        print("2. Device Management Menu")
        print("3. Quick Configuration Menu") 
        print("4. Web Call Controls Menu")
        print("5. Simulate Key Events Menu")
        print("0. Exit")  
        choice = input("Enter your choice[0-5]: ")
        
        if choice == "1":
            # Calls device_infomation_submenu
            menu.clear()
            menu.device_infomation_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "2":
            # Calls device_management_submenu
            menu.clear()
            menu.device_management_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "3":
            # Calls quick_configuration_submenu
            menu.clear()
            menu.quick_configuration_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "4":
            # Calls web_call_controls_submenu
            menu.clear()
            menu.web_call_controls_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "5":
            # Calls simulate_key_events_submenu
            menu.clear()
            menu.simulate_key_events_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-5].")
            time.sleep(1)
            menu.clear()

