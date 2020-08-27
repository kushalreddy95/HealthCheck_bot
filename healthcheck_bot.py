from selenium import webdriver
from time import sleep
import logging
from secrets import username,password


class healthCheckBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        logging.info("Setting up browser")
        logging.info("Loading ASU Healthcheck Page")
        self.driver.get(
            'https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login' +
            '%3Fcallapp%3Dhttps%253A%252F%252Fweblogin.asu.edu%252Fserviceauth%252Foauth2%252Fnative%252Fallow' +
            '%253Finit%253Dfalse%2526response_type%253Dcode%2526client_id%253Dhealthcheck-web%2526redirect_uri' +
            '%253Dhttps%25253A%25252F%25252Fwww.asu.edu%25252Fhealthcheck%25252Fpreferences.html%2526state' +
            '%253DVhBqlF0oMgKm5FPK5o-bqIIXZp8X.3ae5SO69wkpx5CjHhuaRzmYoIo2-h--gZ6b%2526code_challenge_method%253DS256' +
            '%2526code_challenge%253DN4qqQcQjhzcFRAajWMMuQnwXILB6rofk-1A1qggFn4s%2526scope%253Dhttps%25253A%25252F' +
            '%25252Fapp.m.asu.edu%25252Fhealthcheck')
        logging.info("Page Loaded")
        user_ID = self.driver.find_element_by_xpath('//*[@id="username"]')
        user_ID.send_keys(username)
        pass_ID = self.driver.find_element_by_xpath('//*[@id="password"]')
        pass_ID.send_keys(password)
        logging.info("Entered User_Id and Password")
        lgn_btn = self.driver.find_element_by_xpath('//*[@id="login"]/section[2]/div[1]/input')
        lgn_btn.click()
        logging.info("logging In... on your phone.. click approve for Duo")

    def auto(self):
        try:
            hlt_chk_btn = self.driver.find_element_by_xpath('//*[@id="healthCheckContainer"]/a')
            hlt_chk_btn.click()
        except:
            ham_btn = self.driver.find_element_by_xpath('//*[@id="header-main"]/nav/button')
            ham_btn.click()
            logging.info("Navigating to Health Check")
            sleep(2)
            hlt_chk_btn = self.driver.find_element_by_xpath('//*[@id="healthCheckContainer"]/a')
            hlt_chk_btn.click()
        logging.info("Found Health Check")
        sleep(4)
        self.driver.switch_to.frame(0)

        try:
            logging.info("Selecting Options")
            none_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[2]/button[4]')
            none_btn.click()
            logging.info("No illness Selected")
            next_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/button')
            next_btn.click()
            sleep(2)
            none_btn1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[3]/button')
            none_btn1.click()
            logging.info("No symptoms Selected")
            sub_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[3]/div/div[4]/button')
            sub_btn.click()
            sleep(1)
            logging.info("Successfully Submitted")
        except Exception as e:
            logging.error(e)
        self.driver.switch_to.default_content()
        close_btn = self.driver.find_element_by_xpath('//*[@id="healthcheck-modal"]/div/div/div[1]/button')
        close_btn.click()
        logging.info("Closing")

    def logout(self):
        logging.info("Logging_out")
        try:
            log_out = self.driver.find_element_by_xpath('//*[@id="header-top"]/nav/a[6]')
            log_out.click()
        except:
            log_out = self.driver.find_element_by_xpath('//*[@id="menubar"]/div[2]/div/a[4]')
            log_out.click()

    def automate(self):
        self.login()
        sleep(4)
        self.auto()
        sleep(1)
        self.logout()






