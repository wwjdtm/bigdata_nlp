# -*- coding: cp949 -*-

import os
import sys
import random

def unigram():
	f = open('KCC150_K01.txt')

	listt = []
	counts = dict()

	lines = f.readlines()

	for line in lines:
		for i in range(0, len(line)):
			# print(wlist[i])
			if (line[i] != ' ') and (line[i] != '.') and (line[i] != '\n'):
				listt.append(line[i])

	for name in listt :
		if name in counts: 
			counts[name] = counts[name] + 1
		else :
			counts[name] = 1
	
	res = sorted(counts.items(), key=(lambda x:x[1]), reverse= True)
	# print(type(res))
	return(res[:5])
	
	f.close()


def nextrand(start_n) :
	f = open('KCC150_K01.txt')

	listt = []
	counts = dict()

	lines = f.readlines()
	for line in lines:
		for i in range(0, len(line)):
			if line[i] == start_n:
				if (line[i+1] != ' ') and (line[i+1] != '.') and (line[i+1] != '\n'):
					listt.append(line[i+1])

# 	- ���ܻ�Ȳ ó��: next ���� �����󵵰� 1 �̻��� ������ ���� ���
#  --> ���� unigram �󵵰� ���� 10�� ���� �߿��� ���Ƿ� 1�� ���� ����
	if not listt:
		for line in lines:
			for i in range(0, len(line)):
				# print(wlist[i])
				if (line[i] != ' ') and (line[i] != '.') and (line[i] != '\n'):
					listt.append(line[i])

		for name in listt :
			if name in counts: 
				counts[name] = counts[name] + 1
			else :
				counts[name] = 1
	
		res = sorted(counts.items(), key=(lambda x:x[1]), reverse= True)[:10]
		# print(type(res))

		return(res[random.randrange(0,10)])

# P(i, j) ���� ���� ū 3�� ���� �߿��� ���Ƿ� ����
	else:
		for name in listt :
			if name in counts: 
				counts[name] = counts[name] + 1
			else :
				counts[name] = 1

		res = sorted(counts.items(), key=(lambda x:x[1]), reverse= True)[:3]
		# print(type(res))
		return(res[random.randrange(0,3)])
	
	f.close()



if __name__ == "__main__":
	start_list = unigram() 
	a = int(input("n(3~5) = "))
	#����n�� ������ ���� 1�� �������
	randomn = random.randrange(0,a)
	print(start_list)
	# print(randomn)
	fist_n = start_list[randomn][0]
	print('start = \n',fist_n)
	next_list = nextrand(fist_n)
	# print(next_list)
	next_n = next_list[0]
	n = 0
	while(True):
		next_list = nextrand(next_n)
		next_n = next_list[0]
		print(next_n)
		n = n+1
		if n > 9 :
			if next_n == '��' : break
	
