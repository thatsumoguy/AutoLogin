from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


userName = input("What is the username?")
password = input("What is the password?")

# This was used in Belarc system. It might be pointless for you, also this is nothing special
# Just a command prompt asking a question
searchTerm = input("Are you looking for a PC (1) or a User (2)?: ")
while searchTerm != '1' and searchTerm != '2':
    print("You did not select PC or User")
    searchTerm = input("Are you looking for a PC (1) or a User(2)?: ")


if searchTerm == '1':
    pcn = input("What is the PCN?: ")
else:
    searchUser = input("What is the username?: ")

# I am needing to move this onto IE and Firefox, but for now Chrome was easier for testing for me.
browser = webdriver.Chrome()
browser.get(('interal site'))
login_wait = WebDriverWait(browser, 20)

#Fill in username and password

username = browser.find_element_by_name('userName')
username.send_keys(userName)
password = browser.find_element_by_name('password')
password.send_keys(password)

# Press login
login = browser.find_element_by_name("Login")

# Because Chrome, for whatever reason, doesn't work well with it's own webdriver app
# We have to do an action move, click in the box, then press return. This happens again below
actions = webdriver.ActionChains(browser)
actions.move_to_element(login)
actions.click()
actions.send_keys(Keys.RETURN)
actions.perform()

print(browser.current_url)

# If looking for a PC it will pull the sid param and then create a new tab with the newly created address
# You may not have a sid (a session ID basically), but you may need something similar. The .query should be able to pull it

if searchTerm == '1':
    browser.find_element_by_name('mainFrame').send_keys(Keys.CONTROL + 't')
    sid = urlparse(browser.current_url).query
    str(sid)
    url = 'internal site'
    browser.get(url + sid)
    propetyControl = browser.find_element_by_name("DisplayedPCName")
    propetyControl.send_keys(pcn)
    search = browser.find_element_by_class_name("bodytxtsmall")
    actions = webdriver.ActionChains(browser)
    actions.move_to_element(search)
    actions.click()
    actions.send_keys(Keys.RETURN)
    actions.perform()

# If looking for a user, it does the same as above, just user in place a pcn.
else:
    browser.find_element_by_name('mainFrame').send_keys(Keys.CONTROL + 't')
    sid = urlparse(browser.current_url).query
    str(sid)
    url = 'internal site'
    browser.get(url + sid)
    usersName = browser.find_element_by_name("DisplayedUser")
    usersName.send_keys(searchUser)
    search = browser.find_element_by_class_name("bodytxtsmall")
    actions = webdriver.ActionChains(browser)
    actions.move_to_element(search)
    actions.click()
    actions.send_keys(Keys.RETURN)
    actions.perform()
