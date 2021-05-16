#list

values=[1,2,"poonam",4,5]
print(values)       #o/p: [1, 2, 'poonam', 4, 5]
print(values[0])    #o/p: 1
print(values[2])    #o/p: poonam
print(values[-1])   #o/p: 5 (-1 fetches the last index item)
print(values[-5])   #o/p: 1
print(values[1:3])  #o/p: [2, 'poonam']  (it will print from index value of 1 and 2, 3 is excluded)
print(values[-5:-1])#o/p: [1, 2, 'poonam', 4] (it will exclude value at -1 position and print till -5)

#insert in list
values.insert(3,"shetty")
print(values)       #o/p: [1, 2, 'poonam', 'shetty', 4, 5]

values.insert(2, "shukla")
print(values)

#insert value at the end of list
values.append("newlyadded")
print(values)

values.append("lastOne")
print(values)

#updation in list
values[2]="UPDATED ONE"
print(values)

#deletion in list
del values[0]
print(values)

