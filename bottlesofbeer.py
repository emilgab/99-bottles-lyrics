## ~* 99 bottles of beer on the wall *~ ##

# Imports the time module to pause before each line output
import time

# iterates through the range function and prints out numbers with lyrics
for number in range(99,0,-1):
    # If the number is 1 or 2, the lyric changes. Else, we print the "standard"
    if number != 1:
        print(number, "bottles of beer on the wall,", number, "bottles of beer.")
   
    if number == 2:
        print("Take one down and pass it around,", (number-1), "bottle of beer on the wall.")
        
    elif number == 1:
        print(number, "bottle of beer on the wall,", number, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall")
        
    else:
        print("Take one down and pass it around,", (number-1), "bottles of beer on the wall.")
    print(" ")
    time.sleep(8)

## FINISHING LYRICS ##
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
print(" ")