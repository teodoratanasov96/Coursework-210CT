x = input("your toughts here")
org_list = x.split()

new_list = []
def reverse(org_list, new_list):
    word = org_list[-1]
    org_list.remove(word)
    new_list.append(word)
x = len(org_list)
for r in range(x):
    reverse(org_list, new_list)
rev = " ".join(new_list)
print (new_list)

"""
pseudocode:

REVWORDS(wordlist, revlist)
    word <-- wordlist[-1]
    wordlist.REMOVE(word)
    revlist.APPEND(word)

x <-- lenght[wordlist]
for i <-- 0 to x
    REVWORDS(wordlist, revlist)

revstrig <-- " ".join(revlist)
return revstring

"""
