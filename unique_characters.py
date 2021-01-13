string = input("Enter a string : ")

def countLetterAndDigits(string):
    lcount = dcount = 0
    for c in string:

        if c.isalpha():
            lcount+=1
    return lcount, dcount

letters, digits = countLetterAndDigits(string)

print("No of letters/alphabets : ", letters)
