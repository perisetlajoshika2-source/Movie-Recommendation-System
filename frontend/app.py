import streamlit as st
import requests

st.title("Movie Recommendation System")

movie = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    response = requests.post(
        "http://127.0.0.1:8000/recommend",
        json={"title": movie}
    )

    result = response.json()

    st.subheader("Recommended Movies")

    for m in result["recommendations"]:
        st.write(m)