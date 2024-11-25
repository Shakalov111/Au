import time
import os
import random
import getpass
import pygetwindow as gw



password = "0"
question = "Сколько:"

def util():
    window = gw.getActiveWindowTitle()
    windows = window.split("-")
    with open('users_action.data',"w") as file:
                file.write('Дії користувача:')
    for i in windows:
        massage = f'''
        {i}
        {time.strftime("%Y,%m,%d,%H:%M,%S",time.localtime())}
        '''
        try:
            with open('users_action.data',"a") as file:
                file.write(massage)
        except:
            print("Error")

def main ():
    while True:
        window = gw.getActiveWindowTitle()
        util()
        answer = getpass.getpass(question)
        if answer == password:
            print("Вірно")
        else:
            #os.system("shutdown /l")
            print('os.system("shutdown /l /t 10")')

if __name__ == "__main__":

    main()
    