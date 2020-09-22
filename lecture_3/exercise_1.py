file_name = input('Enter file name: ') + '.txt'
lst = file_name.split('.')
new_file_name = lst[0] + 'Hello' + '.txt'

with open(file_name, 'r') as file_to_read:
    with open(new_file_name, 'w') as file_to_write:
        for line in file_to_read:
            file_to_write.write(line)
        file_to_write.write('\nJunk')

