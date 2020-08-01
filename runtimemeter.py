#!/usr/bin/python3
# -*- coding: utf-8 -*-


def RuntimeMeter(function):
    import time

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print("[*] Execution time: {0}".format(end - start) + "s")

    return wrapper