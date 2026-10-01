import math
from collections import Counter

def word_count(text):
    return len(text.split())

def char_stats(text):
    counts = Counter(text)
    size = len(text)
    entropy = -math.fsum((n / size) * math.log2(n / size) for n in counts.values()) if size else 0
    return {"всего": size, "букв": sum(c.isalpha() for c in text), "уникальных": len(counts), "энтропия": round(entropy, 3)}
