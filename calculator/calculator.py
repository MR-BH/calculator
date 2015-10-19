# -*- coding: utf-8 -*-

'''The string module'''
import string


def count(num_first, num_second, operate):
    '''Computing the result

    :param: num_first：  the first number user input.
    :param: num_second： the second number user input.
    :param: operate：    the operate user input.
    :returns: the computing result
    :exception: transform string to float fail
    '''
    try:
        num_one = string.atof(num_first)
        num_two = string.atof(num_second)
    except BaseException:
        exit("输入错误，数字格式不正确")
    opetation_instance = Operation(num_one, num_two, operate)
    return opetation_instance.get_result()


class Operation(object):
    '''The Operation class'''

    def __init__(self, num_one, num_two, operate):
        '''Initialization class Operation

        :param: num_a: the first number user input
        :param: num_b: the second number user input
        :param: operate: the operate user input
        '''

        self._number_first = num_one
        self._number_second = num_two
        self._operate = operate

    def get_result(self):
        ''' The real function computing the result'''
        try:
            return self.operators[self._operate](self)
        except KeyError:
            exit("错误的操作符")

    def func_add(self):
        '''Computing add'''
        return  self._number_first + self._number_second

    def func_sub(self):
        '''Computing sub'''
        return  self._number_first - self._number_second

    def func_mul(self):
        '''Computing mul'''
        return  self._number_first * self._number_second

    def func_div(self):
        '''Computing div'''
        return  self._number_first / self._number_second

    operators = {
        '+': func_add,
        '-': func_sub,
        '*': func_mul,
        '/': func_div}



