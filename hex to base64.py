import base64
h=raw_input()
#h=int(h,16)
b=base64.b64encode(h.decode("hex"))
print b