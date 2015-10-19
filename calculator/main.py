# -*- coding: utf-8 -*-
from calculator import *

if __name__ == '__main__':
    input_num_1 = raw_input('请输入number A:')
    input_operate = raw_input('请输入运算符号:')
    input_num_2 = raw_input('请输入number B:')
    result = count(input_num_1, input_num_2, input_operate)
    print result

