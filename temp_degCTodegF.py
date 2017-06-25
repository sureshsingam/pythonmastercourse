
def celciusToFahrenheit(celcius):
    if float(celcius) < -273.15:
        return "Cannot process conversion of temperatures lower than -273.15"
    else:
        return "{:.2f} Fahrenheit".format((celcius*9/5) + 32)
'''
userVal = input("Enter temp in celcius: \t")
if float(userVal) < -273.15:
    print("Cannot process conversion of temperatures lower than -273.15")
else:
    userValConvert = celciusToFahrenheit(float(userVal))
    print("Temperature in celcius in 2 decimal degree {:.2f}: ".format(userValConvert))
'''
temperatures=[10,-20,-289,100]

for temp in temperatures:
    print(" {0} celsius  is {1} ".format(temp,celciusToFahrenheit(temp)))
