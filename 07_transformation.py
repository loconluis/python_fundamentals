name = "Luis"
print(type(name))
# dinamicamente le cambiamos el tipo solo al asignarle un valor distinto
name = 12
print(type(name))

age = 29

print("Mi edad es" + str(age))
print(f"Mi edad es {age}")

age_input = int(input("cual es tu edad?"))
age_input += 10
print(f"A tu edad le sume 10 ahora es {age_input}")