#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pip install streamlit


# In[1]:


#pip install joblib


# In[4]:


import streamlit as st
import joblib
import pandas as pd
import category_encoders as ce

# Load the pre-trained model
model = joblib.load("random_forest_model.pkl")  # Replace with the actual filename
print(model)


# Define the background image CSS with a relative path
background = """
<style>
body {
    background-image: url("https://d1m75rqqgidzqn.cloudfront.net/wp-data/2021/09/22153728/iStock-1203763961.jpg");
    background-size: cover;
    background-attachment: fixed;
}
</style>
"""

# Set the app title and background
st.set_page_config(page_title="Credit Card Fraud Detection App", page_icon="🔒")
# Apply the background using st.markdown
st.markdown(background, unsafe_allow_html=True)

# Streamlit app content
st.title("Credit Card Fraud Detection App")

dataset=pd.read_csv("Dataset/credit_card_subset.csv")
# Load your dataset using Pandas (replace 'your_data.csv' with your actual file)
preprocessed_dataset = pd.read_csv("cleaned_dataset.csv")
filtered_dataset = pd.read_csv("filtered_dataset.csv")
# Extract a specific column from the dataset for the dropdown
column_name = 'merchant'  # Replace with the name of the column you want to use
data_values_merchant = dataset[column_name].unique()

# Create a dropdown using st.selectbox
merchant = st.selectbox("Merchant", data_values_merchant)
st.write("You selected:", merchant)

# Extract a specific column from the dataset for the dropdown
column_name = 'category'  # Replace with the name of the column you want to use
data_values_category = dataset[column_name].unique()

# Create a dropdown using st.selectbox
category = st.selectbox("Category", data_values_category)
st.write("You selected:", category)

# Extract a specific column from the dataset for the dropdown
column_name = 'job'  # Replace with the name of the column you want to use
data_values_job = dataset[column_name].unique()

# Create a dropdown using st.selectbox
job = st.selectbox("Job", data_values_job)
st.write("You selected:", job)

# Extract a specific column from the dataset for the dropdown
column_name = 'state'  # Replace with the name of the column you want to use
data_values_state = dataset[column_name].unique()

# Create a dropdown using st.selectbox
state = st.selectbox("State", data_values_state)
st.write("You selected:", state)

# Extract a specific column from the dataset for the dropdown
column_name = 'city'  # Replace with the name of the column you want to use
data_values_city = dataset[column_name].unique()

# Create a dropdown using st.selectbox
city = st.selectbox("City", data_values_city)
st.write("You selected:", city)

age = st.number_input("Age", min_value=0, max_value=120, value=30, placeholder="Type an age...")
st.write('The current age is ', age)

amount = st.number_input('Amount')
st.write('The current amount is ', amount)

# Capture user inputs
user_input = {
    'city': city,
    'state': state,
    'job': job,
    'merchant': merchant,
    'category': category,
    'amount': amount,
    'age': age,
}
# Create a DataFrame with user input
user_data = pd.DataFrame([user_input])

# Create a binary encoder for categorical columns
categorical_columns = ['city', 'state', 'job', 'merchant', 'category']  # Update with columns from your preprocessed dataset
encoder = ce.BinaryEncoder(cols=categorical_columns)

# Fit the encoder on your training data (assuming 'filtered' is your training dataset)
# Assuming you already have your 'filtered' DataFrame with your training data
encoder.fit(filtered_dataset)
# Apply the same encoder to the user input
user_data_encoded = encoder.transform(user_data)

# Make predictions using the loaded model
if st.button("Predict"):
     # Prepare the input data based on your model's requirements
    prediction = model.predict(user_data_encoded)
    st.write("Prediction:", prediction[0])


# In[ ]:




