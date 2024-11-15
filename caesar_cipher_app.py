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
st.title("Sezar Şifreleme (Caesar Cipher)")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!")
    
st.write("")

# Yan sekmeler oluştur
tab1, tab2, tab3 = st.tabs(["Sezar Şifreleme Algoritması", "Şifreleme (Encode)", "Çözme (Decode)"])

import os
print(os.getcwd())  # Çalıştığınız dizini kontrol edin
print(os.path.exists("caesar_cipher_ring.jpg"))  # Dosyanın mevcut olup olmadığını kontrol edin

# Açıklama Sekmesi
with tab1:
    # Renkli bir başlık
    st.markdown("<h3 style='color:#4A90E2;'>Sezar Şifreleme Algoritması Nedir?</h3>", unsafe_allow_html=True)
    
    # Görsel ekleme (Sezar Çarkı)
    st.image("caesar_cipher_ring.jpeg", caption="Sezar Şifreleme Algoritması'nın Tarihsel Sembolü", width=250)


    # Giriş açıklaması
    st.write("""
    Sezar Şifreleme, harflerin belirli bir kaydırma sayısına göre ileri veya geri alınarak şifrelendiği basit bir algoritmadır. 
    Bu yöntem, Jül Sezar tarafından M.Ö. 1. yüzyılda, orduları arasındaki iletişimi güvenli hale getirmek için geliştirilmiştir. 
    Sezar, düşmanlarının mesajları kolayca okuyamamasını sağlamak amacıyla, harflerin yerini belirli bir kaydırma değeriyle değiştiren bu yöntemi kullanmıştır.

    Örneğin, bir mesajdaki her harf 3 birim sağa kaydırılarak şifrelenebilir. Şifrelenmiş bir mesajı çözmek için ise aynı işlem 3 birim sola kaydırılarak orijinal haline döndürülür. 
    Bu, mesajların yalnızca belirli bir "anahtar" değerine sahip kişiler tarafından anlaşılmasını sağlar.

    **Tarihsel Arka Plan:** Jül Sezar, ordusunun Galya'daki (günümüz Fransa) seferleri sırasında bu yöntemi kullanmıştır. Askerler ve komutanlar arasındaki mesajlar, 
    Sezar’ın belirlediği anahtar (örneğin, 3) ile şifrelenerek gizli tutulmuştur. Bu basit ama etkili yöntem, dönemin düşmanlarının iletişimi kolayca deşifre etmesini engellemiştir.
    """)

    # Kullanım alanları
    st.write("**Kullanım Alanları:**")
    st.write("""
    - Ordular arası gizli iletişim
    - Basit şifreleme yöntemleri ile veri gizliliği sağlama
    - Günümüzde eğitimde şifreleme mantığını öğretmek için kullanılan örnek bir algoritma
    """)


    st.write("")
    st.write("")
    
    # Algoritmanın açıklaması
    st.markdown("<h4 style='color:#FF6347;'>Adım Adım Sezar Şifreleme</h4>", unsafe_allow_html=True)
    
    st.write("""
    1. 🔑**Anahtar Seçin**: Şifreleme işlemi için bir kaydırma değeri (örneğin, 3) belirleyin.
    2. 🔐**Şifreleme İşlemi**: Her harfi anahtar değeri kadar ileri kaydırın.
    3. 🔓**Çözme İşlemi**: Şifrelenmiş metni geri almak için her harfi anahtar değeri kadar geri kaydırın.
    """)
    
    st.write("")
    st.write("")
    
    # Algoritmanın nasıl çalıştığını açıklayan tablo
    st.markdown("<h5 style='color:#32CD32;'>🔡 Türkçe Alfabesi ve İndeksleme</h5>", unsafe_allow_html=True)
    alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
    alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    positions = list(range(29))  # Pozisyonlar
    
    table = pd.DataFrame({
        "Büyük Harf": list(alphabet_upper),
        "Küçük Harf": list(alphabet_lower),
        "İndeks": positions
    })
    st.dataframe(table, width=400)

    st.write("")
    st.write("")
    
    # Kullanıcı etkileşimi için örnek
    st.markdown("<h4 style='color:#FF6347;'>📝 Örnek Şifreleme İşlemi</h4>", unsafe_allow_html=True)
    st.write("Aşağıdaki örnekte, 'Merhaba Dünya' ifadesini 3 birim sağa kaydırarak nasıl şifrelediğimizi göreceksiniz.")

    # Örnek metin
    example_text = "Merhaba Dünya"
    example_key = 3
    st.write(f"**Girdi:** {example_text}")
    st.write(f"**Anahtar (Key):** {example_key}")
    
    # Şifrelenmiş örnek metin
    def caesar_cipher_encode(plaintext, key):
        alphabet_lower = "abcçdefgğhıijklmnoöprsştuüvyz"
        alphabet_upper = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
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

    st.write("")
    st.write("")
    
    # Önemli terimleri bilgi kutuları ile vurgulama
    st.markdown("<h4 style='color:#FFD700;'>⚠️ Önemli Terimler</h4>", unsafe_allow_html=True)
    st.info("**Anahtar (Key):** Şifreleme ve çözme işlemi için kullanılan kaydırma değeri.")
    st.info("**Şifrelenmiş Metin (Ciphertext):** Şifreleme algoritması ile dönüştürülmüş metin.")
    st.info("**Açık Metin (Plaintext):** Orijinal, şifrelenmemiş metin.")

    st.write("")
    st.write("")
    
    # Kullanıcı etkileşimi için alan
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

st.caption("📝 Eee Sezar'ın hakkı Sezar'a! 😆")

st.image("caesar_statue.jpeg", caption="Benden Bahsetmeyin LAN!", width=250)
