# Layouts 
# st.title("Chai taste polls")
# col1, col2 = st.columns(2)
# with col1:
#     st.header("Masala Chai")
#     st.image("https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Findian-tea&ved=0CBcQjRxqFwoTCNDg4JSyy5cDFQAAAAAdAAAAABAH&opi=89978449", width=200)
#     vote1 = st.button("Vote Masala Chai")
# with col2:
#     st.header("Green Tea")
#     vote2 = st.button("Vte Green Tea")
# if vote1:
#     st.success("Thanks for voting")
# elif vote2:
#     st.success("Thanks for vooting")
# name = st.sidebar.text_input("ENter your name")
# tea = st.sidebar.selectbox("Chose your chai", ["Masala", "Green"])
# st.write(f"Welcome {name} and you {tea} is ready")

# with st.expander("Show chai making instructions"):
#     st.write("1. Boil water with tea leaves 2. add milk and spices 3. serve hot" )
# st.markdown('### welcome')
# st.markdown('## welcome')
# st.markdown('# welcome')
# st.markdown('> Blockquote')

# VISUALIZATION USING STREAMLIT
# import pandas as pd
# st.title("Chai sales")
# file = st.file_uploader("upload your file", type=["csv"])

# if file:
#     df = pd.read_csv(file)
#     st.subheader("Data Review")
#     st.dataframe(df)

# if file:
#     st.subheader("SUmmary")
#     st.write(df.describe()) 
# if file:
#     unique = df["restingBP"].unique()
#     box = st.selectbox("filter by resting bp", unique)
#     filtered_data = df[df["restingBP"] == box]
#     st.dataframe(filtered_data) # to display the data frame





# # WEB REQ
# import streamlit as st
# import requests

# st.title("Live currency Converter")
# amount = st.number_input("Enter the amount in INR", min_value=1)
# target_currency = st.selectbox("Covert to", ["USD", "Euro", "Yen", "CHF"])

# if st.button("COnvert"):
#     url =   "https://www.oanda.com/currency-converter/en/?from=EUR&to=USD&amount=1"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         # rate = data["column_name"][target_currency]
#         # converted = rate * amount
#         # st.success(f"{amount} INR = {converted:.2f} {target_currency}")
#     else:
#         st.error("Failed to convert Data")