import os
import sys

class Strongg:
  
  def __init__(self, ip, port):
    self.PORT = 19132
    self.STARTED = true
    self.SERVER_VERSION = "1.1"
    self.ADRESS = "localhost"
    self.startAll()
    
  def startAll():
    print("Starting Strongg server on ip " + self.ADRESS + ":" + self.PORT);
    self.sck = ServerSocket(self.ADRESS, self.PORT)
    
