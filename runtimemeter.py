#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def RuntimeMeter(function) -> str:
    from datetime import datetime

    def wrapper():
        start = datetime.now()
        function()
        print(f"[*] Execution time: {datetime.now() - start}")

    return wrapper
