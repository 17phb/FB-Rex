#!/usr/local/bin/python

from __future__ import print_function

from colorama import init, Fore, Back, Style

import webbrowser as wb

hd = 'n'
while hd=='n':
    print(Fore.WHITE + '''
#######################################################
#    
#  d88888b d8888b.        d8888b. d88888b db    db 
#  88'     88  `8D        88  `8D 88'     `8b  d8' 
#  88ooo   88oooY'        88oobY' 88ooooo  `8bd8'  
#  88~~~   88~~~b. C8888D 88`8b   88~~~~~  .dPYb.  
#  88      88   8D        88 `88. 88.     .8P  Y8. 
#  YP      Y8888P'        88   YD Y88888P YP    YP 
#
#              coded by T-Rex
#     
#          www.facebook.com/17phb
#
#          www.github.com/T-Rex17
#
#######################################################
\n''')
    print(Fore.YELLOW + "1)" + Fore.RESET + "Privacy Rights - Request to remove an photo")
    print(Fore.YELLOW + "2)" + Fore.RESET + "Account Removal Request for a Medically Incapacitated Person")
    print(Fore.YELLOW + "3)" + Fore.RESET + "Report Something on Facebook")
    print(Fore.YELLOW + "4)" + Fore.RESET + "Special request for the deceased person")
    print(Fore.YELLOW + "5)" + Fore.RESET + "Report an Impostor Account")
    print(Fore.YELLOW + "6)" + Fore.RESET + "remove my account")
    print(Fore.YELLOW + "7)" + Fore.RESET + "unblock request")
    print(Fore.YELLOW + "8)" + Fore.RESET + "Send your ID card")
    print(Fore.YELLOW + "9)" + Fore.RESET + "Reporting a Violation or Infringement of Your Rights\n")
    a =input("enter Your choice number:")
    if a == 1:
        wb.open_new_tab('https://www.facebook.com/help/contact/144059062408922')
    elif a == 2:
       wb.open_new_tab('https://www.facebook.com/help/contact/191122007680088')
    elif a == 2:
        wb.open_new_tab('https://www.facebook.com/help/contact/191122007680088')
    elif a == 4:
        wb.open_new_tab('https://www.facebook.com/help/contact/?id=228813257197480')
    elif a == 5:
        wb.open_new_tab('https://www.facebook.com/help/contact/169486816475808')
    elif a == 6:
        wb.open_new_tab('https://www.facebook.com/help/delete_account')
    elif a == 7:
        wb.open_new_tab('https://www.facebook.com/help/contact/571927962827151')
    elif a == 8:
        wb.open_new_tab('https://www.facebook.com/help/contact/183000765122339')
    elif a == 9:
        wb.open_new_tab('https://www.facebook.com/help/contact/634636770043106')
    hd = raw_input ("exit or not:[y-n]")
