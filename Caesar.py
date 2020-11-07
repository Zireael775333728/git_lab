# -*- coding:utf-8 -*-
import sys
import string
a=sys.argv[1]
a=a.strip()
a=a.replace('\r','')
for i in range(1,26):
    b=""
    for j in a:
        if j in string.ascii_letters:
            c=chr(ord(j)+i)
            if ord(c)>ord("z") or (ord(c)>ord("Z") and ord(c)<ord("a")):
                c=chr(ord(c)-26)
        else:
            c=j
        b+=c
    print(i,b)