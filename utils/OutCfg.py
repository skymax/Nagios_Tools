#!/usr/bin/python
# coding=UTF-8


import os
import sys

dir_base = os.path.abspath(__file__)
dir_base = os.path.dirname(dir_base)
dir_base = os.path.dirname(dir_base)
sys.path.append(dir_base)
from logger.Logger import Logger


class OutCfg(object):
    dir_template = ""

    def __init__(self, dir_template, map_Hosts, map_Linuxs, map_Hps, map_Windows, logger=None):
        self.map_Hosts = map_Hosts
        self.map_Linuxs = map_Linuxs
        self.map_Hps = map_Hps
        self.map_Windows = map_Windows
        self.dir_template = dir_template
        self.file_template_host_linux = dir_template + "/linux_template_host.tpl"
        self.file_template_host_hp = dir_template + "/hpux_template_host.tpl"
        self.file_template_host_windows = dir_template + "/win_template_host.tpl"
        self.file_template_os_linux = dir_template + "/linux_template_os.tpl"
        self.file_template_os_hp = dir_template + "/hpux_template_os.tpl"
        self.file_template_os_windows = dir_template + "/win_template_os.tpl"
        self.file_template_os_disk = dir_template + "/linux_template_os_disk.tpl"
        self.file_template_tcp = dir_template + "/linux_template_tcp.tpl"
        self.file_template_url = dir_template + "/linux_template_url.tpl"
        self.file_template_log = dir_template + "/linux_template_log.tpl"
        self.file_template_oracle = dir_template + "/linux_template_oracle.tpl"
        self.file_template_oracle_tbs = dir_template + "/linux_template_oracle_tbs.tpl"
        self.file_template_oracle_ogg = dir_template + "/linux_template_oracle_ogg.tpl"
        self.file_template_servicegroup = dir_template + "/ServiceGroup.tpl"
        self.file_template_contact = dir_template + "/contact.tpl"
        self.file_template_contactgroup = dir_template + "/contactgroup.tpl"
        self.file_template_contact_apd = dir_template + "/contact_apd_template.tpl"
        self.file_template_mail = dir_template + "/win_template_mail.tpl"
        self.file_template_weblogicconsole = dir_template + "/weblogic_console.tpl"
        if logger is None:
            logger = Logger.new_logger(self.__class__.__name__)
        self.logger = logger

    def __str__(self):
        return ''

    def out_Cfg_ServiceesCalation(self, dic_beans, classBean, out_dir, dic_fullfilename_cfg):
        # for each serviceescalation in dic
        items = dic_beans.items()
        for v_key, serviceescalation in items:
            v_hostname = serviceescalation.host_name
            v_usergroups = serviceescalation.user_groups
            v_group = v_usergroups[0]
            v_servicedesc = serviceescalation.service_desc
            # file_cfg_name
            file_cfg_name = self.get_file_cfg_name_of_servicecalation(serviceescalation)
            v_out_cfg = out_dir + '/' + file_cfg_name
            if dic_fullfilename_cfg.has_key(v_group):
                pass
            else:
                dic_fullfilename_cfg[v_group] = v_out_cfg
                self.init_file_cfg(v_out_cfg)

            v_f_out = self.get_cfg_use_template_contact_apd(self.file_template_contact_apd, serviceescalation)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_ContactGroup(self, dic_beans, classBeanm, v_file_cfg):
        # for each contactgroup in dic
        items = dic_beans.items()
        self.init_file_cfg(v_file_cfg)
        for v_key, contactgroup in items:
            v_out_cfg = v_file_cfg
            v_f_out = self.get_cfg_use_template_contactgroup(self.file_template_contactgroup, contactgroup)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Contact(self, dic_beans, classBeanm, v_file_cfg):
        # for each contact in dic
        items = dic_beans.items()
        self.init_file_cfg(v_file_cfg)
        for v_key, contact in items:
            v_out_cfg = v_file_cfg
            v_f_out = self.get_cfg_use_template_contact(self.file_template_contact, contact)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_ServiceGroup(self, dic_beans, classBeanm, v_file_cfg):
        # for each servicegroup in dic
        items = dic_beans.items()
        self.init_file_cfg(v_file_cfg)
        for v_key, servicegroup in items:
            v_out_cfg = v_file_cfg
            v_f_out = self.get_cfg_use_template_servicegroup(self.file_template_servicegroup, servicegroup)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Tcp(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each tcp in dic
        items = dic_beans.items()
        for v_key, tcp in items:
            v_ip = tcp.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_tcp(self.file_template_tcp, tcp)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_WeblogicConsole(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each tcp in dic
        items = dic_beans.items()
        for v_key, weblogicconsole in items:
            v_ip = weblogicconsole.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_weblogicconsole(self.file_template_weblogicconsole, weblogicconsole)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Oracle_GoldenGate(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each oracle_goldengate in dic
        items = dic_beans.items()
        for v_key, oracle_goldengate in items:
            v_ip = oracle_goldengate.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_oracle_goldengate(self.file_template_oracle_ogg, oracle_goldengate)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Oracle_Tbs(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each oracle_tbs in dic
        items = dic_beans.items()
        for v_key, oracle_tbs in items:
            v_ip = oracle_tbs.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_oracle_tbs(self.file_template_oracle_tbs, oracle_tbs)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Mail(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each mail in dic
        items = dic_beans.items()
        for v_key, mail in items:
            v_ip = mail.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_mail(self.file_template_mail, mail)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Oracle(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each oracle in dic
        items = dic_beans.items()
        for v_key, oracle in items:
            v_ip = oracle.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_oracle(self.file_template_oracle, oracle)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Log(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each log in dic
        items = dic_beans.items()
        for v_key, log in items:
            v_ip = log.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_log(self.file_template_log, log)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Url(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each url in dic
        items = dic_beans.items()
        for v_key, url in items:
            v_ip = url.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_url(self.file_template_url, url)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_cfg_Disk(self, dic_beans, classBeanm, dic_fullfilename_cfg):
        # for each disk in dic
        items = dic_beans.items()
        for v_key, disk in items:
            v_ip = disk.ip
            # get out cfg file from dic using ip
            v_out_cfg = dic_fullfilename_cfg[v_ip]
            v_f_out = self.get_cfg_use_template_os_disk(self.file_template_os_disk, disk)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_Cfg_Windows(self, dic_beans, classBean, out_dir, dic_fullfilename_cfg):
        # for each Windows in dic
        items = dic_beans.items()
        for v_key, windows in items:
            # file_cfg_name
            v_ip = windows.ip
            file_cfg_name = self.get_file_cfg_name(windows)
            v_out_cfg = out_dir + '/' + file_cfg_name
            dic_fullfilename_cfg[v_ip] = v_out_cfg
            self.init_file_cfg(v_out_cfg)
            v_f_out = self.get_cfg_use_template_host_windows(self.file_template_host_windows, windows)
            self.write_to_cfg(v_out_cfg, v_f_out)
            v_f_out = self.get_cfg_use_template_os_windows(self.file_template_os_windows, windows)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_Cfg_Linux(self, dic_beans, classBean, out_dir, dic_fullfilename_cfg):
        # for each linux in dic
        items = dic_beans.items()
        for v_key, linux in items:
            # file_cfg_name
            v_ip = linux.ip
            file_cfg_name = self.get_file_cfg_name(linux)
            v_out_cfg = out_dir + '/' + file_cfg_name
            dic_fullfilename_cfg[v_ip] = v_out_cfg
            self.init_file_cfg(v_out_cfg)
            v_f_out = self.get_cfg_use_template_host_linux(self.file_template_host_linux, linux)
            self.write_to_cfg(v_out_cfg, v_f_out)
            v_f_out = self.get_cfg_use_template_os_linux(self.file_template_os_linux, linux)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def out_Cfg_Hp(self, dic_beans, classBean, out_dir, dic_fullfilename_cfg):
        # for each linux in dic
        items = dic_beans.items()
        for v_key, hp in items:
            # file_cfg_name
            v_ip = hp.ip
            file_cfg_name = self.get_file_cfg_name(hp)
            v_out_cfg = out_dir + '/' + file_cfg_name
            dic_fullfilename_cfg[v_ip] = v_out_cfg
            self.init_file_cfg(v_out_cfg)
            v_f_out = self.get_cfg_use_template_host_hp(self.file_template_host_hp, hp)
            self.write_to_cfg(v_out_cfg, v_f_out)
            v_f_out = self.get_cfg_use_template_os_hp(self.file_template_os_hp, hp)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def init_file_cfg(self, f_out):
        f_w = open(f_out, 'w')
        f_w.close()

    def write_to_cfg(self, f_out, strOut):
        f_w = open(f_out, 'a')
        f_w.write(strOut)
        f_w.close()

    def get_cfg_use_otemplate_contactgroup(self, f_template, contactgroup):
        v_tpl = self.get_tpl_str(f_template)

        v_name = contactgroup.name
        v_alias = contactgroup.alias
        v_members = contactgroup.members
        str_member = ''
        i = 0
        for s in v_members:
            if i > 0:
                str_member += ','
            str_member += s
            i += 1

        # contactgroup_name       #CONTACTGROUP_NAME#						            ; Short name of usergroup
        # alias                   #ALIAS#												; Full name of usergroup
        # members                 #MEMBERS#											; split by ,

        v_tpl = v_tpl.replace('#CONTACTGROUP_NAME#', v_name)
        v_tpl = v_tpl.replace('#ALIAS#', v_alias)
        v_tpl = v_tpl.replace('#MEMBERS#', str_member)

        return v_tpl

    def get_cfg_use_template_contact_apd(self, f_template, serviceescalation):
        v_tpl = self.get_tpl_str(f_template)

        host_name = serviceescalation.host_name
        service_desc = serviceescalation.service_desc
        user_groups = serviceescalation.user_groups

        str_member = ''
        i = 0
        for s in user_groups:
            if i > 0:
                str_member += ','
            str_member += s
            i += 1

        # HOST_NAME# #SERVICE_DESC# #USER_GROUPS#
        v_tpl = v_tpl.replace('#HOST_NAME#', host_name)
        v_tpl = v_tpl.replace('#SERVICE_DESC#', service_desc)
        v_tpl = v_tpl.replace('#USER_GROUPS#', str_member)

        return v_tpl

    def get_cfg_use_template_contactgroup(self, f_template, contactgroup):
        v_tpl = self.get_tpl_str(f_template)

        v_name = contactgroup.name
        v_alias = contactgroup.alias
        v_members = contactgroup.members
        str_member = ''
        i = 0
        for s in v_members:
            if i > 0:
                str_member += ','
            str_member += s
            i += 1

        # contactgroup_name       #CONTACTGROUP_NAME#						            ; Short name of usergroup
        # alias                   #ALIAS#												; Full name of usergroup
        # members                 #MEMBERS#											; split by ,

        v_tpl = v_tpl.replace('#CONTACTGROUP_NAME#', v_name)
        v_tpl = v_tpl.replace('#ALIAS#', v_alias)
        v_tpl = v_tpl.replace('#MEMBERS#', str_member)

        return v_tpl

    def get_cfg_use_template_contact(self, f_template, contact):
        v_tpl = self.get_tpl_str(f_template)
        v_name = contact.name
        v_alias = contact.alias
        v_use = contact.use
        v_email = contact.email
        v_phone_number = contact.phone_number
        v_weixinid = contact.weixinid

        # contact_name                    #CONTACT_NAME#                          ; Short name of user
        # use                             #USE#                                   ; Inherit default values from generic-contact template (defined above)
        # alias                           #ALIAS#                                 ; Full name of user
        # email                           #EMAIL#                                 ; EMAIL ADDRESS
        # pager                           #PHONE_NUMBER#                          ; phone number
        # _weixinid                       #WEIXINID#                              ; weixin

        v_tpl = v_tpl.replace('#CONTACT_NAME#', v_name)
        v_tpl = v_tpl.replace('#ALIAS#', v_alias)
        v_tpl = v_tpl.replace('#USE#', v_use)
        v_tpl = v_tpl.replace('#EMAIL#', v_email)
        v_tpl = v_tpl.replace('#PHONE_NUMBER#', v_phone_number)
        v_tpl = v_tpl.replace('#WEIXINID#', v_weixinid)

        return v_tpl

    def get_cfg_use_template_servicegroup(self, f_template, servicegroup):
        v_tpl = self.get_tpl_str(f_template)
        v_name = servicegroup.name
        v_alias = servicegroup.alias

        # servicegroup_name  #SERVICE_NAME# ; The name of the servicegroup
        # alias  #ALIAS# ; Long name of the g2roup

        v_tpl = v_tpl.replace('#SERVICE_NAME#', v_name)
        v_tpl = v_tpl.replace('#ALIAS#', v_alias)

        return v_tpl

    def get_cfg_use_template_tcp(self, f_template, tcp):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = tcp.ip
        v_port = tcp.port

        # host_name               #HOST_NAME#
        # service_description     #CHECK_DESC#
        # check_command           check_nrpe!#CHECK_CMD#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]

        v_str_cmd = 'check_tcp_stat'
        v_str_desc = 'check-tcp-stat'
        if v_port != '':
            v_str_cmd += '_port_' + v_port
            v_str_desc += '-port-' + v_port

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#CHECK_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#CHECK_CMD#', v_str_cmd)

        return v_tpl

        v_str_cmd = 'check_tcp_stat'
        v_str_desc = 'check-tcp-stat'
        if v_port != '':
            v_str_cmd += '_port_' + v_port
            v_str_desc += '-port-' + v_port

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#CHECK_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#CHECK_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_weblogicconsole(self, f_template, weblogicconsole):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = weblogicconsole.ip
        v_port = weblogicconsole.port

        # host_name               #HOST_NAME#
        # service_description     check-wls-console-#WLS_PORT#-JDBC
        # check_command           check_nrpe!check_wls_console_#WLS_PORT#_JDBC

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#WLS_PORT#', v_port)

        return v_tpl

    def get_cfg_use_template_oracle_goldengate(self, f_template, oracle_goldengate):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = oracle_goldengate.ip
        v_goldengate_path = oracle_goldengate.goldengate_path
        v_goldengate_process = oracle_goldengate.goldengate_process

        # host_name               #HOST_NAME#
        # service_description     #OGG_DESC#
        # check_command           check_nrpe!#OGG_CMD#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]

        v_str_desc = 'check-goldengate-' + v_goldengate_process.lower()
        v_str_cmd = 'check_goldengate_' + v_goldengate_process.lower()

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#OGG_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#OGG_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_oracle_tbs(self, f_template, oracle_tbs):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = oracle_tbs.ip
        v_tbs = oracle_tbs.tbs
        # host_name               #HOST_NAME#
        # service_description     #TBS_DESC#
        # check_command           check_nrpe!#TBS_CMD#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
        v_str_desc = 'check-oracle-tbs-' + v_tbs.lower()
        v_str_cmd = 'check_oracle_tbs_' + v_tbs.lower()

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#TBS_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#TBS_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_mail(self, f_template, mail):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = mail.ip

        # host_name               #HOST_NAME#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
        elif v_type == 'win':
            windows = self.map_Windows[v_ip]

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)

        return v_tpl

    def get_cfg_use_template_oracle(self, f_template, oracle):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = oracle.ip

        # host_name               #HOST_NAME#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)

        return v_tpl

    def get_cfg_use_template_log(self, f_template, log):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = log.ip
        v_pattern = log.pattern

        v_desc = log.desc

        # host_name               #HOST_NAME#
        # service_description     #LOG_DESC#
        # check_command           check_nrpe!#LOG_CMD#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
        v_str_cmd = 'check_log_' + v_desc
        v_str_desc = 'check-log-' + v_desc.replace('_', '-')

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#LOG_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#LOG_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_url(self, f_template, url):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = url.ip
        v_url = url.url
        v_port = url.port

        # host_name               #HOST_NAME#
        # service_description     #URL_DESC#
        # check_command           check_nrpe!#URL_CMD#

        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
        arr_val = v_url.split('/')
        vs_url = arr_val[1]
        v_str_desc = 'check-url-' + vs_url + '-' + v_port
        v_str_cmd = 'check_url_' + vs_url + '_' + v_port

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#URL_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#URL_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_os_disk(self, f_template, disk):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = disk.ip
        v_pathname = disk.pathname

        # host_name               #HOST_NAME#
        # service_description     #DISK_DESC# Free Space
        # check_command           check_nrpe!#DISK_CMD#
        v_type = self.map_Hosts[v_ip]
        v_hname = self.get_hname(v_ip, v_type)
        if v_type == 'linux':
            linux = self.map_Linuxs[v_ip]
        elif v_type == 'hp':
            hp = self.map_Hps[v_ip]
        elif v_type == 'win':
            windows = self.map_Windows
        v_str_desc = v_pathname
        if v_type == 'win':
            v_str_cmd = 'alias_disk_' + v_pathname.replace(':', '')
        else:
            v_str_cmd = 'check_disk' + v_pathname.replace('/', '_')

        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#DISK_DESC#', v_str_desc)
        v_tpl = v_tpl.replace('#DISK_CMD#', v_str_cmd)

        return v_tpl

    def get_cfg_use_template_os_windows(self, f_template, windows):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = windows.ip
        v_hostname = windows.hostname
        v_group_name = windows.group_name
        v_type = windows.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_cfg_use_template_os_linux(self, f_template, linux):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = linux.ip
        v_hostname = linux.hostname
        v_group_name = linux.group_name
        v_type = linux.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_cfg_use_template_os_hp(self, f_template, hp):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = hp.ip
        v_hostname = hp.hostname
        v_group_name = hp.group_name
        v_type = hp.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_cfg_use_template_host_linux(self, f_template, linux):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = linux.ip
        v_hostname = linux.hostname
        v_group_name = linux.group_name
        v_type = linux.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        # alias                   #HOST_NAME#(#MACHINE_NAME#)
        # hostgroups              #HOST_GROUPS#
        # address                 #HOST_IP#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#MACHINE_NAME#', v_hostname)
        v_tpl = v_tpl.replace('#HOST_GROUPS#', v_group_name)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_hname(self, v_ip, v_type):
        v_hname = v_type + '_' + v_ip
        return v_hname

    def get_cfg_use_template_host_hp(self, f_template, hp):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = hp.ip
        v_hostname = hp.hostname
        v_group_name = hp.group_name
        v_type = hp.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        # alias                   #HOST_NAME#(#MACHINE_NAME#)
        # hostgroups              #HOST_GROUPS#
        # address                 #HOST_IP#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#MACHINE_NAME#', v_hostname)
        v_tpl = v_tpl.replace('#HOST_GROUPS#', v_group_name)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_cfg_use_template_host_windows(self, f_template, windows):
        v_tpl = self.get_tpl_str(f_template)
        v_ip = windows.ip
        v_hostname = windows.hostname
        v_group_name = windows.group_name
        v_type = windows.type
        v_hname = self.get_hname(v_ip, v_type)

        # host_name               #HOST_NAME#
        # alias                   #HOST_NAME#(#MACHINE_NAME#)
        # hostgroups              #HOST_GROUPS#
        # address                 #HOST_IP#
        v_tpl = v_tpl.replace('#HOST_NAME#', v_hname)
        v_tpl = v_tpl.replace('#MACHINE_NAME#', v_hostname)
        v_tpl = v_tpl.replace('#HOST_GROUPS#', v_group_name)
        v_tpl = v_tpl.replace('#HOST_IP#', v_ip)

        return v_tpl

    def get_tpl_str(self, f_template):
        f_tpl = open(f_template, 'r')
        line = f_tpl.readline()
        v_tpl = ''
        while line:
            v_tpl += line
            line = f_tpl.readline()
        f_tpl.close()

        return v_tpl

    def out_Cfg_Hp(self, dic_beans, classBean, out_dir, dic_fullfilename_cfg):
        # for each hp in dic
        items = dic_beans.items()
        for v_key, hp in items:
            # file_cfg_name
            file_cfg_name = self.get_file_cfg_name(hp)
            v_out_cfg = out_dir + '/' + file_cfg_name
            v_ip = hp.ip
            dic_fullfilename_cfg[v_ip] = v_out_cfg
            self.init_file_cfg(v_out_cfg)
            v_f_out = self.get_cfg_use_template_host_hp(self.file_template_host_hp, hp)
            self.write_to_cfg(v_out_cfg, v_f_out)
            v_f_out = self.get_cfg_use_template_os_hp(self.file_template_os_hp, hp)
            self.write_to_cfg(v_out_cfg, v_f_out)

    def get_file_cfg_name(self, host):
        v_str = ''
        v_str = host.type + '_' + host.ip + '.cfg'
        return v_str

    def get_file_cfg_name_of_servicecalation(self, servicecalation):
        v_str = ''
        v_group = servicecalation.user_groups[0]
        v_str = 'contact_apd__' + v_group + '.cfg'
        return v_str

    def out_Cfg_group(self, dic_beans, file_templat, classBean, out_file):
        items = dic_beans.items()
        f = open(out_file, 'w')
        f_tpl = open(file_templat, 'r')
        line = f_tpl.readline()
        v_tpl_tmp = ''
        while line:
            v_tpl_tmp += line
            line = f_tpl.readline()
        f_tpl.close()

        for v_key, group in items:
            v_name = group.get_Name()
            v_alais = group.get_Alias()
            v_tpl = v_tpl_tmp.replace('#HOSTGROUP_NAME#', v_name)
            v_tpl = v_tpl.replace('#ALIAS#', v_alais)
            f.write(v_tpl)
            f.write('\n\n')
        f.close()
