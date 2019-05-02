## ~* 99 bottles of beer on the wall *~ ##

#############
## imports ##
#############

# uses the time module to pause before each line output
import time

# list to store our values in
bottles = []

# iterates through the range function and appends each number
for number in range(99,0,-1):
    bottles.append(number)
    
# for each number, we print out that number followed by the lyrics
for num in bottles:
    # if number is 1 or 2, the lyrics changes
    # if not then we just print out the "standard"
    if num != 1:
        print(num, "bottles of beer on the wall,", num, "bottles of beer.")
        
    if num is 2:
        print("Take one down and pass it around,", (num-1), "bottle of beer on the wall.")
    elif num is 1:
        print(num, "bottle of beer on the wall,", num, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall")
    else:
        print("Take one down and pass it around,", (num-1), "bottles of beer on the wall.")
    print(" ")
    time.sleep(8)
    
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")