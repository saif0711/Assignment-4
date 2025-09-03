file = open('sample.txt','r')
reading_file = file.readlines()
print(reading_file)
file.close()

file = open('output.txt','r+')
writing_file = file.write('Hello, Python!')
print(writing_file)
file.close()

file = open('output.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()

file = open('output.txt','a')
appending_file = file.write('Learning fiel handling in Python.')
print(appending_file)
file.close()

file = open('output.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()

