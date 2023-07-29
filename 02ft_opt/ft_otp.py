import sys
import argparse
from cryptography.fernet import Fernet

original_stdout = sys.stdout

def encryptKey(args):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encKey = fernet.encrypt(args.encode())
    return encKey
    # print(fernet.decrypt(encKey).decode())

def checkHex(args):
    try:
        int(args, 16)
        return 0
    except:
        print("error: key must be 64 hexadecimal characters.")
        exit(1)

def checkKey(args):
    if len(args) < 64:
        print("error: key must be 64 hexadecimal characters.")
        exit(1)
    checkHex(args)
    file = open("ft_otp.key", "w")
    sys.stdout = file
    print(encryptKey(args))
    sys.stdout = original_stdout

def checkArgs(args):
    for x in args:
        if x == ".":
            return 1
    return 2
    
def main():
    if (len(sys.argv) == 1):
        print("Invalid options: try -h for help")
        exit(1)

    parse = argparse.ArgumentParser(description="")
    parse.add_argument("-g", help="the program receive a hex key of 64 characteres at least.")
    parse.add_argument("-k", help="[file] generate a new temp pass based on the key on the file.")
    args = parse.parse_args()
    if (args.g):
        ret = checkArgs(args.g)
        if ret == 1:
                return
        else:
            checkKey(args.g)
    # elif (args.k):
    #     generatePass()

main()