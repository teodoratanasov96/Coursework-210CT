n = int(input("enter your number")) 

def check(x): 
    for i in (2, x): 
        if x%i == 0:    
            print ("It's not prime") 
            return 
        else:
            print ("it's prime")
            return
check(n)


"""

pseudocode:

CHECK(x)
 FOR i IN (2, x)
   IF x%i = 0
   RETURN TRUE
 ELSE
   RETURN FALSE

"""
