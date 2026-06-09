"""
XOR Analyzer - Cracking single-byte and repeating-key XOR encryption
"""
import string
from typing import Tuple, List

# Basic English character frequency scoring
def score_english(text_bytes: bytes) -> float:
    score = 0.0
    for b in text_bytes:
        c = chr(b).lower()
        if c in 'etaoin shrdlu':
            score += 2
        elif c in string.ascii_lowercase:
            score += 1
        elif chr(b) in string.printable:
            score -= 1
        else:
            score -= 5
    return score

def crack_single_byte_xor(ciphertext: bytes) -> Tuple[int, bytes, float]:
    """
    Brute-forces a single-byte XOR cipher.
    Returns (key_byte, decrypted_bytes, score)
    """
    best_score = float('-inf')
    best_key = 0
    best_decrypted = b""
    
    for key in range(256):
        decrypted = bytes([b ^ key for b in ciphertext])
        score = score_english(decrypted)
        
        if score > best_score:
            best_score = score
            best_key = key
            best_decrypted = decrypted
            
    return best_key, best_decrypted, best_score

def hamming_distance(b1: bytes, b2: bytes) -> int:
    """Calculates bitwise Hamming distance between two byte strings."""
    dist = 0
    for x, y in zip(b1, b2):
        val = x ^ y
        while val > 0:
            dist += val & 1
            val >>= 1
    return dist

def guess_xor_key_length(ciphertext: bytes, max_len: int = 40) -> int:
    """Estimates the repeating XOR key length using Hamming distance."""
    best_len = 2
    best_dist = float('inf')
    
    max_len = min(max_len, len(ciphertext) // 2)
    if max_len < 2:
        return 1
        
    for keysize in range(2, max_len + 1):
        distances = []
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        
        # Compare first 4 chunks if possible
        num_chunks = min(len(chunks), 4)
        if num_chunks < 2:
            break
            
        for i in range(num_chunks - 1):
            if len(chunks[i]) == keysize and len(chunks[i+1]) == keysize:
                dist = hamming_distance(chunks[i], chunks[i+1])
                distances.append(dist / keysize)
                
        if distances:
            avg_dist = sum(distances) / len(distances)
            if avg_dist < best_dist:
                best_dist = avg_dist
                best_len = keysize
                
    return best_len

def crack_repeating_key_xor(ciphertext: bytes, key_length: int = 0) -> Tuple[bytes, bytes]:
    """
    Breaks repeating-key XOR encryption.
    """
    if not ciphertext:
        return b"", b""
        
    if key_length == 0:
        key_length = guess_xor_key_length(ciphertext)
        
    key = bytearray()
    
    # Break ciphertext into blocks of key_length, transpose, and solve as single-byte XOR
    for i in range(key_length):
        block = bytes([ciphertext[j] for j in range(i, len(ciphertext), key_length)])
        best_key_byte, _, _ = crack_single_byte_xor(block)
        key.append(best_key_byte)
        
    # Decrypt with the recovered key
    decrypted = bytearray()
    for i, b in enumerate(ciphertext):
        decrypted.append(b ^ key[i % len(key)])
        
    return bytes(key), bytes(decrypted)
