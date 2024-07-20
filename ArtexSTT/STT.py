from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from mtranslate import translate
from pathlib import Path

class Listener:

    def __init__(self, write_text_file_path, translate=True):
        self.__output_file_path = write_text_file_path
        self.__translate = translate
        self.__fine = True
        if not self.__check_arguments():
            self.__fine = False
        self.__chrome_options = Options()
        self.__user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
        self.__chrome_options.add_argument(f'user-agent={self.__user_agent}')
        self.__chrome_options.add_argument("--use-fake-ui-for-media-stream")
        self.__chrome_options.add_argument("--use-fake-device-for-media-stream")
        self.__chrome_options.add_argument("--headless=new")
        self.__service = Service(ChromeDriverManager().install())
        self.__driver = webdriver.Chrome(service=self.__service, options=self.__chrome_options)
        self.__work = True

    def __check_arguments(self):
        if not isinstance(self.__translate, bool):
            raise TypeError("Parameter translate must be boolean")
            return False
        if not isinstance(self.__output_file_path, str):
            raise TypeError("Parameter write_text_file_path must be string")
            return False
        if not self.__output_file_path:
            raise ValueError("Please provide the input_file_path")
            return False
        return True

    def __translate_to(self, text):
        return translate(text, "en-us")

    def StopRecognition(self):
        self.__work = False
        self.__driver.quit()

    def __writter(self, data):
        with open(self.__output_file_path, 'w') as f:
            f.write(data)

    def listen(self):
        if not self.__fine:
            return
        self.__driver.get(str(Path(__file__).resolve().parent / 'STT.html'))
        self.__driver.find_element(by=By.ID, value="start").click()
        while self.__work:
            try:
                Text = self.__driver.find_element(by=By.ID, value="output").text
                if Text:
                    self.__driver.find_element(by=By.ID, value="end").click()
                    Text = self.__translate_to(Text) if self.__translate else Text
                    self.__writter(Text)
                    sleep(0.333)
                    self.__driver.find_element(by=By.ID, value="start").click()
                else:
                    sleep(0.333)
            except Exception as e:
                self.__work = False
                return
        self.StopRecognition()


import threading
import os

ai = Listener(os.getcwd() + "/inp.txt")

th = threading.Thread(target=ai.listen)
th.start()

import time

time.sleep(15)
ai.StopRecognition()
th.join()