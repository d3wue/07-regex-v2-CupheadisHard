import re

reg = re.compile("(https?://)*www\.[a-zA-Z0-9\.\-]+\.(de|com)[a-zA-Z0-9\.\-/]*") #Punkt innerhalb von Exkigen Klammern ist ein echter .

m = reg.match("www.google.com")
print(m)

m = reg.match("https://www.youtube.com")
print(m)

m = reg.match("http://www.uni-wuerzburg.de")
print(m)

m = reg.match("www.wiwi.uni-wuerzburg.de/wiba/startseite/")
print(m)