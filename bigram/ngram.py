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

# 	- 예외상황 처리: next 음절 출현빈도가 1 이상인 음절이 없는 경우
#  --> 음절 unigram 빈도가 높은 10개 음절 중에서 임의로 1개 음절 선택
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

# P(i, j) 값이 가장 큰 3개 음절 중에서 임의로 선택
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
	#상위n개 음절중 임의 1개 음절출력
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
			if next_n == '다' : break
	
