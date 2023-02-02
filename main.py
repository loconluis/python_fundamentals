# This is just the main file that should contain a main function that runs first

# Juego Piedra Papel o tijera RETO 1
import random

username = input("Escoge un nombre de usuario \n")
print(f"Hola {str(username)}, listo para jugar...")

choice = input("cual es tu mano? \n")

plays = ["piedra", "papel", "tijera"]

randomChoice = random.choice(plays)

if (choice.lower() == randomChoice):
  print("Play again")
elif (choice.lower() == "tijera"):
  if (randomChoice == "piedra"):
    print("Machine wins")
  else:
    print(f"{username} wins")
elif (choice.lower() == "piedra"):
  if (randomChoice == "papel"):
    print("Machine wins")
  else:
    print(f"{username} wins")
elif (choice.lower() == "papel"):
  if (randomChoice == "tijera"):
    print("Machine wins")
  else:
    print(f"{username} wins")
