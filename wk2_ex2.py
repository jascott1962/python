#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 5

def login_telnet(IP_ADDR, USERNAME, PASSWORD):

    remote_conn = telnetlib.Telnet(IP_ADDR, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until("ogin:", TELNET_TIMEOUT)
    remote_conn.write(USERNAME + "\n")
    output += remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(PASSWORD + "\n")
    time.sleep(1)
    output += remote_conn.read_very_eager()
    print output
    return remote_conn

def send_command(remote_conn, cmd):
    remote_conn.write(cmd + "\n")
    time.sleep(1)
    output = remote_conn.read_very_eager()
    return output

def main():

    IP_ADDR = "184.105.247.70"
    USERNAME = "pyclass"
    PASSWORD = "88newclass"

    remote_conn = login_telnet(IP_ADDR, USERNAME, PASSWORD)
    output = send_command(remote_conn,"show ip int brief")
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()
