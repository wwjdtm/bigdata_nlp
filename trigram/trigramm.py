# -*- coding: cp949 -*-
import os
import sys
import random

def trigram(senten):
    len_senten = len(senten)
  
    freq = [] #음절빈도수
    condi_freq = [] #앞에음절뒤에나올확률
    for a in range(0, len_senten):
        freq.append(0)
        condi_freq.append(0)

    f = open('KCC150_K01.txt')
    lines = f.readlines()

    #빈도수계산
    for line in lines:
        for i in range(0,len(line)):
            for a in range(0, len_senten):
                if a == len_senten - 1 :
                    if line[i] == senten[a]: freq[a] = freq[a]+1
                else:
                    if line[i] == senten[a]:
                        freq[a] = freq[a]+1
                        
                        if line[i+1] == senten[a+1]:
                            condi_freq[a+1] = condi_freq[a+1]+1

    answer = freq[0] * freq[len_senten-1] #시작값/마지막값

    for k in range(0,len_senten-1):
        #확률값이 0.0이면 매우작은 값으로 셋팅
        mull = 0.0000000000000001 if condi_freq[k+1]/freq[k] == 0 else condi_freq[k+1]/freq[k]
        # print(mull)
        answer = answer * mull

    return answer
    

if __name__ == "__main__":

    ##########1-1 주석지우고 출력
    a_sen = ['나','는',' ','밥','을',' ','좋','아','했','다']
    print(trigram(a_sen))
    b_sen = ['나','는',' ','법','을',' ','좋','아','했','다']
    print(trigram(b_sen))
    c_sen = ['너','는',' ','밥','을',' ','좋','아','햇','다']
    print(trigram(c_sen))
    d_sen = ['노','는',' ','법','을',' ','조','아','해','따']
    print(trigram(d_sen))

    ###########1-2 주석지우고 출력

    # a_sen = ['사','진','을',' ','찍','으','러',' ','공','원','에',' ','갔','다']
    # print(trigram(a_sen))
    # b_sen = ['사','진','을',' ','찍','으','로',' ','공','원','에',' ','갔','다']
    # print(trigram(b_sen))

    # print('#############')
    # #########2-1 주석지우고 출력

    # a_sen = ['누','난',' ','바','블',' ','좋','아','햇','따']
    # a_aa = trigram(a_sen)
    # b_sen = ['나','눈',' ','밤','을',' ','조','하','해','따']
    # b_bb = trigram(b_sen)
    # c_sen = ['눈','은',' ','밥','을',' ','조','아','했','다']
    # c_cc = trigram(c_sen)

    # ddic = { '누난 바블 좋아햇따' : a_aa , '나눈 밤을 조하해따' : b_bb , '눈은 밥을 조아했다' : c_cc }

    # sdict = sorted(ddic.items(), key=(lambda x:x[1]), reverse= True)

    # print(sdict[0])
    # print(sdict[1])
    # print(sdict[2])

    # print('#############')
    # #########2-2 주석지우고 출력
    
    # a_senn = ['사','진','을',' ','찍','으','라',' ','공','원','애',' ','갔','따']
    # a_aaa = trigram(a_senn)
    # b_senn = ['사','딘','을',' ','찍','으','로',' ','공','원','에',' ','갓','따']
    # b_bbb = trigram(b_senn)
    # c_senn = ['소','진','을',' ','짝','으','로',' ','공','뭔','에',' ','겄','다']
    # c_ccc = trigram(c_senn)

    # ddicc = { '사진을 찍으라 공원애 갔따' : a_aa , '사딘을 찍으로 공원에 갓따' : b_bb , '소진을 짝으로 공뭔에 겄다' : c_cc }

    # sdictt = sorted(ddicc.items(), key=(lambda x:x[1]), reverse= True)

    # print(sdictt[0])
    # print(sdictt[1])
    # print(sdictt[2])

	