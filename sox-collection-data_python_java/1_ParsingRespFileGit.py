#!/usr/bin/python
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

def sqlupdate(addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name):
    concur.execute('INSERT INTO tab_main_resp_server(addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name) VALUES  ( ?, ?, ?, ?, ?, ?, ?, ?, ? )', (addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name,));
    conn.commit();

def sqlselect(server_name):
    concur.execute("""SELECT * FROM tab_main_resp_server WHERE server_name =?""",(server_name,))
    # Fetches all entries from table 
    var_srv = concur.fetchall()
      
    if var_srv is 'None':
	var_srv = '-------------------------------------|| This server ' + server_name + ' will add into list || ------------------------------------------------'
    else:
	var_srv
    
    return var_srv


#with open("listacct.txt", "rb") as lfr:
def get_info():
    count = 0    
    files_in_dir = os.listdir(_pwd_)
    
    print _pwd_
    
    with open(_pwd_ + "/" + "responsibility-list.txt", "rb") as fp:
	for lines in fp:  
	    count = count +1 
	    server_name = lines.split(":")[0]; print 'This server is in file ' + _pwd_ + "/" +'responsibility-list.txt' ,server_name
	    first_resp_person = lines.split(":")[1]; #print first_resp_person
	    second_resp_person = lines.split(":")[2]; #print second_resp_person
	    customer = lines.split(":")[3]; #print customer
	    system_name = lines.split(":")[4]; #print system_name
	    project_name = lines.split(":")[5]; #print project_name
	    operation_system = lines.split(":")[6]; #print operation_system
	    platform_name = lines.split(":")[7]; #print platform_name
	    addit_info = ""
	    res_check_indb = (sqlselect(server_name))
	    if len(res_check_indb) ==0:
		sqlupdate(addit_info, customer, first_resp_person, operation_system, platform_name, project_name, second_resp_person, server_name, system_name)
		
get_info()
