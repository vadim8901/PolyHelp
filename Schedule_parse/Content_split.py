#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Schedule_parse import Schedule_parser


def content_split():
    result = ''
    content = Schedule_parser.parse()
    for item in content:
        result += item.split('{}')

content_split()