import asyncio
import nest_asyncio
import spacy
import pandas as pd
from fuzzywuzzy import fuzz
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import time

tm = time.time()
nest_asyncio.apply()
nlp = spacy.load('ru_core_news_lg')


async def preprocess_text(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    return text


async def jaccard_similarity(text1, text2):
    text1 = await preprocess_text(text1)
    text2 = await preprocess_text(text2)

    set1 = set(text1)
    set2 = set(text2)

    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    similarity = intersection / union

    return similarity


async def consul_eq(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    vector1 = np.mean([word.vector for word in doc1], axis=0)
    vector2 = np.mean([word.vector for word in doc2], axis=0)

    return cosine_similarity([vector1], [vector2])[0][0]


async def semantic_eq(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


async def fuzz_eq(text1, text2):
    similarity_ratio = fuzz.ratio(text1, text2)
    partial_similarity_ratio = fuzz.partial_ratio(text1, text2)
    token_sort_similarity_ratio = fuzz.token_sort_ratio(text1, text2)
    return (
        similarity_ratio
        + partial_similarity_ratio
        + token_sort_similarity_ratio
    )


async def get_res(text, count):
    df = pd.read_json('info.json').reset_index(drop=True)
    if count > len(df['question'].values.tolist()):
        raise ValueError('count is greater than len(df["question"])')

    all_val = []
    for i in df['question']:
        all_val.append(
            await jaccard_similarity(i, text)
            + await semantic_eq(i, text)
            + await consul_eq(i, text)
            + await fuzz_eq(i, text)
        )

    answer = []
    for i in range(count):
        new = max(all_val)
        answer.append(df.loc[all_val.index(new)].answer)
        all_val[all_val.index(new)] = 0
    return answer


async def main():
    text = 'Цена'
    count = 3
    result = await get_res(text, count)
    print(result)


# Запуск асинхронного кода
asyncio.run(main())
print(time.time() - tm)
