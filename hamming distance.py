def hamming(a,b):
    a=a.encode("hex")
    b=b.encode("hex")
    if len(a)!=len(b):
        return -1
    x=bin(int(a,16)^int(b,16))
    string=str(x)[2:]
    num=0
    for i in string:
        if i == "1":
            num+=1
    return num
    

def main():
    a=raw_input()
    b=raw_input()
    print hamming(a,b)

if __name__ == '__main__':
	main()