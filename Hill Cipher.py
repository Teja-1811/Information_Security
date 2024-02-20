import numpy as np

def createMatrix(data):
    matrix = []
    for i in range(0,len(data),3):
        row = []
        for j in range(3):
            row.append(ord(data[i+j]) % 65)
        matrix.append(row)
    return matrix

def cipher(key,msg,data = 1):
    key = createMatrix(key)
    msg = createMatrix(msg)
    if data == 2:
        key = MatrixInverse(key)

    hill_cipher = []

    for i in msg:
        for j in range(len(key)):
            a = ((i[0]*key[j][0]+i[1]*key[j][1]+i[2]*key[j][2]) % 26) + 65
            hill_cipher.append(chr(a))
    return "".join(hill_cipher)

def MatrixInverse(K):
    det = int(np.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = np.delete(Dji, (j), axis=0)
            Dji = np.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv

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

while True:
    key = input("Enter the key : ").upper()
    if len(key) == 9:
        msg = input("Enter the MSG : ").upper().replace(" ","")
        while len(msg) % 3 != 0:
            msg += "X"
        break
    else:
        print("Enter the key of length 9")

print(cipher(key,msg,choice()))