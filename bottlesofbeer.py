## ~* 99 bottles of beer on the wall *~ ##

#############
## imports ##
#############

# uses the time module to pause before each line output
import time

# iterates through the range function and prints out numbers and lyrics
for number in range(99,0,-1):
    
    # If the number is 1 or 2, the lyric changes
    # Else, we print out the "standard" lyric"
    if number != 1:
        print(number, "bottles of beer on the wall,", number, "bottles of beer.")
        
    if number is 2:
        print("Take one down and pass it around,", (number-1), "bottle of beer on the wall.")
        
    elif number is 1:
        print(number, "bottle of beer on the wall,", number, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall")
        
    else:
        print("Take one down and pass it around,", (number-1), "bottles of beer on the wall.")
    print(" ")
    time.sleep(8)
    
######################
## FINISHING LYRICS ##
######################

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
print(" ")