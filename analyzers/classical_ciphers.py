"""
Classical Ciphers Analyzer - Cracking Caesar and Vigenere ciphers
"""
from typing import Dict, Tuple
from .frequency_analyzer import chi_squared, clean_text, calculate_ioc

def crack_caesar(ciphertext: str) -> Tuple[int, str]:
    """
    Brute-forces the Caesar cipher and returns the most likely shift and plaintext
    based on the lowest Chi-squared statistic.
    """
    best_shift = 0
    best_chi = float('inf')
    best_text = ""
    
    for shift in range(26):
        plaintext = []
        for char in ciphertext:
            if char.isalpha():
                base = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - base - shift) % 26 + base)
                plaintext.append(decrypted_char)
            else:
                plaintext.append(char)
                
        candidate = "".join(plaintext)
        chi = chi_squared(candidate)
        
        if chi < best_chi:
            best_chi = chi
            best_shift = shift
            best_text = candidate
            
    return best_shift, best_text

def guess_vigenere_key_length(ciphertext: str, max_length: int = 20) -> int:
    """Estimates Vigenere key length using Index of Coincidence."""
    cleaned = clean_text(ciphertext)
    best_len = 1
    best_ioc = 0.0
    
    for length in range(1, max_length + 1):
        iocs = []
        for i in range(length):
            segment = cleaned[i::length]
            iocs.append(calculate_ioc(segment))
            
        avg_ioc = sum(iocs) / len(iocs)
        # English IoC is roughly 0.066
        if abs(avg_ioc - 0.066) < abs(best_ioc - 0.066):
            best_ioc = avg_ioc
            best_len = length
            
    return best_len

def crack_vigenere(ciphertext: str, key_length: int = 0) -> Tuple[str, str]:
    """
    Attempts to crack a Vigenere cipher. If key_length is 0, it guesses the length.
    """
    cleaned = clean_text(ciphertext)
    if not cleaned:
        return "", ciphertext
        
    if key_length == 0:
        key_length = guess_vigenere_key_length(cleaned)
        
    key = []
    for i in range(key_length):
        segment = cleaned[i::key_length]
        # Treat each segment as a Caesar cipher and crack it
        shift, _ = crack_caesar(segment)
        key.append(chr(shift + ord('a')))
        
    key_str = "".join(key)
    
    # Decrypt with the recovered key
    plaintext = []
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = ord(key_str[key_idx % key_length]) - ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext.append(decrypted_char)
            key_idx += 1
        else:
            plaintext.append(char)
            
    return key_str, "".join(plaintext)
