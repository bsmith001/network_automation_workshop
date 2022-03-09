import re


rconf = """
Building configuration...
Current configuration : 5878 bytes!! 
Last configuration change at 16:01:10 UTC Sat Oct 9 2021
!
version 16.12
service timestamps debug datetime msec
service timestamps log datetime msec
! Call-home is enabled by Smart-Licensing.
service call-home
platform qfp utilization monitor load 80
platform punt-keepalive disable-kernel-core
platform console serial
!
hostname rtr1
!
boot-start-marker
boot-end-marker
!
"""

def main():
    result = re.search(r"version \d{2}\.\d{2}", rconf)
    print(result)
    print(type(result), dir(result))



if __name__ == "__main__":
    main()
