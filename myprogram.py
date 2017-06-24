
def age_foo(age):
    new_age = int(age) + 50
    return new_age


age = input("Enter your age: ")
ageVal = age_foo(age)
print(ageVal)
