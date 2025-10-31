import streamlit as st 
import datetime
st.title("Age Calculator")
st.subheader("You can now calculate your age ")
today=datetime.date.today()
dob=st.date_input("Enter your Date: ")
z=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
st.write(f"You are {z} years old. Happy Living.")