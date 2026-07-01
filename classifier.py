from config import QUERY_CATEGORIES


def classify_query(query: str) -> str:
    """
    Classifies incoming query into a content category.
    Used downstream for CDN routing and content filtering.

    Returns: 'standard' | 'restricted'
    """
    q = query.lower().strip()

    for category, keywords in QUERY_CATEGORIES.items():
        if any(kw in q for kw in keywords):
            return category

    return "standard"
