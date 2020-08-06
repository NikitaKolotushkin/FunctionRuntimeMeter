#!/usr/bin/python3
# -*- coding: utf-8 -*-

def RuntimeMeter(function):
    from datetime import datetime

    def wrapper():
        start = datetime.now()
        function()
        print("[*] Execution time: {0}".format(datetime.now() - start))
    
    return wrapper
