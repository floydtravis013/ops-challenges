#!/users/fuzzh python

# Description: If i'm green i only show to the readers
# Author : T
# LastUpdated: 11/30/2021

import socket
import sys

#Function Definition does not execute intil function invocation

def simple_math(nums):
    total = 0
    for item in nums:
        total += int(item)
        print("  [~] running total: ",total)
        
    print("[+]What is the sum of your numbers?", total)

# Function Definion

def main(args):
    # DO SOME WORK
    
def get_host_ip():
    host = socket.getaddrinfo(socket.gethostname(), 1)
    print(host)

    host = socket.getaddrinfo(socket.gethostname(), 1)


if __name__ == '__main__':
 # Function Execution
    main(sys.argv)
