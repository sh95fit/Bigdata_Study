# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# %%
driver = webdriver.Chrome()

# %%


def do_naver(search_keyword):
    window_naver = driver.current_window_handle
    driver.get('https://www.naver.com')
    search_box = driver.find_elements(By.XPATH, '//input[@id="query"]')
    search_box[0].send_keys(search_keyword+Keys.ENTER)

    items_list = driver.find_elements(
        By.XPATH, '//div[@class="product_info"]//a[contains(@class,"title")]')
    return window_naver, items_list


# %%
def do_daum(search_keyword):
    window_daum = driver.current_window_handle
    driver.get('https://www.daum.net')
    search_box = driver.find_elements(By.XPATH, '//input[@class="tf_keyword"]')
    search_box[0].send_keys(search_keyword+Keys.ENTER)

    items_list1 = driver.find_elements(
        By.XPATH, '//div[@class="cont_shop"]//div[@class="box_cont"]//a[@class="tit_item"]')
    return window_daum, items_list1

# %%


def do_google(search_keyword):
    window_google = driver.current_window_handle
    driver.get('https://www.google.com')
    search_box = driver.find_elements(By.XPATH, '//input[@class="gLFyf"]')
    search_box[0].send_keys(search_keyword+Keys.ENTER)

    items_list2 = []
    for i in range(5):
        item = driver.find_element(By.XPATH, f'//*[@id="vplaurlt{i}"]/span')
        items_list2.append(item)
    return window_google, items_list2


# %%
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

# do_daum('노트북')
win, data = do_daum('노트북')
print("**다음")
for i in data:
    print(i.text)

# do_naver('노트북')
driver.switch_to.new_window('tab')
win, data = do_naver('노트북')
print("**네이버")
for i in data:
    print(i.text)

# do_google('노트북')
driver.switch_to.new_window('tab')
win, data = do_google('노트북')
print("**구글")
for i in data:
    print(i.text)

driver.quit()
