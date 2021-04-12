from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get('https://ve.cbi.ir/tasreq.aspx')
    inputtbIDNo = driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbIDNo')
    inputtbIDNo.send_keys(tbIDNo)

    inputtbBRNo = driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbBRNo')
    inputtbBRNo.send_keys(tbBRNo)

    inputddlBrDay = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBrDay')
    inputddlBrDay.send_keys(ddlBrDay)

    inputddlBrMonth= driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlBrMonth')
    inputddlBrMonth.send_keys(ddlBrMonth)

    inputtbBrYear = driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbBrYear')
    inputtbBrYear.send_keys(bBrYear)

    if radios == 1:
        inputradio1 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_rbtnMarrKind1')
        inputradio1.click()
    if radios == 2:
        inputradio2 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_rbtnMarrKind2')
        inputradio2.click()
    if radios == 3:
        inputradio3 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_rbtnMarrKind3')
        inputradio3.click()
    if radios == 4:
        inputradio4 = driver.find_element_by_id('ctl00_ContentPlaceHolder1_rbtnMarrKind4')
        inputradio4.click()
    else:
        print("Your number is doesn't exist")
    
    chack = driver.find_element_by_id('ctl00_ContentPlaceHolder1_chkBoxAlert')
    chack.click()

    imnotrobat = driver.find_element_by_class_name('recaptcha-checkbox-border')
    imnotrobat.click()
    
 

tbIDNo= int (input('ID:'))
tbBRNo = int (input('Birth certificate: '))
print("Date of birth")
ddlBrDay = int (input('Day: '))
ddlBrMonth = int (input('Month: '))
bBrYear = int (input('Year: '))

print("hello")
print("hello")
print("hello")
print("hello")

radios = int (input('enter: '))



if '__main__'==__name__:
    main()
