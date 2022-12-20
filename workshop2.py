from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import date

driver = webdriver.Chrome()

driver.get("https://www.kodlama.io/")
driver.maximize_window()
sleep(2)

# kurs sayısı 6 ise test başarılı dönmeli.

courseBox = driver.find_elements(By.CLASS_NAME,"col-sm-6")
numberOfCourseBox = len(courseBox)
print(numberOfCourseBox)
driver.save_screenshot(str(date.today()) + ' ' + "test1.png")
driver.execute_script("window.scroll(0, 500)")
driver.save_screenshot(str(date.today()) + ' ' + 'test1_2.png') #Sayfanın altında kalan kurslar için ss

if numberOfCourseBox == 6:
    print("Test Başarılı")
else:
    print("Test Başarısız!")

# Senior diye aratınca çıkan sayfada 1 kurs var ve kursun ismi
# Senior Yazılım Geliştirici Yetiştirme Kampı (.NET) ise test başarılı dönmeli.

findCourse = driver.find_element(By.ID,"search-courses")
findCourse.send_keys("Senior")
sleep(3)

courseBox2 = driver.find_elements(By.CLASS_NAME, "course-list")
numberOfCourseBox2 = len(courseBox2)
print(f'Kurs Sayısı: {numberOfCourseBox2}')

courseName = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/a/div/div[2]")
print(f'Kurs ismi: {courseName.text}')
driver.save_screenshot(str(date.today()) + ' ' + 'test2.png')

if numberOfCourseBox2 == 1 and courseName.text == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Test başarılı")
else:
    print("Test başarısız!")
