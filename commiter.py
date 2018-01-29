#! /usr/bin/env python

import os


num =range(0,10)



for i in num:
	open("counter", 'a').write("1")
	os.system('git add --all :/')
	os.system('git commit -m "adding a 1"')
	os.system('git push')

open("counter", 'a').close()

print "You are now commited"
