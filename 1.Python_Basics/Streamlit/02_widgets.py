import streamlit as st
st.title("Demo")
#button
x=st.button("Start")
if x:
    st.write("Test is a success.")
#checkbox
st.checkbox("Add hell")
#radio buttons
y=st.radio(" ",['1','2','3','4'])
st.write(f"{y} selected")

#slider
z=st.slider("Adjust slider: ",0,10,3)
st.write(f"Selected Level :{z}")

#custom input
p=st.number_input("Slect the no. of input :",min_value=1,max_value=10,step=1)
q=st.text_input("write your name :" )
st.write(f"given name : {q}")
dob=st.date_input("")
st.write(f"{dob}")

#IMAGES

st.image("C:/Users/Asus/OneDrive/Desktop/GENAI/Python_Basics/Streamlit/wallpaperflare.com_wallpaper (9).jpg")






