n = int(input("your number here "))

def perfsqr(n):
    x=0
    while True:
        x = x + 1

        if (x*x) > n:
            print((x-1)*(x-1))
            break
    return

perfsqr(n)

#pseudocode:

#PERFECT_SQUARE(num)
    #x <-- 0
    #while True
        #x <-- x + 1
        #if (x*x) > num
            #output((x-1)*(x-1))
