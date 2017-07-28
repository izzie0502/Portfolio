



#random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
#86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
#52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]


#prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


n = int(input("Choose a number between 0 and 500.\n"))
pri = input("Do you want to see if your number is prime? Type Y for yes and N for no.\n")

if (pri == "Y" or pri == "y"):
    if n % 2 != 0 and n % 3 != 0 and p % 5 != 0 and p % 7 != 0 and p % 11 != 0 and p % 13 != 0 and p % 17 != 0 and p % 19 != 0 and p % 23 != 0:
        print("Would you look at that, your number is prime!")
    else:
        print("Aw shucks, your number is composite!")

five = input("Do you want to see if your number is a multiple of five? Type Y for yes and N for no.\n")

if (five == "Y" or five == "y"):
    if n % 5 == 0:
        print("Would you look at that, your number is a multiple of 5!")
    else:
        print("Aw shucks, your number is not divisible by 5!")






#random_Prime = []
#i = 0
#
#for p in random_numbers:
#    if p % 2 != 0 and p % 3 != 0 and p % 5 != 0 and p % 7 != 0:
#        random_Prime.append(p)
#
#for c in random_Prime:
#    i = i + c
#
#print(i)


#x = 0
#for i in random_numbers:
#    if i % 5 == 0:
#        x = x + i
#for f in random_numbers:
#    if f % 3 == 0:
#        x = x + f
#for c in random_numbers:
#    if c % 15 == 0:
#        x = x - c
#print(x)


#mult=[]

#twenty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#for i in twenty:
#    mult.append(5 * i)
#
#for z in mult:
#    if z == :
#        random_numbers.index(z)
