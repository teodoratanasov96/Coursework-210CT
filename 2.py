import math # 1

n = int(input("your number here")) # 1
x = math.factorial(n) # 1
count = 0 # 1

while True: # n
    
    check = x%10 # n
    x = x//10 # n
    
    if check==0: # n
        count = count+1 # ?n
    elif check!=0: # n
        break # ?n

print(count) # 1

#the notation is O(n)
