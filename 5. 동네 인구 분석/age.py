# -*- coding: euc-kr -*-
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open('2020�� 11�� ������ �α�1�찣�����, ����������, ANSI.csv', 'rt', encoding='euc-kr')
data = csv.reader(f)

'''
for row in data:
    if '����1��' in row[0]:
        print(len(row[3:]))# 101 �� ��µȴ�.
        for i in row[3:]:# 0�� ~ 100�� �̻���� �α��� ��� �� 101���� �� ���
            print(i)
'''
# ����Ʈ�� ����1���� ������� 0�� ~ 100�� ������ ���������� ���
result = []
for row in data:
    if '����1��' in row[0]:
        for i in row[3:]:
            #result.append(i)# �̷��� �ϸ� ���ڿ����·� �����
            result.append(int(i))
print(result)

# ���� ������ �ð�ȭ�� �غ���
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'MalGun Gothic')    # �ѱ���� ���� �ڵ� 
plt.rcParams['axes.unicode_minus'] = False  # # �ѱ���� ���� �ڵ�
plt.title('������ ����1�� ���̺� �α���')
plt.xlabel('����')
plt.ylabel('�α���')
plt.plot(result)
plt.show()

