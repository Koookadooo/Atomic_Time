import socket
import time

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

# create a socket object nicknamed s
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to time.nist.gov on port 37
    host_port = ('time.nist.gov', 37)
    s.connect(host_port)

    # receive the time from the server and decode from bytes to int
    data = s.recv(1024)
    data = int.from_bytes(data, byteorder='big')
    print(data)

    # close the socket
    s.close()

# print the number of seconds since 1900 on the system
print(system_seconds_since_1900())
