#!/usr/bin/python3
def uppercase(str):
    for m in str:
        if(65 <= ord(m) <= 122):
           if(97 <= ord(m) <= 122):
              m = chr(ord(m) - 32)
        print("{:s}".format(m), end="")
    print("")
