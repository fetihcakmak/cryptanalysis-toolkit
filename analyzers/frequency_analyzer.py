"""
Frequency Analyzer - Statistical analysis of text for cryptanalysis
"""
import string
from typing import Dict, Counter
import collections

# Standard English letter frequencies
ENGLISH_FREQ = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

def clean_text(text: str) -> str:
    """Removes non-alphabetic characters and converts to lowercase."""
    return ''.join(c.lower() for c in text if c.isalpha())

def get_frequencies(text: str) -> Dict[str, float]:
    """Calculates letter frequencies in a given text."""
    cleaned = clean_text(text)
    if not cleaned:
        return {}
    
    counts = collections.Counter(cleaned)
    length = len(cleaned)
    return {char: count / length for char, count in counts.items()}

def calculate_ioc(text: str) -> float:
    """Calculates the Index of Coincidence (IoC) of a text."""
    cleaned = clean_text(text)
    n = len(cleaned)
    if n <= 1:
        return 0.0
    
    counts = collections.Counter(cleaned)
    ioc = sum(count * (count - 1) for count in counts.values()) / (n * (n - 1))
    return ioc

def chi_squared(text: str) -> float:
    """Calculates the Chi-Squared statistic against standard English frequencies."""
    cleaned = clean_text(text)
    length = len(cleaned)
    if length == 0:
        return float('inf')
    
    counts = collections.Counter(cleaned)
    chi_sq = 0.0
    
    for char in string.ascii_lowercase:
        observed = counts.get(char, 0)
        expected = length * ENGLISH_FREQ[char]
        if expected > 0:
            chi_sq += ((observed - expected) ** 2) / expected
            
    return chi_sq
