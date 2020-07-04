# diff_archiver

初、 patch という言葉がさっと出てこなくて、こんなネーミングになった

# 使い方

まだコード自体を書き終わってないですが、 diff_archiver.py の docstring に書いてあります。

python sample.py をたたくとサンプルを試せます。

# テスト

python -m unittest discover tests

テストが通らないやつは push しないでね

# バージョンを上げる方法

- diff_archiver/**init**,py にある version の値を編集。
- バージョン番号の付け方は、 [Semantic Versioning](https://semver.org/) に従うこと。
- v(major).(minor).(patch)でリリースタグを切る
- 前回バージョンからの PR を見て更新内容を書き、リリース。
