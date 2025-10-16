import streamlit as st
import requests

st.title("Anlık Hava Durumu")

sehir = st.text_input("Şehir adı girin")
api_key = "7a91bf30f06c2e345b1d6a21f322682c"

if st.button("Sorgula") and sehir:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr"
    r = requests.get(url)
    if r.status_code == 200:
        veri = r.json()
        st.write("Sıcaklık:", veri["main"]["temp"], "°C")
        st.write("Durum:", veri["weather"][0]["description"])
        st.write("Nem:", veri["main"]["humidity"])
    else:
        st.error("Şehir bulunamadı veya API anahtarı hatalı.")