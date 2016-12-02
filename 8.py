mytext = input(" your toughts here " )
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
result = ''
for letter in mytext:
    if letter not in vowels:
        result += letter
print(result)

"""

pseudocode:

FOR letter IN text
   IF letter NOT IN vowels
      result = result + letter
PRINT result

"""

