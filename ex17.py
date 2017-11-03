from sys import argv
first,second,third = argv
open(third,'w').write(open(second).read())
