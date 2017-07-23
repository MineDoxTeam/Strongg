import sys
import socket

class ServerSocket:
  
  def __init__(self, host, port):
    self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.PORT = port
    self.ADRESS = host
    try:
            self.sck.bind((self.HOST, self.PORT))
    except self.sck.error:
            print("Error! Perhaps server is running on this port!")
    finally:
            self.sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sck.listen(5)
            threading.Thread(target=self.listenPackets, daemon=True).start()
            
    def listenPackets(self):
      print("Listening:D")
