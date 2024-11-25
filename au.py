import time
import os
import random
import getpass
import pygetwindow as gw
import sqlite3


password = "0"
question = "Сколько:"

def createdb():
    conn = sqlite3.connect("question.db")
    cursor = conn.cursor()
    create_table = '''
    CREATE TABLE IF NOT EXISTS user_action(
    id INTEGER PRYMARY KEY,
    name TEXT NOT NULL,
    time TEXT)
    '''
    conn.execute(create_table)
    conn.commit()
    conn.close()

def insert(str):
    time0 = time.strftime("%Y,%m,%d,%H:%M,%S",time.localtime())
    add_new_action = f'''
    INSERT INTO user_action(name,time) VALUES ({str},{time0})
    '''
def select():
    conn = sqlite3.connect("question.db")
    cursor = conn.cursor()
    select_query = 'Select * FROM user_action'
    cursor.execute(select_query)
    data = cursor.fetchall()
    print(data)
def main ():
    while True:
        window = gw.getActiveWindowTitle()

        answer = getpass.getpass(question)
        if answer == password:
            print("Вірно")
        else:
            #os.system("shutdown /l")
            print('os.system("shutdown /l")')

if __name__ == "__main__":
    createdb()
    insert(gw.getActiveWindowTitle())
    select()
    main()