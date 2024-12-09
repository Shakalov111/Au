import time
import os
import random
import getpass
import pygetwindow as gw




questions = {"Питання 1":'1',"Питання 2":'2',"Питання 3":'3',"Питання 4":'4',"Питання 5":'5',"Питання 6":'6'}
N = 1

#Запис в файл активності користувача
def track_active_window(flag:bool):

    window = gw.getActiveWindowTitle()
    windows = window.split("-")

    with open('users_action.data',"a") as file:
                file.write('Дії користувача:\n\t')
                
                if flag:
                     file.write("Введено невірний пароль\n\t"+ time.strftime("%Y,%m,%d,%H:%M,%S",time.localtime()))
    
    
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
        answers = []
        for i in range(2):
            question = list(questions.keys())[random.randint(0,5)]
            answer = getpass.getpass(question)
            answers.append(answer == questions[question])
        #Перевірка відповіді
        if answers[0] and answers[1]:
            print("Вірно")
            track_active_window(False)
        else:
            os.system("shutdown /l")
            track_active_window(True)
        time.sleep(N*60)

if __name__ == "__main__":

    main()
    
