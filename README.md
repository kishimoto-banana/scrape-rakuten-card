# About
楽天カードのwebからログインして、請求金額を抽出します。

ライブラリの他にChromeDriverが必要です。
適宜[こちら](http://chromedriver.chromium.org/downloads)からダウンロードして下さい。

- scrape-requests.py
  
  `requests` により取得を行います。ただし金額が動的に記載されるため、正しく取得できません。
- scrape-selenium.py

  `selenium` を用いて取得を行います。こちらは正しく取得できます。
  
  # Usage
  - ライブラリのインストール
  ```
  $ pip install -r requirements.txt
  ```
  - `config/setting.json` に認証情報を記載
  - 実行
  ```
  $ python scrape-selenium.py
  ```
