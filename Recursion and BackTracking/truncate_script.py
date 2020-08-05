# import fileinput
import fileinput

# Using fileinput.input() method
for line in fileinput.input(files='gfg.txt'):
    inp = line.strip()

    print('select * from  ' + inp.split(' ')[2][0:len(inp.split(' ')[2])-1] + ' limit 5;')
