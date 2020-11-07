def repeating_xor(message,key):
    strlen=len(key)
    meslen=len(message)
    encmes=""
    for i in range(meslen):
        c=chr(ord(message[i]) ^ ord( key[((i+1)%strlen)-1] ) )
        encmes+=c
    print encmes.encode("hex")

def main():
    #f=open("Implement repeating-key XOR.txt","r")
    string="ICE"
    #message=f.read()
    message='Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
    repeating_xor(message,string)

if __name__ == '__main__':
	main()