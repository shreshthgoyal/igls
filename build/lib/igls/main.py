from typing import Type
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from urllib.parse import urljoin
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def scrape():
# Setting up the user
  print(f"{bcolors.WARNING}[IMP]-If you want to scrape a private account enter your own credentials.{bcolors.ENDC}")
  ans = input(f"{bcolors.BOLD}Your personal information won't be stored by this program. Are you comfortable with sharing your Instagram credentials?[Y/N]{bcolors.ENDC} ")

  if ans.lower()=='n':
     print(f"{bcolors.BOLD}Using trial account. If error occurs contact owner.{bcolors.ENDC}")
     in_user="AccountOnRent"
     in_pass="123asd456"
     account = input("Input any public account which you want to scrape: ")

  elif ans.lower()=='y':
     in_user=input(f"{bcolors.UNDERLINE}\nEnter username: {bcolors.ENDC}")
     in_pass=input(f"{bcolors.UNDERLINE}\nEnter Password: {bcolors.ENDC}")
     account = input(f"{bcolors.BOLD}Input any public account or any private account which you follow that you want to scrape: {bcolors.ENDC}")

  ask = input(f"{bcolors.BOLD}Get likes of particular post?[Y/N] {bcolors.ENDC}")

  if ask.lower()=='y':
     keyword='#'+input(f"{bcolors.BOLD}Enter tag according to which posts should be filtered: {bcolors.ENDC}")

  print(f"{bcolors.WARNING}**[IMP]-Dont click any thing on the upcoming browser screen, Everything is automated.\n{bcolors.ENDC}")
  time.sleep(1)
# Setting up the driver/browser
  s=Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=s)
  driver.get("https://www.instagram.com")

  time.sleep(2)

  username=driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
  password=driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
  username.clear()
  password.clear()
  username.send_keys(in_user)
  password.send_keys(in_pass)
  login = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()
  time.sleep(2)
  notnow = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]").click()
#turn on notif
  time.sleep(2)
  notnow2 = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]").click()

  while(notnow2):
       notnow2 = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]").click()
       time.sleep(2)

 

  time.sleep(5)
  searchbox=driver.find_element(by=By.CSS_SELECTOR, value="input[placeholder='Search']")
  searchbox.clear()
  searchbox.send_keys(account)
  time.sleep(2)
  searchbox.send_keys(Keys.ENTER)
  time.sleep(2)
  searchbox.send_keys(Keys.ENTER)

  driver.get("https://www.instagram.com/%s" % account)

  content = driver.page_source
  soup = BeautifulSoup(content, features="html.parser")

# Getting all the posts

  links = soup.findAll('a', href=True)
  posts=[]

  for link in links:
        post = link.get('href')
        if '/p/' in post and '/liked_by/' not in post:
            url= "https://www.instagram.com"+post
            if url not in posts:
              posts.append(url)
 
  scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")

  time.sleep(5)

  content = driver.page_source
  soup = BeautifulSoup(content, features="html.parser")

  links = soup.findAll('a', href=True)

  for link in links:
        post = link.get('href')
        if '/p/' in post and '/liked_by/' not in post:
            url= "https://www.instagram.com"+post
            if url not in posts:
                posts.append(url)

  match=False
  x=1

# Scrolling through the webpage 

  while(match==False):
    
     last_count = scrolldown
     scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
     time.sleep(5)

     content = driver.page_source
     soup = BeautifulSoup(content, features="html.parser")

     links = soup.findAll('a', href=True)

     for link in links:
            post = link.get('href')
            if '/p/' in post and '/liked_by/' not in post:
                 url= "https://www.instagram.com"+post
            if url not in posts:                                       # Adding each post only once
                 posts.append(url)               
     x+=1
          
     if last_count==scrolldown:
         match=True

  likes = []

  finalpost=[]
  finallike=[]

# Going through each post to get likes

  if ask.lower()=='n':
    for post in posts:
        driver.get('%s' % post)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        a= soup.findAll('a', class_='zV_Nj')
        for titles in a:
            title = titles.find('span').get_text()
            finalpost.append(post)
            if title:
              likes.append(title)
            else:
              likes.append("Not an image")


 
#Getting posts based on keyword

  else: 
    for post in posts:
        driver.get('%s' % post)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        a= soup.findAll('a', class_='xil3i', href=True)  
        for key in a:
         if keyword in key:
          likes_post= soup.find('a', class_='zV_Nj')
          for like in likes_post:
              like =likes_post.find('span').get_text()
              finalpost.append(post)
              if like:
                likes.append(like)
              else:
                likes.append("Not an image")
                
# Save it in a .csv file :-

  print(f"\n{bcolors.OKBLUE}[LOG]-Succesfully scraped %d posts from the instagram handle{bcolors.ENDC}" % len(finalpost))
  print(f"{bcolors.OKBLUE}[LOG]-Creating your .csv file and scoring post links and associated likes{bcolors.ENDC}")
  df = pd.DataFrame({'Image Url' : finalpost , ' Likes' : likes})
  df.to_csv('posts.csv', index=False, encoding='utf-8')
  print("\nThank you for using this scraper")
  
def show(val):
   try:
    if val:
        file=open('posts.csv', 'r')
        print(file.read())
   except:
     print(f"{bcolors.FAIL}[ERR]-No file right now. Scrape a instagram page first.{bcolors.ENDC}")


def main():
    parser =  argparse.ArgumentParser(description= "Web scrapper for Instagram, to scrape likes of a particular page.")
    parser.add_argument("-s","--scrape",  default=None, action='store_true',help="Initialises your Instagram Scraping")
    parser.add_argument("-o","--open", default=None, action='store_true', help="Opens .csv file")
    args = parser.parse_args()
    if args.scrape != None:
       scrape()
    elif args.open != None:
       show(True)    

if __name__ == "__main__":
        main()