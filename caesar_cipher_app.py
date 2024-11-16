# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Türkçe alfabeye göre küçük ve büyük harf eşlemeleri
alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"


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
tab1, tab2, tab3 = st.tabs(["Sezar Şifreleme Algoritması", "Şifreleme (Encode)", "Çözme (Decode)"])


# Açıklama Sekmesi
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Türkçe alfabeye göre küçük ve büyük harf eşlemeleri
alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"


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
st.title("Sezar Şifreleme ve Çözme Aracı")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!")

# Yan sekmeler oluştur
tab1, tab2, tab3 = st.tabs(["Sezar Şifreleme Algoritması", "Şifreleme (Encode)", "Çözme (Decode)"])


# Açıklama Sekmesi
with tab1:
    st.markdown("<h2 style='color:#4A90E2;'> Sezar Şifreleme Algoritması Nedir?</h2>", unsafe_allow_html=True)
    st.write("Sezar Şifreleme, harfleri belirli bir kaydırma sayısına göre ileri veya geri alarak yapılan basit bir şifreleme algoritmasıdır.")
    
    st.markdown("<h3 style='color:#FF6347;'>📜 Adım Adım Sezar Şifreleme</h3>", unsafe_allow_html=True)
    st.write("""
    1. **Anahtar Seçin** 🔑: Şifreleme işlemi için bir kaydırma değeri (örneğin, 3) belirleyin.
    2. **Şifreleme İşlemi** 🔐: Her harfi anahtar değeri kadar ileri kaydırın.
    3. **Çözme İşlemi** 🔓: Şifrelenmiş metni geri almak için her harfi anahtar değeri kadar geri kaydırın.
    """)
    
    # Algoritmanın nasıl çalıştığını açıklayan tablo
    st.markdown("<h4 style='color:#32CD32;'>📊 Türkçe Alfabesi ve İndeksleme</h4>", unsafe_allow_html=True)
    table = pd.DataFrame({
        "Büyük Harf": list(alphabet_upper),
        "Küçük Harf": list(alphabet_lower),
        "İndeks": list(range(29))
    })
    st.table(table)

    st.markdown("<h4 style='color:#FF6347;'>💡 Örnek Şifreleme İşlemi</h4>", unsafe_allow_html=True)
    example_text = "Merhaba Dünya"
    example_key = 3
    st.write(f"**Girdi:** {example_text}")
    st.write(f"**Anahtar (Key):** {example_key}")

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
    
    encrypted_example = caesar_cipher_encode(example_text, example_key)
    st.write(f"**Şifrelenmiş Metin:** {encrypted_example}")

    # Kullanıcı etkileşimi alanı
    st.markdown("<h4 style='color:#FF6347;'>🧪 Deneme Alanı: Şifreleme ve Çözme İşlemini Kendiniz Deneyin</h4>", unsafe_allow_html=True)
    
    # Kullanıcıdan metin girişi
    user_text = st.text_input("Şifrelemek istediğiniz metni buraya yazın:", "Merhaba Dünya")
    user_key = st.number_input("Anahtar (Key) değeri seçin:", min_value=1, max_value=29, value=3, step=1)
    
    if st.button("Şifrele ve İndeksleri Göster"):
        encrypted_user_text = caesar_cipher_encode(user_text, user_key)
        
        # Şifrelenmiş metni ve indeksleri göster
        indices_original = [(alphabet_lower.index(char.lower()) if char.lower() in alphabet_lower else -1) for char in user_text]
        indices_encrypted = [(alphabet_lower.index(char.lower()) + user_key) % len(alphabet_lower) if char.lower() in alphabet_lower else -1 for char in user_text]
        
        st.write(f"**Şifrelenmiş Metin:** {encrypted_user_text}")
        st.write("### İndeksler")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Orijinal Karakterler**")
            st.write(list(user_text))
        with col2:
            st.write("**Orijinal İndeksler**")
            st.write(indices_original)
        with col3:
            st.write("**Şifrelenmiş İndeksler**")
            st.write(indices_encrypted)
        
        # İndeks grafiğini oluştur ve genişlet
        fig, ax = plt.subplots(figsize=(10, 3))
        ax.bar(range(len(user_text)), indices_encrypted, tick_label=list(user_text))
        ax.set_xlabel("Karakterler")
        ax.set_ylabel("İndeksler (Şifrelenmiş)")
        st.pyplot(fig)


    # Emoji ile alt bilgi
    st.caption("🔍 Sezar Şifreleme yöntemi tarih boyunca basit güvenlik önlemleri için yaygın olarak kullanılmıştır.")

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

st.caption("Sezar'ın hakkı Sezar'a! 😆")

    # Emoji ile alt bilgi
    st.caption("🔍 Sezar Şifreleme yöntemi tarih boyunca basit güvenlik önlemleri için yaygın olarak kullanılmıştır.")

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

st.caption("📝 Sezar'ın hakkı Sezar'a! 😆")


