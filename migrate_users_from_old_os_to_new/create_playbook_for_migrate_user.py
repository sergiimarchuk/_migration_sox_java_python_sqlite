#!/usr/bin/python
import os.path
import subprocess
import crypt
import glob
import os
import ast
from collections import Counter
import datetime
import sqlite3
import glob
import os
import ast

#variables
checklog_file_ = "local_report"
file_log_name = "migr_users.yml"
dict_user = {}
list_groups = []
#function for befin yml file
def BeginFile():
        with open (file_log_name, 'a') as f: f.write ("---" + '\n')
        with open (file_log_name, 'a') as f: f.write ("- hosts: all" + '\n')
        with open (file_log_name, 'a') as f: f.write ("  remote_user: e220314" + '\n')
        with open (file_log_name, 'a') as f: f.write ("  sudo: yes" + '\n')
        with open (file_log_name, 'a') as f: f.write ("  tasks:" + '\n')

def extract_data():
  with open(checklog_file_, "rb") as fp:
        for user_line in fp:
                #print type(ast.literal_eval(user_line))
                user_name = (ast.literal_eval(user_line)).get("user_name"); #print 'AAAAAAAAAAAAA',user_name
                gecos = (ast.literal_eval(user_line)).get("gecos"); #print "gecos is ",gecos #gecos
                supl_groups = (ast.literal_eval(user_line)).get("groups")[0:-2]; print 'AAAAAAAAAAAAAAAA',supl_groups  #print supl_groups #supl. groups
                shell_var = (ast.literal_eval(user_line)).get("shell"); print 'FFFFFFFFFFFFFFFFFFFF',shell_var,len(shell_var)

                if "cfeusr" in supl_groups or "games" in supl_groups or "root" in supl_groups or "daemon" in supl_groups or "sys" in supl_groups or "adm" in supl_groups or "disk" in supl_groups or "wheel" in supl_groups or "lp" in supl_groups or "sync " in supl_groups or "shutdown " in supl_groups or "halt " in supl_groups or "mail" in supl_groups or "news" in supl_groups or "uucp" in supl_groups or "operator " in supl_groups or "users" in supl_groups or "games " in supl_groups or "gopher" in supl_groups or "ftp" in supl_groups or "nobody" in supl_groups or "nscd" in supl_groups or "vcsa" in supl_groups or "pcap" in supl_groups or "rpc" in supl_groups or "mailnull" in supl_groups or "smmsp" in supl_groups or "ntp" in supl_groups or "dbus" in supl_groups or "avahi" in supl_groups or "sshd" in supl_groups or "rpcuser" in supl_groups or "nfsnobody" in supl_groups or "haldaemon" in supl_groups or "avahi-autoipd" in supl_groups or "xfs" in supl_groups or "audio" in supl_groups or "gdm" in supl_groups :
                        print 'BBBBBBBBBBBBBBB',user_name,supl_groups
                else:
                        print "CCCCCCCCCCCCCCCCCCCC"
                        home_dir = (ast.literal_eval(user_line)).get("home_directory"); #print 'AAAAAAAAAAA',home_dir # home directory
                        shadow = (ast.literal_eval(user_line)).get("shadow")
                        dict_user.update({'user_name': user_name,'groups':supl_groups,'home_directory': home_dir,'shadow':shadow})
                        print dict_user

                        UserName = ("      " + "- user: name=" + "'" + user_name + "'")
                        Comment = var_comment = (" comment=" + "'" + gecos   + "'")
                        #HomeUser = (" comment=" + "'" + home_dir   + "'")
                        var_HomeUser = " home=" + "'" + home_dir  + "'"
                        Shell = '/bin/bash'
                        var_Shell = " shell=" + "'" + shell_var + "'"
                        var_password =" password=" + "'" + shadow + "'"
                        var_groups = " groups=" + "'" + supl_groups + "'"
                        with open (file_log_name, 'a') as f: f.write (UserName  + Comment + var_HomeUser  + var_Shell + var_password + '\n')
                        print "var_groups",type(var_groups),var_groups
                        if  dict_user.get('groups') != '':
                                print "groups ",dict_user.get('groups')
                                with open (file_log_name, 'a') as f: f.write (UserName  + Comment + var_HomeUser  + var_Shell + var_groups+ '\n')
                        else:
                                print ""
                                with open (file_log_name, 'a') as f: f.write (UserName  + Comment + var_HomeUser  + var_Shell + '\n')


def CheckerYmlFile():
        if os.path.isfile(file_log_name) == False:
                BeginFile()
                extract_data()
        else:
                extract_data()
CheckerYmlFile()

def checklog_file():
        with open (checklog_file_, 'a') as f: f.write (str(dict_user) + '\n')

#checklog_file()
