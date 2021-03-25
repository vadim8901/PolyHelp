#!/usr/bin/env python
# -*- coding: utf-8 -*-
def check(data):
    if len(data) == 1:
        return False
    else:
        if len(data[0]) == 0 or len(data[1]) == 0:
            return False
        if ' ' in data[0] or ' ' in data[1]:
            return False
        else:
            return True
