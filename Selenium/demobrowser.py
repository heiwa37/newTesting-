from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print (driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.back()
#driver.close()                # this closes only the current window
driver.refresh()
driver.minimize_window()
driver.quit() # this used  when all windows needs to be closed