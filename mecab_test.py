import MeCab


# MeCabの初期化
mecab = MeCab.Tagger('-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')

# 解析するテキスト
text = "これはサンプルテキストです。"

# 形態素解析を実行
parsed_text = mecab.parse(text)

print(parsed_text)

