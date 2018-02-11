#!/usr/bin/python
# -*- coding:gb2312 -*-

import os
from ParseCfg import ParseCfg


class DefElement(object):
    use = ''
    tuple_type = ('aix', 'contact', 'contactgroup', 'disk', 'group', 'host', 'hp', 'linux', 'log', 'mail', 'oracle',
                  'oracle_goldengate', 'oracle_tbs', 'serviceescalation', 'servicegroup', 'tcp', 'url', 'windows')

    def __init__(self, type, use, fields, f_out):
        self.type = type  # in tuple_type
        self.use = use
        self.fields = tuple(fields)
        self.f_out = f_out  # file output

    def __str__(self):
        return ''


class CfgReader(object):
    l_type = ('contact', 'contactgroup', 'serviceescalation', 'host', 'service')
    l_field_contact = ('contact_name', 'use', 'alias', 'email', 'pager', '_weixinid')
    l_field_contactgroup = ('contactgroup_name', 'alias', 'members')
    l_field_serviceescalation = ('host_name', 'service_description', 'contact_groups')
    dir_etc_base = ''
    dic_defelement = {}
    dic_host = {}  # [host_name] = ip

    def init_f_out(self):
        items = self.dic_defelement.iteritems()
        for key, element in items:
            self.write_to_file(element.f_out, '', 'w')

    def __init__(self):
        dir_out_base = 'D:/PycharmProjects/Nagios_Tools/reader'

        v_type = 'linux'
        use = 'linux-server'
        fields = ('group_name', 'ip', 'hostname')
        file_out = dir_out_base + '/host_linux.txt'
        defElement = DefElement(v_type, use, fields, file_out)
        self.dic_defelement[v_type] = defElement

        v_type = 'disk'
        use = 'os-service'
        fields = ('ip', 'pathname')
        file_out = dir_out_base + '/disk.txt'
        defElement = DefElement(v_type, use, fields, file_out)
        self.dic_defelement[v_type] = defElement

        v_type = 'oracle_tbs'
        use = 'db-service'
        fields = ('ip', 'sid', 'tbs')
        file_out = dir_out_base + '/oracle_tbs.txt'
        defElement = DefElement(v_type, use, fields, file_out)
        self.dic_defelement[v_type] = defElement

        v_type = 'oracle'
        use = 'db-service'
        fields = ('ip', 'sid', 'port')
        file_out = dir_out_base + '/oracle.txt'
        defElement = DefElement(v_type, use, fields, file_out)
        self.dic_defelement[v_type] = defElement

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

    def do_parse_element(self, element):
        v_type = ParseCfg.get_element_type(element)
        dic_item = {}
        if v_type == 'host':
            # print(element)
            dic_item = {}
            dic_out = {}
            dic_item['hostgroups'] = ''
            for s in element.split('\n'):
                if (s.find('{') > -0 or s.find('}')) >= 0:
                    continue
                att_s = s.split()
                if len(att_s) < 2:
                    continue
                s_key = att_s[0].strip()
                s_val = att_s[1].strip()
                dic_item[s_key] = s_val

            v_use = dic_item['use']
            host_name = dic_item['host_name']
            hostgroups = dic_item['hostgroups']
            v_alias = dic_item['alias']
            address = dic_item['address']
            v_host_type = host_name.split('_')[0]
            self.dic_host[host_name] = address
            ip = address
            hostname = v_alias.split('(')[-1].split(')')[0]
            dic_out['ip'] = ip
            dic_out['hostname'] = hostname
            dic_out['group_name'] = hostgroups
            element = self.dic_defelement[v_host_type]
            # print element.fields
            s_out = self.get_out_txt(dic_out, element.fields)
            self.write_to_file(element.f_out, s_out + '\n')

        elif v_type == 'service':
            # print(element)
            dic_item = {}
            dic_out = {}
            dic_item['hostgroups'] = ''
            for s in element.split('\n'):
                if (s.find('{') > -0 or s.find('}')) >= 0:
                    continue
                att_s = s.split()
                if len(att_s) < 2:
                    continue
                s_key = att_s[0].strip()
                s_val = att_s[1].strip()
                dic_item[s_key] = s_val
            host_name = dic_item['host_name']
            ip = self.dic_host[host_name]
            v_use = dic_item['use']
            service_description = dic_item['service_description']
            check_command = dic_item['check_command']
            s_tmp = check_command.split('!')[1].strip()
            if s_tmp.find('check_oracle_login') >= 0:
                # check_oracle_login
                # oracle
                # oracle_tbs
                dic_out['ip'] = ip
                dic_out['sid'] = 'SID'
                dic_out['port']  = '1521'
                v_service_type = 'oracle'
                element = self.dic_defelement[v_service_type]
                # print element.fields
                s_out = self.get_out_txt(dic_out, element.fields)
                # print s_out
                self.write_to_file(element.f_out, s_out + '\n')

            elif s_tmp.find('check_oracle_tbs_') >= 0:
                # oracle_tbs
                dic_out['ip'] = ip
                dic_out['sid'] = 'SID'
                v_tbs = s_tmp.replace('check_oracle_tbs_', '')
                dic_out['tbs']  = v_tbs
                v_service_type = 'oracle_tbs'
                element = self.dic_defelement[v_service_type]
                # print element.fields
                s_out = self.get_out_txt(dic_out, element.fields)
                # print s_out
                self.write_to_file(element.f_out, s_out + '\n')

            elif s_tmp.find('check_load') >= 0:
                # check_load
                # os
                pass
            elif s_tmp.find('check_disk') >= 0:
                pathname = dic_item['service_description']
                dic_out['ip'] = ip
                dic_out['pathname'] = pathname
                v_service_type = 'disk'
                element = self.dic_defelement[v_service_type]
                # print element.fields
                s_out = self.get_out_txt(dic_out, element.fields)
                # print s_out
                self.write_to_file(element.f_out, s_out + '\n')

    #
    #
    # Write info to txt
    def write_to_file(self, f_out, s_out, f_mode='a'):
        f_w = open(f_out, f_mode)
        f_w.write(s_out)
        f_w.close()

    def do_read_and_parse_cfg(self, file_cfg_r):
        parseCfg = ParseCfg.nagiosCfg(file_cfg_r)
        i_idx = 0
        for element in parseCfg:
            i_idx += 1
            self.do_parse_element(element)


if __name__ == "__main__":
    cnfReader = CfgReader()
    dir_cfg = 'D:/PycharmProjects/Nagios_Tools/etc/objects/linux'
    i = 0
    cnfReader.init_f_out()
    for f in os.listdir(dir_cfg):
        v_f_cfg = dir_cfg + '/' + f
        # print v_f_cfg
        if os.path.isfile(v_f_cfg):
            if i > 0:
                write_type = 'a'
        cnfReader.do_read_and_parse_cfg(v_f_cfg)
        i += 1
