from selenium import webdriver
import time 
 
keyword = input('어떤 이미지를 다운로드 받고 싶으신가요?')
# want_num = int(input('몇 장의 이미지를 다운로드 받고 싶으신가요?'))

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') # 창을 띄우지 않고 실행
wd = webdriver.Chrome('C://Users//asus//Documents//AI-math//chromedriver.exe')   #위의 옵션을 포함하여 웹드라이브를 실행함.
wd.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword))
print(f'네이버 이미지 검색에서 {keyword}를 검색하였습니다.')

time.sleep(3)
image = wd.find_element_by_xpath('//*[@id="main_pack"]/section/div/div[1]/div[1]/div[6]/div/div[1]/a/img')
url = image.get_attribute('src')
print(url)

### 파일 저장