from gensim.models import KeyedVectors

# テキスト形式のベクトルデータを読み込む
model = KeyedVectors.load_word2vec_format('model_neo_nouns_only.vec', binary=False)

# バイナリ形式で保存する
model.save_word2vec_format('model_neo_nouns_only.bin', binary=True)
