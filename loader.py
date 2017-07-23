import sys
import os
os.chdir(os.path.realpath(sys.argv[0]).replace(os.sep + "loader.py", "))
import platform
if platform.system() == "Linux":
  print("Strongg does not support Linux Devices!")
  
if sys.version_info > (3,2):
  print("Update your Python version to version 3.2 or higher!")
  print("You can download it on http://python.org/downloads")
elif platform.system() == "Windows":
  //Construct Strongg class
   
