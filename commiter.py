#! /usr/bin/env python

import os

EmptyFile = open("counter", 'a')

num =range(0,3)

os.system('git pull')


for i in num:
	EmptyFile.write("1")
	os.system('git add --all :/')
	os.system('git commit -m "adding a 1"')
	os.system('git push')
	os.system('sleep 15')

EmptyFile.close()

print "You are now commited"
