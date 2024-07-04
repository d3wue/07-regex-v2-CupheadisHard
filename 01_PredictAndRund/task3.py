import re

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
string = "\."
print("Hello World")
reg = re.compile(".")
print(reg.match(string)) #Match \\ weil . ein Platzhalter ist
print(reg.findall(string))# Match einmal \\ und einmal ein .

reg = re.compile("\.")
print(reg.match(string))
print(reg.search(string))

reg = re.compile("\\\\")
print(reg.match(string))

reg = re.compile("\\\\.")
print(reg.match(string))

reg = re.compile("\\\\\.")
print(reg.match(string))

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("is")
match = re.findall(reg, text)
print(match)
#Findet zwei is
reg = re.compile("\d")
match = re.findall(reg, text)
print(match)
# \d matches ein digit
text = "This book on tennis cost $893.99 at Walmart."
reg=re.compile("\$\d+\.\d{2}")
match=re.search(reg,text)
print(match)
#$ must be escaped since $ a command for python ist.