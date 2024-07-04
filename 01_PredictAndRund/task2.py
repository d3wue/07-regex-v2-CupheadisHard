import re

text = "This book on tennis cost $3.99 at Walmart."

reg2 = re.compile("$This")
match = reg2.search(text)
print(match)
#wird nichts finden. ER sucht nach This am Zeilenende, aber $ macht nur sinn nach dme Wort

reg2 = re.compile("^This")
match = reg2.search(text)
print(match)
#^ sucht am Anfang der Zeile. Was stimmt. Er wird ein match findet

reg2 = re.compile("This^")
match = reg2.search(text)
print(match)
#Wird kein Sinn ergeben, diese ^muss vor dem wort sein

reg2 = re.compile("This$")
match = reg2.search(text)
print(match)
#Sucht nach This am Ende der Zeile was nicht der Fall sit
reg2 = re.compile("Walmart\.$")
match = reg2.search(text)
print(match)
#\. sucht nach einem echten Punkt. In diesem Fall sucht er nach Walmart. am Ende der Zeile was stimmtc.ß<dfghjklöä
