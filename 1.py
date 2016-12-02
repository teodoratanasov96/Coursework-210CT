import random # 1

org_list = [1, 3, 5, 7, 8, 10, 13] # 1
new_list = [] # 1

def shuffle(org_list, new_list): # 1
    randNum = random.choice(org_list) # 1
    org_list.remove(randNum) # 1
    new_list.append(randNum) # 1

n = len(org_list) # 1

for i in range(n): # n
    
    shuffle(org_list, new_list) # n

org_list = new_list # 1

print(org_list) # 1

# the notation is O(n)



