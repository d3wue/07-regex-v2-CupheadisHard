import re
"""
reg = re.compile("www.google.de|com")
print(reg.search("www.google.com"))
#Hier findet er ein match von com nur. Zuerst prüft er das ganze mit.de aber weil er das nicht findet sucht er NUR nach com


reg = re.compile("www.google.de|com")
print(reg.match("www.google.com"))
#Das findet er nicht. Denn er sucht nach dem Anfang. Er findet www.google.de nicht dann prüft er auf com. Aber das ist ja nicht am Anfang


reg = re.compile("www.google.(de|com)")
print(reg.match("www.google.com"))
#So würde es funktionieren er such nicht zuerst nach dem sondern gleichzeitig nach beiden Ausdrücken

reg = re.compile("www\.google\.(de|com)")
print(reg.match("www.google.de")) #Match auf diesen
print(reg.match("wwwwgoogle.de"))#Kein match. Denn es keinen echten . zwischen www und google gibt
#
string = "Niko Stein"

reg = re.compile("Nikolai Stein")
print(reg.match(string))
#Nicht match. ER sucht nach Nikolai Stein nicht nach Niko Stein
reg = re.compile("Niko Stein")
print(reg.match(string))
#Das findet er. Er sucht nach Niko Stein
reg = re.compile("Niko|Nikolai Stein")
print(reg.match(string))
#Es wurde nur nicht finden. Er sucht er entweder NIko am Anfang oder Nikolai Stein. Aber NIko ist zuerst. Er findet Niko
reg = re.compile("(Niko | Nikolai) Stein")
print(reg.match(string))
#None, weil die Leerzeichen nicht passen. Sonst gäbe es doppelt Leerzeichen
reg = re.compile("(Niko|Nikolai) Stein")
print(reg.match(string))
#Hier findet er Niko Stein
"""
string = "\."
reg = re.compile(".")
print(reg.match(string)) #Match \\ weil . ein Platzhalter ist
print(reg.findall(string))# Match einmal \\ und einmal ein .
#If a string which we are trying to match has a \ python will output \\ just to clarify that it is a real backslash
reg = re.compile("\.")
print(reg.match(string))# It will match nothing. Since match is comparing the beginning but the beginning of the string is \
print(reg.search(string)) #It will match . 
string="\."
reg = re.compile("\\\\") #We have 2 real backslashes
print(reg.match(string))

reg = re.compile("\\\\\\.")
print(reg.match(string))

reg = re.compile("\\\\\.")
print(reg.match(string))

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("is")
match = reg.findall(text)
print(match)
#Findet zwei is
reg = re.compile("\d")
match = reg.findall(text)
print(match)
# \d matches ein digit
text = "This book on tennis cost $893.99 at Walmart."
reg=re.compile("\$\d+\.\d{2}")
match=re.search(reg,text)
print(match)
#$ must be escaped since $ a command for python ist.

print("What is your name\\")
print("\\\.")