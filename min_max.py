# Author: Justin Huang
# GitHub username: huangjus
# Date: 1/25/23
# Description: Prints the minimum and maximum numbers from a list of numbers inputted by the user

num_int = int(input('How many integers would you like to enter?'))

print('Please enter ', num_int, ' integers.')
number = int(input())

minimum = number
maximum = number

index = 0

while index < num_int - 1:
    number = int(input(''))
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
    index = index + 1

print('min:', minimum)
print('max:', maximum)
