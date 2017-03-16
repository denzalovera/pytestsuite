from selenium import webdriver
from config import Config

browser = webdriver.Chrome(Config.get_ChromeWebdriver())
browser.get('http://seleniumhq.org/')

