#!/usr/bin/env python
"""
This Python script returns a free network port. 
You can optionally, on Linux only and requiring sudo specify the network interface.
"""
import socket


SO_BINDTODEVICE=25 #http://stackoverflow.com/questions/8437726/can-python-select-what-network-adapter-when-opening-a-socket

def freeport(iface=None):
    s = socket.socket()

    if iface: # Linux only, requires sudo
        s.setsockopt(socket.SOL_SOCKET, SO_BINDTODEVICE, bytes(iface,'utf8'))

    s.bind(('',0))
    port = s.getsockname()[1]
    s.close() #slight race condition

    return port

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('-i','--iface',help='network interface to use (requires Linux and sudo)')
    p = p.parse_args()

    port = freeport(p.iface)

    print(port)
