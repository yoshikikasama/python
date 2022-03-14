"""module設計
■utils.pyのような汎用的な名前は避ける。
データをフィルターする処理はmodels.pyなどにまとめる。
リクエストに関係する処理はrequest.pyなどにまとめる。

■ビジネスロジック(業務に必要な処理)をモジュールに分割する。
例えば、商品、購入、在庫などを1つずつのモジュールにする。
一貫性を保つべきビジネス上の処理は1つの関数にまとめておく。

■モジュールのまとめ方
・意味でまとめられる時は積極的に分割する。
・モジュールが大きくなった場合は、パッケージ(__init__.pyのあるディレクトリ)にまとめる。
ex)
.
├── api # 外部APIにアクセスする処理をまとめる
│   ├── __init__.py
│   ├── item.py # 商品に関するAPI処理をまとめる
│   └── user.py # ユーザーに関するAPI処理をまとめる
├── commands # コマンドラインツールのサブコマンドをまとめる
│   ├── __init__.py
│   ├── list.py # 商品の一覧を表示するコマンドの入出力を扱う処理をまとめる
│   └── purchase.py # 商品を購入するコマンドの入出力を扱う処理をまとめる
├── consts.py # バックエンドAPIのホストなど定数をまとめる(もしくはconstants.py)
├── main.py # ツールのエントリーポイントのmain関数を置く 
├── models.py # 商品やユーザーのデータを永続化するクラスをまとめる
├── purchase.py # 商品を購入する処理をまとめる
└── validators.py # コマンドラインからの入力をチェックする処理をまとめる

■使いやすいモジュール名
認証：　authentication.py
認可、パーミッション： permission.py / authorization.py
バリデーション：　validations.py / validators.py
例外： exceptions.py

"""