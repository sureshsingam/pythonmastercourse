
import random, string

def generateRandomAlphabet():
    
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercaseg)
    name = letter1 + letter2 + letter3
    return name



print(generateRandomAlphabet())
