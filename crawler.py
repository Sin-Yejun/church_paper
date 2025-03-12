from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def get_image_url():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get('http://mokposarang.org/sub9_8')
        time.sleep(2)

        bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a')
        bar.click()
        time.sleep(2)

        img = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/article/div/p[3]/img[1]').get_attribute('src')
        return img
    
    except Exception as e:
        return f"에러 발생: {str(e)}"
    
    finally:
        driver.quit()

def save_to_file():
    img_url = get_image_url()
    with open("img_url.txt", "w", encoding="utf-8") as f:
        f.write(img_url)
    print(f"이미지 URL 저장 완료: {img_url}")

if __name__ == "__main__":
    save_to_file()