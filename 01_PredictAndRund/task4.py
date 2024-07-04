import re

text = "This book on tennis cost $3.99 at Walmart."

reg = re.compile("([A-Z][a-z]+) ([A-Z]*)( )?([A-Z][a-z]+)")# ()? ist ein optionales Leerzeichen nachdem ? kommt.
m = reg.match("Hanna J Gruber")
print(m) # matches alles
print(m.group(2)) #matches J. Die zweite Gruppe ist ([A-Z]*)
print(m.group(0)) #Group 0 is everythin
print(m.group(1))
print(m.group(3))
print(m.group(4))
print("Hello")
m = reg.match("Hanna Gruber")
print(m)
print("hey")
print(m.group(4))
#match gruber
m = reg.match("Hanna Jana Gruber")
print(m)
print(m.group(4))

m = reg.match("Albert KD Klein")
print(m)
print(m.group(2))

m = reg.match("Christoph M Flath")
print(m)
print(m.group(2))

m = reg.search("Hanna J Gruber, PhD")
print(m)
print(m.group(2))

m = reg.search("xw. Alfred Nobel")
print(m)
print(m.group(2))