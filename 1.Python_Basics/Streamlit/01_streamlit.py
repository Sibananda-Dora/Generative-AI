import streamlit as st

st.title("Language Picker")
# st.subheader("Good Morning !")
st.text("Choose a Programming Language from the Dropdown Menu.")
st.write("Choose : ")
#dropdown box
x=st.selectbox(" ",['','Python','C','C++','js'])
st.write(f'Nice!! You have selected {x}.')

st.success("You are good to go !")
