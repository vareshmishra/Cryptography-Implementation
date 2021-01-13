import random

# K is the limit for Largest positive integer upto 
# which we want to generate Prime
K = 1000000

# Global List for Prime Numbers upto K
prime = []
prime = [True for i in range(K + 1)] 

# Utility Functions
# 1. This function will generate prime sieve upto integer n
def generateSieveForPrime(n):
    prime[0]= False
    prime[1]= False
    p = 2
    while (p * p <= n):  
        if (prime[p] == True):       
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1

# 2. GCD using Euclid's Algorithm
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)


# 3. This will pick a random prime number
def pickPrime(n):
    randomElem = random.randrange(2,n+1)
    while(prime[randomElem] != True):
        randomElem = random.randint(2,n)
    return randomElem



'''
This function will pick two prime numbers p and q such 
that p = q = 3 mod 4 and will return n = p*q
'''
def genN(maxValue):
    # Pick prime numbers p and q such that
    # p = q = 3 mod 4
    p = pickPrime(maxValue)
    while(p % 4 != 3):
        p = pickPrime(maxValue)
    
    q = pickPrime(maxValue)
    while(q % 4 != 3 or p == q):
        q = pickPrime(maxValue)
    return p*q



'''
This function will generate a list of Random Bits as specified by 
argument numberOfBits
Input: seed, numberOfBits, N(generated using function genN)
Output: List containing outputbits
'''
def PseudoRandomBitsGenerator(seed, numberOfBits, N):
    x0 = (seed**2)%N
    outputbits = []
    for i in range(0, numberOfBits):
        x0 = (x0**2)%N
        # Extract random bit as last bit of x0
        randomBit = x0 % 2
        outputbits.append(randomBit)
    return outputbits


# Init. Prime List
generateSieveForPrime(K)
N = genN(K)

# Get seed value such that gcd(seed, N) = 1
S = int(input("Enter Seed value less than (which is coprime to) " + str(N) +": "))

while((gcd(N, S) != 1) or S <= 0 or S >= N):
    S = int(input("Enter Seed value less than (which is coprime to) " + str(N) +": "))

numberOfBits = int(input("Enter number of Pseudo Random bits to generate: "))

while(numberOfBits <= 0):
    numberOfBits = int(input("Enter number of Pseudo Random bits to generate: "))
    

print(PseudoRandomBitsGenerator(S, numberOfBits, N))