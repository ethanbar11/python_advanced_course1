# how to read from file
# file_stream = open('.\\text.txt', 'r')
# data_read = file_stream.readlines()
# print(data_read)
# file_stream.close()

# How to write to file
s = open('.\\text.txt', 'w')
s.writelines(['One\n', 'Two\n', 'Three'])
s.flush()
s.close()

# Sugar syntax of with
with open('.\\text.txt', 'r') as f:
    print(f.read())

print('Woho, Im out of the with!')
