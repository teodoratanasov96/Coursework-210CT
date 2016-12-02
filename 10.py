org_list = [71, 21 , 41 ,1 ,6 ,10 ,24 ,35]
new_list = [0]
last_list = []

def maxlen(list):
    global new_list
    for i in list:
        if i > new_list[-1]:
            new_list.append(i)
        elif i <= new_list[-1]:
            if (len(new_list) - 1) > len(last_list):
                last_list.clear()
                for n in new_list:
                    last_list.append(n)
                last_list.remove(0)
                new_list = [0, i]
            elif (len(new_list) - 1) <= len(last_list):
                new_list = [0]
    if (len(new_list) - 1) > len(last_list):
        last_list.clear()
        for n in new_list:
            last_list.append(n)
        last_list.remove(0)

maxlen(org_list)
print(last_list)


