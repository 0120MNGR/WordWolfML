from flask import Flask, request, jsonify, Response
import gensim
import json

app = Flask(__name__)

global model
print('ファイル読み込み中のため、接続しないでください。')
model = gensim.models.KeyedVectors.load_word2vec_format('model_nouns_only.vec', binary=False)
print('読み込み完了')

@app.route('/similar', methods=['GET'])
def similar():
    word = request.args.get('word', '')
    if not word:
        return jsonify({'error': 'No word provided'}), 400

    try:
        similar_words = model.most_similar(positive=[word])
        words_text = similar_words[0][0] + " " + word
        # response_data = {'similar_words': word_lst}
        # response_json = json.dumps(response_data, ensure_ascii=False)
        return Response(words_text, content_type="text/plain; charset=utf-8")

    except KeyError:
        return jsonify({'error': 'Word not in vocabulary'}), 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
