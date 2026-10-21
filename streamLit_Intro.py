# TO RUN IT ON BOWSER streamlit run /Users/rishidevpande/Desktop/ODE_Gold_NP/streamLit_Intro.py
# TO TERMINATE THE TERMINAL control + c


# import streamlit as st
# st.title("Hello!")
# st.subheader("On Streamlit")
# st.text("First SL App")
# st.write("Chose Your Data")
# s = st.selectbox("Your Value", ["A", "B", "C", "D"])
# st.write(f"You Chose {s} Nice Choice")
# st.success("Success")


# Streamlit program to select your fav lang
# st.title("Your Fav Prog Lang")
# st.write("Choose Your Lang")
# s = st.selectbox("Your Options", ["R", "C++", "Java", "Python", "Ocaml"])
# st.write(f"Your choice {s} is excellent")
# st.success("Lets Goo")


import streamlit as st
st.title("chai maker app")
if st.button("Make chai"):
    st.success("Your Chai is being brewed")
add = st.checkbox("Add Masala")
if add:
    st.write("Masala Added")

tea_type = st.radio("Pick your chai base", ["Milk", "Water", "Honey"])
st.write(f"Selected Base {tea_type}")
flavour = st.selectbox("Chose Flavour: ", ["adrak", "kesar", "elaichi", "neem"])
st.write(f"Selected Flavour {flavour}")
sugar = st.slider("Sugar level", 0, 5, 2) # 2 is the default value
st.write(f"the spoon of sugar {sugar}")

cups = st.number_input("How many cups? ", min_value=0, max_value=10, step=1)
st.write(f"The cups are {cups}")
name = st.text_input("Enter Your Name")
if name:
    st.write(f"Welcome {name} your chai is on the way")

dob = st.date_input("Select Your DOB")
st.write(f"DOB is {dob} Happy Birthday")
