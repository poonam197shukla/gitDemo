#automating a website


itemsInCart=0

#2 items will be added to cart

#if itemsInCart!=2:
#   raise Exception("Product cart count does not match")


assert (itemsInCart==0)

#try catch mechanism
'''
try:
    with open('fielLog.txt','r') as reader:   #here filename is invalid, so it is failing and going to except block
        reader.read()

except:
    print("i reached here beacause there is a failure")
'''

'''
try:
    with open('tefgh.txt','r') as reader:   #here filename is valid, so it is not failing. so control wont go to except block
        reader.read()

except:
    print("i reached here beacause there is a failure")
    
'''

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:    #to print the message python is throwing
    print(e)

finally:
    print("this is finally printing")


