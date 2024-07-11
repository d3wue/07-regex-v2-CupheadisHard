import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here
reg=re.compile("^([0-9a-f]{4}:){7}([0-9a-f]{4})$")
m = reg.match("2001:0db8:85a3:0000:0000:8a2e:0370:7343")
print(m)

#regv4=re.compile("([0-9]{1,3}\.){3}([0-9]{1,3})")
regv4 = re.compile("^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})){3}$")


