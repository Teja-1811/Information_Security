data = input("Enter MSG : ")
key = int(input("Enter the key : "))
output = ""
output1 = ""

for letter in data:
        num = ord(letter)
        if num in range(65,88) or num in range(97,120):
            output += chr(num+key)
        else:
            output += chr(num-23)


for letter in output:
    num = ord(letter)
    if num in range(65,89) or num in range(97,121):
        output1 += chr(num-key)
    else:
        output1 += chr(32)

print(f"Encrypted MSG : {output}")
print(f"Decrypted MSG : {output1}")