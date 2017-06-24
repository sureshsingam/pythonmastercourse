print(1)
''' Create function
'''

def currency_converter(rate,euros):
    dollars = euros*rate
    return dollars

def minutes_to_hours(seconds, minutes=70):
    hours = minutes/60 + seconds/3600
    return hours


#call minutes to hours (pass in seconds value, minutes uses default minutes)
answer_hours = minutes_to_hours(70)
print("Answer in hours is %f" % answer_hours)
print("answer without formatting", answer_hours)
print("Using String formatting:\n\
\tFirst input has 2 decimal values  {:.2f} \n\
\tSecond input has \
5 decimal values {:.5f} ".format(answer_hours,answer_hours))

#call function with both inputs
answer_hours = minutes_to_hours(3600,3600)
print("Answer in hours is %f" % answer_hours)
print("answer without formatting", answer_hours)
print("Using String formatting:\n\
\tFirst input has 2 decimal values  {:.2f} \n\
\tSecond input has \
5 decimal values {:.5f} ".format(answer_hours,answer_hours))
