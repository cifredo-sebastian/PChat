# PChat

#### Introduction
  Accessible programming language that provides easy UDP based server communication between two or more devices. UDP allows lower bandwidth and latency for simple messages.
  
#### Commands
  1.	open – Opens a server for receiving messages.
  2.	set (IP Address) – Write set followed by the IP Address of target computer.
  3.	connect – Once the target IP Address is established, connects to target server.
  4.	send ‘message’ – Sends a message to target server. Write message enclosed between single quotation marks.
  5.	close – Closes the sender server.

#### Installation and Instructions

###### Requirements:
  •	Python
  
  •	PLY

###### Receiver
  1.	Run parser.py using Python.
  2.	Write open to open server for receiving.

###### Sender
  1.	Run parser.py using Python.
  2.	Find the IP Address of the target computer you which to communicate to, then write set (XXX.XXX.XXX.XXX) (e.g. set (192.168.0.12)).
  3.	Write connect to initiate connection between servers.
  4.	Write send followed by your message enclosed between single quotation marks (e.g. send ‘hello’).
  5.	Write close to terminate connection once you’re finished.

###### Developers
Sebastian Cifredo
Carlos Machin
Project for University of Puerto Rico in Mayaguez Programming Languages course by Dr. Wilson Rivera.
