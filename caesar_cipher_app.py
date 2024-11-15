# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Türkçe alfabeye göre küçük ve büyük harf eşlemeleri
alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

# Şifreleme fonksiyonu
def caesar_cipher_encode(plaintext, key):
    ciphertext = []
    for char in plaintext:
        if char in alphabet_lower:
            new_position = (alphabet_lower.index(char) + key) % len(alphabet_lower)
            ciphertext.append(alphabet_lower[new_position])
        elif char in alphabet_upper:
            new_position = (alphabet_upper.index(char) + key) % len(alphabet_upper)
            ciphertext.append(alphabet_upper[new_position])
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

# Çözme fonksiyonu
def caesar_cipher_decode(ciphertext, key):
    plaintext = []
    for char in ciphertext:
        if char in alphabet_lower:
            original_position = (alphabet_lower.index(char) - key) % len(alphabet_lower)
            plaintext.append(alphabet_lower[original_position])
        elif char in alphabet_upper:
            original_position = (alphabet_upper.index(char) - key) % len(alphabet_upper)
            plaintext.append(alphabet_upper[original_position])
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Streamlit uygulaması
st.title("🔐 Sezar Şifreleme ve Çözme Aracı")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!")

# Yan sekmeler oluştur
tab1, tab2, tab3 = st.tabs(["Açıklama", "Şifreleme", "Çözme"])

# Açıklama Sekmesi
with tab1:
    st.header("📚 Sezar Şifreleme Nedir? Nasıl Kullanılır?")
    st.write("""
    Sezar Şifreleme, harflerin belirli bir kaydırma sayısına göre ileri veya geri alınarak şifrelendiği basit bir şifreleme algoritmasıdır.
    Örneğin, bir harf 3 birim sağa kaydırılarak şifrelenebilir ve çözme işlemi için 3 birim sola kaydırılarak orijinal haline döndürülür.
    """)
    st.write("**Kullanım Alanları:** Bu şifreleme yöntemi, özellikle basit güvenlik önlemleri için kullanılır ve tarih boyunca şifreli iletişimi sağlamak için yaygın olarak kullanılmıştır.")

    # Türkçe alfabe ve pozisyon tablosunu gösterme
    st.write("### Türkçe Alfabesi ve İndeksleme")
    positions = list(range(29))  # 0-28 arası pozisyonlar
    table = pd.DataFrame({
        "Büyük Harfler": list(alphabet_upper),
        "Küçük Harfler": list(alphabet_lower),
        "İndeks": positions
    })
    st.dataframe(table)

    # Etkileşimli Şifreleme ve Çözme Örneği
    st.write("### Etkileşimli Şifreleme ve Çözme İşlemi")
    st.write("1. Aşağıya **Merhaba Dünya** yazın ve 'Göster' butonuna basın.")
    input_text = st.text_input("Şifrelemek istediğiniz metni yazın:", "Merhaba Dünya")
    
    if st.button("Göster"):
        indices = [alphabet_lower.index(char) if char in alphabet_lower else -1 for char in input_text.lower()]
        valid_indices = [idx for idx in indices if idx != -1]
        labels = [char for char, idx in zip(input_text, indices) if idx != -1]
        
        fig, ax = plt.subplots()
        ax.bar(range(len(valid_indices)), valid_indices, tick_label=labels)
        ax.set_xlabel("Karakterler")
        ax.set_ylabel("İndeks Değerleri")
        st.pyplot(fig)
        st.write(f"**İndeks Değerleri:** {valid_indices}")

    st.write("2. Şifrelemek için bir anahtar (örneğin 3) seçin ve 'Şifrele' butonuna basın.")
    key = st.number_input("Anahtar (key) değeri seçin:", min_value=1, max_value=29, value=3, step=1)
    
    if st.button("Şifrele"):
        encrypted_text = caesar_cipher_encode(input_text, key)
        indices_encrypted = [(alphabet_lower.index(char) + key) % len(alphabet_lower) if char in alphabet_lower else -1 for char in input_text.lower()]
        valid_indices_encrypted = [idx for idx in indices_encrypted if idx != -1]
        encrypted_labels = [char for char, idx in zip(encrypted_text, indices_encrypted) if idx != -1]

        fig, ax = plt.subplots()
        ax.bar(range(len(valid_indices_encrypted)), valid_indices_encrypted, tick_label=encrypted_labels)
        ax.set_xlabel("Şifrelenmiş Karakterler")
        ax.set_ylabel("Şifrelenmiş İndeks Değerleri")
        st.pyplot(fig)
        st.write(f"**Şifrelenmiş Metin:** {encrypted_text}")
        st.write(f"**Şifrelenmiş İndeks Değerleri:** {valid_indices_encrypted}")

    st.write("3. Şifreli metni çözmek için anahtarı (key) paylaşın. Karakterlerin indekslerini **anahtar** sayısı kadar geri kaydırarak orijinal metni elde edebiliriz.")

# Şifreleme Sekmesi
with tab2:
    st.header("🔒 Şifreleme Paneli")
    plaintext = st.text_area("Şifrelemek istediğiniz metni buraya yazın:", placeholder="Metninizi buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1)
    if st.button("Şifrele", key="encrypt_button"):
        if plaintext.strip():
            encrypted_text = caesar_cipher_encode(plaintext, key)
            st.success(f"Şifrelenmiş Metin: {encrypted_text}")
        else:
            st.warning("Lütfen şifrelemek için bir metin girin.")

# Çözme Sekmesi
with tab3:
    st.header("🔓 Çözme Paneli")
    ciphertext = st.text_area("Çözmek istediğiniz şifreli metni buraya yazın:", placeholder="Şifreli metni buraya yazın...")
    key = st.number_input("Anahtar (key) değeri girin:", min_value=1, max_value=29, value=3, step=1, key="decode_key")
    if st.button("Çöz", key="decrypt_button"):
        if ciphertext.strip():
            decrypted_text = caesar_cipher_decode(ciphertext, key)
            st.success(f"Çözümlenmiş Metin: {decrypted_text}")
        else:
            st.warning("Lütfen çözmek için bir şifreli metin girin.")

# Alt bilgi
st.write("---")
st.caption("Sezar Şifreleme ve Çözme Aracı - Güvenli ve Eğlenceli! ")

st.caption("📝 Unutmayın ki, Sezar'ın hakkı Sezar'a! 😆")


