#  in building HAkcing tools you must understand some error 
# occur soo you must provide statmenets and code to urn incase these errorr  happen 

 # in this scenario we are going to check for Connectivity Error

# Python Libary for Networking
import  socket

try:
    s = socket.socket()  # creating a socket Object
    s.settimeout(1) # settng the time out fo thesocket connectonm to 1s
    s.connect(("192.168.1.2", 80)) # checking if an Ip allows connecton to its port 80  ( http )
    print("Port Open") 
except socket.timeout: # if the socmet connection timesout
    print("Time Out") # print messafe to let user know what type of t Error 
except ConnectionRefusedError: # chekcing if the connection wad refused by the  remote HOST
    print("Port Closed") #  error messafe to print out to user
except Exception as e: # incase if any other Error Return this 
    print(f"Unknown Error: {e}")
finally:
    s.close()  # close the socket connection