#!/usr/bin/python
# coding=UTF-8

# dir_base = "D:/PycharmProjects/Nagios_Tools"
import os
import sys

# get base directory
dir_base = os.path.abspath(__file__)
dir_base = os.path.dirname(dir_base)
sys.path.append(dir_base)
# sys.path.append(dir_base + "/beans")
# sys.path.append(dir_base + "/utils")

from beans.Disk import Disk
from beans.Aix import Aix
from beans.Contact import Contact
from beans.ContactGroup import ContactGroup
from beans.Group import Group
from beans.Host import Host
from beans.Hp import Hp
from beans.Linux import Linux
from beans.Log import Log
from beans.Mail import Mail
from beans.Oracle import Oracle
from beans.Oracle_GoldenGate import Oracle_GoldenGate
from beans.Oracle_Tbs import Oracle_Tbs
from beans.ServiceesCalation import ServiceesCalation
from beans.ServiceGroup import ServiceGroup
from beans.Tcp import Tcp
from beans.Url import Url
from beans.WeblogicConsole import WeblogicConsole
from beans.Windows import Windows

from utils.BeanInit import BeanInit
from utils.OutCfg import OutCfg
from utils.OutTxt import OutTxt
from logger.Logger import Logger

# from Disk import Disk
# from Group import Group
# from Hp import Hp
# from Linux import Linux
# from Windows import Windows
# from Url import Url
# from Tcp import Tcp
#
# from Oracle import Oracle
# from Oracle_Tbs import Oracle_Tbs

# from BeanInit import BeanInit
# from OutCfg import OutCfg
# from OutTxt import OutTxt
# from Log import Log
# from ServiceGroup import ServiceGroup
# from Contact import Contact
# from ContactGroup import ContactGroup
# from ServiceesCalation import ServiceesCalation
# from Oracle_GoldenGate import Oracle_GoldenGate
# from Mail import Mail
# from WeblogicConsole import WeblogicConsole

# dir_
dir_in = dir_base + "/in"
file_in_disk = dir_in + "/disk.txt"
file_in_linux = dir_in + "/linux-host.txt"
file_in_win = dir_in + "/win-host.txt"
file_in_url = dir_in + "/url.txt"
file_in_group = dir_in + "/group.txt"
file_in_hp = dir_in + "/hp-host.txt"
file_in_oracle = dir_in + "/oracle.txt"
file_in_oracle_tbs = dir_in + "/oracle_tbs.txt"
file_in_log = dir_in + "/chk_log.txt"
file_in_tcp = dir_in + "/tcp.txt"
file_in_servicegroup = dir_in + "/servicegroup.txt"
file_in_contact = dir_in + "/servicegroup.txt"
file_in_servicegroup = dir_in + "/servicegroup.txt"
file_in_contact = dir_in + "/contact.txt"
file_in_contactgroup = dir_in + "/contactgroup.txt"
file_in_serviceescalation = dir_in + "/serviceescalation.txt"
file_in_oracle_goldengate = dir_in + "/goldengate.txt"
file_in_mail = dir_in + "/mail.txt"
file_in_weblogicconsole = dir_in + "/weblogic-console.txt"

dir_templates = dir_base + "/templates"
file_tpl_group = dir_templates + "/Group.tpl"

dir_out_cfg = dir_base + "/cfg"

file_cfg_group = dir_out_cfg + "/Groups.cfg"
file_cfg_servicegroup = dir_out_cfg + "/servicegroup.cfg"
file_cfg_contact = dir_out_cfg + "/contact.cfg"
file_cfg_contactgroup = dir_out_cfg + "/contactgroup.cfg"

dir_out_cfg_linux = dir_out_cfg + '/linux'
dir_out_cfg_hp = dir_out_cfg + '/hpux'
dir_out_cfg_win = dir_out_cfg + '/win'
dir_out_cfg_contact = dir_out_cfg + '/contact'

dir_out_txt = dir_base + "/out"
file_out_hosts_linux = dir_out_txt + "/f_host1.txt"
file_out_hosts_hp = dir_out_txt + "/f_host_hp1.txt"
file_out_hosts_win = dir_out_txt + "/f_host_win.txt"
file_out_urls = dir_out_txt + "/f_url1.txt"
file_out_disks = dir_out_txt + "/f_disk1.txt"
file_out_oracles = dir_out_txt + "/f_oracle1.txt"
file_out_oracle_tbss = dir_out_txt + "/f_oracle_tbs1.txt"
file_out_chklog = dir_out_txt + "/f_chk_log.txt"
file_out_tcp = dir_out_txt + "/f_tcp.txt"
file_out_goldengate = dir_out_txt + "/f_oracle_ogg.txt"

# Diske [index] = Diks()
dic_Disks = {}

# Linux
# s
# [index] = Linux()
dic_Linuxs = {}
# [ip] = Linux()
map_Linuxs = {}

# Hp
# [index] = Hp()
dic_Hps = {}
# [ip] = Hp()
map_Hps = {}

# Win
# [index] = Windows()
dic_Windows = {}
# [ip] = Windows()
map_Windows = {}

# Aix

# Url
# [index] = Url()
dic_Urls = {}

# Log
# [index] = Log()
dic_Logs = {}

# hosts_types
# [ip] = Type(linux,hp)
map_Hosts = {}

# Group
# [index] = Group()
dic_Groups = {}
# [name] = Group()
map_Groups = {}

# Oracle
dic_Oracles = {}

# Oracle_Tbs
dic_Oracle_Tbss = {}

# Tcps
dic_Tcps = {}

# cfg file
# [ip] = full filename with path
dic_fullfilename_cfg = {}

# servicegroup
# [index] = ServiceGroup
dic_servicegroup = {}

# Contact
# [index] = Contact
dic_contacts = {}

# ContactGroup
# [index] = ContactGroup
dic_contactgroups = {}

# ServiceesCalation
# [index] = ServiceesCalation
dic_serviceescalation = {}

# cfg file
# [ip] = full filename with path
dic_fullfilename_contact_cfg = {}

# Oracle_GoldenGate
# [index] = Oracle_GoldenGate
dic_oracle_goldengate = {}

# Mail
# [index] = Mail
dic_mail = {}

# WeblogicConsole
# [index] = WeblogicConsole()
dic_weblogicconsole = {}

if __name__ == "__main__":
    c_logger = Logger(__name__, dir_base)
    logger = c_logger.get_logger()
    logger.info('Begin BeanInit')
    beanInit = BeanInit()
    # init  dic and map
    beanInit.init_Disk(dic_Disks, file_in_disk, Disk)
    beanInit.init_Linux(dic_Linuxs, map_Linuxs, file_in_linux, Linux, map_Hosts)
    beanInit.init_Hp(dic_Hps, map_Hps, file_in_hp, Hp, map_Hosts)
    beanInit.init_Windows(dic_Windows, map_Windows, file_in_win, Windows, map_Hosts)
    beanInit.init_Group(dic_Groups, map_Groups, file_in_group, Group)
    beanInit.init_Url(dic_Urls, file_in_url, Url)
    beanInit.init_Oracle(dic_Oracles, file_in_oracle, Oracle)
    beanInit.init_Oracle_Tbs(dic_Oracle_Tbss, file_in_oracle_tbs, Oracle_Tbs)
    beanInit.init_Log(dic_Logs, file_in_log, Log)
    beanInit.init_Tcp(dic_Tcps, file_in_tcp, Tcp)
    beanInit.init_ServiceGroup(dic_servicegroup, file_in_servicegroup, ServiceGroup)
    beanInit.init_Contact(dic_contacts, file_in_contact, Contact)
    beanInit.init_ContactGroup(dic_contactgroups, file_in_contactgroup, ContactGroup)
    beanInit.init_ServiceesCalation(dic_serviceescalation, file_in_serviceescalation, ServiceesCalation)
    beanInit.init_Oracle_GoldenGate(dic_oracle_goldengate, file_in_oracle_goldengate, Oracle_GoldenGate)
    beanInit.init_Mail(dic_mail, file_in_mail, Mail)
    beanInit.init_WeblogicConsole(dic_weblogicconsole, file_in_weblogicconsole, WeblogicConsole)

    logger.info('Begin OutInit')
    outCfg = OutCfg(dir_templates, map_Hosts, map_Linuxs, map_Hps, map_Windows)
    outCfg.out_Cfg_group(dic_Groups, file_tpl_group, Group, file_cfg_group)
    outCfg.out_Cfg_Linux(dic_Linuxs, Linux, dir_out_cfg_linux, dic_fullfilename_cfg)
    outCfg.out_Cfg_Hp(dic_Hps, Hp, dir_out_cfg_hp, dic_fullfilename_cfg)
    outCfg.out_Cfg_Windows(dic_Windows, Windows, dir_out_cfg_win, dic_fullfilename_cfg)
    outCfg.out_cfg_Disk(dic_Disks, Disk, dic_fullfilename_cfg)
    outCfg.out_cfg_Url(dic_Urls, Url, dic_fullfilename_cfg)
    outCfg.out_cfg_Log(dic_Logs, Log, dic_fullfilename_cfg)
    outCfg.out_cfg_Oracle(dic_Oracles, Oracle, dic_fullfilename_cfg)
    outCfg.out_cfg_Oracle_Tbs(dic_Oracle_Tbss, Oracle_Tbs, dic_fullfilename_cfg)
    outCfg.out_cfg_Tcp(dic_Tcps, Tcp, dic_fullfilename_cfg)
    outCfg.out_cfg_ServiceGroup(dic_servicegroup, ServiceGroup, file_cfg_servicegroup)
    outCfg.out_cfg_Contact(dic_contacts, Contact, file_cfg_contact)
    outCfg.out_cfg_ContactGroup(dic_contactgroups, ContactGroup, file_cfg_contactgroup)
    outCfg.out_Cfg_ServiceesCalation(dic_serviceescalation, ServiceesCalation, dir_out_cfg_contact,
                                     dic_fullfilename_contact_cfg)
    outCfg.out_cfg_Oracle_GoldenGate(dic_oracle_goldengate, Oracle_GoldenGate, dic_fullfilename_cfg)
    outCfg.out_cfg_Mail(dic_mail, Mail, dic_fullfilename_cfg)
    outCfg.out_cfg_WeblogicConsole(dic_weblogicconsole, WeblogicConsole, dic_fullfilename_cfg)

    logger.info('Begin OutTxt')
    outTxt = OutTxt(map_Hosts, map_Linuxs, map_Hps, map_Windows)
    outTxt.out_Txt_Host_(dic_Linuxs, Linux, file_out_hosts_linux)
    outTxt.out_Txt_Host_(dic_Hps, Hp, file_out_hosts_hp)
    outTxt.out_Txt_Host_(dic_Windows, Windows, file_out_hosts_win)
    outTxt.out_Txt_Url(dic_Urls, Url, file_out_urls)
    outTxt.out_Txt_Disk(dic_Disks, Disk, file_out_disks)
    outTxt.out_Txt_Oracle(dic_Oracles, Oracle, file_out_oracles)
    outTxt.out_Txt_Oracle_Tbs(dic_Oracle_Tbss, Oracle_Tbs, file_out_oracle_tbss)
    outTxt.out_Txt_Log(dic_Logs, Log, file_out_chklog)
    outTxt.out_Txt_Tcp(dic_Tcps, Tcp, file_out_tcp)
    outTxt.out_Txt_Oracle_GoldenGate(dic_oracle_goldengate, Oracle_GoldenGate, file_out_goldengate)
    sys.exit(0)
