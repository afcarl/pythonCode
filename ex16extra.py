from sys import argv

script, filename = argv

#ask them if they want to read the file % filename
print "Hello, would you like me to read %r?" % filename
print "Hit CTRL-C(^C) if you would like to quit."
print "Otherwise hit ENTER."

raw_input("?")


#open the file
print "Very well, I shall open %r." % filename
target = open(filename, "r")

#proceed with reading the file
print target.read()

#close the file
target.close()
