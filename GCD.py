
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)
a = int(input("Enter first value:"))
b = int(input("Enter second value:"))
GCD = gcd(a, b)
print("GCD is ",GCD)
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
