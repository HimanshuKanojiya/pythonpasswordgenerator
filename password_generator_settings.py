"""

This file is the core of every single function.
Without this file, the whole program is like garbage.
This file is only responsible for every function which you will use.

Program Name: Password Generator
Version: 1.0
Created By Himanshu Kanojiya
Email Address: himanshukanojiya825@gmail.com


"""
import csv
import datetime
import pandas
import os
import sys

csv_created = [0]

program_phase_setting = {"Phase 2 Working":"Not Working, have some issues",
                         "Phase 4 Working":"Not Working, have some issues",
                         "Phase 5 Working":"Not Working, have some issues",
                         "Phase 6 Working":"Not Working, have some issues",
                         "Phase 7 Working":"Not Working, have some issues"}

lowercase_alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_inclusion = [0,1,2,3,4,5,6,7,8,9]
special_characters = ['!','@','#','$','%','^','&','*','(',')','-','+','_','=',';',':',',','<','.','>','/','?','"',"'",'[','{',']','}',"\ ","|"]

class csv_inder:

    #program phase 6

    program_phase_setting["Phase 6 Working"] = "Yes"
    
    def __init__(self, filename):
        self.filename = filename

    def row_take_out(row_conf):
        data_is = pandas.read_csv(row_conf.filename)
        return len(data_is.index) + 1

    def pro_restart(pro_conf):
        default_name = pro_conf.filename
        files_list = os.listdir(".")
        if default_name in files_list:
            csv_created[0] = 1
        elif default_name not in files_list:
            csv_created[0] = 0
                
    

def default_values(Your_Choice):

    #Program Phase 2 & 4

    program_phase_setting["Phase 2 Working"] = "Yes"
    program_phase_setting["Phase 4 Working"] = "Yes"
    
    password_length = 50
    logs_generate = True
    password_save_in_excel = True
    special_characters = True
    lowercase_allowed = True
    uppercase_allowed = True
    alpha_numeric_allowed = True
    
    if Your_Choice == "password_length":
        return password_length
    
    elif Your_Choice == "logs_generate":
        return logs_generate

    elif Your_Choice == "password_save_in_excel":
        return password_save_in_excel

    elif Your_Choice == "special_characters":
        return special_characters
    
    elif Your_Choice == "lowercase_allowed":
        return lowercase_allowed

    elif Your_Choice == "uppercase_allowed":
        return uppercase_allowed

    elif Your_Choice == "alpha_numeric_allowed":
        return alpha_numeric_allowed


def password_saver(YourPasswordIs):

    #program phase 5

    program_phase_setting["Phase 5 Working"] = "Yes"
    
    field_names = ["Usage", "Creation Time", "Password Created"]
    i_can = default_values("password_save_in_excel")
    current_time = datetime.datetime.now()
    current_time = current_time.strftime("%c")

    access_start = csv_inder("Password Manager.csv")
    access_start.pro_restart()
    
    try:

        if i_can == True and csv_created[0] == 0:
            saver = open("Password Manager.csv", 'a')
            write_in = csv.DictWriter(saver, fieldnames=field_names)
            write_in.writeheader()
            write_in.writerow({'Usage':1, 'Creation Time':current_time, 'Password Created':str(YourPasswordIs)})       
            saver.close()
            csv_created[0] = 1

        elif i_can == True and csv_created[0] == 1:
            saver = open("Password Manager.csv", 'a')
            write_in = csv.DictWriter(saver, fieldnames=field_names)
            write_in.writerow({'Usage':str(access_start.row_take_out()), 'Creation Time':current_time, 'Password Created':str(YourPasswordIs)})
            saver.close()
        
        
        elif i_can == False:
            print("Not Accessed")
    except:
        print("Malfunction in password manager")

    

def logs_generate(datas, container_number):

    #program phase 7

    program_phase_setting["Phase 7 Working"] = "Yes"
    
    i_can = default_values("logs_generate")
    try:
        if i_can == True and container_number == 1:
            current_time = datetime.datetime.now()
            current_time = current_time.strftime("%c")
            logs_create = open("PasswordGenerator_logs.txt", "a")
            logs_create.write("\nThis is the Log File of Password Generator")
            logs_create.write("\nYour Platform is " + str(sys.platform))
            logs_create.write("\nTime, when script has used " + str(current_time))
            logs_create.write("\nMethod Used to Create Password: ")
            logs_create.write("\n 1.Easy Password: " + str(datas["easy_password"]))
            logs_create.write("\n 2.Medium Password: " + str(datas["medium_password"]))
            logs_create.write("\n 3.Hard Password: " + str(datas["hard_password"]))
            logs_create.close()
        elif i_can == True and container_number == 2:
            logs_create = open("PasswordGenerator_logs.txt", "a")
            logs_create.write("\nPassword Generator Phases Working Report: ")
            logs_create.write("\n 1.Phase 1 Working: " + str(datas["Phase 1 Working"]))
            logs_create.write("\n 2.Phase 2 Working: " + str(program_phase_setting["Phase 2 Working"]))
            logs_create.write("\n 3.Phase 3 Working: " + str(datas["Phase 3 Working"]))
            logs_create.write("\n 4.Phase 4 Working: " + str(program_phase_setting["Phase 4 Working"]))
            logs_create.write("\n 5.Phase 5 Working: " + str(program_phase_setting["Phase 5 Working"]))
            logs_create.write("\n 6.Phase 6 Working: " + str(program_phase_setting["Phase 6 Working"]))
            logs_create.write("\n 7.Phase 7 Working: " + str(program_phase_setting["Phase 7 Working"]) + "\n")
            logs_create.close()
            
        elif i_can == False:
            print("Logs Generator Will be off")
        elif i_can == None:
            print("Issues in Calling")
    except:
        print("Issues in Logs Generate Modules")

    
