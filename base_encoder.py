#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Author : By HiFeV - 10/04/2021

import base64
import sys

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("usage : %s --help" % (sys.argv[0]))
        exit(1)
    
    elif sys.argv[1] == "-eb16":
        print("Encoded in base16 : %s " % (base64.b16encode(sys.argv[2].encode("utf-8")).decode("utf-8")))
    
    elif sys.argv[1] == "-db16":
        print("Decoded in base16 : %s " % (base64.b16decode(sys.argv[2]).decode("utf-8")))
    
    elif sys.argv[1] == "-eb32":
        print("Encoded in base32 : %s " % (base64.b32encode(sys.argv[2].encode("utf-8")).decode("utf-8")))
    
    elif sys.argv[1] == "-db32":
        print("Decoded in base32 : %s " % (base64.b32decode(sys.argv[2]).decode("utf-8")))
    
    elif sys.argv[1] == "-eb64":
        print("Encoded in base64 : %s " % (base64.b64encode(sys.argv[2].encode("utf-8")).decode("utf-8")))
    
    elif sys.argv[1] == "-db64":
        print("Decoded in base64 : %s " % (base64.b64decode(sys.argv[2]).decode("utf-8")))
    
    elif sys.argv[1] == "--help":
        print("Dev by HiFeV - https://github.com/HiFeV")
        print("command  /   descriptions")
        print("--help   /   show this page")
        print("-eb16    /   encode in base16")
        print("-db16    /   decode in base16")
        print("-eb32    /   encode in base32")
        print("-db32    /   decode in base32")
        print("-eb64    /   encode in base64")
        print("-db64    /   decode in base64")

    else:
        print("[-] Error base not found !")