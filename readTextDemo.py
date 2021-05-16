file=open('test.txt')

#print(file.read())   #to read all content of file

#print(file.read(4))   #to ready only till 4 bytes. only 4 letters

#print(file.readline(3))      #print first line
#print(file.readline())      #print second line
#print(file.readline())      #print third line


#to print all content line by line
#line=file.readline()
#Ewhile line!="":
  #  print(line)
   # line=file.readline()



#readLines method

print(file.readlines())   #all values from file get stored in form of list

for line in file.readlines():   #to iterate the list after getting converted
    print(line)


file.close()