import random
import math

# Utility Functions

# 1. GCD using Euclid's Algorithm

def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a%b)

# 2. Naive test for primality.

def primeTest(a):
	if(a == 2):
		return True
	if(a < 2 or a % 2 == 0):
		return False
	for i in range(3, int(math.sqrt(a)) + 2, 2):
		if(a % i == 0):
			return False
	return True

# 3. Naive function for calculating 
#    Multiplicative Inverse 

def multiInverse(a, m):
	a = a % m
	for i in range(1, m):
		if((a*i) % m == 1):
			return i
	return 1

# 4 Print string from List.
#   This will print equivalent string of a list
def printStringFromList(inputList):
    output = ""
    for i in inputList:
        output += chr(i)
    print(output)


'''
Keygen : Generates public and private key pairs
Input : Prime numbers p and q
Output: Public Key (e, n) and Private Key (d, n)
'''
def Keygen(p, q):
	if(p == q):
		print("Error, p and q should not be the same")
	if not (primeTest(p) and primeTest(q)):
		print("Error, Please choose prime numbers")

	n = p*q

	EulerToitent = (p-1)*(q-1)

	e = random.randrange(1, EulerToitent)

	g = gcd(e, EulerToitent)
	while(g != 1):
		e = random.randrange(1, EulerToitent)
		g = gcd(e, EulerToitent)

	d = multiInverse(e, EulerToitent)

	#Public Key (e, n)
	pubKey = (e, n)

	#Private Key (d, n)
	pvtKey = (d, n)

	return (pubKey, pvtKey)


'''
Encrypt will encrypt the plaintext using RSA Algorithm
Input : public Key and Plaintext
Output : A list of integer representing cipher text

Note : We are returning a list because we can identify seperate
	   values while decrypting. We can print equivalent ciphertext
	   using utility function.
'''
def Encrypt(pubKey, Plaintext):
	key, n = pubKey
	cipherList = []
	for ch in Plaintext:
		cipherList.append((ord(ch) ** key) % n)

	return cipherList

'''
Decrypt will decrypt the plaintext using RSA Algorithm
Input : private Key and CipherList
Output : Plaintext
'''
def Decrypt(pvtKey, CipherList):
	key, n = pvtKey
	plain = ""
	for ch in CipherList:
		plain += chr((ch ** key) % n)

	return plain

def RSAMain():
    print("Implementation of RSA in Python")
    
    p = int(input("Enter prime p: "))
    q = int(input("Enter another prime number q: "))
    
    print("Generating Public and Private Keys")
    
    publicKey, privateKey = Keygen(p, q)
    
    print("Your public key is ", publicKey )
    print("Your private key is ", privateKey)
    
    plainText = input("Enter Plaintext to encrypt: ")
    
    cipherTextList = Encrypt(publicKey, plainText)
    
    # Print Encrypted CipherText
    print("Printing CipherText after encryption")
    printStringFromList(cipherTextList)
    
    # Print Decrypted PlainText
    print("Printing PlainText after decryption")
    print(Decrypt(privateKey, cipherTextList))