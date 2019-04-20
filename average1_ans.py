numbers =[]
sum = 0
count = 0
curr = str(input("enter a number or Enter to finish: "))

while curr != "":
    try:
        count += 1
        sum += int(curr)
        numbers.append(int(curr))
        curr = str(input("enter a number or Enter to finish: "))
    except ValueError as err:
        print(err)

if(len(numbers)>0):
    print("numbers: ", numbers)
    print("count = ", count, " sum = ", sum, " lowest = ", min(numbers), " highest = ", max(numbers), " mean = ", sum/count)