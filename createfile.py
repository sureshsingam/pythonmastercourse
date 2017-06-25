import datetime

def createfile():
    todays_date = datetime.datetime.now()
    todays_date= todays_date.strftime("%Y-%m-%d-%H-%M-%S")
    with open("file-{}.txt".format(todays_date),"w") as file:
        file.write("File was created on {}\n".format(todays_date))


createfile()
