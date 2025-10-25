# 24 October 2025
# Program 1: Print name of the open file
########################################################
########################################################
##                                                    ##
##  ######  ##  ##  ######  ##   ##  ####### #######  ##
##  ##  ##  ##  ##  ######  ##   ##  ##   ## ##   ##  ##
##  ######  ##  ##    ##    #######  ##   ## ####     ##
##  ##  ##  ##  ##    ##    ##   ##  ##   ## ##  ##   ##
##  ##  ##  ######    ##    #3   ##  ####### ##   ##  ##
##                                                    ##
########################################################
########################################################

f = open('test.txt', 'r')

print(f.name)

f.close()


# Program 2: Print mode in which file is open

f = open('test.txt', 'r')

print(f.mode)

f.close()


# Program 3: Open file using context managers

with open('test.txt', 'r') as f:
    pass


# Program 4: Read first two lines of a file

with open('test.txt', 'r') as f:
    # f_contents = f.read()
    f_contents = f.readline()
    print(f_contents, end='')

    f_contents = f.readline()
    print(f_contents, end='')
    
    
# Program 5: Read the entire file by iterating through it

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')


# Program 6: Read using read() method but just 100 characters at once

with open('test.txt', 'r') as f:

    size_to_read = 100

    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


# Program 7: use seek() method to go to the beginning of the file

with open('test.txt', 'r') as f:

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents, end='')


# Program 8: Write data into a file

with open('test.txt', 'w') as f:
    f.write('Test!')


# Program 9: Copy the contents of the original file to a new file

with open('test.txt', 'r') as rf:
    with open('test_write.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# Program 10: Copy an image using binary mode
with open('cat.png', 'rb') as rf:
    with open('catfish.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# Program 11: Replace a word within a file

def replace_word(filename, old_word, new_word):
    with open(filename, 'r') as f:
        content = f.read()

    content = content.replace(old_word, new_word)

    with open(filename, 'w') as f:
        f.write(content)

filename = 'file1.txt'
old_word = 'Heading'
new_word = 'Wedding'

replace_word(filename, old_word, new_word)


