#!/usr/bin/env python3
"""
Cryptanalysis Toolkit - Ana CLI Modülü
Kullanım: python main.py --demo
"""
import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyzers.classical_ciphers import crack_caesar, crack_vigenere
from analyzers.xor_analyzer import crack_single_byte_xor, crack_repeating_key_xor

# --- ANSI Renk Kodları ---
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
MAGENTA= "\033[95m"
BOLD   = "\033[1m"
RESET  = "\033[0m"
GRAY   = "\033[90m"

BANNER = f"""{BOLD}{MAGENTA}
██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗
██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
██║      ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
██║      ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
╚██████╗ ██║  ██║   ██║   ██║        ██║   
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   
█████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗
██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝██╔════╝██╔════╝
███████║██╔██╗ ██║███████║██║   ╚████╔╝ ███████╗█████╗  
██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝  ╚════██║██╔══╝  
██║  ██║██║ ╚████║██║  ██║███████╗██║   ███████║███████╗
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝   ╚══════╝╚══════╝
       CRYPTANALYSIS TOOLKIT v1.0{RESET}
"""

def print_section(title: str):
    print(f"\n{BOLD}{CYAN}{'='*60}{RESET}")
    print(f"{BOLD}{CYAN}  {title}{RESET}")
    print(f"{BOLD}{CYAN}{'='*60}{RESET}")

def hex_to_bytes(hex_str: str) -> bytes:
    try:
        return bytes.fromhex(hex_str)
    except ValueError:
        print(f"{RED}Hata: Geçersiz hex dizgesi.{RESET}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Cryptanalysis Toolkit - Şifre Çözme ve Analiz Araçları'
    )
    parser.add_argument('--caesar', help='Caesar şifresini kır (metin)')
    parser.add_argument('--vigenere', help='Vigenere şifresini kır (metin)')
    parser.add_argument('--xor-single', help='Tek baytlık XOR kır (hex formatında)')
    parser.add_argument('--xor-repeat', help='Tekrarlı XOR kır (hex formatında)')
    parser.add_argument('--demo', action='store_true', help='Demo modunda çalıştır')
    
    args = parser.parse_args()
    print(BANNER)
    
    if not (args.caesar or args.vigenere or args.xor_single or args.xor_repeat or args.demo):
        print(f"{YELLOW}Kullanım örnekleri:{RESET}")
        print("  python main.py --demo")
        print("  python main.py --caesar \"KHOOR ZRUOG\"")
        print("  python main.py --xor-single \"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736\"")
        sys.exit(0)

    if args.demo:
        print_section("DEMO: CAESAR KIRMACA")
        caesar_cipher = "WKLV LV D VHFUHW PHVVDJH HQFUBSWHG ZLWK FDHVDU"
        print(f"  {GRAY}Şifreli Metin:{RESET} {caesar_cipher}")
        shift, plaintext = crack_caesar(caesar_cipher)
        print(f"  {GREEN}Bulunan Kaydırma:{RESET} {shift}")
        print(f"  {GREEN}Çözülen Metin:{RESET} {plaintext}")

        print_section("DEMO: VIGENERE KIRMACA")
        vigenere_cipher = "VPTZ VZ C ZTMKVM DIIZTUM MGYKTEKMU QXMY PQQMVMBM" # Key: SECRET, text: THIS IS A SECRET MESSAGE ENCRYPTED WITH VIGENERE
        print(f"  {GRAY}Şifreli Metin:{RESET} {vigenere_cipher}")
        key, plaintext = crack_vigenere(vigenere_cipher)
        print(f"  {GREEN}Bulunan Anahtar:{RESET} {key.upper()}")
        print(f"  {GREEN}Çözülen Metin:{RESET} {plaintext}")

        print_section("DEMO: TEK BAYT XOR KIRMACA")
        xor1_cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        print(f"  {GRAY}Şifreli Metin (Hex):{RESET} {xor1_cipher}")
        key_byte, decrypted, score = crack_single_byte_xor(bytes.fromhex(xor1_cipher))
        print(f"  {GREEN}Bulunan Anahtar:{RESET} '{chr(key_byte)}' (0x{key_byte:02x})")
        print(f"  {GREEN}Çözülen Metin:{RESET} {decrypted.decode('ascii', errors='replace')}")
        
    if args.caesar:
        print_section("CAESAR ŞİFRE ANALİZİ")
        shift, plaintext = crack_caesar(args.caesar)
        print(f"  {GREEN}Bulunan Kaydırma:{RESET} {shift}")
        print(f"  {GREEN}Çözülen Metin:{RESET} {plaintext}")
        
    if args.vigenere:
        print_section("VIGENERE ŞİFRE ANALİZİ")
        key, plaintext = crack_vigenere(args.vigenere)
        print(f"  {GREEN}Bulunan Anahtar:{RESET} {key.upper()}")
        print(f"  {GREEN}Çözülen Metin:{RESET} {plaintext}")
        
    if args.xor_single:
        print_section("TEK BAYT XOR ANALİZİ")
        data = hex_to_bytes(args.xor_single)
        key_byte, decrypted, score = crack_single_byte_xor(data)
        print(f"  {GREEN}Bulunan Anahtar:{RESET} '{chr(key_byte)}' (0x{key_byte:02x})")
        print(f"  {GREEN}Çözülen Metin:{RESET} {decrypted.decode('ascii', errors='replace')}")
        
    if args.xor_repeat:
        print_section("TEKRARLI XOR ANALİZİ")
        data = hex_to_bytes(args.xor_repeat)
        key_bytes, decrypted = crack_repeating_key_xor(data)
        print(f"  {GREEN}Bulunan Anahtar:{RESET} {key_bytes.decode('ascii', errors='replace')} ({key_bytes.hex()})")
        print(f"  {GREEN}Çözülen Metin:{RESET}\n{decrypted.decode('ascii', errors='replace')[:200]}...")

    print()

if __name__ == '__main__':
    main()
