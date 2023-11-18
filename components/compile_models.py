from joblib import load

model_category = load(
    'components/ml_models/eng/category/support_category.joblib'
)
model_category_vectorizer = load(
    'components/ml_models/eng/category/support_category_vectorizer.joblib'
)
model_important = load(
    'components/ml_models/eng/important/support_important.joblib'
)
model_important_vectorizer = load(
    'components/ml_models/'
    'eng/'
    'important/'
    'support_important_vectorizer.joblib'
)


def text_category(text: str) -> str:
    """
    :param text: Вопрос
    :return: Категория
    """
    new_text_tfidf = model_category_vectorizer.transform([text])
    predicted_request = model_category.predict(new_text_tfidf)
    return predicted_request[0]


def text_important(text: str) -> int:
    """
    :param
    text: Вопрос
    :return: Важность
    вопроса
    """
    new_text_tfidf = model_important_vectorizer.transform([text])
    predicted_request = model_important.predict(new_text_tfidf)
    return int(predicted_request[0])
