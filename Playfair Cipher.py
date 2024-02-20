def c_matrix(key):
    matrix = []
    characters = [chr(i) for i in range(65,91)]

    for i in reversed(key):
        characters.remove(i)
        characters.insert(0,i)

    characters.remove("J")

    i = 0
    while i < 25:
        row = characters[i:i+5]
        matrix.append(row)
        i += 5
    
    return matrix

def ssl(msg):
    index = 0
    while (index<len(msg)):
        l1 = msg[index]
        if index == len(msg)-1:
            msg = msg + 'X'
            index += 2
            continue
        l2 = msg[index+1]
        if l1==l2:
            msg = msg[:index+1] + "X" + msg[index+1:]
        index +=2   
    return msg

def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue

def playfair(key, msg, choice):
    inc = 1
    if choice == '2':
        inc = -1

    matrix = c_matrix(key)
    msg = msg.replace(' ','')
    msg = msg.replace('J','I')
    
    msg = ssl(msg)
    cipher_text=''
    for (l1, l2) in zip(msg[0::2], msg[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: #Rule 2, the letters are in the same row
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:# Rule 3, the letters are in the same column
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: #Rule 4, the letters are in a different row and column
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text

msg = input("Enter the MSG : ").upper()
key = input("Enter the key : ").upper()

choice = input("1.Encrypt \n2.Decrypt \nChoose the option : ")
print("Encrypting ........\nEncrypted MSG : " if choice == '1' else "Decrypting.......\nDecrypted MSG : ")
print(playfair(key,msg,choice))