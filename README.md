# get_address_info

[郵便番号データ](https://www.post.japanpost.jp/zipcode/dl/readme.html)からダウンロード出来るCSVファイルから、同一の郵便番号を保つ住所情報を削除して、JSONファイルを生成するコード。

ただし、キーとして、zipcode, prefecture, city, townを持つ。

## 使い方

1. [郵便番号データ](https://www.post.japanpost.jp/zipcode/dl/readme.html)からダウンロード出来るCSVファイルをダウンロードする
2. カナなどの情報を削除し、郵便番号、都道府県、市区町村、町域のみの情報にする
3. 列名を、zipcode, prefecture, city, townにする
4. `data/` に配置する
5. 実行する