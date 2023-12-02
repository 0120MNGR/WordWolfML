import gensim


model = gensim.models.KeyedVectors.load_word2vec_format('model_nouns_only.vec', binary=False)

print(model.most_similar(positive=['日本人']))
