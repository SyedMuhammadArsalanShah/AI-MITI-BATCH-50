import streamlit as st
import requests

st.title("Hadith Nabawi SAW")


meriHbooks=requests.get("https://hadithapi.com/api/books?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e")

allBooksDATA= meriHbooks.json()["books"]


options=[]

for b in allBooksDATA:
    options.append(f"{b["bookName"]} | {b["bookSlug"]}")


itemBook=st.selectbox("choose the H book",options)

bookSlug=itemBook.split(" | ")[1]

st.write(bookSlug)


meriHChapters =requests.get(f"https://hadithapi.com/api/{bookSlug}/chapters?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e")

allChapDATA= meriHChapters.json()["chapters"]


optionsChap=[]

for c in allChapDATA:
    optionsChap.append(f"{c["chapterNumber"]} | {c["chapterArabic"]} | {c["chapterUrdu"]}")


itemchap=st.selectbox("choose the Chapters",optionsChap)

chapterNO=itemchap.split(" | ")[0]


hadith= requests.get(f"https://hadithapi.com/api/hadiths/?apiKey=$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e&book={bookSlug}&chapter={itemchap}&paginate={100000}")



allHadith =hadith.json()["hadiths"]["data"]




for a in allHadith:
    st.title(a["hadithNumber"])
    st.info(a["hadithArabic"])
    st.success(a["hadithUrdu"])
    st.warning(a["hadithEnglish"])





