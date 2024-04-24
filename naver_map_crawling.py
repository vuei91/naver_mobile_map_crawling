import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://m.map.naver.com/search2/search.naver?query=%EA%B3%A0%EC%96%91%EC%8B%9C%20%EC%9A%94%EC%96%91%EB%B3%91%EC%9B%90&sm=hty&style=v5#/list"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
search_list = driver.find_elements(By.CSS_SELECTOR, '._item._lazyImgContainer')
datas = []
i = 0
while i < len(search_list):
    driver.execute_script(f"window.scrollTo(0, {i * 100});")
    title = search_list[i].get_attribute('data-title')
    tel = search_list[i].get_attribute('data-tel')
    longitude = search_list[i].get_attribute('data-longitude')
    latitude = search_list[i].get_attribute('data-latitude')
    sid = search_list[i].get_attribute('data-sid')
    driver.get(f'https://m.place.naver.com/place/{sid}/home')
    driver.implicitly_wait(10)
    address = driver.find_element(By.CLASS_NAME, 'LDgIH').text
    flag_title = driver.find_element(By.CLASS_NAME, 'DJJvD').text
    webpage = None
    try:
        webpage = driver.find_element(By.CSS_SELECTOR, '.CHmqa').text
    except Exception as e:
        print(e)

    doctors = None
    try:
        doctors_parent = driver.find_element(By.CSS_SELECTOR,
                                             '.O8qbU:not(.tQY7D):not(.pSavy):not(.nbXkr):not(.yIPfO):not(.Uv6Eo)')
        doctors = doctors_parent.find_element(By.CSS_SELECTOR, '.vV_z_').text
    except Exception as e:
        print(e)

    times = None
    time_data = []
    try:
        driver.find_element(By.CLASS_NAME, 'gKP9i').click()
        time.sleep(1)
        times = driver.find_elements(By.CSS_SELECTOR, '.w9QyJ:not(.vI8SM):not(.yN6TD)')
        for timex in times:
            obj = {}
            span = timex.find_element(By.CSS_SELECTOR, '.y6tNq > .A_cdD > .i8cJw')
            div = timex.find_element(By.CSS_SELECTOR, '.y6tNq > .A_cdD > .H3ua4')
            obj['weekName'] = span.text
            obj['weekTime'] = div.text
            time_data.append(obj)
    except Exception as e:
        print(e)

    subject = None
    try:
        s = []
        subjects = driver.find_elements(By.CLASS_NAME, 'zxtJF')
        for subject in subjects:
            s.append(subject.text)
        subject = '|||'.join(s)
    except Exception as e:
        print(e)

    data = {
        'id': i,
        'title': title,
        'category': flag_title,
        'tel': tel,
        'longitude': longitude,
        'latitude': latitude,
        'doctors': doctors,
        'address': address,
        'webpage': webpage,
        'subject': subject,
        'clinicHoursList': time_data,
    }
    print(data)
    datas.append(data)
    driver.back()
    time.sleep(5)
    i = i + 1
    search_list = driver.find_elements(By.CSS_SELECTOR, '._item._lazyImgContainer')
    driver.implicitly_wait(10)

f2 = open('nursing_home_center.json', 'w', encoding='utf-8')
json.dump(datas, f2, ensure_ascii=False)
f2.close()

driver.quit()
