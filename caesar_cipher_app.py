# -*- coding: utf-8 -*-

import pandas as pd

import streamlit as st

# Bilgilendirme Sekmesi
with st.expander("📚 Sezar Şifreleme Nedir? Nasıl Kullanılır?"):
    st.subheader("Sezar Şifreleme Algoritması")
    st.write("""
    Sezar Şifreleme, harflerin belirli bir kaydırma sayısına göre ileri veya geri alınarak şifrelendiği basit bir şifreleme algoritmasıdır.
    Örneğin, bir harf 3 birim sağa kaydırılarak şifrelenebilir ve çözme işlemi için 3 birim sola kaydırılarak orijinal haline döndürülür.
    **Kullanım Alanları:** Bu şifreleme yöntemi, özellikle basit güvenlik önlemleri için kullanılır ve tarih boyunca şifreli iletişimi sağlamak için yaygın olarak kullanılmıştır.
    """)

    # Türkçe alfabe ve pozisyon tablosunu gösterme
    st.write("### Türkçe Alfabesi ve Pozisyonları")
    alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
    positions = list(range(29))  # 0-28 arası pozisyonlar
    table = pd.DataFrame({
        "Alphabet": list(alphabet_lower),
        "Position": positions
    })
    st.dataframe(table)

    # Örnek Şifreleme ve Çözme
    st.write("### Örnek Şifreleme ve Çözme İşlemi")
    st.write("Girdi: 'Merhaba Dünya' | Anahtar (Key): 3")
    example_text = "Merhaba Dünya"
    example_key = 3

    # Şifreleme ve çözme örneği
    def caesar_cipher_example_encode(plaintext, key):
        encrypted = []
        for char in plaintext:
            if char in alphabet_lower:
                new_idx = (alphabet_lower.index(char) + key) % len(alphabet_lower)
                encrypted.append(alphabet_lower[new_idx])
            elif char.lower() in alphabet_lower:
                new_idx = (alphabet_lower.index(char.lower()) + key) % len(alphabet_lower)
                encrypted.append(alphabet_lower[new_idx].upper())
            else:
                encrypted.append(char)
        return ''.join(encrypted)

    encrypted_example = caesar_cipher_example_encode(example_text.lower(), example_key)
    st.write(f"Şifrelenmiş Metin: {encrypted_example}")

    def caesar_cipher_example_decode(ciphertext, key):
        decrypted = []
        for char in ciphertext:
            if char in alphabet_lower:
                new_idx = (alphabet_lower.index(char) - key) % len(alphabet_lower)
                decrypted.append(alphabet_lower[new_idx])
            elif char.lower() in alphabet_lower:
                new_idx = (alphabet_lower.index(char.lower()) - key) % len(alphabet_lower)
                decrypted.append(alphabet_lower[new_idx].upper())
            else:
                decrypted.append(char)
        return ''.join(decrypted)

    decrypted_example = caesar_cipher_example_decode(encrypted_example.lower(), example_key)
    st.write(f"Çözümlenmiş Metin: {decrypted_example}")

# Türkçe alfabeye göre küçük ve büyük harf eşlemeleri
alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

# Şifreleme fonksiyonu
def caesar_cipher_encode(plaintext, key):
    ciphertext = []

    for char in plaintext:
        if char in alphabet_lower:
            # Küçük harflerde şifreleme
            new_position = (alphabet_lower.index(char) + key) % len(alphabet_lower)
            ciphertext.append(alphabet_lower[new_position])
        elif char in alphabet_upper:
            # Büyük harflerde şifreleme
            new_position = (alphabet_upper.index(char) + key) % len(alphabet_upper)
            ciphertext.append(alphabet_upper[new_position])
        else:
            # Harf dışında karakter ise olduğu gibi ekle
            ciphertext.append(char)

    return ''.join(ciphertext)

# Çözme fonksiyonu
def caesar_cipher_decode(ciphertext, key):
    plaintext = []

    for char in ciphertext:
        if char in alphabet_lower:
            # Küçük harflerde çözme
            original_position = (alphabet_lower.index(char) - key) % len(alphabet_lower)
            plaintext.append(alphabet_lower[original_position])
        elif char in alphabet_upper:
            # Büyük harflerde çözme
            original_position = (alphabet_upper.index(char) - key) % len(alphabet_upper)
            plaintext.append(alphabet_upper[original_position])
        else:
            # Harf dışında karakter ise olduğu gibi ekle
            plaintext.append(char)

    return ''.join(plaintext)

# Streamlit uygulaması
st.title("🔐 Sezar Şifreleme ve Çözme Aracı")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!")

# Yan sekmeler oluştur
tab1, tab2 = st.tabs(["Şifreleme", "Çözme"])

# Şifreleme Paneli
with tab1:
    st.header("🔒 Şifreleme Paneli")
    plaintext = st.text_area("Şifrelemek istediğiniz metni buraya yazın:", placeholder="Metninizi buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1)
    if st.button("Şifrele"):
        if plaintext.strip():
            encrypted_text = caesar_cipher_encode(plaintext, key)
            st.success(f"Şifrelenmiş Metin: {encrypted_text}")
        else:
            st.warning("Lütfen şifrelemek için bir metin girin.")

# Çözme Paneli
with tab2:
    st.header("🔓 Çözme Paneli")
    ciphertext = st.text_area("Çözmek istediğiniz şifreli metni buraya yazın:", placeholder="Şifreli metni buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1, key="decode_key")
    if st.button("Çöz"):
        if ciphertext.strip():
            decrypted_text = caesar_cipher_decode(ciphertext, key)
            st.success(f"Çözümlenmiş Metin: {decrypted_text}")
        else:
            st.warning("Lütfen çözmek için bir şifreli metin girin.")

# Alt bilgi
st.write("---")
st.caption("Sezar Şifreleme ve Çözme Aracı - Güvenli ve Eğlenceli! ")

st.caption("📝 Sezar'ın hakkı Sezar'a! 😆")
