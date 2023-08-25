#Ceaser Cipher encryption and decryption

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


def ceaser(begin_text, amount_shifted, which_cipher):
    final_text = ""
    alphabet_length = len(alphabet)
    if which_cipher == "decode":
            amount_shifted *= -1        
    for letter in begin_text:
        letter_index = alphabet.index(letter) + amount_shifted  
        if letter_index > alphabet_length or letter_index < 0:
            letter_index = letter_index % alphabet_length  
        final_text += alphabet[letter_index]
    print(f"The final text is {final_text} \n")
        
        
ceaser(begin_text=text, amount_shifted=shift, which_cipher=direction )
        





#..................................................Longer version..........................................................................
""" #Create fucntion
def encrypt(text = text, shift = shift):
    
    #Create empty string to input cipher 
    encrypted = ""
    
    #loop to encrypt the text input
    for position in range(len(text)):
        letter_index = alphabet.index(text[position]) + shift
        while letter_index > alphabet_length:
            letter_index -= alphabet_length
        encrypted += alphabet[letter_index]
    print(f"The encoded text is {encrypted} \n")



def decrypt(text = text, shift = shift):
    
    decryption = ""
    for position in range(len(text)):
        letter_index = alphabet.index(text[position]) - shift
        while letter_index < 0:
            letter_index += alphabet_length
        decryption += alphabet[letter_index]
    print(f"The decoded text is {decryption} \n")
    
    
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Sorry you have to pick 'encode' or 'decode'.")
     """