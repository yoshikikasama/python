# レビュー観点（レビュアー、reviewee双方が確認する)

- A:自動チェックできる項目
  - レビュー対象としない
  - コーディングスタイルは自動検証しておくこと
- B:イディオムレベルの項目
  - レビュー対象としない
  - 本質でないためレビューの段階では行わない
- C:セキュリティのためのチェック内容
  - レビューする
  - csrfトークンの使用等
- D:仕様観点レビュー
  - レビューする
  - 機能単体に着目したレビュー
    - 仕様に示された機能の入出力(画面、DB、メール、外部API呼び出しなど)を網羅しているか
    - 機能が対象とするモデルの絞り込みは仕様に示された通りに適切か(不必要なデータまで処理の対象に含めていないか？)
    - エラー発生時にロールバックされるデータと記録必須のデータが仕様に示された通りに区別されているか
  - 機能の結合に関連したレビュー
    - 機能に入力されるデータはどこからくるか
    - 機能が作成した出力をどの機能が利用するか