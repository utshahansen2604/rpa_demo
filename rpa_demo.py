import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


# get the path of ChromeDriverServer
dir = os.path.dirname("C:\\Users\\Utshahan.Sen\\Desktop\\Codes")
chrome_driver_path = dir + "\\chromedriver.exe"



# create a new Chrome session
driver = webdriver.Chrome("C:\\Users\\Utshahan.Sen\\Desktop\\Codes\\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
url="https://shell.service-now.com/sp?id=sc_cat_item_guide&sys_id=2859127bdbe17f0081b6fd961d961917" #Linux/Unix Services Pages
driver.get(url)
time.sleep(5)

action=ActionChains(driver)


def field_fill(item_xpath,text):
    driver.find_element_by_xpath(item_xpath).send_keys(text)
    #action.move_to_element(item_xpath)
    time.sleep(2)  

def select_text(item_link,text):
    Select(driver.find_element_by_xpath(item_link)).select_by_visible_text(text)
    time.sleep(2)


driver.find_element_by_xpath("//*[@id='sp_formfield_sh_make_a_selection']/div[2]/label/input").click()
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='f9e0d3c9db921f00bd27f9231d961907']/div[1]/div/div").click()

time.sleep(3)
###########################################################

def but_click(item_xpath):
    try:
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
    
    except (TimeoutException) as py_ex:
        print(str(py_ex) + " :Exception @ "+ str(item_xpath))
    
    #action.move_to_element(item_xpath)
    driver.find_element_by_xpath(item_xpath).click()



field_fill("//*[@id='sp_formfield_sh_provide_business_justification']","Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_200_reason_for_request']","Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_300_valid_computer_user_id_gid']", "Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_400_user_physical_location']","Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_500_user_phone_number']", "Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_600_domainsite_for_account']", "Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_700_hostnameservice_required_for_']", "Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_800_group_membership__application']", "Lorem Ipsum")
but_click("//*[@id='sp_formfield_sh_900_require_home_directory']/label[1]/input")

field_fill("//*[@id='sp_formfield_sh_1010_site_location']"," Lorem Ipsum")
field_fill("//*[@id='sp_formfield_sh_1100_comments']", "Lorem Ipsum")



#but_click("//*[@id='sp_formfield_sh_100_operating_system_required_on_r']/label[1]/input")

#but_click("//*[@id='sp_formfield_sh_200_blade_type_required___note_po']/label[1]/input")

#field_fill("//*[@id='sp_formfield_sh_400_customer_physical_location__e']","Lorem Ipsum")

#select_text("//*[@id='sp_formfield_sh_500_location_to_be_accessed_using_']","AMS - Amsterdam NL")

#dropdown_fill("//*[@id='s2id_autogen2_search']", "BNG - Bangalore IN")
#dropdown_fill("//*[@id='s2id_autogen3_search']", "Yes")

#field_fill("//*[@id='sp_formfield_sh_710_provide_details_of_current_loc']", "Lorem Ipsum")




#driver.quit()

