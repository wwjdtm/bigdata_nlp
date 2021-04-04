# -*- coding: cp949 -*-
import os
import sys
import random

def trigram(senten):
    len_senten = len(senten)
  
    freq = [] #�����󵵼�
    condi_freq = [] #�տ������ڿ�����Ȯ��
    for a in range(0, len_senten):
        freq.append(0)
        condi_freq.append(0)

    f = open('KCC150_K01.txt')
    lines = f.readlines()

    #�󵵼����
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

    answer = freq[0] * freq[len_senten-1] #���۰�/��������

    for k in range(0,len_senten-1):
        #Ȯ������ 0.0�̸� �ſ����� ������ ����
        mull = 0.0000000000000001 if condi_freq[k+1]/freq[k] == 0 else condi_freq[k+1]/freq[k]
        # print(mull)
        answer = answer * mull

    return answer
    

if __name__ == "__main__":

    ##########1-1 �ּ������ ���
    a_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    print(trigram(a_sen))
    b_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    print(trigram(b_sen))
    c_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    print(trigram(c_sen))
    d_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    print(trigram(d_sen))

    ###########1-2 �ּ������ ���

    # a_sen = ['��','��','��',' ','��','��','��',' ','��','��','��',' ','��','��']
    # print(trigram(a_sen))
    # b_sen = ['��','��','��',' ','��','��','��',' ','��','��','��',' ','��','��']
    # print(trigram(b_sen))

    # print('#############')
    # #########2-1 �ּ������ ���

    # a_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    # a_aa = trigram(a_sen)
    # b_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    # b_bb = trigram(b_sen)
    # c_sen = ['��','��',' ','��','��',' ','��','��','��','��']
    # c_cc = trigram(c_sen)

    # ddic = { '���� �ٺ� �����޵�' : a_aa , '���� ���� �����ص�' : b_bb , '���� ���� �����ߴ�' : c_cc }

    # sdict = sorted(ddic.items(), key=(lambda x:x[1]), reverse= True)

    # print(sdict[0])
    # print(sdict[1])
    # print(sdict[2])

    # print('#############')
    # #########2-2 �ּ������ ���
    
    # a_senn = ['��','��','��',' ','��','��','��',' ','��','��','��',' ','��','��']
    # a_aaa = trigram(a_senn)
    # b_senn = ['��','��','��',' ','��','��','��',' ','��','��','��',' ','��','��']
    # b_bbb = trigram(b_senn)
    # c_senn = ['��','��','��',' ','¦','��','��',' ','��','��','��',' ','��','��']
    # c_ccc = trigram(c_senn)

    # ddicc = { '������ ������ ������ ����' : a_aa , '����� ������ ������ ����' : b_bb , '������ ¦���� ������ �δ�' : c_cc }

    # sdictt = sorted(ddicc.items(), key=(lambda x:x[1]), reverse= True)

    # print(sdictt[0])
    # print(sdictt[1])
    # print(sdictt[2])

	