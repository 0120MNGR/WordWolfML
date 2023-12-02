import requests

def get_similar_words(word):
    response = requests.get(f"http://localhost:5000/similar", params={'word': word})
    if response.status_code == 200:
        return response.text
    else:
        return {'error': f'Error: {response.status_code}'}

word = "日本人"
result = get_similar_words(word)
print(result)