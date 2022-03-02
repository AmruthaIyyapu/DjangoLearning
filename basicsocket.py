import socket

mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org' , 80))

cmd = 'GET htp://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
""" the last two \r\n are to return as a new line. The second new line is used to indicate we are not passing any headers. 
The encode is used to convert the data into UTF-8 format so that we can send it over iternet
"""
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
   print(data.decode(), end = '')
  
 mysock.close()
