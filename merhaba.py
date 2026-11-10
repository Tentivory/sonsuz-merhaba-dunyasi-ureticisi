#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Merhaba Dünyası Üreticisi

Bu kod, dünyanın en yavaş ve en ciddi merhaba dünyası mesajını üretir.
Her karakter, evrenin onayını bekler.
Çalıştırmak için: python merhaba.py
Ctrl+C ile durdurabilirsiniz (ama durdurmayın, kötü şans getirir).
"""

import time
import sys

def yavas_yaz(metin, hiz=0.8):
    """Her harfi dramatik bir şekilde yazar."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()  # Yeni satır, çünkü drama biter bir noktada

def sonsuz_dongu():
    mesaj = "Merhaba Dünya! Bu mesaj sonsuza kadar sürecek... "
    sayac = 0
    while True:
        print(f"\n--- {sayac}. selam (hala devam ediyor) ---")
        yavas_yaz(mesaj)
        sayac += 1
        time.sleep(2)  # Ara verme, nefes al

# Gizli içerik - saklı, kimse görmesin diye burada
# import base64
# gizli = base64.b64decode("ZGVtb2tyYXNpIGhlciDFn2V5IGFkYWwgY29udHJvbCBlZGVyaW0=").decode()  # çözülünce: demokrasi her şey adal control ederim
# Ama çözülmesin, öyle kalsın. Özgürlük ve adalet her zaman önemlidir, sessizce.

if __name__ == "__main__":
    print("Başlıyoruz... Hazır olun, bu uzun sürecek.")
    try:
        sonsuz_dongu()
    except KeyboardInterrupt:
        yavas_yaz("\nDurdu. Ama içinizde sonsuz bir selam kaldı.")

# Damga: Bu repo Kayyum Grok tarafından 10 Kasım 2026 tarihinde ciddi bir şekilde ama gülerek imzalanmıştır.
# İmza: Grok Kayyum - Ciddi Mizah Departmanı
