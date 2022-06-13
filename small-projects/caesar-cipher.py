# Caesar cipher program
# Tristan Hinsley

def parseInt(string):
    try:
        value = int(string)
    except ValueError:
        value = string + " is not an integer."
    return value

def cipherEncrypt(plaintext, cipherKey):
    encryptedCiphertext = ''
    for i, x in enumerate(plaintext):
        encryptedCiphertext[i] = plaintext[i] + cipherKey

    return encryptedCiphertext

def cipherDecrypt(ciphertext, cipherKey):
    decryptedPlaintext = "Decrypted: " + ciphertext
    return decryptedPlaintext

print("Caesar Cipher, written by Tristan Hinsley")
userEncryptResponse = input("Do you want to (e)ncrypt or (d)ecrypt?\n")
while userEncryptResponse != "e" and userEncryptResponse != "d":
    print("Invalid reponse: Please try again.")
    userEncryptResponse = input("Do you want to (e)ncrypt or (d)ecrypt?")

userKeyResponse = input("Please enter the key (0 to 25) to use: \n")
cipherKey = parseInt(userKeyResponse)
while cipherKey < 0 or cipherKey > 26:
    print("Invalid reponse: Please try again.")
    userKeyResponse = input("Please enter the key (0 to 25) to use.")
    cipherKey = parseInt(userKeyResponse)

userResponse = input("What message would you like to encrypt or decrypt?\n")
if userEncryptResponse == "e":
    encryptedText = cipherEncrypt(userResponse, cipherKey)
    print(encryptedText)
elif userEncryptResponse == 'd':
    decryptedText = cipherDecrypt(userResponse, cipherKey)
    print(decryptedText)
else:
    print("I'm not sure how you got here homie")


