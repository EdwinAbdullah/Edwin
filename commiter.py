#! /usr/bin/env python

import os


num =range(0,200)



for i in num:
	open("counter", 'a').write("1")
	os.system('git add --all :/')
	os.system('git commit -m "adding a 1"')
	os.system('git push')

'counter'.close()

print "You are now commited"
