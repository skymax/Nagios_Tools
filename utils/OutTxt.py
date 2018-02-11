#!/usr/bin/python
# -*- coding:gb2312 -*-

import os
import sys

dir_base = os.path.abspath(__file__)
dir_base = os.path.dirname(dir_base)
dir_base = os.path.dirname(dir_base)
sys.path.append(dir_base)
from logger.Logger import Logger


class OutTxt(object):
    map_Hosts = {}
    map_Linuxs = {}
    map_Hps = {}

    def __init__(self, map_Hosts, map_Linuxs, map_Hps, map_Windows, logger=None):
        self.map_Hosts = map_Hosts
        self.map_Linuxs = map_Linuxs
        self.map_Hps = map_Hps
        self.map_Windows = map_Windows
        if logger is None:
            logger = Logger.new_logger(self.__class__.__name__)
        self.logger = logger

    def __str__(self):
        return ''

    def get_out_of_(self, linux):
        v_str_rnt = ''
        v_type = linux.type
        v_group_name = linux.group_name
        v_hostname = linux.hostname
        v_ip = linux.ip
        # 9.20.128.10^linux_9.20.128.10^newcore-app-128-10^ncp-policy
        # ip^type_ip^hostname^group_nmae
        v_str_rnt = v_ip + '^' + v_type + '_' + v_ip + '^' + v_hostname + '^' + v_group_name
        return v_str_rnt

    def get_out_of_url(self, url):
        v_str_rnt = ''
        v_ip = url.ip
        v_port = url.port
        v_url = url.url

        v_str_hosts = self.get_str_hosts(v_ip)

        # 9.23.29.35^linux_9.23.29.35^xg_app_29_35^nsale-app^check-url-plant-7001^check_url_plant_7001
        # hots^
        arr_val = v_url.split('/')
        vs_url = arr_val[1]
        v_str_desc = 'check-url-' + vs_url + '-' + v_port
        v_str_cmd = 'check_url_' + vs_url + '_' + v_port

        v_str_rnt = v_str_hosts + '^' + v_str_desc + '^' + v_str_cmd
        return v_str_rnt

    def get_str_hosts(self, v_ip):
        v_type = self.map_Hosts[v_ip]
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
            v_str_hosts = self.get_out_of_(linux)
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
            v_str_hosts = self.get_out_of_(hp)
        elif v_type == 'win':
            windows = self.map_Windows[v_ip]
            v_str_hosts = self.get_out_of_(windows)
        return v_str_hosts

    def get_out_of_tcp(self, tcp):
        v_str_rnt = ''
        v_ip = tcp.ip
        v_port = tcp.port

        v_str_hosts = self.get_str_hosts(v_ip)
        # 9.23.19.63^linux_9.23.19.63^coreapp-19-63^ecc-shouyintaicenter-app-servers^check-tcp-stat^check_tcp_stat
        # 9.23.19.63^linux_9.23.19.63^coreapp-19-63^ecc-shouyintaicenter-app-servers^check-tcp-stat-port-7001^check_tcp_stat_port_7001
        v_str_cmd = 'check_tcp_stat'
        v_str_desc = 'check-tcp-stat'
        if v_port != '':
            v_str_cmd += '_port_' + v_port
            v_str_desc += '-port-' + v_port

        v_str_rnt = '%s^%s^%s' % (v_str_hosts, v_str_desc, v_str_cmd)
        return v_str_rnt

    def get_out_of_log(self, log):
        v_str_rnt = ''
        v_ip = log.ip
        v_desc = log.desc
        v_pattern = log.pattern

        v_str_hosts = self.get_str_hosts(v_ip)

        # 9.23.29.35^linux_9.23.29.35^xg_app_29_35^nsale-app^check-log-srv-out-jdbc-disable^check_log_srv_out_jdbc_disable
        # hots^
        v_str_cmd = 'check_log_' + v_desc
        v_str_desc = 'check-log-' + v_desc.replace('_', '-')

        v_str_rnt = v_str_hosts + '^' + v_str_desc + '^' + v_str_cmd
        return v_str_rnt

    def get_out_of_disk(self, disk):
        v_str_rnt = ''
        v_ip = disk.ip
        v_pathname = disk.pathname

        v_str_hosts = self.get_str_hosts(v_ip)
        v_type = self.map_Hosts[v_ip]
        # 9.20.128.2^linux_9.20.128.2^newcore-app-128-2^ncp-policy^\/ncwebapps_inc^check_disk_ncwebapps_inc
        # alias_disk_e
        # hots^
        v_str_desc = v_pathname.replace('/', '\/')
        if v_type == 'win':
            v_str_cmd = 'alias_disk_' + v_pathname.replace(':', '')
        else:
            v_str_cmd = 'check_disk' + v_pathname.replace('/', '_')

        v_str_rnt = v_str_hosts + '^' + v_str_desc + '^' + v_str_cmd
        return v_str_rnt

    def get_out_of_oracle(self, oracle):
        v_str_rnt = ''
        v_ip = oracle.ip
        v_str_hosts = self.get_str_hosts(v_ip)
        v_str_rnt = v_str_hosts
        return v_str_rnt

    def get_out_of_oracle_goldengate(self, oracle_goldengate):
        v_str_rnt = ''
        v_ip = oracle_goldengate.ip
        v_goldengate_path = oracle_goldengate.goldengate_path
        v_goldengate_process = oracle_goldengate.goldengate_process

        v_str_hosts = self.get_str_hosts(v_ip)
        # 9.23.2.81^hp_9.23.2.81^cxnewpolicydb01^ncp-policy^check-goldengate-repgpc15^check_goldengate_repgpc15
        v_str_desc = 'check-goldengate-' + v_goldengate_process.lower()
        v_str_cmd = 'check_goldengate_' + v_goldengate_process.lower()

        v_str_rnt = v_str_hosts + '^' + v_str_desc + '^' + v_str_cmd
        return v_str_rnt

    def get_out_of_oracle_tbs(self, oracle_Tbs):
        v_str_rnt = ''
        v_ip = oracle_Tbs.ip
        v_tbs = oracle_Tbs.tbs
        v_str_hosts = self.get_str_hosts(v_ip)
        # 9.23.2.81^hp_9.23.2.81^cxnewpolicydb01^ncp-policy^check-oracle-tbs-system^check_oracle_tbs_system
        v_str_desc = 'check-oracle-tbs-' + v_tbs.lower()
        v_str_cmd = 'check_oracle_tbs_' + v_tbs.lower()

        v_str_rnt = v_str_hosts + '^' + v_str_desc + '^' + v_str_cmd
        return v_str_rnt

    def out_Txt_Host_(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, linux in items:
            self.logger.debug(linux)
            v_str_out = self.get_out_of_(linux)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Tcp(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, tcp in items:
            v_str_out = self.get_out_of_tcp(tcp)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Url(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, url in items:
            v_str_out = self.get_out_of_url(url)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Oracle(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, oracle in items:
            v_str_out = self.get_out_of_oracle(oracle)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Oracle_GoldenGate(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, oracle_goldengate in items:
            v_str_out = self.get_out_of_oracle_goldengate(oracle_goldengate)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Oracle_Tbs(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, oracle_Tbs in items:
            v_str_out = self.get_out_of_oracle_tbs(oracle_Tbs)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Disk(self, dic_beans, className, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, disk in items:
            v_str_out = self.get_out_of_disk(disk)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()

    def out_Txt_Log(self, dic_beans, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        for v_key, log in items:
            v_str_out = self.get_out_of_log(log)
            self.logger.debug(v_str_out)
            f.write(v_str_out)
            f.write('\n')
        f.close()
