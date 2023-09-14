# import another_mod

# print(another_mod.another_variable)

# from turtle import Turtle, Screen

# ben = Turtle()
# ben.shape("turtle")
# ben.color("blue")
# ben.forward(100)


# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)