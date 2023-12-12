import MeCab
import ipadic
from tqdm import tqdm

# MeCabの初期化
mecab = MeCab.Tagger(ipadic.MECAB_ARGS)

# 元の.vecファイルを開く
with open('model_nouns_only.vec', 'r', encoding='utf-8') as file:
    # ヘッダー行を読み込む
    header = file.readline()
    # ファイルの残りの部分を読み込む
    lines = file.readlines()

# 新しい.vecファイル用のデータを格納
new_lines = []

for line in tqdm(lines):
    # 単語を抽出
    word = line.split(' ')[0]
    # print(word)
    # 形態素解析を使用して品詞を取得
    node = mecab.parseToNode(word)
    while node:
        features = node.feature.split(',')
        # 品詞が名詞であれば、リストに追加
        if features[0] == '名詞' and features[1] == "一般":
            # print(word, features)
            new_lines.append(line)
            break
        node = node.next

# 単語の総数を更新
num_words = len(new_lines)

# 新しい.vecファイルにデータを保存
with open('./noun_vec/m_ippan.vec', 'w', encoding='utf-8') as file:
    # 更新されたヘッダー行を書き込む
    file.write(f"{num_words} {header.split(' ')[1]}")
    for line in new_lines:
        file.write(line)

