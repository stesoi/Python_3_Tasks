numbers = []
sum = 0
count = 0
curr = str(input("enter a number or Enter to finish: "))

while curr != "":
    try:
        count += 1
        sum += int(curr)
        numbers.append(int(curr))
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if(numbers[i]>numbers[j]):
                    tmp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = tmp

        curr = str(input("enter a number or Enter to finish: "))
    except ValueError as err:
        print(err)

if(len(numbers)>0):
    print("numbers: ", numbers)
    print("count = ", count, " sum = ", sum, " lowest = ", min(numbers), " highest = ", max(numbers), " mean = ", sum/count)
    if(len(numbers)%2 != 0):
        print("median = ", numbers[int((len(numbers)-1)/2)])
    else:
        print("median = ", (numbers[int((len(numbers)/2)-1)]+numbers[int((len(numbers)/2))])/2)