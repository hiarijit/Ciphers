alphabet = "abcdefghijklmnopqrstuvwxyz"
x = input("Enter the ciphertext(in capital letters) to be broken : ")
print()
for i in range(26):
    string = ""
    for j in range(len(x)):
        if x[j] in alphabet:
            for k in range(len(alphabet)):
                if alphabet[k] == x[j].lower():
                    string += alphabet[(k + i) % 26]
                    break
        else:
            string += x[j]
    print(string)

