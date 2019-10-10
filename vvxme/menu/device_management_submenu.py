#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import menu
import time


# In[ ]:


def device_management_submenu(dev):  
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
            importconfiguration_submenu(dev)
            menu.clear()
        elif choice == "2":
            # Reset Configuration
            menu.clear()
            resetconfig_submenu(dev)
            menu.clear()
        elif choice == "3":
            # Update Configuration
            menu.clear()
            print("Update Configuration - /api/v1/mgmt/updateConfiguration")
            print("=======================================================")
            res = menu.getconfirmation_input("Update Configuration")
            if res:
                print("Updating Configuration...")
                print(dev.updateConfig())
            else:
                print("\nNo action taken.")            
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "4":
            # Restart Device
            menu.clear()
            print("Restart Device - /api/v1/mgmt/safeRestart")
            print("=========================================")
            res = menu.getconfirmation_input("Restart Device")
            if res:
                print("Restarting Device...")
                print(dev.safeRestart())
            else:
                print("\nNo action taken.")
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "5":
            # Reboot Device
            menu.clear()
            print("Reboot Device - /api/v1/mgmt/safeReboot")
            print("=======================================")
            res = menu.getconfirmation_input("Reboot Device")
            if res:
                print("Rebooting Device...")
                print(dev.safeReboot())
            else:
                print("\nNo action taken.")
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "6":
            # Factory Reset Device
            menu.clear()
            print("Factory Reset - /api/v1/mgmt/factoryReset")
            print("=========================================")
            res = menu.getconfirmation_input("Factory Reset Device")
            if res:
                print("Factory Resetting Device...")
                print(dev.factoryReset())
            else:
                print("\nNo action taken.")
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


# In[ ]:


def resetconfig_submenu(dev):  
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
            ## Reset all
            menu.clear()
            print("Reset Configuration - /api/v1/mgmt/configReset")
            print("==============================================")
            print(dev.resetConfig())
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "2":
            ## Reset cloud
            menu.clear()
            print("Reset Configuration - /api/v1/mgmt/configReset/cloud")
            print("====================================================")
            print(dev.resetConfig("cloud"))
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "3":
            ## Reset local
            menu.clear()
            print("Reset Configuration - /api/v1/mgmt/configReset/local")
            print("====================================================")
            print(dev.resetConfig("local"))
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "4":
            ## Reset web
            menu.clear()
            print("Reset Configuration - /api/v1/mgmt/configReset/web")
            print("==================================================")
            print(dev.resetConfig("web"))
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "5":
            ## Reset web
            menu.clear()
            print("Reset Configuration - /api/v1/mgmt/configReset/device")
            print("=====================================================")
            print(dev.resetConfig("device"))
            print("")
            input("Press Enter to continue...")
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-5].")
            time.sleep(1)
            menu.clear()


# In[ ]:


def importconfiguration_submenu(dev):
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
        
        print("*** Quick Note #1 : Expecting configuration file in current folder only. ***")
        print("*** Quick Note #2 : Parser will attempt to parse with xml first, and then with json. ***")
        print("*** Quick Note #3 : xml - uses VVX/UCS syntax, Root Element is not parsed! ***")
        print("*** Quick Note #4 : json - { 'data' : { 'parameter1' : 'value1', 'parameter2' : 'value2', ... } } ***")
        print("*** Quick Note #5 : It is ultimately your responsibilty to ensure correctness of your file!!! ***\n")
        filename = input("Enter filename (default='import.cfg'),or E(x)it: ")
        
        if (filename == 'x') | (filename == 'X'):
            return
        
        if filename == "":
            filename = "import.cfg"
        
        if os.path.isfile(filename):                   
            body_dict = menu.configfile_parser(filename)

            if body_dict != None:
                
                import_loop = True
                menu.display_dict(body_dict)
                
                while import_loop:
                
                    import_proceed = input("\nPlease review parsed parameters. Proceed with import [Y/n]: ")

                    if (import_proceed == "") | (import_proceed == "Y") | (import_proceed == "y"):
                        print(dev.setConfig(body_dict))
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
    
    
