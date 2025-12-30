import re

def extract_url_features(url):
    """
    Placeholder for manual feature extraction.
    Currently, the model uses TF-IDF on the raw URL string.
    """
    features = {
        'url_length': len(url),
        'hostname_length': len(re.search(r'://([^/]+)', url).group(1)) if '://' in url else len(url.split('/')[0]),
        'count_dots': url.count('.'),
        'count_hyphens': url.count('-'),
        'count_ats': url.count('@'),
        'count_questions': url.count('?'),
        'count_and': url.count('&'),
        'count_equals': url.count('='),
        'is_https': 1 if url.startswith('https') else 0
    }
    return features
