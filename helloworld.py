
# String format
name = "Hello {0}".format("Luciano")
#print(name)

# if
nome = "Luciano" if 1 > 2 else "Correia"
#print(nome)

# Lists
names = ["Luciano", "Teixeira", "Correia"]
names.append("Salvador")
del names[3]
existe = "Luciano" in names
tamanho = len(names) == 4

# print(names[1:])  # ['Teixeira', 'Correia']
# print(names[1:-1])  # ['Teixeira']

# Loops
for name in names:
    print("Nome: {0}".format(name))
    
