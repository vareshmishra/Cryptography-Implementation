'''
This function takes plaintext and a shift key as input
and produces Caesar cipher based on the shift key.
Input : 
plainText - Plain-text to be encrypted.
shiftKey - a integral value to determine the shift

Output:
cipherText - The encrypted text.
'''
def encrypt(plainText, shiftKey): 
    cipherText = "" 
    for i in range(len(plainText)): 
        char = plainText[i] 
  
        # Case 1 : For uppercase characters 
        if (char.isupper()): 
            # ord(char) returns an integer representing the Unicode 
            ZeroIndexRep = ord(char) - 65
            cipherText += chr((ZeroIndexRep + shiftKey) % 26 + 65) 
  
        # Case 2 : For lowercase characters 
        else: 
            ZeroIndexRep = ord(char) - 97
            cipherText += chr((ZeroIndexRep + shiftKey) % 26 + 97)

    return cipherText 

'''
This function takes ciphertext and a shift key as input
and produces plaintext based on Caesar cipher and shift key.
Input : 
cipherText - Cipher-text to be decrypted.
shiftKey - a integral value to determine the shift

Output:
plainText - The decrypted text.
'''

def decrypt(cipherText, shiftKey): 
    plainText = "" 
  
    for i in range(len(cipherText)): 
        char = cipherText[i] 
  
        # Case 1 : For uppercase characters 
        if (char.isupper()):
            ZeroIndexRep = ord(char) - 65
            plainText += chr((ZeroIndexRep - shiftKey) % 26 + 65) 
  
        # Case 2 : For lowercase characters  
        else: 
            ZeroIndexRep = ord(char) - 97
            plainText += chr((ZeroIndexRep - shiftKey) % 26 + 97)
    return plainText 

  
#check the above function 
text = "SECRET"
s = 4
print("Text  : " + text)
print("Shift : " + str(s)) 
print("Cipher: " + encrypt(text,s))

print("Text : " + decrypt(encrypt(text, s), s))
