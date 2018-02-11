#!/usr/bin/python
# -*- coding:gb2312 -*-
import os
import sys

dir_base = os.path.abspath(__file__)
dir_base = os.path.dirname(dir_base)
dir_base = os.path.dirname(dir_base)
sys.path.append(dir_base)
from logger.Logger import Logger

class BeanInit(object):

    def __init__(self, logger = None):
        if logger is None:
            logger = Logger.new_logger(self.__class__.__name__)
        self.logger = logger


    def __str__(self):
        return ''

    def init_Oracle_GoldenGate(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            # ip|goldengate_path|goldengate_process
            ip = arr_val[0].strip()
            goldengate_path = arr_val[1].strip()
            goldengate_process = arr_val[2].strip()
            oracle_goldengate = classBean(ip, goldengate_path, goldengate_process)
            dic_Beans[i_idx] = oracle_goldengate
            self.logger.debug("%s = %s" % (i_idx, oracle_goldengate))
            line = f.readline()
        f.close()

    def init_ServiceesCalation(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            i_idx += 1
            arr_val = line.split('|')
            # 'host_name', 'service_description', 'contact_groups'
            host_name = arr_val[0].strip()
            service_description = arr_val[1].strip()
            contact_groups = arr_val[2].strip().split(',')
            servicecalation = classBean(host_name, service_description, contact_groups)
            dic_Beans[i_idx] = servicecalation
            self.logger.debug("%s = %s" % (i_idx, servicecalation))
            line = f.readline()
        f.close()

    def init_ContactGroup(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            # 'contactgroup_name', 'alias', 'members')
            contactgroup_name = arr_val[0].strip()
            alias = arr_val[1].strip()
            members = arr_val[2].strip().split(',')
            contact = classBean(contactgroup_name, alias, members)
            dic_Beans[i_idx] = contact
            self.logger.debug("%s = %s" % (i_idx, contact))
            line = f.readline()
        f.close()

    def init_Contact(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            # 'contact_name', 'use', 'alias', 'email', 'pager', '_weixinid'
            contact_name = arr_val[0].strip()
            use = arr_val[1].strip()
            alias = arr_val[2].strip()
            email = arr_val[3].strip()
            pager = arr_val[4].strip()
            weixinid = arr_val[5].strip()
            contact = classBean(contact_name, use, alias, email, pager, weixinid)
            dic_Beans[i_idx] = contact
            self.logger.debug("%s = %s" % (i_idx, contact))
            line = f.readline()
        f.close()

    def init_Disk(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_pathname = arr_val[1].strip()
            disk = classBean(v_ip, v_pathname)
            dic_Beans[i_idx] = disk
            self.logger.debug("%s = %s" % (i_idx, disk))
            line = f.readline()
        f.close()

    def init_Mail(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            mail = classBean(v_ip)
            dic_Beans[i_idx] = mail
            self.logger.debug("%s = %s" % (i_idx, mail))
            line = f.readline()
        f.close()

    def init_Oracle(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_sid = arr_val[1].strip()
            v_port = arr_val[2].strip()
            oracle = classBean(v_ip, v_sid, v_port)
            dic_Beans[i_idx] = oracle
            self.logger.debug("%s = %s" % (i_idx, oracle))
            line = f.readline()
        f.close()

    def init_Oracle_Tbs(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_sid = arr_val[1].strip()
            v_tbs = arr_val[2].strip()
            oracle_tbs = classBean(v_ip, v_sid, v_tbs)
            dic_Beans[i_idx] = oracle_tbs
            self.logger.debug("%s = %s" % (i_idx, oracle_tbs))
            line = f.readline()
        f.close()

    def init_Linux(self, dic_Beans, map_Beans, c_filename, classBean, map_Hosts):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_group_name = arr_val[0].strip()
            v_ip = arr_val[1].strip()
            v_hostname = arr_val[2].strip()

            linux = classBean(v_group_name, v_ip, v_hostname)
            dic_Beans[i_idx] = linux
            map_Beans[v_ip] = linux
            map_Hosts[v_ip] = linux.type
            self.logger.debug("%s = %s" % (i_idx, linux))

            line = f.readline()
        f.close()

    def init_Hp(self, dic_Beans, map_Beans, c_filename, classBean, map_Hosts):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_group_name = arr_val[0].strip()
            v_ip = arr_val[1].strip()
            v_hostname = arr_val[2].strip()

            hp = classBean(v_group_name, v_ip, v_hostname)
            dic_Beans[i_idx] = hp
            map_Beans[v_ip] = hp
            map_Hosts[v_ip] = hp.type
            self.logger.debug("%s = %s" % (i_idx, hp))

            line = f.readline()
        f.close()

    def init_Windows(self, dic_Beans, map_Beans, c_filename, classBean, map_Hosts):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_group_name = arr_val[0].strip()
            v_ip = arr_val[1].strip()
            v_hostname = arr_val[2].strip()

            windows = classBean(v_group_name, v_ip, v_hostname)
            dic_Beans[i_idx] = windows
            map_Beans[v_ip] = windows
            map_Hosts[v_ip] = windows.type
            self.logger.debug("%s = %s" % (i_idx, windows))

            line = f.readline()
        f.close()

    def init_ServiceGroup(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_name = arr_val[0].strip()
            v_alias = arr_val[1].strip()
            # print "--%s--%s--" % (v_name, v_alias)
            servicegroup = classBean(v_name, v_alias)
            dic_Beans[i_idx] = servicegroup
            self.logger.debug("%s = %s" % (i_idx, servicegroup))
            line = f.readline()
        f.close()

    def init_WeblogicConsole(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_port = arr_val[1].strip()
            weblogicconsole = classBean(v_ip, v_port)
            dic_Beans[i_idx] = weblogicconsole
            self.logger.debug("%s = %s" % (i_idx, weblogicconsole))
            line = f.readline()
        f.close()

    def init_Tcp(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_port = arr_val[1].strip()
            # print "--%s--%s--" % (v_ip, v_port)
            tcp = classBean(v_ip, v_port)
            dic_Beans[i_idx] = tcp
            self.logger.debug("%s = %s" % (i_idx, tcp))
            line = f.readline()
        f.close()

    def init_Url(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue

            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_port = arr_val[1].strip()
            v_url = arr_val[2].strip()
            url = classBean(v_ip, v_port, v_url)
            dic_Beans[i_idx] = url
            self.logger.debug("%s = %s" % (i_idx, url))
            line = f.readline()
        f.close()

    def init_Group(self, dic_Beans, map_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_name = arr_val[0].strip()
            v_alias = arr_val[1].strip()

            group = classBean(v_name, v_alias)
            dic_Beans[i_idx] = group
            map_Beans[v_name] = group
            self.logger.debug( "%s = %s" % (i_idx, group))

            line = f.readline()
        f.close()

    def init_Log(self, dic_Beans, c_filename, classBean):
        # read from file
        # init dic_Beans
        f = open(c_filename, 'r')
        line = f.readline()
        i_idx = 0
        while line:
            if line.find('#') == 0:
                line = f.readline()
                continue
            i_idx += 1
            arr_val = line.split('|')
            v_ip = arr_val[0].strip()
            v_desc = arr_val[1].strip()
            v_pattern = arr_val[2].strip()
            log = classBean(v_ip, v_desc, v_pattern)
            dic_Beans[i_idx] = log
            self.logger.debug( "%s = %s" % (i_idx, log))
            line = f.readline()
        f.close()
