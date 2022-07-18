#!/usr/bin/env python

import sys

def main():
	a = (sys.argv[1])
	b = (sys.argv[2])

	if (sys.argv[3] != ""):  #if it exists
		print("error! more than 2 arguments given..")
	else:
		add(a,b)
def add(a, b):
	c = int(a)  + int(b)
	print(c)

if __name__ == "__main__":
	main()


