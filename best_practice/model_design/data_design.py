"""データ設計

■マスターデータとトランザクションデータを分割する
 マスターデータ・・・データの中でも基礎となるもので、商品情報や従業員情報など1つ一つの基礎的な情報を記録する。
  ex) 商品マスター(商品名、型番、仕様など)
 ことやものなどについて記録したデータ。
 ・誰に(Whom): 顧客、販売先
 ・誰が(Who): ユーザー、管理者
 ・何を(What): 商品、記事
 ・どこ(where): 販売所、地域
 トランザクションデータ・・・システム上で発生した取引などの出来事を記録したデータで、履歴のこと。
  ex)商品の購買履歴、従業員への給与支払い履歴など
 何かの行為を起点に記録されたデータが主な対象となる。
 ・どのように(How): 販売、購入、出荷、操作
 データに付随して利用できそうなデータ
 ・いつ(When): 登録日時、更新日時
 ・どれくらい(How many): 注文数、数量
 ・いくら(How much): 金額
 ・なぜ(Why): 売上、返品、値引き、補充

 ■トランザクションデータは正確に記録しよう
  トランザクションデータに「そのときの行為」をデータとして正確に記録しましょう。安易に正規化して、
  重複を削除して、必要なデータまで削ってしまわないようにする。
  正規化の主な目的は「1つの事実は1箇所で管理する」こと。トランザクションデータであれば、履歴に付随する
  属性データ(いつ、どれくらい、いくら)を正確に記録していくことが必要なので、記録した後にその当時の
  データが正確に取り出せるか(変更されない不変的なものか)という観点で設計する。

■クエリで使いやすいテーブル設計をする
 RDBで正規化だけに着目してテーブル分割を進めると、パフォーマンスの劣化を伴うことがある。
 ほしい結果を得るためにたくさんのテーブルをJOINして無駄に複雑なクエリを作り出してしまう。
 機能的な要件は満たせるものの将来のデータ量を考慮した性能の要件は満たせなくなる。
 JOINによるテーブル結合は、対象となるテーブルのデータ量が大きくなればなるほど性能が劣化していく。
 同様の結果を得つつ、性能を改善するためには、あえて正規化を崩して冗長にデータを持たせる。
 正規化を崩すということは検索性を向上させる一方で更新する手間が増えるというトレードオフの関係にある。
 将来的なデータ量と発行されるクエリの頻度を考慮して十分な性能を発揮できるかを検討する。
"""