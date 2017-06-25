emails=["suresh@gmail.com","someone@yahoo.com","they@gmail.com"]

for email in emails:
    if 'gmail' in email:
        print("gmail address is {}\n\t".format(email))



names = ['james','john','jack']
email_domains=['gmail','hotmail','yahoo']

for i,j in zip(names,email_domains):
    print("Name and e-mail domains at the same time {} {}".format(i,j))
