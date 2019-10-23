import sys
if len(sys.argv)>1:
    file = open(sys.argv[1],'r')
else:
    file = sys.stdin

def readInt():
    for line in file:
        for v in line.split():
            yield int(v)
