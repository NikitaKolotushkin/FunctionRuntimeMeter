#!/usr/bin/python3
# -*- coding: utf-8 -*-


def RuntimeMeter(function):
    import time

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f'[*] Execution time: {start - end}")

    return wrapper