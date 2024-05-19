import streamlit as st
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
def nouns_maker(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    noun_list = []
    for token in tokens:
        if token.part_of_speech.split(",")[0] == ("名詞"):
            if token.surface not in omit_list:
                noun_list.append(token.surface)
    return(" ".join(noun_list))
st.sidebar.title("config")
width = st.sidebar.slider("width",0,1200,800,10)
height = st.sidebar.slider("height",0,1200,500,10)
theme = st.sidebar.selectbox("てーま",["PuBuGn","gist_heat","cubehelix"])
omit_words = st.sidebar.text_input("除外したいワードをスペース区切りで入れてね")
omit_list = omit_words.split(" ")
st.title("Wordcloud Maker")
text = st.text_area("入力欄",placeholder="ここにテキストを入力します")

if st.button("作成"):
    nouns = nouns_maker(text)
    wc = WordCloud(width=width,height=height,font_path="ipaexg.ttf",
                   collocations=False,colormap=theme)
    wc.generate(nouns)
    wc.to_file("test.png")
    st.image("test.png")


