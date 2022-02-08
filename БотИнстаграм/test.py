from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_name import username, password
from selenium.webdriver.chrome.service import Service
import time
import random


def show_message():
    messagebox.showinfo("переводчик", message.get())


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()

def login(username, password):
    try:
        service = Service(executable_path='chromedriver.exe')
        browser = webdriver.Chrome(service=service)
        browser.get('https://www.deepl.com/ru/translator')
        time.sleep(random.randrange(3, 5))

        input_text = browser.find_element(By.XPATH, '/html/body/div[3]/main/div[3]/div[3]/section[1]/div[2]/div[2]/textarea')
        input_text.clear()
        input_text.send_keys(message)
        time.sleep(random.randrange(3, 5))

        msg_translate = browser.find_element(By.XPATH, '/html/body/div[3]/main/div[3]/div[3]/section[2]/div[3]/div[1]/div[1]').text
        browser.close()
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

