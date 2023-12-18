from flask import Flask, Response, request
import gensim
import random
import pandas as pd

app = Flask(__name__)

# モデルの読み込み
global model
model = gensim.models.KeyedVectors.load_word2vec_format('wordwolf_model.bin', binary=True)

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
    # ランダムに言葉を選ぶ
    random_word = random.choice(list(model.key_to_index.keys()))
    
    # コサイン類似度の値を指定
    SIMILARITY = 0.45
    similar_words_lst = model.similar_by_key(random_word)
        
    min_difference = float('inf')
    nearest_word = None
    for word, similarity in similar_words_lst:
        difference = abs(similarity - SIMILARITY)
        if difference < min_difference:
            min_difference = difference
            nearest_word = word

    print(model.similarity(random_word, nearest_word))
    # 結果を文字列にして返す
    words_text = random_word + " " + nearest_word
    return Response(words_text, content_type="text/plain; charset=utf-8")
    

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)