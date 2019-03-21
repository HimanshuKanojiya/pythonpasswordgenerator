"""
This program is to create the password according to the users need.

Program Name: Password Generator
Version: 1.1
Created By Himanshu Kanojiya
Email Address: himanshukanojiya825@gmail.com

Features of this program:
1. As you know the name, it can create the password in three ways.
    (A)Easy password, (B)Medium password, (C)Hard password generator.
2. Inbuilt Password Manager for saving your password (For future use).
3. No need to use internet connection (completely offline).

"""

import password_generator_settings as pgs
import random

logs_data = {"easy_password":"NU", "medium_password":"NU",
             "hard_password":"NU"}

program_phase = {"Phase 1 Working": "Not Working, have some issues",
                 "Phase 3 Working": "Not Working, have some issues" }


def logs_setup():
    pgs.logs_generate(logs_data, 1)
    pgs.logs_generate(program_phase, 2)

def menu_settings():
    print("\n")
    print("\nYou are currently viewing the default setting of Password Generator:")
    print("Default Password Length is: " + str(pgs.default_values("password_length")))
    print("Logs Creator : " + str(pgs.default_values("logs_generate")))
    print("Saved My Passwords in Excel : " + str(pgs.default_values("password_save_in_excel")))
        

class password_generator():
    def __init__(self, password_length):
        self.password_length = password_length
        program_phase["Phase 3 Working"] = "Yes"

    def easy_password(easy_conf):

        #program Phase 3
        
        password_gen = ""
        method_use_0 = pgs.lowercase_alpha
        method_use_1 = pgs.number_inclusion

        method_1 = len(method_use_0)
        method_2 = len(method_use_1)
        
        while len(password_gen) <= easy_conf.password_length:

            if len(password_gen) <= easy_conf.password_length:
                selection = random.randrange(method_1)
                sender = method_use_0[selection]
                password_gen = password_gen + str(sender)

                if len(password_gen) <= easy_conf.password_length:
                    selection = random.randrange(method_2)
                    sender = method_use_1[selection]
                    password_gen = password_gen + str(sender)
                    
            else:
                break

        Your_Pass = str(password_gen[0:len(password_gen) - 1])
        print("Your Password is: " + Your_Pass)
        pgs.password_saver(str(Your_Pass))   
            

    def medium_password(medium_conf):

        #program phase 3

        password_gen = ""
        method_use_0 = pgs.lowercase_alpha
        method_use_1 = pgs.uppercase_alpha
        method_use_2 = pgs.number_inclusion

        method_1 = len(method_use_0)
        method_2 = len(method_use_1)
        method_3 = len(method_use_2)
        
        while len(password_gen) <= medium_conf.password_length:

            if len(password_gen) <= medium_conf.password_length:
                selection = random.randrange(method_1)
                sender = method_use_0[selection]
                password_gen = password_gen + str(sender)
                if len(password_gen) <= medium_conf.password_length:
                    selection = random.randrange(method_2)
                    sender = method_use_1[selection]
                    password_gen = password_gen + str(sender)
                    if len(password_gen) <= medium_conf.password_length:
                        selection = random.randrange(method_3)
                        sender = method_use_2[selection]
                        password_gen = password_gen + str(sender)
            else:
                break

        Your_Pass = str(password_gen[0:len(password_gen) - 1])
        print("Your Password is: " + Your_Pass)
        pgs.password_saver(str(Your_Pass))
        
    def hard_password(hard_conf):

        #program phase 3
        
        password_gen = ""
        method_use_0 = pgs.lowercase_alpha
        method_use_1 = pgs.uppercase_alpha
        method_use_2 = pgs.number_inclusion
        method_use_3 = pgs.special_characters

        method_1 = len(method_use_0)
        method_2 = len(method_use_1)
        method_3 = len(method_use_2)
        method_4 = len(method_use_3)
        
        while len(password_gen) <= hard_conf.password_length:

            if len(password_gen) <= hard_conf.password_length:
                selection = random.randrange(method_1)
                sender = method_use_0[selection]
                password_gen = password_gen + str(sender)
                if len(password_gen) <= hard_conf.password_length:
                    selection = random.randrange(method_2)
                    sender = method_use_1[selection]
                    password_gen = password_gen + str(sender)
                    if len(password_gen) <= hard_conf.password_length:
                        selection = random.randrange(method_3)
                        sender = method_use_2[selection]
                        password_gen = password_gen + str(sender)
                        if len(password_gen) <= hard_conf.password_length:
                            selection = random.randrange(method_4)
                            sender = method_use_3[selection]
                            password_gen = password_gen + str(sender)
                            
            else:
                break

        Your_Pass = str(password_gen[0:len(password_gen) - 1])
        print("Your Password is: " + Your_Pass)
        pgs.password_saver(str(Your_Pass))
        

def program_launcher():

    #Pogram Phase 1
    
    runner = [5]
    choice_Menu = True

    welcome = "Welcome to Password Generator V1.0. This program can create a strong password according to your settings and requirements. Every password, you get through our program will be saved in CSV file by default. \n"
    print welcome
    print("Passsword Generator Menu:")
    menu_options = "1. Easy Password \n2. Medium Password \n3. Hard Password \n4. Password Generator Settings"
    print menu_options
    program_phase["Phase 1 Working"] = "Yes"
    while choice_Menu == True and runner[0] != 0:
        try:
            choice = int(raw_input("Enter Your Choice (1/2/3/4) > "))
            if choice == 1:
                print("You have choosen Easy Password Option")

                password_len = pgs.default_values("password_length")
                sender = password_generator(password_len)
                sender.easy_password()
                logs_data['easy_password'] = "Used"

                reuse = str(raw_input("Wanna Use it Again (Y/N) > "))

                if reuse.lower() == 'y':
                    print("\n")
                    continue

                elif reuse.lower() == "n":
                    break
                
            elif choice == 2:
                print("You have choosen Medium Password Option")

                password_length = pgs.default_values("password_length")
                sender = password_generator(password_length)
                sender.medium_password()
                logs_data['medium_password'] = "Used"
                
                reuse = str(raw_input("Wanna Use it Again (Y/N) > "))

                if reuse.lower() == 'y':
                    print("\n")
                    continue

                elif reuse.lower() == "n":
                    break
                
            elif choice == 3:
                print("You have choosen Hard Password Option")

                password_length = pgs.default_values("password_length")
                sender = password_generator(password_length)
                sender.hard_password()
                logs_data['hard_password'] = "Used"
                
                reuse = str(raw_input("Wanna Use it Again (Y/N) > "))

                if reuse.lower() == 'y':
                    print("\n")
                    continue

                elif reuse.lower() == "n":
                    break
                
            elif choice == 4:
                print("You have choosen Password Generator Setting")
                menu_settings()
                
                reuse = str(raw_input("Wanna Use it Again (Y/N) > "))
                if reuse.lower() == 'y':
                    print("\n")
                    continue

                elif reuse.lower() == "n":
                    break
                
                
            elif choice > 4:
                current = runner[0]
                current = current - 1
                print("Wrong Value Entered, " + str(current) + " chances left!")
                runner[0] = current
            
        except:
            print("Invalid Input, Try Again")
            current = runner[0]
            current = current - 1
            print("You have, " + str(current) + " chances left!")
            runner[0] = current
            print("\n")
    

try:
    program_launcher()
    logs_setup()
except:
    logs_setup()
