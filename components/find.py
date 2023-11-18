import nest_asyncio
import spacy
from fuzzywuzzy import fuzz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time
from call_center.models import Question

tm = time.time()
nest_asyncio.apply()
nlp = spacy.load('ru_core_news_lg')


def preprocess_text(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    return text


def jaccard_similarity(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    set1 = set(text1)
    set2 = set(text2)

    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    similarity = intersection / union

    return similarity


def consul_eq(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    vector1 = np.mean([word.vector for word in doc1], axis=0)
    vector2 = np.mean([word.vector for word in doc2], axis=0)

    return cosine_similarity([vector1], [vector2])[0][0]


def semantic_eq(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


def fuzz_eq(text1, text2):
    similarity_ratio = fuzz.ratio(text1, text2)
    partial_similarity_ratio = fuzz.partial_ratio(text1, text2)
    token_sort_similarity_ratio = fuzz.token_sort_ratio(text1, text2)
    return (
        similarity_ratio
        + partial_similarity_ratio
        + token_sort_similarity_ratio
    )


def get_res(text: str, count: int, data: Question):
    if count > len(data):
        raise ValueError('count is greater than len(df["question"])')

    all_val = []
    for i in data:
        all_val.append(
            jaccard_similarity(str(i), text)
            + semantic_eq(str(i), text)
            + consul_eq(str(i), text)
            + fuzz_eq(str(i), text)
        )

    question = []
    for i in range(count):
        new = max(all_val)
        question.append(str(data[all_val.index(new)]))
        all_val[all_val.index(new)] = 0
    return question
