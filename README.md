<div align="center">
<pre>
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
</pre>
</div>

# 🔓 Cryptanalysis Toolkit

> İstatistiksel frekans analizi, Index of Coincidence (IoC) ve Hamming mesafe hesaplamaları ile klasik şifreleme türlerini (Caesar, Vigenere, XOR) otomatik olarak kıran kriptanaliz aracı.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![Stdlib](https://img.shields.io/badge/Dep-Stdlib_Only-success)](./)
[![Status](https://img.shields.io/badge/Status-Active-success)](./)

---

## 📈 Proje Hakkında

Bu proje, anahtar bilgisi olmadan (brute-force ve istatistiksel analiz yöntemleriyle) çeşitli klasik şifreleme algoritmalarını kırmayı sağlayan bir kriptografi setidir.

**Commit Geçmişi:**
| Commit | Açıklama |
|--------|----------|
| `frequency analyzer and statistical toolkit` | İngilizce harf frekansları, Chi-Kare (χ2) testi, IoC hesaplamaları. |
| `classical ciphers and xor key recovery` | Caesar ve Vigenere kırma, tek baytlık ve tekrarlı XOR analizi. |
| `cli interface and automated decoding engine` | Argparse CLI, hex çözümleme, demo modu ve renkli çıktı. |

---

## 🧠 Mimari

```
main.py
  ├── analyzers/frequency_analyzer.py ← Chi-Kare (χ2) ve IoC ile istatistiksel analiz
  ├── analyzers/classical_ciphers.py  ← Caesar Shift, Vigenere anahtar uzunluğu tahmini
  └── analyzers/xor_analyzer.py       ← Hamming distance ile tekrarlı XOR tespiti
```

---

## ⚡ Kullanım

```bash
# Demo modu (tüm şifre türlerini test eder)
python main.py --demo

# Caesar Şifresi Kırma
python main.py --caesar "KHOOR ZRUOG"

# Vigenere Şifresi Kırma (Anahtar tahmini yapar)
python main.py --vigenere "VPTZ VZ C ZTMKVM DIIZTUM"

# Tek Baytlık XOR Kırma (Hex formatında veri)
python main.py --xor-single "1b37373331363f78151b7f2b783431333d78"

# Tekrarlı Anahtarla Yapılmış XOR Şifresi Kırma (Hex formatında veri)
python main.py --xor-repeat "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20"
```

---

*Fetih Çakmak — Cybersecurity Portfolio*
