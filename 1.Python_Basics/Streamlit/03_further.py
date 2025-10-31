import streamlit as st 

st.title("Vote for the Empowerment of this country.")
x=0
y=0
col1,col2=st.columns(2)

with col1:
    st.header("VOTE BJP")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Bharatiya_Janata_Party_%28icon%29.svg/1159px-Bharatiya_Janata_Party_%28icon%29.svg.png",width=200)
    v1=st.button("Vote BJP")
with col2:
    st.header("VOTE CONGRESS")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Indian_National_Congress_hand_logo.svg/2048px-Indian_National_Congress_hand_logo.svg.png",width=200)
    v2=st.button("Vote Congress")

if v1:
    x+=1
    st.write(f"Thanks for voting BJP.")
if v2:
    y+=1
    st.write(f"Thanks for voting CONGRESS.")

result=st.button("Result")
if result:
    if(x>y):
        st.success("BJP wins")
    else:
        st.success("Congess Wins!!")