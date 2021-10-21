print("Starting")

wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip
  unzip ngrok-stable-linux-386.zip
./ngrok authtoken 1zjUyneuN2WVwmRvii8G83KK5cH_5LxMMFUzWrkysJzGvmhBU
./ngrok http 80
print("Successful")
