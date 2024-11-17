# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer."))
# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1
 
print(int_init)  # displays the initial value of pos_int
print(summed)    # displays the sum of integers from pos_int