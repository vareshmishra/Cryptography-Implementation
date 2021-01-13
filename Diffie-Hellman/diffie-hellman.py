def DiffieHellman(publicPrime, publicPrimitiveRoot, secretKeyA, secretKeyB):
    
    print("Public Prime : " + str(publicPrime))
    print("Public Primitive Root : " + str(publicPrimitiveRoot))
    
    print("SecretKey for A : " + str(secretKeyA))
    print("SecretKey for B : " + str(secretKeyB))
    
    
    '''
    A should compute
    x = (publicPrimitiveRoot)^secretKeyA mod publicPrime
    '''
    x = pow(publicPrimitiveRoot, secretKeyA) % publicPrime
    
    
    
    '''
    B should compute
    y = (publicPrimitiveRoot)^secretKeyB mod publicPrime
    '''
    y = pow(publicPrimitiveRoot, secretKeyB) % publicPrime
    
    
    
        
    '''
    At Receiving End :
    A should compute 
    
    sharedKeyA = y^secretKeyA mod PublicPrime
    '''
    sharedKeyA = pow(y, secretKeyA) % publicPrime
    
    
    '''
    At Receiving End :
    B should compute 
    
    sharedKeyB = x^secretKeyB mod PublicPrime
    '''
    sharedKeyB = pow(x, secretKeyB) % publicPrime
    
    
    
    # If sharedKeyA == sharedKeyB
    # Return sharedKey
    # Else error
    
    if(sharedKeyA == sharedKeyB):
        print("Shared Key : " + str(sharedKeyA))
    else:
        print("Error")


