#!/home/sox-sqlite/python27/bin/python
import socket
import subprocess
import os
#import datetime
from datetime import datetime
datetime_var = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]  #+ "-" + datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1]
time_var = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1]; print (time_var+"t"+time_var)
hostname_var = socket.gethostname()

checklog_file_ = "local_report" #"local_report_" + hostname_var  + "_checklogdic.log-" + "-" + datetime_var + "t" + time_var

dict_user_var = {}

new_dict = {}
group_list = []

cwd = os.getcwd()

def log_rm():
  if os.path.isfile(cwd + '/' + checklog_file_) == True:
    os.remove(cwd + '/' + checklog_file_)

log_rm()

def checklog_file(arguments):
#  with open (checklog_file_, 'a') as f: f.write (str(dict_user_var) + '\n')
        with open (checklog_file_, 'a') as f: f.write (arguments + '\n')

def run_bin_get_lastlog(arg1,arg2,arg3):
        args = (arg1, arg2, arg3)
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        #print output.split(" ")[-6:-1]
        #print output working for test
        return output.split(" ")[-6:]

def run_comm_get_shadow(arg1,arg2,arg3):
        args = (arg1,arg2,arg3)
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        print output
        return output

#Run command id for each of users on server. collect user name and groups into dictionary. users we got from passwd and doing pars for each of lines.
def extract_groups():
  with open("/etc/passwd", "rb") as fp:
        for user_line in fp:
          run_cmd_id = subprocess.Popen(['id', user_line.split(":")[0]], stdout=subprocess.PIPE)
          output_cmd_id = run_cmd_id.communicate()[0]
          #get user name uid
          uname_var=output_cmd_id.split(" ")[0].split("(")[1].replace(")","")
          #get supplementary groups fro user
          groups_var = output_cmd_id.split(" ")[2].split("=")[1]
          #get home directory for user
          home_dir_var = user_line.split(":")[5]
          #shell
          shell_var =  (user_line.split(":")[6]).rstrip('\r\n')

          #add user's info into dictionary
          dict_user_var.update({'user_name': uname_var,'groups':groups_var,'home_directory': home_dir_var,'shell_var':shell_var})
          #get gecos/comment about user
          if len(user_line.split(":")[4]) < 3:
            #add info about gecos/comment into dictionary for user in this case it is empty
            dict_user_var.update({'gecos': 'GECOS IS EMPTY'})
            gecos_var = "GECOS is empty"
          else:
            #add info about gecos/comment into dictionary for user
            dict_user_var.update({'gecos': user_line.split(":")[4]})
            gecos_var = user_line.split(":")[4]
          #checklog_file() #was comments refactoring #1
          #collected info about user into lines in dictionary from file passwd ... these info added into lof file as well
          dict_collected_users = dict_user_var
          #print working for test
          #extract user name
          uname_var = dict_collected_users.get("user_name"); #print "uname is:",uname_var #1

          #extact groups
          new_list = []
          grps_var = dict_collected_users.get("groups").split(",")
          for el_gr in grps_var:
            groups_var =  el_gr.split("(")[1].replace(")","")
            new_list.append([groups_var])
          #print "groups is:",str(new_list).replace("[","").replace("]","").replace("'","").replace("\n","") #2

          #extract shell
          e_shell_var = dict_collected_users.get("shell_var")

          #extract gecos, comments
          gecos_var = dict_collected_users.get("gecos"); #print "gecos:",gecos_var #3
          #print gecos_var,

          #extract home directory
          home_dir_var =  dict_collected_users.get("home_directory"); #print "home_directory is:",home_dir_var #4i
          #lastlog info
          ##dict_user_var.update({'lastlog': run_bin_get_lastlog("lastlog","-u",uname_var)})
          last_log_user_var = run_bin_get_lastlog("lastlog","-u",uname_var);
          #print uname_var,"a",last_log_user_var
          if "Never" in str(last_log_user_var):
            last_log_user_var='Never logged in'
            #print last_log_user_var
          else:
            try:
                if last_log_user_var[1] != '':
                        log_var_month=last_log_user_var[1]; log_var_day_month=last_log_user_var[2]; #print log_var_day_month;
                        log_var_year=last_log_user_var[5];# print log_var_year
                        last_log_user_var=log_var_day_month+"/"+log_var_month+"/"+log_var_year
                        #print last_log_user_var,
                else:
                        log_var_month=last_log_user_var[0]; log_var_day_month=last_log_user_var[2]; #print log_var_day_month;
                        log_var_year=last_log_user_var[5]; #print log_var_year
                        last_log_user_var=log_var_day_month+"/"+log_var_month+"/"+log_var_year
                        #print last_log_user_var,
            except IndexError:
                last_log_user_var='Never logged in'
          # get shadow #grep username /etc/shadow |  awk -F':' '{print $2}'
          var_user_shadow = run_comm_get_shadow("grep",uname_var,"/etc/shadow").split(":")[1]
          supl_groups = str(new_list).replace("[","").replace("]","").replace("'","").replace("\n","")
          ##print gecos_var
          if "CompanyName" not in gecos_var:
            try:
             #print uname_var,gecos_var
             new_dict.update({'user_name': uname_var,'groups':supl_groups,'home_directory': home_dir_var,'gecos':str(gecos_var),'lastlog': last_log_user_var,'datetime_var': datetime_var,'time_var': time_var,'shadow': var_user_shadow,'shell':e_shell_var})
             checklog_file(str(new_dict))
            except IndexError:
              print "UPS"

extract_groups()

def prep_to_excel():
  with open((cwd + '/' + checklog_file_), "rb") as fc:
    for dic_line in fc:
      print dic_line,

#prep_to_excel()
print os.path.isfile(cwd + '/' + checklog_file_)
