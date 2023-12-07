from gensim.models import KeyedVectors
import json

# Word2Vecモデルのロード
model = KeyedVectors.load_word2vec_format('model_nouns_only.bin', binary=True)

with open('word_pairs.json', 'r', encoding='utf-8') as f:
    word_pairs = json.load(f)
# print(word_pairs)
# print(type(word_pairs))

# コサイン類似度のリストを生成
cosine_similarities = []
for word1, word2 in word_pairs:
    if word1 in model.key_to_index and word2 in model.key_to_index:
        similarity = model.similarity(word1, word2)
        cosine_similarities.append((word1, word2, 1-similarity))
        # cosine_similarities.append(similarity)
    else:
        cosine_similarities.append((word1, word2, None))  # 単語がモデルにない場合

print(cosine_similarities)

# cosine_similaritiesには各単語ペアのコサイン類似度が格納されています
