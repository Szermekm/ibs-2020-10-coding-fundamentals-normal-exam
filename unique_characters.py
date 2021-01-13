string = input("Enter a string : ")

def countLetter(string):
    lcount = dcount = 0
    for c in string:

        if c.isalpha():
            lcount+=1
    return lcount, dcount

letters, digits = countLetter(string)

print("No of letters: ", letters)

s = "anagram"

list2 = (list(s))

print(list2)

unique = []
for s in list2:
    if s not in unique:
        unique.append(s)

print(unique)