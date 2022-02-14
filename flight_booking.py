from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
import datetime
from datetime import timedelta
class Transportation:

    def flight(self):

        index_url = "https://arikair.com/"
        firstname = "Bashir"
        lastname = "Alatishe"
        mobile = "8109065446"
        gmail = "bashiralatishe@gmail.com"
        my_date = datetime.date.today() + timedelta(days=5)
        date = my_date.strftime("%d/%m/%Y")
        # The executable_path below is the location of the chrome driver on the PC
        driver = webdriver.Chrome(executable_path="C:\\Users\\bashir.alatishe\\python_projects\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(index_url)
        driver.implicitly_wait(10)

        # This block contains all we have to do to get to the passenger information page
        driver.find_element_by_xpath('//button[@class="btn btn-danger"]').click()
        departure = driver.find_element_by_xpath('//select[@id="depPort"]')
        select_from = Select(departure)
        select_from.select_by_value('LOS')
        time.sleep(2)
        arrival = driver.find_element_by_xpath('//select[@id="arrPort"]')
        select_from = Select(arrival)
        select_from.select_by_visible_text("Abuja (ABV)")
        time.sleep(2)
        departure_date = driver.find_element_by_xpath('//input[@id="departureDate"]')
        departure_date.send_keys(date)
        time.sleep(2)
        passenger = driver.find_element_by_xpath('//select[@id="adult"]')
        select_from = Select(passenger)
        time.sleep(2)
        select_from.select_by_visible_text("1")
        search_opening = driver.find_element_by_xpath('//input[@id="btnSearch"]')
        search_opening.click()

        pick_time = driver.find_element_by_xpath('//div[@id="flightGrid0"]/div[5]//a//button')
        pick_time.click()
        time.sleep(2)
        continue_to_pay = driver.find_element_by_xpath("//input[@id='availabilitySummaryContinueButton']")
        continue_to_pay.click()

        # This block contains all we have to do to get to the payment page
        gender = driver.find_element_by_xpath('//select[@id="gender1"]')
        select_from = Select(gender)
        select_from.select_by_visible_text("Male")
        time.sleep(2)
        name = driver.find_element_by_xpath("//input[@id='name1']")
        name.send_keys(firstname)
        time.sleep(2)
        surname = driver.find_element_by_xpath("//input[@id='surname1']")
        surname.send_keys(lastname)
        time.sleep(2)

        day = driver.find_element_by_xpath('//select[@id="bday_day_1"]')
        select_from = Select(day)
        select_from.select_by_visible_text("6")
        time.sleep(2)
        month = driver.find_element_by_xpath('//select[@id="bday_month_1"]')
        select_from = Select(month)
        select_from.select_by_visible_text("March")
        time.sleep(2)
        year = driver.find_element_by_xpath('//select[@id="bday_year_1"]')
        select_from = Select(year)
        select_from.select_by_visible_text("1998")
        time.sleep(2)

        pnumber = driver.find_element_by_xpath("//input[@id='frst-tel-number0']")
        pnumber.send_keys(mobile)
        time.sleep(2)
        emailaddress = driver.find_element_by_xpath("//input[@id='email0']")
        emailaddress.send_keys(gmail)
        time.sleep(2)
        continue_to_pay = driver.find_element_by_xpath("//input[@id='btnSave']")
        continue_to_pay.click()


run_test = Transportation()
run_test.flight()
