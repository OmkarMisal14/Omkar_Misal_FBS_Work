s = "Firstbit solutions"
s2 = s.upper()
print(s2)
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
s = "PytHon"
print(s.swapcase())
s = "Python Programming"
print(s.find('P'))
print(s.find("Program"))
print(s.find("java"))
print(s.index("Pr"))
print(s.count("P"))
print(s.startswith("P"))
print(s.endswith("ing"))
s = "  Python"
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = "I am good at python"
s2 = s.split()
print(s2)
s = "I,am,good,at,python"
s2 = s.split(",") #*! You can use any symbol here.
print(s2)
r = "-".join(s2)
print(r)

a = "adakdf"
print(a.isalpha())
a = "123kjsdf"
print(a.isalnum())
a = "1343"
print(a.isnumeric())