import re

text = "This book on tennis cost $3.99 at Walmart."

reg1 = re.compile("ten")
match = reg1.match(text)
print(match)
#Hier wird er nichts finden. ER sucht "ten" in der variablen text am Anfang. MATCH ist am anfang
reg2 = re.compile("this")
match = reg2.match(text)
print(match)
#hier wrid er nichts finden, denn this =! This
reg3 = re.compile("This")
match = reg3.match(text)
print(match)
print(match.group(0))
#Hier wird er was finden. Er druckt das auch in range (0,4) 4 ist nicht drinnen
match = reg1.search(text)
print(match)
#Hier wird er was finden. Er sucht nicht nur am Anfang. SEARCH SUCHT ÜBERALL!!!. Im Range von 13,16 [16 ausgeschlossen]
#SEARCH SUCHT NUR FÜR DAS ERSTE. STEHT NOCHMAL TEN IRGENDWO FINDET ER TROTZDEM NUR DEN ERSTEN