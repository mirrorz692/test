import os

print("Starting")

os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip")
os.system("unzip ngrok-stable-linux-386.zip")
os.system("./ngrok authtoken 1zjUyneuN2WVwmRvii8G83KK5cH_5LxMMFUzWrkysJzGvmhBU")
os.system("./ngrok http file:////")
print("Successful")
