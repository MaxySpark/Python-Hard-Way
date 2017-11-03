from sys import argv

script, filename = argv
txt = open(filename)
print txt.read()

prompt = '>'
print "Type The File Name Again"
txt_again = input(prompt)
txt2 = open(txt_again)
print txt2.read()
