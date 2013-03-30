#!/usr/bin/python
def transler(str):
	A='ABCDEF'
	B='GHIJKL'
	C='MNOPQR'
	D='STUVWXYZ'
	translist=[]
	for char in str:
		if char in A : translist.append('A')
		elif char in B : translist.append('B')
		elif char in C : translist.append('C')
		elif char in D: translist.append('D')
		else: translist.append(' ')
	return ''.join(translist)

def main():
	st=str(raw_input("enter string: ")).upper()
	print transler(st)

if __name__=='__main__':
	main()
