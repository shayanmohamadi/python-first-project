from selenium import webdriver
def main():
    #driver = webdriver.Firefox('')
    driver = webdriver.Firefox()
    driver.get('http://google.com')
 
if '__main__'==__name__:
    main()
