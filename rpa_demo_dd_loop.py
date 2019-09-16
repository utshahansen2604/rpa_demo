import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# get the path of ChromeDriverServer
dir = os.path.dirname("C:\\Users\\Utshahan.Sen\\Desktop\\Codes")
chrome_driver_path = dir + "\\chromedriver.exe"



# create a new Chrome session
driver = webdriver.Chrome("C:\\Users\\Utshahan.Sen\\Desktop\\Codes\\chromedriver.exe")
driver.implicitly_wait(15)
driver.maximize_window()



for i in range(0,3): #Loop for 'n' requests
#Navigate to the application home page
    time.sleep(2)
    url="https://shell.service-now.com/sp?id=sc_cat_item_guide&sys_id=54b94727dbf1df40bd27f9231d96199c"  #Linux/Unix Services Pages -> Linux Server Decommission
    driver.get(url)
    action=ActionChains(driver)
    
    def but_click(item_xpath):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        except (TimeoutException) as py_ex:
            print(str(py_ex))
        except (Exception):
            but_click(item_xpath)
        #print(str(py_ex) + " :Exception @ "+ str(item_xpath))
        driver.find_element_by_xpath(item_xpath).click()
        time.sleep(2)

    def field_fill(item_xpath,text):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        except (TimeoutException) as py_ex:
            print(str(py_ex))
        driver.find_element_by_xpath(item_xpath).send_keys(text)
        #action.move_to_element(item_xpath)
        time.sleep(1) 

    def field_fill_with_dropdown(item_xpath,text):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
        except (TimeoutException) as py_ex:
            print(str(py_ex))
        driver.find_element_by_xpath(item_xpath).send_keys(text)
        driver.find_element_by_xpath("//*[@class='select2-result-label']").click()
        time.sleep(2)  

#    def select_text(dropdpwn_link,item_link,text):
#        Select(driver.find_element_by_xpath(item_link)).select_by_visible_text(text)
#        driver.find_element_by_xpath(item_link).send_keys(Keys.ENTER)
#        time.sleep(1)


    but_click("//*[@id='sp_formfield_sh_linux_unix_services']/label[2]/input")
    but_click("//*[@id='sp_formfield_sh_support_maintenance']/div[6]/label/input")
    but_click("//*[@id='submit']")
    time.sleep(10)
    #driver.implicitly_wait(10)
    but_click("//*[@id='1f3d8d91dba95740f16ef1951d961902']")
    time.sleep(2)
    ###########################################################
    
    field_fill("//*[@id='sp_formfield_sh_provide_business_justification']","Lorem Ipsum")
    field_fill_with_dropdown("//*[@id='s2id_autogen3']","CAINCC-N-B00301")
    
    
    but_click("//*[@id='sp_formfield_sh_300_server_type']/label[1]/input")
    but_click("//*[@id='sp_formfield_sh_1100_is_this_system_a_candidate_for']/label[1]/input")
    but_click("//*[@id='sp_formfield_sh_1200_will_this_system_need_to_be_sh']/label[2]/input")
    but_click("//*[@id='sp_formfield_sh_1400_is_this_server_part_of_a_tsys']/label[2]/input")
    but_click("//*[@id='sp_formfield_sh_1700_it_is_required_that_all_databa']/label[3]/input")
    
    field_fill("//*[@id='sp_formfield_sh_1900_server_primary_role']","Lorem Ipsum")
    field_fill("//*[@id='sp_formfield_sh_2000_additional_comments']","Lorem Ipsum")
    
    but_click("//*[@id='sp_formfield_sh_2100_the_recommended_standard_proce']/label[1]/input")
    
    field_fill_with_dropdown("//*[@id='s2id_autogen2']", "TLS -TaCIT")
    
    field_fill("//*[@id='sp_formfield_sh_2400_application_support_email_addr']", "Lorem Ipsum")
    field_fill("//*[@id='sp_formfield_sh_2500_application_support_contact_nu']", "Lorem Ipsum")
    
    but_click("//*[@id='sp_formfield_sh_2600_i_confirm_that_i_have_uploaded']")
    but_click("//*[@id='sp_formfield_sh_2800_is_this_a_msl_tsystems_proj']/label[2]/input")
    but_click("//*[@id='sp_formfield_sh_3000_request_type']/div[4]/label/input")
    
    but_click("//*[@id='submit']")
    
    time.sleep(5)
    
    print("Adding to cart")
    
    
    add_to_cart=driver.find_element_by_xpath("//*[@id='x537430c9db4af300bd27f9231d96194e']/div/div/div/div/div[2]/div/div[2]/button[1]")
    driver.execute_script("arguments[0].click();", add_to_cart)
    #try:
    #   WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, add_to_cart)))
    #except (TimeoutException) as py_ex2:
    #    print(str(py_ex2))
    #
    #but_click(add_to_cart)

    #driver.quit()