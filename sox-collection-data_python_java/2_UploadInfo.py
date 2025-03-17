#!/usr/bin/python
#this script does parsing files with name local_report* and put data into db. data about users, from file /etc/passwd and lastlog ..
from collections import Counter
import datetime
import sqlite3
import glob
import os
import ast

#Current directory path
_pwd_ = os.getcwd()
a = glob.glob("*")

conn = sqlite3.connect(os.getcwd()+'/collect-db.db')
conn.text_factory = str
concur = conn.cursor()
def sql_get_id_server(server_name):
    concur.execute("""SELECT "id_server" FROM "tab_main_resp_server" WHERE "server_name" = ?""",(server_name,))
    
    #concur.execute("""SELECT * FROM tab_main_resp_server WHERE server_name =?""",(server_name,))
    # Fetches all entries from table 
    row = concur.fetchall()
    return row

def sqlupdate(id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name, date_entry, time_entry):
    #concur.execute('INSERT INTO tab_main_resp_server(addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name) VALUES  ( ?, ?, ?, ?, ?, ?, ?, ?, ? )', (addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name,));
    
    concur.execute('INSERT INTO tab_collect_statistic(id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name, date_entry, time_entry) \
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )', (id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name,date_entry,time_entry))   
    conn.commit();

def get_info():
    files_in_dir = os.listdir(_pwd_)
    for files in files_in_dir:
        if "local_report" in files:    
            print files
            try:
                server_name = files.split("local_report_")[1]; print server_name #server_name
            except IndexError:
                server_name = "local"; print server_name #server_name 
            with open(files, "rb") as fp:
                for lines in fp:
                    print type(ast.literal_eval(lines))
                    user_name = (ast.literal_eval(lines)).get("user_name"); #user name
                    gecos = (ast.literal_eval(lines)).get("gecos"); #print "gecos is ",gecos #gecos
                    supl_groups = (ast.literal_eval(lines)).get("groups"); #print supl_groups #supl. groups
                    home_dir = (ast.literal_eval(lines)).get("home_directory"); # home directory
                    lastlog_user = (ast.literal_eval(lines)).get("lastlog"); #print "-----------------------------------",type(str(lastlog_user))
                    date_file = (ast.literal_eval(lines)).get("datetime_var"); #print date_file
                    time_entry = (ast.literal_eval(lines)).get("time_var"); print time_entry
                    if len((server_name)) > 0:
                        sqlupdate(server_name, gecos, home_dir, str(lastlog_user), supl_groups, user_name, server_name, date_file, time_entry)
                    
get_info()
