import re
import unicodedata

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))

stemmer = PorterStemmer()


def preprocess_text(text, scenario='S4'):
    if scenario not in ('S1', 'S2', 'S3', 'S4'):
        raise ValueError("scenario harus S1, S2, S3, atau S4")

    if not isinstance(text, str):
        return ""

    if scenario == 'S1':
        return text

    text = text.lower()
    text = re.sub(r"['’‘]", "", text)
    text = "".join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))
    text = re.sub(r"\b\w*\d\w*\b", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    words = [w for w in text.split() if len(w) > 1]

    if scenario == 'S2':
        return " ".join(words)

    words = [w for w in words if w not in stop_words]

    if scenario == 'S3':
        return " ".join(words)

    return " ".join(stemmer.stem(w) for w in words)
