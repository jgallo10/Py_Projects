#Ceaser Cipher encryption and decryption

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(text = text, shift = shift):
    encrypted = ""
    differance = 26
    if shift > differance:
        while shift > differance:
            differance += differance
    shift = differance - shift
    
    for positon in range(len(text)):
        letter_index = alphabet.index(text[positon]) + shift
        encrypted += alphabet[letter_index]
    print(f"The encoded text is {encrypted}")
    
encrypt(text, shift)
