
import random, string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase


# Start Function generateRandomAlphabet
def generateRandomAlphabet(input1,input2,input3):
    letter1 = ""
    letter2 = ""
    letter3 = ""

    if input1 =='v':
        letter1 = random.choice(vowels)
    elif input1 == 'c':
        letter1 = random.choice(consonants)
    elif input1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1 = input1

    if input2 =='v':
        letter2 = random.choice(vowels)
    elif input2 == 'c':
        letter2 = random.choice(consonants)
    elif input2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2 = input2

    if input3 =='v':
        letter3 = random.choice(vowels)
    elif input3 == 'c':
        letter3 = random.choice(consonants)
    elif input3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3 = input3

    return letter1 + letter2 + letter3
# End Function generateRandomAlphabet

input1 = input("What letter do you want? enter 'v' for vowels, 'c' for consonant  \
             and 'l' for any letter " )


input2 = input("What letter do you want? enter 'v' for vowels, 'c' for consonant  \
             and 'l' for any letter " )

input3 = input("What letter do you want? enter 'v' for vowels, 'c' for consonant  \
             and 'l' for any letter " )


#generateRandomAlphabet
for i in range(20):
    genResult = generateRandomAlphabet(input1,input2,input3)
    print(genResult)
