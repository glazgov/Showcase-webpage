import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Marcin Jusiński")
    content = """
    Hi, i Am Marcin and here is my project showcase website
    """

    st.info(content)


content2 = """
You can find them below
"""
st.write(content2)