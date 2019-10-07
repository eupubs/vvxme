#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import vvxme
import menu

module_version = "1.0.0"
module_date = "Oct 2019"


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
        print("1. Connect to a VVX/Trio")
        print("0. Exit")
        choice = input("Enter your choice[0-1]: ")
        
        if choice == "1":
            
            print(f"Your choice is {choice}")
            menu.clear()
            
            credentials = menu.connect_device(module_version)
            dev = vvxme.vvx(credentials[0],credentials[1])
                        
            if dev.getDeviceInfoV2() != None:
                menu.selection_menu(dev)
                     
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




