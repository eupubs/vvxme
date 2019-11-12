#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import vvxme
from vvxme import menu

<<<<<<< Updated upstream
<<<<<<< Updated upstream
module_version = "1.0.0.post6"
module_date = "Oct 2019"
=======
module_version = "1.1.0"
module_date = "Nov 2019"
>>>>>>> Stashed changes
=======
module_version = "1.1.0.post1"
module_date = "Nov 2019"
>>>>>>> Stashed changes


# In[ ]:


def main():
    """
    Method is the first main menu.
    INPUTS: none 
    OUTPUT: none
    """
    
    loop = True
    choice = ""
    
    while loop:
        
        menu.clear()
        credentials =[]
        print(f"Welcome to VVXME CLI Menu version {module_version}")
        print("")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        print("1. Connect to a VVX")
=======
        print("1. Connect to a VVX by IP Address")
        print("2. Connect to a VVX on PDMS-SP")
>>>>>>> Stashed changes
=======
        print("1. Connect to a VVX by IP Address")
        print("2. Connect to a VVX on PDMS-SP")
>>>>>>> Stashed changes
        print("0. Exit")
        choice = input("Enter your choice[0-2]: ")
        
        if choice == "1":
            
            menu.clear()
            
            credentials = menu.connect_device(module_version)
            dev = vvxme.vvx(credentials[0],credentials[1])         
<<<<<<< Updated upstream
                
            if dev.model != None:
                menu.selection_menu(dev)
            
=======
            if dev.model != None:
                menu.selection_menu(dev)
            else:
                input("\nPress Enter to continue...")
                    
>>>>>>> Stashed changes
        elif choice == "2":
            
            menu.clear()
            
            macaddr = menu.pdmssp_connect_device(module_version)
            credentials = menu.pdmssp_configfile_parser(module_version)
<<<<<<< Updated upstream
            
            if credentials != None:
=======
            if credentials:
>>>>>>> Stashed changes
                print("\nAttempting to connect to PDMS-SP now. Please hold...\n")
                dev = vvxme.vvx(pdmssp=True, pdmssp_credentials=credentials, macaddr=macaddr)

                if (dev.model != None) & (dev.linescount != None):
                    menu.selection_menu(dev, True)
<<<<<<< Updated upstream
            
            else:
                input("\nPress Enter to continue...")
                menu.clear()
            
=======

                elif not dev.token:
                    print(f"\nUnable to acquire access token from PDMS-SP. Check credentials again.")
                    input("\nPress Enter to continue...")

                elif not dev.device_id:
                    print(f"\nDevice not found in PDMS-SP Organization.")
                    input("\nPress Enter to continue...")
                
                else:
                    input("\nPress Enter to continue...")

>>>>>>> Stashed changes
        elif choice == "0":
            print("Goodbye!")
            loop = False
        
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-1] ")
            time.sleep(1)
            menu.clear()


# In[ ]:





# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:




