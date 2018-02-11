#!/usr/bin/python
# -*- coding:gb2312 -*-

import os


class ConfRead(object):
    l_type = ('contact', 'contactgroup', 'serviceescalation', 'host', 'service')
    l_field_contact = ('contact_name', 'use', 'alias', 'email', 'pager', '_weixinid')
    l_field_contactgroup = ('contactgroup_name', 'alias', 'members')
    l_field_serviceescalation = ('host_name', 'service_description', 'contact_groups')
    dir_etc_base = ''

    def __init__(self):
        pass

    def __str__(self):
        return ''

    def read_cfg_serviceescalation(self, f_cfg, f_out, write_type='w'):
        v_file_cfg = f_cfg
        v_file_out = f_out
        f = open(v_file_cfg, 'r')
        f_w = open(v_file_out, write_type)
        line = ''
        line = f.readline()
        i_idx = 0
        i_b = 0
        i_e = 0

        str_para = ''
        while line:
            i_find = line.find('{')
            if i_find >= 0:
                i_b = 1
                i_e = 0
                str_para = ''
                v_type = ''
                for s in self.l_type:
                    if line.find(' ' + s + '{') >= 0:
                        v_type = s
                        break
            if i_b == 1:
                str_para += line
            i_find = line.find('}')
            if i_find >= 0:
                i_e = 1
                i_b = 0

            if i_e == 1 and v_type == 'serviceescalation':
                i_idx += 1
                # is contact
                i_e = 0
                v_out = self.do_gen_serviceescalation(str_para, f_w)
                if (i_idx > 1 or write_type == 'a'):
                    f_w.write('\n')
                f_w.write(v_out)
                str_para = ''

            line = f.readline()

    def read_cfg_contactgroup(self, f_cfg, f_out, write_type='w'):
        v_file_cfg = f_cfg
        v_file_out = f_out
        f = open(v_file_cfg, 'r')
        f_w = open(v_file_out, write_type)
        line = ''
        line = f.readline()
        i_idx = 0
        i_b = 0
        i_e = 0

        str_para = ''
        while line:
            i_find = line.find('{')
            if i_find >= 0:
                i_b = 1
                i_e = 0
                str_para = ''
                v_type = ''
                for s in self.l_type:
                    if line.find(' ' + s + '{') >= 0:
                        v_type = s
                        break
            if i_b == 1:
                str_para += line
            i_find = line.find('}')
            if i_find >= 0:
                i_e = 1
                i_b = 0

            if i_e == 1 and v_type == 'contactgroup':
                i_idx += 1
                # is contact
                i_e = 0
                v_out = self.do_gen_contactgroup(str_para, f_w)
                if i_idx > 1:
                    f_w.write('\n')
                f_w.write(v_out)
                str_para = ''

            line = f.readline()

    def read_cfg_contact(self, f_cfg, f_out, write_type='w'):
        v_file_cfg = f_cfg
        v_file_out = f_out
        f = open(v_file_cfg, 'r')
        f_w = open(v_file_out, write_type)
        line = ''
        line = f.readline()
        i_idx = 0
        i_b = 0
        i_e = 0

        str_para = ''
        while line:
            i_find = line.find('{')
            if i_find >= 0:
                i_b = 1
                i_e = 0
                str_para = ''
                v_type = ''
                for s in self.l_type:
                    if line.find(' ' + s + '{') >= 0:
                        v_type = s
                        break

            if i_b == 1:
                str_para += line
            i_find = line.find('}')
            if i_find >= 0:
                i_e = 1
                i_b = 0

            if i_e == 1 and v_type == 'contact':
                i_idx += 1
                # is contact
                i_e = 0
                v_out = self.do_gen_contact(str_para, f_w)
                if i_idx > 1:
                    f_w.write('\n')
                f_w.write(v_out)
                str_para = ''

            line = f.readline()

    def do_gen_contact(self, str_para, v_file_out):
        dic_vals = {}
        arr_line = str_para.split('\n')
        i_idx = 0
        str_rnt = ''
        for key in self.l_field_contact:
            dic_vals[key] = ''
        for line in arr_line:
            i_idx += 1
            for key in self.l_field_contact:
                str_find = ' ' + key + ' '
                i_find = line.find(str_find)
                if i_find >= 0:
                    str_val = line[i_find + len(str_find):]
                    str_val = str_val.split(';')[0].strip()
                    dic_vals[key] = str_val
        #                    print "%s=%s" % (key, str_val)

        str_rnt = self.get_out_txt(dic_vals, self.l_field_contact)
        return str_rnt

    def do_gen_contactgroup(self, str_para, v_file_out):
        dic_vals = {}
        arr_line = str_para.split('\n')
        i_idx = 0
        str_rnt = ''
        for key in self.l_field_contactgroup:
            dic_vals[key] = ''
        for line in arr_line:
            i_idx += 1
            for key in self.l_field_contactgroup:
                str_find = ' ' + key + ' '
                i_find = line.find(str_find)
                if i_find >= 0:
                    str_val = line[i_find + len(str_find):]
                    str_val = str_val.split(';')[0].strip()
                    dic_vals[key] = str_val
        #                    print "%s=%s" % (key, str_val)

        str_rnt = self.get_out_txt(dic_vals, self.l_field_contactgroup)

        return str_rnt

    def do_gen_serviceescalation(self, str_para, v_file_out):
        dic_vals = {}
        arr_line = str_para.split('\n')
        i_idx = 0
        str_rnt = ''
        for key in self.l_field_serviceescalation:
            dic_vals[key] = ''
        for line in arr_line:
            i_idx += 1
            for key in self.l_field_serviceescalation:
                str_find = ' ' + key + ' '
                i_find = line.find(str_find)
                if i_find >= 0:
                    str_val = line[i_find + len(str_find):]
                    str_val = str_val.split(';')[0].strip()
                    dic_vals[key] = str_val
        #                    print "%s=%s" % (key, str_val)

        str_rnt = self.get_out_txt(dic_vals, self.l_field_serviceescalation)

        return str_rnt

    def get_out_txt(self, dic_vals, keys):
        i_idx = 0
        str_rnt = ''
        for key in keys:
            if i_idx == 0:
                str_rnt += dic_vals[key]
            else:
                str_rnt += '|' + dic_vals[key]
            i_idx += 1
        return str_rnt

    def read_cfg_servicegroup(self, f_cfg, f_out, wriet_type='w'):
        v_file_cfg = f_cfg
        v_file_out = f_out
        f = open(v_file_cfg, 'r')
        f_w = open(v_file_out, write_type)
        line = f.readline()
        i_idx = 0
        i_b = 0
        i_e = 0
        # line = ''
        v_name = ''
        v_alias = ''

        while line:
            if line.find('{') >= 0:
                i_b = 1
                i_e = 0
                v_name = ''
                v_alias = ''

            if line.find('}') >= 0:
                i_e = 1
                i_idx += 1
                i_b = 0
                v_out = '%s|%s' % (v_name, v_alias)
                if i_idx > 1:
                    v_out = '\n' + v_out
                f_w.write(v_out)

            v_find = 'servicegroup_name'
            v_i = line.find(v_find)
            if v_i > 0:
                # servicegroup_name
                v_val = line[v_i + + len(v_find):]
                v_name = v_val.strip()

            v_find = 'alias'
            v_i = line.find(v_find)
            if v_i > 0:
                # alias
                v_val = line[v_i + + len(v_find):]
                v_alias = v_val.strip()
            line = f.readline()
        f.close()


if __name__ == "__main__":
    confReader = ConfRead()
    v_file_r = 'E:/tmp/20180116/objects/contacts.cfg'
    v_file_w1 = 'D:/PycharmProjects/Nagios_Tools/in/contact.txt'
    v_file_w2 = 'D:/PycharmProjects/Nagios_Tools/in/contactgroup.txt'
    confReader.read_cfg_contact(v_file_r, v_file_w1):
    for in os.listdir('E:/tmp/20180116/objects/contacts/'):
        v_f_cfg = dir_serviceescalation + '/' + f
        if os.path.isfile(v_f_cfg):
            if i > 0:
                write_type = 'a'
        confReader.read_cfg_serviceescalation(v_f_cfg, v_file_w_serviceescalation, write_type)
        i += 1
