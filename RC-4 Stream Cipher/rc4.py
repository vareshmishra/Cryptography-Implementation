# Utility Functions

# This function takes in string as input and 
# returns a list containing ASCII equivalent
# of key
def convertKeyToIntegerList(s):  
    outputList = []
    for i in range(0, len(s)):
        outputList.append(ord(s[i]))
    return outputList

# Print string from List.
# This will print equivalent string of a list
def printStringFromList(inputList):
    output = ""
    for i in inputList:
        output += chr(i)
    print(output)
    
 

'''
Key Scheduling Algorithmn as defined for RC-4. 
This is the Initial Permutation of S
Input : List containing ASCII equivalent integer of Key
Output : State Vector represented by Python List
''' 
def KeySchedulingAlgorithm(key):
    keylength = len(key)
    
    # Initialize StateVector S
    S = []
    for i in range(0, 256):
        S.append(i)
        
    j = 0
    for i in range(0, 256):
        # This step will take care of both the cases
        # Key Length < 256 and Key length = 256
        j = (j + S[i] + key[i % keylength]) % 256
        # Performing swap
        S[i], S[j] = S[j], S[i]
    return S


'''
This module will generate Keystream and yield one
at a time.
Input : State Vector S
Yield : Keystream(one element at a time)
'''
def Keygen(S):
    i = 0
    j = 0    
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        K = S[t]
        yield K



'''
This module takes produces a list of integer containing ciphertext
Input : Plaintext stream represented as a list and key as string
Output : Ciphertext represeted as list of integers
'''
def Encrypt(plaintext, key):
    StateVector = KeySchedulingAlgorithm(convertKeyToIntegerList(key))
    keystream = Keygen(StateVector)
    
    ciphertext = []
    for char in plaintext:
        ciphertext.append(ord(char) ^ next(keystream))
    return ciphertext



'''
This module takes produces a list of integer containing plaintext
Input : Ciphertext stream represented as a list and key as a string
Output : Plaintext represeted as list of integers
'''
def Decrypt(ciphertext, key):
    StateVector = KeySchedulingAlgorithm(convertKeyToIntegerList(key))
    keystream = Keygen(StateVector)
    
    plaintext = []
    for i in ciphertext:
        plaintext.append((i ^ next(keystream)))
    return plaintext


# Output testing
key = input("Please enter Key: ")
plainText = input("Please input Plaintext: ")

# Encrypting
ct = Encrypt(plainText, key)
printStringFromList(ct)

# Decrypting
pt = Decrypt(ct, key)
printStringFromList(pt)