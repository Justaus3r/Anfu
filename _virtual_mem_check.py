"""
░█████╗░███╗░░██╗███████╗██╗░░░██╗
██╔══██╗████╗░██║██╔════╝██║░░░██║
███████║██╔██╗██║█████╗░░██║░░░██║
██╔══██║██║╚████║██╔══╝░░██║░░░██║
██║░░██║██║░╚███║██║░░░░░╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░v0.3.10
©Justaus3r 2021
Distributed under GPLV3
  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

This file is a part of Anfu,a Tui tool for encrypting files/folder

_virtual_memory_check.py - Module for checking ram usage and showing warnings when exceeds certain limit.
"""
import psutil
import threading
import time
import os

# A function to change states to true,false continiously after some time 
def show_notification_or_not():
    loopconnected = True
    while loopconnected:
        with open('write_notification_bool','w') as _write_notification_bool:
            _write_notification_bool.write('True')
        time.sleep(3)
        with open('write_notification_bool','w') as _write_notification_bool:
            _write_notification_bool.write('False')        
        time.sleep(300)

def show_notification():
    if os.name == 'nt':
        os.system('start _low_ram_notifier.bat &')
    else:
        os.system('chmod +x _low_ram_notifier.sh && xterm -geometry 100x30+400+500 -e ./_low_ram_notifier.sh &')

def _check_ram_usage():
    loopconnected = True  
    while loopconnected:  
        try:
            time.sleep(2)
            ram_info = psutil.virtual_memory()
            percent_used = ram_info[2]
            with open('write_notification_bool','r') as read_notification_bool:
                show_notification_bool = read_notification_bool.read()
            if int(percent_used) > 20 and show_notification_bool == 'True':
                show_notification() 
        except Exception:
            continue
thread_show_notification_or_not = threading.Thread(target=show_notification_or_not)
thread_check_ram_usage = threading.Thread(target=_check_ram_usage)
thread_show_notification_or_not.start()   
thread_check_ram_usage.start()
