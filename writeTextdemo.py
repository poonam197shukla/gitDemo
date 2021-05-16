#read the file and store all elements to the list
#do vice-versa and write back to txt file

with open('test.txt', 'r') as reader:
    content=reader.readlines()                        #[A,B,C,D,E]
    reversed(content)    #reverese al content in the list   [E,D,C,B,A]
    with open('test.txt', 'w') as writer:
        for i in reversed(content):
            writer.write(i)