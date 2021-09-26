# python_broadcaster
Python Client and Server Broadcaster. Used for sending strings over the internet one way. 

This repository includes two files, a server file that allows connections from the client file and the client file will listen for a broadcast from the server file. 
In the event that the server file broadcasts a string the client will decode the string and print it out on the terminal. The strings are only trasferred one way so the server file can send strings and a client file can only listen.

Syntax: 
On the server file anything you enter will be sent as a string to the client file to be displayed on the client computer.
If you enter "dcusrs" on the server file it will instead of displaying a string it will close all the client connections and terminate the client script on all client computers.
