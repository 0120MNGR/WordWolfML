from flask import Flask, Response, request
import gensim
import random
import pandas as pd

app = Flask(__name__)

# モデルの読み込み
global model
model = gensim.models.KeyedVectors.load_word2vec_format('bin/model_nouns_only.bin', binary=True)

# 頻度ランキングのDataFrameを読み込む
df = pd.read_pickle("bin/frec_jawiki-latest-pages-articles.pkl")

@app.route('/similar', methods=['GET'])
def similar():
    word = request.args.get('word', '')
    if not word:
        return Response('Error: No word provided', status=400, content_type="text/plain; charset=utf-8")

    try:
        similar_words = model.most_similar(positive=[word])
        words_text = similar_words[0][0] + " " + word
        return Response(words_text, content_type="text/plain; charset=utf-8")

    except KeyError:
        return Response('Error: Word not in vocabulary', status=404, content_type="text/plain; charset=utf-8")

@app.route('/get_random', methods=['GET'])
def get_random():
    
    # 単語の出現頻度数の閾値を指定
    FREQUENCY_THRESHOLD = 20000
    df_higher_rank = df[df["Frequency"] >= FREQUENCY_THRESHOLD]
    
    while True:
        # random_word = random.choice(list(model.key_to_index.keys()))
        random_word = df_higher_rank["Word"].sample(n=1).iloc[0]
        if random_word in model and len(random_word) >= 3:
            break
    
    # コサイン類似度の値を指定
    SIMILARITY = 0.45
    similar_words_lst = model.similar_by_key(random_word, topn=1000)
        
    min_difference = float('inf')
    nearest_word = None
    for word, similarity in similar_words_lst:
        difference = abs(similarity - SIMILARITY)
        if difference < min_difference and word in df_higher_rank["Word"].values:
            min_difference = difference
            nearest_word = word

    print(model.similarity(random_word, nearest_word))
    # # 結果を文字列にして返す
    words_text = random_word + " " + nearest_word
    return Response(words_text, content_type="text/plain; charset=utf-8")
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)