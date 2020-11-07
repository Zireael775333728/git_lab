#!/usr/bin/python3
# -*- coding:utf-8 -*-
import base64
import sys
import pyperclip
from urllib import unquote
a=sys.argv[1]
a=a.strip()
a=a.replace('\r','')
b=base64.b64decode(a)
b=unquote(b)
filename = 'b64result.txt'
with open(filename, 'w') as file_object:
    file_object.write(b)
print b
pyperclip.copy(b)
