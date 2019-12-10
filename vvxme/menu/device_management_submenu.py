#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vvxme import menu
import time


# In[ ]:


def device_management_submenu(dev, pdmssp=False):  
    """
    Method - Show Device Information Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    loop = True
    menu.clear()

    while loop:
        print("Device Management Menu")
        print("======================")
        print("1. Import from cfg (xml/json)")
        print("2. Reset Configuration")
        print("3. Update Configuration")
        print("4. Restart Device")
        print("5. Reboot Device")
        print("6. Factory Reset")
        print("0. Exit")
        choice = input("Enter your choice[0-6]: ")

        if choice == "1":
            # Import from cfg
            menu.clear()
            importconfiguration_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "2":
            # Reset Configuration
            menu.clear()
            resetconfig_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "3":
            # Update Configuration
            menu.clear()
            print(f"Update Configuration - {dev._qpaths_dict['updateConfig']}")
            print("=======================================================")
            res = menu.getconfirmation_input("Update Configuration")
            if res:
                print("Updating Configuration...")
                print(dev.updateConfig(pdmssp))
            else:
                print("\nNo action taken.")            
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "4":
            # Restart Device
            menu.clear()
            print(f"Restart Device - {dev._qpaths_dict['safeRestart']}")
            print("=========================================")
            res = menu.getconfirmation_input("Restart Device")
            if res:
                print("Restarting Device...")
                print(dev.safeRestart(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "5":
            # Reboot Device
            menu.clear()
            print(f"Reboot Device - {dev._qpaths_dict['safeReboot']}")
            print("=======================================")
            res = menu.getconfirmation_input("Reboot Device")
            if res:
                print("Rebooting Device...")
                print(dev.safeReboot(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "6":
            # Factory Reset Device
            menu.clear()
            print(f"Factory Reset - {dev._qpaths_dict['factoryReset']}")
            print("=========================================")
            res = menu.getconfirmation_input("Factory Reset Device")
            if res:
                print("Factory Resetting Device...")
                print(dev.factoryReset(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-6].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def resetconfig_submenu(dev, pdmssp=False):  
    """
    Method - Show Reset Config Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()

    while loop:
        print("Reset Configuration Menu")
        print("========================")
        print("1. Reset All")
        print("2. Reset Cloud")
        print("3. Reset Local")
        print("4. Reset Web")
        print("5. Reset Device")
        print("0. Exit")
        choice = input("Enter your choice[0-5]: ")

        if choice == "1":
            # Reset all
            menu.clear()
            print(f"Reset Configuration - {dev._qpaths_dict['resetConfig']}")
            print("==============================================")
            res = menu.getconfirmation_input("Reset All configuration")
            if res:
                print("Resetting ALL configuration...")
                print(dev.resetConfig("all", pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "2":
            # Reset cloud
            menu.clear()
            print(f"Reset Configuration - {dev._qpaths_dict['resetConfig_cloud']}")
            print("====================================================")
            res = menu.getconfirmation_input("Reset Cloud configuration")
            if res:
                print("Resetting Cloud configuration...")
                print(dev.resetConfig("cloud", pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "3":
            # Reset local
            menu.clear()
            print(f"Reset Configuration - {dev._qpaths_dict['resetConfig_local']}")
            print("====================================================")
            res = menu.getconfirmation_input("Reset Local configuration")
            if res:
                print("Resetting Local configuration...")
                print(dev.resetConfig("local", pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "4":
            # Reset web
            menu.clear()
            print(f"Reset Configuration - {dev._qpaths_dict['resetConfig_web']}")
            print("==================================================")
            res = menu.getconfirmation_input("Reset Web configuration")
            if res:
                print("Resetting Web configuration...")
                print(dev.resetConfig("web", pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "5":
            # Reset device
            menu.clear()
            print(f"Reset Configuration - {dev._qpaths_dict['resetConfig_device']}")
            print("=====================================================")
            res = menu.getconfirmation_input("Reset Device configuration")
            if res:
                print("Resetting Device configuration...")
                print(dev.resetConfig("device", pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-5].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def importconfiguration_submenu(dev, pdmssp=False):
    """
    Method - Show the parsed content and ask user confirmation for import.
    INPUTS: none 
    OUTPUT: none
    """
    import os.path
    
    body_dict = {}
    loop = True
    menu.clear()
    
    while loop:
        
        if not pdmssp:
            print("Import Mode: [Direct]")
        elif pdmssp:
            print("Import Mode: [PDMS-SP]")
        
        print("\n*** Quick Note #1 : Expecting configuration file in current folder only. ***")
        print("*** Quick Note #2 : Parser will attempt to parse with xml first, and then with json. ***")
        print("*** Quick Note #3 : xml - uses VVX/UCS syntax, Root Element is not parsed! ***")
        print("*** Quick Note #4 : json - { 'data' : { 'parameter1' : 'value1', 'parameter2' : 'value2', ... } } ***")
        print("*** Quick Note #5 : It is ultimately your responsibilty to ensure correctness of your file!!! ***")
        
        
        if not pdmssp: 
            print("*** Quick Note #6 : Direct Import Mode ***")
            print("\t\t  i) Assumming low latency to device, no limit to no. of parameters per cfg.")
            print("\t\t ii) Import execution in chunk size of 20 parameters per request.")
        elif pdmssp:
            print("*** Quick Note #6 : PDMS-SP Import Mode ***")
            print("\t\tDue to significantly longer network latency in this mode:")
            print("\t\t  i) Limit number of parameters per cfg to 5 or lesser.")
            print("\t\t ii) Additional parameters will probably fail as device reboot/restart.")
            print("\t\tiii) As device restart/reboot, you may see HTTP errors even at successful import.")

        filename = input("\nEnter filename (default='import.cfg'),or E(x)it: ")
        
        if (filename == 'x') | (filename == 'X'):
            return
        
        if filename == "":
            filename = "import.cfg"
        
        if os.path.isfile(filename):                   
            body_dict = menu.ucs_configfile_parser(filename)

            if body_dict != None:
                
                import_loop = True
                menu.display_dict(body_dict)
                
                while import_loop:
                
                    import_proceed = input("\nPlease review parsed parameters. Proceed with import [Y/n]: ")

                    if (import_proceed == "") | (import_proceed == "Y") | (import_proceed == "y"):
                        
                        if not pdmssp:
                            print(dev.setConfig(body_dict))
                        elif pdmssp:
                            # chunk size set to 5 for pdmssp mode.
                            print(dev.setConfig(rdata=body_dict, chunk_size=5, pdmssp=pdmssp))
                        
                        print("\n**Device may reboot after import**\n")
                        input("Press Enter to continue...")
                        return
                    elif (import_proceed == "N") | (import_proceed == "n"):
                        print("Import did not proceed!")
                        input("Press Enter to continue...")
                        return
                    else:
                        print(f"Invalid input '{import_proceed}' >> Expecting [y/Y/n/N].")
                        time.sleep(1)
                
            else:
                menu.clear()
        
        else:
            print(f"\nFile Not Found: '{filename}'. Please try again...\n")
            input("Press Enter to continue...")
            menu.clear()
    
    

