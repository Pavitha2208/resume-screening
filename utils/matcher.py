# utils/matcher.py

def match_keywords(text, keywords):
    matched = [kw for kw in keywords if kw.lower() in text.lower()]
    score = int((len(matched) / len(keywords)) * 100) if keywords else 0
    return score, matched
