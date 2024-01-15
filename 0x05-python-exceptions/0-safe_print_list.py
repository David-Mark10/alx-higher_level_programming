#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	for i in range(x):
		n = 0
		try:
			j = my_list[i]
			print(j, end=" ")
			n += 1
		except IndexError:
			break
	print()
	return n
			

