#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import menu
import time


# In[ ]:


def web_call_controls_submenu(dev):
    """
    Method - Web Call Control Menu
    INPUTS: dev as object 
    OUTPUT: none
    """

    loop = True
    menu.clear()

    while loop:
        print("Web Call Control Menu")
        print("=====================")
        print("1. Call Dial")
        print("0. Exit")
        choice = input("Enter your choice[0-1]: ")
        
        if choice == "1":
            menu.clear()
            calldial_submenu(dev)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-1].")
            time.sleep(1)
            menu.clear()        


# In[ ]:


def calldial_submenu(dev):
    
    menu.clear()
    
    linetype = "TEL"
    line = 1
    dest = ""
    duration = 0
    
    print("Current Call Dial Settings")
    print("==========================")
    print(f">> Line Type: [ {linetype} ] \n>> Line: [ {line} ] \n>> Dest: [ {dest} ] \n>> Duration: [ {duration} ]\n")
        
                         
    linetype = menu.getlinetype_input()
    line = menu.getline_input()
    dest = menu.getdest_input(linetype)
    duration = menu.getduration_input()
     
    #print(f"Final Call Dial Settings >> Line Type: [{linetype}], Line: [{line}], Dest: [{dest}], Duration: [{duration}]\n")
    res = dev.callDial(dest, line, linetype, duration)
    print(res)
    input("Press Enter to continue...")
    

