import sys, time
from selenium import webdriver

username = "EnterYourGithubUserName"
password = "EnterYourGithubPassword"
reponame = sys.argv[1]

browser = webdriver.Chrome("path/to/your/webdriver")
browser.get("http://github.com/login")


def remove():
    browser.find_element_by_xpath(
        "//*[@id='login_field']").send_keys(username)
    browser.find_element_by_xpath("//*[@id='password']").send_keys(password)
    browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details").click()
    browser.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()
    browser.find_element_by_xpath("//*[@id='repository_name']").send_keys(reponame)
    time.sleep(1)
    browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()

if __name__ == "__main__":
    remove()
