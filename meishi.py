# import MeCab
# import re
# from tqdm import tqdm



# # MeCab の初期化
# mecab = MeCab.Tagger()

# # 元の .vec ファイルを開く
# with open('model.vec', 'r', encoding='utf-8') as file:
#     lines = file.readlines()

# # 新しい .vec ファイル用のデータを格納
# new_lines = []

# for line in tqdm(lines):
#     # 単語を抽出
#     word = line.split(' ')[0]

#     # 形態素解析を使用して品詞を取得
#     node = mecab.parseToNode(word)
#     features = node.next.feature.split(',')

#     # 品詞が名詞であれば、リストに追加
#     if features[0] == '名詞':
#         new_lines.append(line)

# # 新しい .vec ファイルにデータを保存
# with open('model_nouns_only.vec', 'w', encoding='utf-8') as file:
#     for line in tqdm(new_lines):
#         file.write(line)

import MeCab
import re
from tqdm import tqdm

# MeCabの初期化
mecab = MeCab.Tagger()

# 元の.vecファイルを開く
with open('model.vec', 'r', encoding='utf-8') as file:
    # ヘッダー行を読み込む
    header = file.readline()
    # ファイルの残りの部分を読み込む
    lines = file.readlines()

# 新しい.vecファイル用のデータを格納
new_lines = []

for line in tqdm(lines):
    # 単語を抽出
    word = line.split(' ')[0]

    # 形態素解析を使用して品詞を取得
    node = mecab.parseToNode(word)
    while node:
        features = node.feature.split(',')
        # 品詞が名詞であれば、リストに追加
        if features[0] == '名詞':
            new_lines.append(line)
            break
        node = node.next

# 単語の総数を更新
num_words = len(new_lines)

# 新しい.vecファイルにデータを保存
with open('model_nouns_only.vec', 'w', encoding='utf-8') as file:
    # 更新されたヘッダー行を書き込む
    file.write(f"{num_words} {header.split(' ')[1]}")
    for line in new_lines:
        file.write(line)
