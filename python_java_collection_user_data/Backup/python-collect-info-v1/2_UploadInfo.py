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

conn = sqlite3.connect(os.getcwd()+'/untitled.db')
conn.text_factory = str
concur = conn.cursor()
def sql_get_id_server(server_name):
    concur.execute("""SELECT "id_server" FROM "tab_main_resp_server" WHERE "server_name" = ?""",(server_name,))
    
    #concur.execute("""SELECT * FROM tab_main_resp_server WHERE server_name =?""",(server_name,))
    # Fetches all entries from table 
    row = concur.fetchall()
    return row



def sqlupdate(id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name, date_entry):
    #concur.execute('INSERT INTO tab_main_resp_server(addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name) VALUES  ( ?, ?, ?, ?, ?, ?, ?, ?, ? )', (addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name,));
    
    
    concur.execute('INSERT INTO tab_collect_statistic(id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name, date_entry) \
    VALUES ( ?, ?, ?, ?, ?, ?, ?, ? )', (id_server, gecos, home_dir, lastlog_user, supl_groups, user_name, server_name,date_entry,))   
    conn.commit();

def select():
    t = ('RHAT',)
#	concur.execute('SELECT * FROM tab_data')
#	print(concur.fetchone())
#	concur = conn.cursor()
    concur.execute("SELECT * FROM tab_collect_statistic")
    rows = concur.fetchall()
    for row in rows:
        print(row)

select()   

def get_info():
    files_in_dir = os.listdir(_pwd_)
    for files in files_in_dir:
        if "local_report" in files:    
            print files
            server_name = files.split("_")[2]; #print server_name #server_name
            #print sqlselect(server_name),server_name
            #print sql_get_id_server(server_name),server_name," ",type(sql_get_id_server(server_name)),len(sql_get_id_server(server_name))
            #getting id_server from main table tab_main_resp_server
            
            
            date_file = files.split("--")[1]; #print date_file #date_entry

            with open(files, "rb") as fp:
                for lines in fp:
                    #print ast.literal_eval(lines)
                    user_name = (ast.literal_eval(lines)).get("user_name"); #user name
                    gecos = (ast.literal_eval(lines)).get("gecos"); #print "gecos is ",gecos #gecos
                    supl_groups = (ast.literal_eval(lines)).get("groups"); #print supl_groups #supl. groups
                    home_dir = (ast.literal_eval(lines)).get("home_directory"); # home directory
                    lastlog_user = (ast.literal_eval(lines)).get("lastlog"); #print "-----------------------------------",type(str(lastlog_user))
                    #print "sercver_name -",server_name
                    #print "date entry -",date_file
                    #print "user_name -",user_name
                    #print "gecos -",gecos
                    #print "supl group -",supl_groups
                    #print "home dir -",home_dir
                    #print "lstlog -",str(lastlog_user)
                    
                    if len(sql_get_id_server(server_name)) > 0:
                        var_id_server = str(sql_get_id_server(server_name)[0]).replace(",","").replace("(","").replace(")","")
                        print var_id_server
                        #id_server_date_entry =var_id_server  + "_" + date_file;
                        sqlupdate(var_id_server, gecos, home_dir, str(lastlog_user), supl_groups, user_name, server_name, date_file)
                    else:
                        print " This server is not in responsibility list :"," ",server_name                    
                    
                    
                    #sqlupdate(date_entry, gecos, home_dir, id_server, lastlog_user, supl_groups, user_name)
                
                    
get_info()
