import time
import os
import random
import getpass
import pygetwindow as gw




questions = {"Питання 1":'1',"Питання 2":'2',"Питання 3":'3',"Питання 4":'4',"Питання 5":'5',"Питання 6":'6'}
N = 1
def track_active_window():
    window = gw.getActiveWindowTitle()
    windows = window.split("-")
    with open('users_action.data',"a") as file:
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

def t():
       try:
            with open('users_action.data',"a") as file:
                file.write("Введено невірний пароль\n\t"+ time.strftime("%Y,%m,%d,%H:%M,%S",time.localtime()))
       except:
            print("Error")
def main ():
    while True:
        track_active_window()
        question = list(questions.keys())[random.randint(0,5)]
        answer = getpass.getpass(question)
        if answer == questions[question]:
            print("Вірно")
        else:
            #os.system("shutdown /l")
            print('os.system("shutdown /l /t 10")')
            t()

        time.sleep(N*60)

if __name__ == "__main__":

    main()
    