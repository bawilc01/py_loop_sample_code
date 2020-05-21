# Looping through numbers in python


# will print numbers 1 - 10 using for loop
# i = 0
#
# for i in range(10):
#     # same as i = i + 1
#     # i = 0, i = 0 + 1, which = 1.
#     # first number to print will be 1
#
#     i+=1
#
#     # print i until reaching the last number in the range
#     print(i)
#
#
# # will print numbers 0 - 9 using for loop
# i = 0
#
# for i in range(10):
#     # print i until reaching the last number in the range
#     # nothing has been done to i yet, so it will print first value of i,
#         # which is 0
#     print(i)
#
#
#     # same as i = i + 1
#     # i = 0, i = 0 + 1, which = 1.
#     # first number to print will be 1
#
#     i += 1


# THIS WAS A REAL INTERVIEW QUESTION ON A TECHNICAL INTERVIEW
# prints the sum of the last sum + sum for 10 numbers using for loop
    # i interates by 1, all the way up to 10
    # example, first answer is 0 + 1 = 1; sum starts at 0, sum increments by 1, then sum = 1
    # next answer is 1 + 1

# sum = 0
# # sum will change
#
# i = 0
# # i is numbers 1 - 10
#
# for i in range(10):
#     sum = sum + i
#     # or sum += 1
#     # first answer 0 + 1 = 1
#
#     print(sum)
    # sum is now = 1
    # starting over at the loop, we are now going to move to the second number (i) in the range, which is 2.
    # sum = 1, i = 2
    # the next number printed is new sum = 1 (current sum) + 2 (value of i)
    # sum is now = 3 and will be printed
    # next number is new sum = 3 (current sum) + 3 ( value of i)
    # sum is now = 6
    # the next 10 sums to be printed will appear in the console until all i's up to 10 are interated through


# print numbers i * 1 and interates i by 1 before returning to loop to screen using while loop until i equals 10
# will print numbers 0 - 10
# if you remove the = and make it while i < 10, then 0 - 9 will print to the screen because once i hits 10, the loop will stop because 10 is not less than 10



i = 0
while i<=10:
	print(i*1)
	i=i+1

# create an array or list of things and print all to the screen with a loop
# data = {"Brittney Coble", "some string", "another string"}
#
# for data in list:
#     print(data)
