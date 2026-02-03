print ( "welcome to place the rabbit" )
field = [ ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]
, ["🌿", "🌿", "🌿"] ]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nwhere should the rabbit go? 🐇")
position =input("choose a row and column \n")
row =int(position[0])
column=int(position[1])
field[row-1][column-1] ="🐇"

print("\nsucces....\n")

print(f"{field[0]} \n{field[1]} \n{field[2]}")
