# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Türkçe ve İngilizce alfabeler
alphabet_tr = {
    "upper": "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ",
    "lower": "abcçdefgğhıijklmnoöprsştuüvyz",
    "length": 29
}

alphabet_en = {
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "length": 26
}

# Varsayılan dil (default language)
if "language" not in st.session_state:
    st.session_state.language = "tr"  # Türkçe

# Dil seçimi (Language selection)
with st.sidebar:
    st.header("Dil Seçin / Choose Language")
    if st.button("Türkçe"):
        st.session_state.language = "tr"
    if st.button("English"):
        st.session_state.language = "en"

# Alfabe seçimi
lang = st.session_state.language
alphabet = alphabet_tr if lang == "tr" else alphabet_en

# Şifreleme fonksiyonu
def caesar_cipher_encode(plaintext, key, alphabet):
    ciphertext = []
    for char in plaintext:
        if char in alphabet["lower"]:
            new_position = (alphabet["lower"].index(char) + key) % alphabet["length"]
            ciphertext.append(alphabet["lower"][new_position])
        elif char in alphabet["upper"]:
            new_position = (alphabet["upper"].index(char) + key) % alphabet["length"]
            ciphertext.append(alphabet["upper"][new_position])
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

# Çözme fonksiyonu
def caesar_cipher_decode(ciphertext, key, alphabet):
    plaintext = []
    for char in ciphertext:
        if char in alphabet["lower"]:
            original_position = (alphabet["lower"].index(char) - key) % alphabet["length"]
            plaintext.append(alphabet["lower"][original_position])
        elif char in alphabet["upper"]:
            original_position = (alphabet["upper"].index(char) - key) % alphabet["length"]
            plaintext.append(alphabet["upper"][original_position])
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Başlık ve açıklama
st.title("Sezar Şifreleme (Caesar Cipher)" if lang == "tr" else "Caesar Cipher")
st.write("Metinlerinizi güvenli bir şekilde şifreleyin veya şifrelerini çözün!" if lang == "tr" else "Encrypt or decrypt your messages securely!")

# Yan sekmeler oluştur
tab1, tab2, tab3 = st.tabs(
    ["Sezar Şifreleme Algoritması", "Şifreleme (Encode)", "Çözme (Decode)"] if lang == "tr" else 
    ["What is Caesar Cipher?", "Encrypt", "Decrypt"]
)

# Açıklama Sekmesi
with tab1:
    # Renkli bir başlık ve görsel
    st.markdown(
        "<h3 style='color:#4A90E2;'>Sezar Şifreleme Algoritması Nedir?</h3>" if lang == "tr" else 
        "<h3 style='color:#4A90E2;'>What is Caesar Cipher?</h3>", 
        unsafe_allow_html=True
    )
    # Görsel ekleme (Sezar Çarkı)
    st.image("caesar_cipher_ring.jpeg", caption="Sezar Şifreleme Algoritması'nın Tarihsel Sembolü" if lang == "tr" else "Historical Symbol of Caesar Cipher", width=250)

    # Giriş açıklaması
    st.write("""
        Sezar Şifreleme, harflerin belirli bir kaydırma sayısına göre ileri veya geri alınarak şifrelendiği basit bir algoritmadır.
        Bu yöntem, Jül Sezar tarafından M.Ö. 1. yüzyılda, orduları arasındaki iletişimi güvenli hale getirmek için geliştirilmiştir.
        Sezar, düşmanlarının mesajları kolayca okuyamamasını sağlamak amacıyla, harflerin yerini belirli bir kaydırma değeriyle değiştiren bu yöntemi kullanmıştır.

        Örneğin, bir mesajdaki her harf 3 birim sağa kaydırılarak şifrelenebilir. Şifrelenmiş bir mesajı çözmek için ise aynı işlem 3 birim sola kaydırılarak orijinal haline döndürülür.
        Bu, mesajların yalnızca belirli bir "anahtar" değerine sahip kişiler tarafından anlaşılmasını sağlar.

        **Tarihsel Arka Plan:** Jül Sezar, ordusunun Galya'daki (günümüz Fransa) seferleri sırasında bu yöntemi kullanmıştır. Askerler ve komutanlar arasındaki mesajlar,
        Sezar’ın belirlediği anahtar (örneğin, 3) ile şifrelenerek gizli tutulmuştur. Bu basit ama etkili yöntem, dönemin düşmanlarının iletişimi kolayca deşifre etmesini engellemiştir.""" if lang == "tr" else 
        """
        Caesar Cipher is a simple algorithm where letters are encrypted by shifting them forward or backward by a specific number of positions.
        This method was developed by Julius Caesar in the 1st century BC to secure communication among his armies.
        Caesar used this technique, which involved replacing letters with others shifted by a specific value, to ensure that enemies could not easily read the messages.

        For example, each letter in a message can be encrypted by shifting it 3 positions to the right. To decrypt an encoded message, the same process can be applied by shifting 3 positions to the left, restoring it to its original form.
        This ensures that the messages can only be understood by those with the correct “key” value.

        **Historical Background:** Julius Caesar employed this method during his campaigns in Gaul (modern-day France). Messages between soldiers and commanders were encrypted using a key (e.g., 3) determined by Caesar to keep them confidential. This simple yet effective technique prevented the enemies of the time from easily deciphering the communications.
        """)

    # Kullanım alanları
    st.write("**Kullanım Alanları:**" if lang == "tr" else "**Use Cases:**")
    st.write("""
        - Ordular arası gizli iletişim
        - Basit şifreleme yöntemleri ile veri gizliliği sağlama
        - Eğitimde şifreleme mantığını öğretmek için kullanılan örnek bir algoritma
    """ if lang == "tr" else 
    """
        - Secure communication between armies
        - Simple encryption to ensure data privacy
        - Educational purposes to teach the concept of encryption
    """)
    
    st.write("")
    st.write("")

    # Algoritmanın açıklaması
    st.markdown("<h4 style='color:#FF6347;'>Adım Adım Sezar Şifreleme</h4>" if lang == "tr" else "<h4 style='color:#FF6347;'>Step-by-Step Caesar Cipher</h4>", unsafe_allow_html=True)

    st.write("""
    1. 🔑**Anahtar Seçin**: Şifreleme işlemi için bir kaydırma değeri (örneğin, 3) belirleyin.
    2. 🔐**Şifreleme İşlemi**: Her harfi anahtar değeri kadar ileri kaydırın.
    3. 🔓**Çözme İşlemi**: Şifrelenmiş metni geri almak için her harfi anahtar değeri kadar geri kaydırın.""" if lang == "tr" else 
    """
    1. 🔑**Choose a Key**: Select a shift value (e.g., 3) for the encryption process.
    2. 🔐**Encryption Process**: Shift each character forward by the key value.
    3. 🔓**Decryption Process**: Retrieve the original text by shifting each character backward by the key value.""")

    st.write("")
    st.write("")

    
    # Algoritmanın nasıl çalıştığını açıklayan tablo
    st.markdown(
    "<h5 style='color:#32CD32;'>🔡 Türkçe Alfabesi ve İndeksleme</h5>" if lang == "tr" else 
    "<h5 style='color:#32CD32;'>🔡 Alphabet and Indexing</h5>", 
    unsafe_allow_html=True
    )

    # Alfabe ve indeks bilgileri dil seçimine göre ayarlanıyor
    alphabet_lower = alphabet["lower"]
    alphabet_upper = alphabet["upper"]
    positions = list(range(alphabet["length"]))  # Pozisyonlar

    # Tabloyu oluşturma
    table = pd.DataFrame({
    "Büyük Harf" if lang == "tr" else "Uppercase": list(alphabet_upper),
    "Küçük Harf" if lang == "tr" else "Lowercase": list(alphabet_lower),
    "İndeks" if lang == "tr" else "Index": positions
    })

    # Tabloyu gösterme
    st.dataframe(table, width=400)

    st.write("")
    st.write("")


    # Kullanıcı etkileşimi için örnek
st.markdown(
    "<h4 style='color:#FF6347;'>📝 Örnek Şifreleme İşlemi</h4>" if lang == "tr" else 
    "<h4 style='color:#FF6347;'>📝 Example Encryption Process</h4>",
    unsafe_allow_html=True
)

st.write(
    "Aşağıdaki örnekte, 'Merhaba Dünya' ifadesini 3 birim sağa kaydırarak nasıl şifrelediğimizi göreceksiniz."
    if lang == "tr" else
    "In the example below, see how the phrase 'Hello World' is shifted 3 units to the right."
)

# Örnek metin ve anahtar
example_text = "Merhaba Dünya" if lang == "tr" else "Hello World"
example_key = 3
st.write(f"**{'Girdi' if lang == 'tr' else 'Input'}:** {example_text}")
st.write(f"**{'Anahtar (Key)' if lang == 'tr' else 'Key'}:** {example_key}")

# Şifrelenmiş örnek metin
def caesar_cipher_encode(plaintext, key, alphabet_lower, alphabet_upper):
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

encrypted_example = caesar_cipher_encode(
    example_text,
    example_key,
    alphabet["lower"],
    alphabet["upper"]
)
st.write(f"**{'Şifrelenmiş Metin' if lang == 'tr' else 'Encrypted Text'}:** {encrypted_example}")

st.write("")
st.write("")

# Önemli terimleri bilgi kutuları ile vurgulama
st.markdown(
    "<h4 style='color:#FFD700;'>⚠️ Önemli Terimler</h4>" if lang == "tr" else 
    "<h4 style='color:#FFD700;'>⚠️ Important Terms</h4>", 
    unsafe_allow_html=True
)

st.info("**Anahtar (Key):** Şifreleme ve çözme işlemi için kullanılan kaydırma değeri." if lang == "tr" else 
        "**Key:** The value used for encoding and decoding.")
st.info("**Şifrelenmiş Metin (Ciphertext):** Şifreleme algoritması ile dönüştürülmüş metin." if lang == "tr" else 
        "**Ciphertext:** The text transformed by the encryption algorithm.")
st.info("**Açık Metin (Plaintext):** Orijinal, şifrelenmemiş metin." if lang == "tr" else 
        "**Plaintext:** The original, unencrypted text.")

st.write("")
st.write("")

# Kullanıcı etkileşimi için alan
st.markdown(
    "<h4 style='color:#FF6347;'>🧪 Deneme Alanı: Şifreleme ve Çözme İşlemini Kendiniz Deneyin</h4>" if lang == "tr" else 
    "<h4 style='color:#FF6347;'>🧪 Try It Yourself: Encrypt and Decrypt</h4>",
    unsafe_allow_html=True
)

# Kullanıcıdan metin girişi
user_text = st.text_input(
    "Şifrelemek istediğiniz metni buraya yazın:" if lang == "tr" else 
    "Enter the text you want to encrypt here:", 
    "Merhaba Dünya" if lang == "tr" else "Hello World"
)
user_key = st.number_input(
    "Anahtar (Key) değeri seçin:" if lang == "tr" else 
    "Select the Key value:", 
    min_value=1, 
    max_value=alphabet["length"], 
    value=3, 
    step=1
)

if st.button("Şifrele ve İndeksleri Göster" if lang == "tr" else "Encrypt and Show Indices"):
    encrypted_user_text = caesar_cipher_encode(user_text, user_key, alphabet["lower"], alphabet["upper"])

    # Şifrelenmiş metni ve indeksleri göster
    indices_original = [
        (alphabet["lower"].index(char.lower()) if char.lower() in alphabet["lower"] else -1)
        for char in user_text
    ]
    indices_encrypted = [
        (alphabet["lower"].index(char.lower()) + user_key) % alphabet["length"] 
        if char.lower() in alphabet["lower"] else -1
        for char in user_text
    ]

    st.write(f"**{'Şifrelenmiş Metin' if lang == 'tr' else 'Encrypted Text'}:** {encrypted_user_text}")
    st.write("### İndeksler" if lang == "tr" else "### Indices")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Orijinal Karakterler**" if lang == "tr" else "**Original Characters**")
        st.write(list(user_text))
    with col2:
        st.write("**Orijinal İndeksler**" if lang == "tr" else "**Original Indices**")
        st.write(indices_original)
    with col3:
        st.write("**Şifrelenmiş İndeksler**" if lang == "tr" else "**Encrypted Indices**")
        st.write(indices_encrypted)

# Emoji ile alt bilgi
st.caption("🔍 Sezar Şifreleme yöntemi tarih boyunca basit güvenlik önlemleri için yaygın olarak kullanılmıştır." if lang == "tr" else 
           "🔍 The Caesar cipher has historically been used as a simple security measure.")


# Şifreleme Sekmesi
with tab2:
    st.header("🔒 Şifreleme Paneli" if lang == "tr" else "🔒 Encryption Panel")
    plaintext = st.text_area(
        "Şifrelemek istediğiniz metni buraya yazın:" if lang == "tr" else 
        "Enter the text you want to encrypt here:",
        placeholder="Metninizi buraya yazın..." if lang == "tr" else 
        "Enter your text here..."
    )
    key = st.number_input(
        "Anahtar (key) değeri girin:" if lang == "tr" else 
        "Enter the key value:",
        min_value=1, 
        max_value=alphabet["length"], 
        value=3, 
        step=1
    )
    if st.button("Şifrele" if lang == "tr" else "Encrypt", key="encrypt_button"):
        if plaintext.strip():
            encrypted_text = caesar_cipher_encode(plaintext, key, alphabet["lower"], alphabet["upper"])
            st.success(f"**{'Şifrelenmiş Metin' if lang == 'tr' else 'Encrypted Text'}:** {encrypted_text}")
        else:
            st.warning(
                "Lütfen şifrelemek için bir metin girin." if lang == "tr" else 
                "Please enter some text to encrypt."
            )

# Çözme Sekmesi
with tab3:
    st.header("🔓 Çözme Paneli" if lang == "tr" else "🔓 Decryption Panel")
    ciphertext = st.text_area(
        "Çözmek istediğiniz şifreli metni buraya yazın:" if lang == "tr" else 
        "Enter the encrypted text you want to decrypt here:",
        placeholder="Şifreli metni buraya yazın..." if lang == "tr" else 
        "Enter the encrypted text here..."
    )
    key = st.number_input(
        "Anahtar (key) değeri girin:" if lang == "tr" else 
        "Enter the key value:",
        min_value=1, 
        max_value=alphabet["length"], 
        value=3, 
        step=1, 
        key="decode_key"
    )
    if st.button("Çöz" if lang == "tr" else "Decrypt", key="decrypt_button"):
        if ciphertext.strip():
            decrypted_text = caesar_cipher_decode(ciphertext, key, alphabet["lower"], alphabet["upper"])
            st.success(f"**{'Çözümlenmiş Metin' if lang == 'tr' else 'Decrypted Text'}:** {decrypted_text}")
        else:
            st.warning(
                "Lütfen çözmek için bir şifreli metin girin." if lang == "tr" else 
                "Please enter some encrypted text to decrypt."
            )

# Alt bilgi
st.write("---")
st.caption(
    "Sezar Şifreleme ve Çözme Aracı - Güvenli ve Eğlenceli! " if lang == "tr" else 
    "Caesar Cipher Tool - Secure and Fun!"
)
st.caption(
    "📝 Eee Sezar'ın hakkı Sezar'a! 😆" if lang == "tr" else 
    "📝 Give Caesar what belongs to Caesar! 😆"
)

