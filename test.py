with open('test.txt', 'r+') as file:
    line1 = 'This is line 1\n'
    line2 = [[1, 2, 3], [3, 2, 6]]
    line3 = 'Text of line 3\n'
    if False:
        file.write(line1)
        file.write(str(line2)+'\n')
        file.write(line3)
    for line in file:
        print(line, end='')
    print('')
    print()
