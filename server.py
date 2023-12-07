from flask import Flask, request, jsonify, Response
import gensim
import random

app = Flask(__name__)

global model
print('ファイル読み込み中のため、クライアントを接続しないでください。')
model = gensim.models.KeyedVectors.load_word2vec_format('model_nouns_only.bin', binary=True)
print('読み込み完了')

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
    # モデルの語彙からランダムに単語を選択
    print(len(list(model.key_to_index.keys())))
    random_word = random.choice(list(model.key_to_index.keys()))

    # 選択した単語に類似した単語を見つける
    similar_word = model.most_similar(positive=[random_word])[0][0]

    # 結果を文字列にして返す
    words_text = random_word + " " + similar_word
    return Response(words_text, content_type="text/plain; charset=utf-8")


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)