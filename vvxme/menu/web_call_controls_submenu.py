#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vvxme import menu
import time


# In[ ]:


def web_call_controls_submenu(dev, pdmssp=False):
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
        print("1. Check Call Status")        
        print("2. Call Dial")
        print("3. Call Answer")
        print("4. Call Reject")
        print("5. Call Ignore")
        print("6. Call Hold")
        print("7. Call Resume")
        print("8. Call End")
        print("0. Exit")
        choice = input("Enter your choice[0-8]: ")
        
        if choice == "1":
            menu.clear()
            print("Check Call Status - /api/v2/webCallControl/callStatus")                  
            print("=====================================================")
            print("")                  
            res = dev.getCallStatusV2(pdmssp)
            if res != None:
                menu.display_dict(res["data"]["body"]["data"]) if pdmssp else menu.display_dict(res["data"])
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "2":
            menu.clear()
            calldial_submenu(dev, pdmssp)
            menu.clear()            
        elif choice == "3":
            menu.clear()
            print(f"Call Answer - {dev._qpaths_dict['callanswer']}")
            print("=========================================")
            res = menu.getconfirmation_input("Call Answer")
            if res:
                print("Answering Call...")
                print(dev.callAnswer(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "4":
            menu.clear()
            print(f"Call Reject - {dev._qpaths_dict['callreject']}")
            print("=========================================")
            res = menu.getconfirmation_input("Call Reject")
            if res:
                print("Rejecting Call...")
                print(dev.callReject(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()
        elif choice == "5":
            menu.clear()
            print(f"Call Reject - {dev._qpaths_dict['callignore']}")
            print("=========================================")
            res = menu.getconfirmation_input("Call Reject")
            if res:
                print("Ignoring Call...")
                print(dev.callIgnore(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()   
        elif choice == "6":
            menu.clear()
            print(f"Call Hold - {dev._qpaths_dict['callhold']}")
            print("=====================================")
            res = menu.getconfirmation_input("Call Hold")
            if res:
                print("Holding Call...")
                print(dev.callIgnore(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()                                    
        elif choice == "7":
            menu.clear()
            print(f"Call Resume - {dev._qpaths_dict['callresume']}")
            print("=========================================")
            res = menu.getconfirmation_input("Call Resume")
            if res:
                print("Resuming Call...")
                print(dev.callIgnore(pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()   
        elif choice == "8":
            menu.clear()
            print(f"Call End - {dev._qpaths_dict['callend']}")
            print("===================================")
            callhandle = input("Enter callHandle: ")
            res = menu.getconfirmation_input("Call End")
            if res:
                print("Ending Call...")
                print(dev.callEnd(callhandle, pdmssp))
            else:
                print("\nNo action taken.")
            input("\nPress Enter to continue...")
            menu.clear()                                                                        
        elif choice == "0":
            # Exit menu
            loop = False
        else:
            print(f"Invalid input '{choice}' >> Expecting [0-8].")
            time.sleep(1)
            menu.clear()        


# In[ ]:


def calldial_submenu(dev, pdmssp=False):
    
    menu.clear()
    
    linetype = "TEL"
    line = 1
    dest = ""
    duration = 10
    
    print("Current Call Dial Settings")
    print("==========================")
    print(f">> Line Type: [ {linetype} ] \n>> Line: [ {line} ] \n>> Dest: [ {dest} ] \n>> Duration: [ {duration} ]\n")
        
                         
    linetype = menu.getlinetype_input()
    line = menu.getline_input()
    dest = menu.getdest_input(linetype)
    duration = menu.getduration_input()
     
    #print(f"Final Call Dial Settings >> Line Type: [{linetype}], Line: [{line}], Dest: [{dest}], Duration: [{duration}]\n")
    res = dev.callDial(dest, line, linetype, duration, pdmssp)
    if res != None:
        print(res)
    input("Press Enter to continue...")
    

