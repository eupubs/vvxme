#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import keyboard
from vvxme import menu
import time
import sys


# In[ ]:


def simulate_key_events_submenu(dev, pdmssp=False):
    """
    Method - Simulate Key Events Menu
    INPUTS: dev as object 
    OUTPUT: none
    """
    
    loop = True
    menu.clear()

    while loop:
        print("Simulate Key Events Menu")
        print("========================")
        print("1. Simulate Keys")
        print("0. Exit")
        choice = input("Enter your choice[0-1]: ")
        
        if choice == "1":
            menu.clear()
            simulatekeys_submenu(dev, pdmssp)
            menu.clear()
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-1].")
            time.sleep(1)
            menu.clear()        


# In[ ]:


def simulatekeys_submenu(dev, pdmssp=False):
    """
    Method uses keyboard module to capture keyboard event (.is_pressed) and then match to return valid 
    '/api/v1/mgmt/simulateKeyEvent' value. Tested on Win10 and MacOS 10.x. 
    *TAKE NOTE on Mac: Run in sudo mode and allow Accessbility to allow keyboard module to work.
    INPUTS: none 
    OUTPUT: none
    """
    from sys import platform as _platform
    
    menu.clear()
    kb = keyboard
    
    keys_dict = {    
        "up" : "ArrowUp",
        "down" : "ArrowDown",
        "right" : "ArrowRight",
        "left" : "ArrowLeft",
        "0" : "Dialpad0",
        "1" : "Dialpad1",
        "2" : "Dialpad2",
        "3" : "Dialpad3",
        "4" : "Dialpad4",
        "5" : "Dialpad5",
        "6" : "Dialpad6",
        "7" : "Dialpad7",
        "8" : "Dialpad8",
        "9" : "Dialpad9",
        "h" : "Home",
        "H" : "Home",
        "m" : "MicMute",
        "M" : "MicMute",
        "r" : "Redial",
        "R" : "Redial",
        "enter" : "Select",
        "backspace" : "Delete",
        "delete" : "Delete",
        "!" : "SoftKey1",
        "@" : "SoftKey2",
        "#" : "SoftKey3",
        "$" : "SoftKey4",
        "+" : "VolUp",
        "-" : "VolDown"
    }
    
    mac_softkeys_dict = {
        "Softkey1" : [ 56, 18 ],
        "Softkey2" : [ 56, 19 ],
        "Softkey3" : [ 56, 20 ],
        "Softkey4" : [ 56, 21 ]
    }
    
    print("Keyboard Legend:")
    print("================")
    print("Arrows:[up, down, left, right], Numbers:[0-9]") 
    print("Letters:[(h)ome, (m)icMute, (r)edial, (e)nter, backspace/delete]")
    print("Softkeys(1,2,3,4): [!, @, #, $], Volume: [+,-]")
    print("\nPress 'esc' to exit.\n")
        
    def print_pressed_keys(e):
        
        if ( _platform == "win32" ) | ( _platform == "win32" ): 
            # Windows
            keys = kb._pressed_events 
            for item in list(keys):
                if keys[item].name in keys_dict:
                    pressed_key = keys_dict[keys[item].name]                
                    print(f"Keyboard code pressed: {item}, translated to '{pressed_key}' for VVX", end='\r')
                    sys.stdout.write("\033[K")  # clears previous print() line
                    dev.simulateKeyEvent(pressed_key, pdmssp)
    
        elif _platform == "darwin":
            # MacOS
            keys = kb._pressed_events           
            if len(keys) == 1: 
                # single input
                for item in list(keys):
                    if keys[item].name in keys_dict:
                        pressed_key = keys_dict[keys[item].name]                
                        print(f"Keyboard code pressed: {item}, translated to '{pressed_key}' for VVX", end='\r')
                        sys.stdout.write("\033[K")  # clears previous print() line
                        dev.simulateKeyEvent(pressed_key, pdmssp)
            elif len(keys) == 2:
                # double inputs - looking for shift + 1,2,3,4
                list_keys = list(keys)
                for k, v in mac_softkeys_dict.items():
                    if ( list_keys[0] in v ) & ( list_keys[1] in v ):
                        print(f"Keyboard code pressed: {v}, translated to '{k}' for VVX", end='\r')
                        sys.stdout.write("\033[K")  # clears previous print() line
                        dev.simulateKeyEvent(k, pdmssp)               
    
    kb.hook(print_pressed_keys)
    kb.wait('esc')
    keyboard.unhook_all()
    menu.flush_input()

