list_of_numbers = [10,1,2,3,4,40,40,60,80,50]
count = 0
max_number = 0
for number in list_of_numbers:
    print ('Current number in list: ' + str(list_of_numbers[count]))
    loop_number = (list_of_numbers[count])
    if loop_number > max_number:
        max_number = loop_number
    else:
        max_number = max_number
    count = count + 1
print ('Largest number in list is: ' + str(max_number))