#!/usr/bin/env python

import sys

def main():
	a = (sys.argv[1])
	b = (sys.argv[2])
	add(a, b)

def add(a, b):
	c = int(a)  + int(b)
	print(c)

if __name__ == "__main__":
	main()


