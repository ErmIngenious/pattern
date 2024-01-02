#set number of rows in a variable
rows = 9

# Looping through each row
for i in range(rows):
        
# Printing the top half of the pyramid
   if i < rows // 2:
      for _ in range(i + 1):
         print("*", end=" ")

# Printing the bottom half of the pyramid
   else:
      for j in range(i, rows):
         print("*", end=" ")

 # Moving to the next line after printing each row
   print()
