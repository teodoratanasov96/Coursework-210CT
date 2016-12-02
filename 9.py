orglist = [1, 2, 3, 5, 10, 19, 23, 51]
minrange = 11
maxrange = 15
def binsearch(orglist,minrange,maxrange ):
    
    first = 0
    last = len(orglist)-1
    found = False
    
    while first <= last and not found :
        
        midpoint = (first + last)//2
        
        if orglist[midpoint] in range(minrange,(maxrange+1)):
            found = True
        else:
            if orglist[midpoint] > minrange:
                last = midpoint - 1
            else:
                first = midpoint + 1

    print(found)
    return found
    

binsearch(orglist, minrange, maxrange)
#The notation is O(logn)

"""

pseudocode:

BINARYSEARCH(orglist, minrange, maxrange)
    
    first <-- 0
    last <-- len(orglist)-1
    found <-- False

    WHILE first<=last and found
        mid <-- (first+last)//2

        IF orglist[midpoint] <-- minrange to maxrange+1
            found = True
        ELSE
            if orglist[midpoint] > minrange
                last <-- mid - 1
            ELSE
                first <-- mid + 1
    RETURN found

BINARYSEARCH(orglist, minrange, maxrange)
""" 
