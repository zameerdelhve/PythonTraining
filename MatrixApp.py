# matrix = [[1,2,3],[4,5,6]]
one_d = [1,2,3,4]
one_d.insert(0,12)
one_d.append(13)
#one_d.sort(reverse=True)
one_d.sort()
for number in one_d:
    print('Number is ' + str(number))
    print('Index is ' + str(one_d.index(number)))
#print (one_d)
# print (matrix)
# print (matrix[1][0])
# for row in matrix:
#    for column in row:
#        print (column)
