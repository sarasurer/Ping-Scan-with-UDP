# Ping-Scan-with-UDP
This program helps to scan ping with UDP instead of ICMP. As we all know, ICMP does not have a port number since it is in the network layer of computer networks. Therefore, with the help of this program, we can find a port number with ping. But I should say that UDP is not a reliable protocol. The entire code is written in Python, IDE is IDLE. I can see the ping with Wireshark. To do this, we have to run this program on the command prompt while Wireshark captures the data.


```
import socket
from socket import *
```


```
python udp.py
```
