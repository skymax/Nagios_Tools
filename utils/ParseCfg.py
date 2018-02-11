#!/usr/bin/python
# -*- coding:gb2312 -*-

import os


class ParseCfg(object):

    def __init__(self):
        pass

    def __str__(self):
        return ''

    @staticmethod
    def get_element_type(element):
        arr_str = element.split('\n')
        v_type = ''
        for s in arr_str:
            i_find = s.find('define')
            if i_find >= 0:
                v_type = s.split()[-1].split('{')[0]
                break
        return v_type

    @staticmethod
    def nagiosCfg(file_name_in):
        f_r = open(file_name_in, 'r')
        line = f_r.readline()
        element = ''
        v_type = ''
        i_b = 0
        i_e = 0
        i_idx = 0
        while line:

            i_find = line.find('#')
            if i_find == 0:
                # # not an element
                line = f_r.readline()
                continue

            i_find = line.find('{')
            if i_find >= 0:
                # Begin
                i_b = 1
                i_e = 0
                v_type = ''
                element = ''
                # for s in self.l_type:
                #     if line.find(' ' + s + '{') >= 0:
                #         v_type = s
                #         break

            if i_b == 1:
                # in the same {}
                element += line

            i_find = line.find('}')
            if i_find >= 0:
                i_e = 1
                i_b = 0

            if i_e == 1:
                i_idx += 1
                # is contact
                i_e = 0
                yield element
                element = ''
            line = f_r.readline()

        f_r.close()


if __name__ == "__main__":

    v_file = r'D:\PycharmProjects\Nagios_Tools\etc\objects\linux\linux_9.23.2.53.cfg'
    parse = ParseCfg.nagiosCfg(v_file)
    i_index = 0
    for element in parse:
        i_index += 1
        print i_index
        print element
