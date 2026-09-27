letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
choice = 'yes'

# single method for encode and decode
def caesar(msg, shiftNum, encode_or_decode):
    output = ""
    for letter in msg:
        if encode_or_decode == "decode":
            shiftNum *= -1
        pos = letters.index(letter) - shiftNum
        pos %= len(letters)
        output += letters[pos]
    print("Encoded message:", output)

# For Encoding
def encrypt(msg, shiftNum):
    cipher = ""
    for letter in msg:
        if letter not in letters:
            cipher += letter
        else:
            pos = letters.index(letter) + shiftNum
            pos %= len(letters)
            cipher += letters[pos]
    return cipher

# For Decoding
def decrypt(msg, shiftNum):
    decipher = ""
    for letter in msg:
        if letter not in letters:
            decipher += letter
        else:
            pos = letters.index(letter) - shiftNum
            pos %= len(letters)
            decipher += letters[pos]
    return decipher

while choice == 'yes':
    value = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if value == "encode":
        print("Encrypting...")
        msg = input("Type your message:\n")
        shiftNum = int(input("Type your shift number:\n"))
        txt = encrypt(msg.lower(),shiftNum)
        print("Encrypted message:", txt)

    elif value == "decode":
        print("Decrypting...")
        msg = input("Type your message:\n")
        shiftNum = int(input("Type your shift number:\n"))
        txt = decrypt(msg.lower(),shiftNum)
        print("Decrypted message:", txt)

    else:
        print("Please type 'encode' or 'decode'")

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")


