import streamlit as st

st.title("Pratik's startup")

import streamlit as st
st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('photo.png')
with col2:
    st.header('I love quotes')

st.header('Courses')
st.subheader("DSA")
st.subheader("DBMS")
st.subheader("DSMP")
