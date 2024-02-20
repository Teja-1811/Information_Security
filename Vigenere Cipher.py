def cipher(msg,key,data = 1):
    operation = 1
    if data == 2:
        operation = -1
    cipher = []
    for i in range(len(msg)):
        letter = ((ord(msg[i])+(operation*ord(key[i])))%26)+65
        cipher.append(chr(letter))

    return "".join(cipher)

def modify_key(msg,key):
    i = 0
    while True:
        if len(msg) == len(key):
            return key
        key += key[i]
        i += 1

msg = input("Enter the MSG : ").upper().replace(" ","")
key = input("Enter the key : ").upper()

key = modify_key(msg,key)

def choice():
    while True:
        try:
            ch = int(input("1.True\n2.False\nEnter your choice : "))
            if ch < 1 or ch > 2:
                print("Please enter valid option")
                choice()
            return ch
                
        except Exception as err:
            print("Please choose correct option")

print(cipher(msg,key,choice()))