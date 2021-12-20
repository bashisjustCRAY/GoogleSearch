from selenium import webdriver
import time

class Search:

    def searched_item(self):
        index_url = "https://google.com"
        item = 'Snake'
        count = 0
        # The executable_path below is the location of the chrome driver on the PC
        driver = webdriver.Chrome(executable_path="C:\\Users\\bashir.alatishe\\python_projects\\drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.get(index_url)
        driver.implicitly_wait(10)

        # This block searches for whatever is stored in the item variable
        search_field = driver.find_element_by_xpath('//input[@title="Search"]')
        search_field.send_keys(item)
        search_button = driver.find_element_by_css_selector('.FPdoLc [value="Google Search"]')
        search_button.click()

        # time.sleep(3)

        # This block gets all the results and finds the matches with the item
        search_result = driver.find_elements_by_partial_link_text(item)
        for element in search_result:
            count += 1

        print(f"We found {count} matches")

run_test = Search()
run_test.searched_item()
