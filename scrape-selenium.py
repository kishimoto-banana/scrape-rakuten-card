from selenium import webdriver
import time
import json

# 設定ファイル
conifg_path = 'config/setting.json'
with open(conifg_path) as f:
    conf = json.load(f)

# headless chromeの設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, executable_path='driver/chromedriver')

# トップページにアクセス
driver.get('https://www.rakuten-card.co.jp/')
time.sleep(1)

# ログイン
id = driver.find_element_by_id('u')
id.send_keys(conf['auth']['id'])
password = driver.find_element_by_id('p')
password.send_keys(conf['auth']['pass'])
driver.find_element_by_xpath('//*[@id="indexForm"]/fieldset/button').submit()
time.sleep(1)

# 金額の取得
billing = driver.find_element_by_xpath('//*[@id="js-bill-mask"]/em').text
print(billing)

# セッションの終了
driver.quit()
