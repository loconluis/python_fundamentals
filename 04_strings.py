name = "Luis"
surname = "Locon"
age = 29

# concatenacion

full_name = name + surname
print(full_name)

quote = 'I\'m Luis'
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# Format of strings
template = "Hola mi nombre es " + name + " y mi apellido es " + surname
print(template)

template2 = "Hola mi nombre es {} y mi apellido es {}.".format(name, surname)
print(template2)

template3 = f"Hola mi nombre es {name} y mi apellido es {surname} y tengo {age} años de edad."
print(template3)