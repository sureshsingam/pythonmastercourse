import time
from datetime  import datetime as dt

host_path = r'C:\Windows\System32\drivers\etc\hosts'
host_temp = r'C:\Users\Suresh\Documents\GitHub\Python_MasterCourse\blocker_app\hosts'
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.hotmail.com","hotmail.com", "outlook.live.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 14) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 20):
        print("Working hours")
        #read the host file
        with open(host_path,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    print(website + " is in host" )
                else:
                    print(website + " added to host")
                    file.write("\n" + redirect + " " + website)
    else:
        print("Fun Hours")
        # Remove the restriction from the host files
        with open(host_path,"r+") as file:
            content=file.readlines()
            file.seek(0)
            file.truncate()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)


    time.sleep(5)
