#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

scan_ports = [21,22,23,25,53,80,139,443,445,1433,1521,2049,3306,3389,5945,5985,8080,8443,9090,9443,5900,389,636,8000,27017,27108,27019]

def scan_ip(ip):
    # Clear the screen
    subprocess.call('clear', shell=True)    

    # Ask for input
    remoteServer    = ip
    remoteServerIP  = socket.gethostbyname(remoteServer)    

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60    

    # Check what time the scan started
    t1 = datetime.now()    

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)    

    # We also put in some error handling for catching errors    

    try:
        i = 0
        while i < len(scan_ports):
            port = scan_ports[i]
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()
            i += 1    

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()    

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()    

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()    

    # Checking the time again
    t2 = datetime.now()    

    # Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1    

    # Printing the information to screen
    print 'Scanning Completed in: ', total

def main():
    ip_list = "/tmp/ips.txt"
    lines = [line.rstrip('\n') for line in open(ip_list)]
    for line in lines:
        ip = line
        scan_ip(ip)

if __name__ == "__main__":
    main()
