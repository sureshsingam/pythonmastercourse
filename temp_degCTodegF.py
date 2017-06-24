
def celciusToFahrenheit(celcius):
    return (celcius*9/5) + 32

userVal = input("Enter temp in celcius: \t")
userValConvert = celciusToFahrenheit(int(userVal))
print("Temperature in celcius in 2 decimal degree {:.2f}: ".format(userValConvert))
