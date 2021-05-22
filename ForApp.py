
input_number=int(input('Please input number: '))
for x in range (input_number):
    print(x)

input_string=input('Please input string: ')
for x in input_string:
    print(x)

number_of_items = int(input('Please enter number of items: '))

counter = 1
list_of_prices = []
while counter <= number_of_items:
    item_price = int(input('Please enter price of item ' + str(counter) + ' '))
    list_of_prices.append(item_price)
    counter = counter + 1
print (list_of_prices)

total_price = sum(list_of_prices)
print('Total price = ' + str(total_price))

for_count = 0
for price in list_of_prices:
    print(list_of_prices[for_count])
    for_count = for_count + 1
    total_price = total_price + price
    print(total_price)
print(total_price)