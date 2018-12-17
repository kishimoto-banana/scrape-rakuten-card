import requests
from bs4 import BeautifulSoup
import json

# 設定ファイル
conifg_path = 'config/setting.json'
with open(conifg_path) as f:
    conf = json.load(f)

# セッションを開始
session = requests.session()

# ログイン情報
login_info = {
    'u':conf['auth']['id'],
    'p':conf['auth']['pass'],
    'service_id':'f425',
    'param':'login',
    'pp_version':'20170213'
}

# ログイン
url_login = 'https://grp01.id.rakuten.co.jp/rms/nid/login?'
res = session.post(url_login, data=login_info)
res.raise_for_status()

# 金額の取得
soup = BeautifulSoup(res.content, 'html.parser')
billing = soup.select_one('#js-bill-mask > em').get_text()
print(billing)

