import os
import time


uname = os.uname()

ASCII_LOGO = """                 
  %%%%%%%%%%%    
 %%%        %%%  
%%%          %%  
 %%%        %%   
   %%%   %%%     
%%%%%%   %%%%%%  
                 
                 
"""

sys_info = (
  uname["sysname"],
  len(uname["sysname"])*"-",
  "OS: " + uname["release"],
  "Host: " + uname["machine"],
  "Uptime: " + str(time.monotonic()),
  "Shell: " + "µpython " + uname["version"],
  "Resolution: 320x240",
  "MCU: " + ("STM32F730V8T6" if uname["machine"] == "NumWorks N110" else "STM32F412"),
  "Memory: " + ("8Mo" if uname["machine"] == "NumWorks N110" else "1Mo"),
  "RAM: " + ("256Ko" if uname["machine"] == "NumWorks N110" else "1Mo"),
  "Screen: " + ("IPS-LCD" if uname["machine"] == "NumWorks N110" else "TFT-LCD")
)

def numfetch():
  for line, info in zip(ASCII_LOGO.split("\n"), sys_info):
    print(line + info)
 
