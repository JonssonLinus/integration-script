from flask import Flask, redirect, url_for, request
#Only log on to survey system

#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait

import pandas as pd
import os
import re

app = Flask(__name__)

@app.route('/process_url', methods=['GET'])
def process_url():
    # Get the URL parameter from the request
    email = request.args.get('email')
    print('E-mail address: '+ email)
    # Perform any necessary processing with the URL

    # Redirect the user's browser to a new URL
    return redirect(url_for('new_page'))

@app.route('/new_page')
def new_page():
    return "Thank you for completing the survey!"

@app.route('/create_patient')
def create_patient():
    options = ChromeOptions()
    options.add_argument("--headless=new") #Comment out this line to deactivate headless option
    driver=webdriver.Chrome(options)
    login_url='https://svara.enkatfabriken.com/b/index.php?r=admin/authentication/sa/login'

    driver.get(login_url)
    user = driver.find_element(By.ID,'user')
    user.send_keys('Narcolepsy')
    pwd = driver.find_element(By.ID,'password')
    pwd.send_keys('LaWNuS5v8aXA')

    loginbutton=driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/form/div[2]/div/p/button')
    loginbutton.click()
    return(url_for('new_page'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)