#!/usr/bin/env python
# coding: utf-8

# In[8]:


def clear(): 
    """
    Method clears the terminal screen.
    INPUTS: none
    OUTPUT: none
    """
    from os import system, name 
    
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
         


# In[9]:


def display_dict(dev, indent_count=0):
    """
    Method recursively prints data body containing either dict or list
    INPUTS: none 
    OUTPUT: none
    """
    
    indent = "\t"
    
    if isinstance(dev, dict): 
        
        for k, v in dev.items():
            if isinstance(v, dict):
                if indent_count == 0:
                    print(f"{k}:")
                else:
                    print(f"{indent_count*indent}{k}:")
                
                display_dict(v, indent_count+1)
                
            elif isinstance(v, list):
                if indent == 0:
                    print(f"{k}:")
                else:
                    print(f"{indent_count*indent}{k}:")
                    
                display_dict(v, indent_count+1)
                
            else:
                if indent == 0:
                    print(f"{k} = {v}")
                else:
                    print(f"{indent_count*indent}{k} = {v}")
    
    elif isinstance(dev, list):
        
        for i in range( len(dev) ):
            if indent == 0:
                display_dict(dev[i])
            else:
                display_dict(dev[i], indent_count+1)
        


# In[10]:


def getline_input():
    """
    Method collects user inputs for phone line number 
    INPUTS: none 
    OUTPUT: Returns int
    """
   
    loop = True
    
    while loop:
        
        line = input("Enter line no. (default=1): ")
        
        if line == "":
            # empty input defaults to 1.
            return 1
        
        if line.isdigit(): 
            if int(line) <= 0:
                print(f"Invalid input '{line}' >> Expecting integer(>=1).")
            else:
                loop = False
        else:
            print(f"Invalid input '{line}' >> Expecting integer(>=1).")            
    
    return int(line)
    


# In[11]:


def getlinetype_input():
    """
    Method collects user inputs for line type - TEL or SIP 
    INPUTS: none 
    OUTPUT: Returns str
    """
    
    valid_values = ( "TEL", "SIP" )
    loop = True
    
    while loop:
        
        linetype = input(f"Enter line type, {valid_values} (default='TEL'): ")
        
        if linetype == "":
            # empty input defaults to 1.
            return "TEL"
        
        if linetype.upper() in valid_values: 
            loop = False
        else:
            print(f"Invalid input '{linetype}' >> Expecting [{valid_values}].")            
    
    return linetype.upper()    
    


# In[12]:


def getdest_input(linetype="TEL"):
    """
    Method collects user inputs for destination dialstring - TEL or SIP 
    INPUTS: linetype as str ('TEL' or 'SIP') 
    OUTPUT: Returns str
    """
    import re
       
    loop = True
    
    while loop:
        
        dest = input(f"Enter destination dialstring [{linetype}]: ")
        
        if dest != "":
            
            if linetype == "TEL":
                res = re.match("\d+", dest)
                if res:
                    loop = False
                else:
                    print(f"Invalid input '{dest}' >> Expecting TEL(E.164) dialstring.")
                    
            elif linetype == "SIP":
                res = re.match("([^@|\s]+@[^@]+\.[^@|\s]+)", dest)
                if res:
                    loop = False
                else:
                    print(f"Invalid input '{dest}' >> Expecting SIP URI dialstring.")
                
        else:
            print(f"Empty input '{dest}' >> Expecting {linetype} dialstring.")
    
    return dest
    


# In[ ]:


def getduration_input():
    """
    Method collects user inputs for duration in seconds, minimum value is 0 and maximum value is 600s. Defaults to 0 
    if not inputs from user.
    INPUTS: none 
    OUTPUT: Returns int. 
    """
   
    loop = True
    
    while loop:
        
        duration = input("Enter call duration(s) (default=10): ")
        
        if duration == "":
            # empty input defaults to 10.
            return 10
        
        if duration.isdigit(): 
            if ( int(duration) < 0 ) | ( int(duration) > 600 ):
                print(f"Invalid input '{duration}' >> Expecting integer(0-600).")
            else:
                loop = False
        else:
            print(f"Invalid input '{duration}' >> Expecting integer.")            
    
    return int(duration)
    


# In[ ]:


def connect_device(module_version, username="Polycom", password="789"):
    """
    Method collects user inputs for phone's IP address, username and password
    INPUTS: none 
    OUTPUT: Returns a result as list, [ ip, (username, passwd) ]
    """
    import ipaddress
    
    ip = ""
    loop = True
    
    print(f"Welcome to VVXME CLI Menu version {module_version}\n")

    while loop:            
        try:
            ip = ipaddress.ip_address( input("Enter IP address of the phone: ") )
            print(f"{ip} is a valid IP{ip.version} address")
            loop = False
        except ValueError as err:
            print(f"Value Error: <{err}>")


    usr = input(f"Enter username(Default: '{username}') :")
    if usr != "":
        username = usr

    pwd = input(f"Enter password(Default: '{password}'): ")
    if pwd != "":
        password = pwd

    return [ip.exploded, (username, password)]

