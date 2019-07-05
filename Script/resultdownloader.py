from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  Select
from tkinter import messagebox
import os




#ASSINGMENT OF VARIABLES & WEBSITE ELEMNETS

def result(rollno):
    messagebox.showinfo("Update", "Process Has Been Started, Please Wait Till Next Notification.")
    #WEBDRIVER (EDITED)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    #OPENING URL (EDITED)
    driver.get("https://www.rtmnuresults.org/")

    try:

        faculty = Select(driver.find_element_by_name("ddlselectfaculty"))
        faculty.select_by_index(1)
                                                                                                    # TRYING TO WORK OUT
        semester = Select(driver.find_element_by_name("ddlselectexam"))
        semester.select_by_value('1301')
        rollbox = driver.find_element_by_name('txtrollno')
        roll_no = rollno
        rollbox.clear()
        rollbox.send_keys(roll_no)
        result_button = driver.find_element_by_name('imgbtnviewmarksheet')
        result_button.click()
        driver.get_screenshot_as_file(str(roll_no)+'.png')
        messagebox.showinfo("Success", "Your Result Has Been Successfully Saved As %s"%(os.getcwd()+"/"+str(roll_no)+'.png'))
        driver.close()
    except:                                                                                             # IF ANY INVALID ROLL NUMBER OCCURS, RAISE AN ERROR
        driver.close()
        messagebox.showerror("Error", "Please Enter Valid Roll Number")              
    
