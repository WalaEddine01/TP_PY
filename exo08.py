sum = 0
for i in range(31):
    if i % 3 == 0:
        print(i, "Divisible by 3")
        sum += i
    else:
        print("Not Divisible by 3")
    print("the total is", sum)    
