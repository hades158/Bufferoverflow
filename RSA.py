import random

#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e,z):
    r1, s1 = 1, 0 #z = 60 = <1, 0>
    r2, s2 = 0, 1 #e = 37 = <0, 1>
    x = z 	  #save initial value of z into x, since z changes in while loop
    while z!=0:
        q = e//z  	#q = 60//37 = 1 is temp variable performing floor division
        e, z = z, e%z	
        s = r1-q*s1	#s = 1 is temp variable, to replace s1
        r1, s1 = s1, s	#<1 , 0> => <0 , 1>
        t = r2-q*s2	#t = -1 is temp variable, to replace s2
        r2, s2 = s2, t	#<0 , 1> => <1 , -1>
        d = r1		#only need x
    d = d % x
    if(d < 0):
        d += x
    return (d)
    
def is_prime (num):
    if num > 1:   
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    
    z = (p-1)*(q-1)
    n = p * q
    r = 2
    while True:
        if gcd(r,z) == 1:
            break
        else:
            r +=1
    e = r
    d = get_d(e,z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    m = ord(plaintext)
    e = pk[0]
    n = pk[1]
    cipher= pow(m,e,n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext

    d = pk[0]
    n = pk[1]
    m = pow(ciphertext,d,n)
    plain = chr(m)
    return ''.join(plain)
