#!/usr/bin/env python
# coding: utf-8

# In[4]:


__all__ = [ "clear", "display_dict", "getline_input", "getlinetype_input", "getdest_input", "getduration_input",
            "connect_device", "selection_menu", "device_infomation_submenu", "quick_configuration_submenu", 
            "acousticfencemenu_submenu", "headsetconfiguration_submenu", "messagewaitingindicator_submenu", 
            "networkcdp_submenu", "networklldp_submenu", "remotepacketcapture_submenu", "screencapture_submenu", 
            "sipautoanswer_submenu", "sipdebuglogging_submenu", "web_call_controls_submenu", "calldial_submenu", 
            "simulate_key_events_submenu", "simulatekeys_submenu" ]


# In[ ]:


from .menu_commons import clear
from .menu_commons import display_dict
from .menu_commons import getline_input
from .menu_commons import getlinetype_input
from .menu_commons import getdest_input
from .menu_commons import getduration_input
from .menu_commons import connect_device
from .selection_menu import selection_menu
from .device_infomation_submenu import device_infomation_submenu
from .quick_configuration_submenu import quick_configuration_submenu
from .quick_configuration_submenu import acousticfencemenu_submenu
from .quick_configuration_submenu import headsetconfiguration_submenu
from .quick_configuration_submenu import messagewaitingindicator_submenu
from .quick_configuration_submenu import networkcdp_submenu
from .quick_configuration_submenu import networklldp_submenu
from .quick_configuration_submenu import remotepacketcapture_submenu
from .quick_configuration_submenu import screencapture_submenu
from .quick_configuration_submenu import sipautoanswer_submenu
from .quick_configuration_submenu import sipdebuglogging_submenu
from .web_call_controls_submenu import web_call_controls_submenu
from .web_call_controls_submenu import calldial_submenu
from .simulate_key_events_submenu import simulate_key_events_submenu
from .simulate_key_events_submenu import simulatekeys_submenu


# In[ ]:




