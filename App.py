#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import joblib
import category_encoders as ce

# Set the app title and background
st.set_page_config(page_title="Credit Guard Pro", page_icon="🔒")

# Define the background image within a div and set it to cover the entire page
# Define the HTML structure and CSS for your app


# Load the pre-trained model
model = joblib.load("random_forest_model.pkl")  # Replace with the actual filename
print(model)

# Streamlit app content
st.title("Credit Guard Pro 🔐")

dataset = pd.read_csv("Dataset/credit_card_subset.csv")
training_dataset = pd.read_csv("filtered_dataset.csv")

# Streamlit App
def main():
    st.write("CreditGuard Pro is your go-to solution for safeguarding your credit card transactions. Our advanced model is designed to meticulously spot potential fraud, ensuring your financial peace of mind. Simply input transaction details, and CreditGuard Pro will provide you with an instant prediction: Fraudulent or Legitimate.")
    st.write("Embrace financial security like never before, with the power of AI in your pocket. Trust CreditGuard Pro to keep your transactions secure and your finances in check!")
    st.divider()
    st.write(':blue[_📝 Fill in the Details: Click the left sidebar to enter the required information._]')
    #st.divider()
    st.write("_🔍 Predict Fraud Status: To reveal the prediction for the transaction's fraud status, click the button below :red[after you've provided the necessary information.]_")

    # Sidebar with user inputs
    st.sidebar.header("Enter The Transaction Details", divider="violet")

    # Extract a specific column from the dataset for the dropdown
    column_name = 'merchant'  # Replace with the name of the column you want to use
    data_values_merchant = dataset[column_name].unique()

    column_name = 'category'  # Replace with the name of the column you want to use
    data_values_category = dataset[column_name].unique()

    column_name = 'job'  # Replace with the name of the column you want to use
    data_values_job = dataset[column_name].unique()

    column_name = 'state'  # Replace with the name of the column you want to use
    data_values_state = dataset[column_name].unique()

    column_name = 'city'  # Replace with the name of the column you want to use
    data_values_city = dataset[column_name].unique()

    # Collect user input
    def user_input_features():
        merchant = st.sidebar.selectbox('Merchant', data_values_merchant)
        category = st.sidebar.selectbox('Category', data_values_category)
        job = st.sidebar.selectbox('Job', data_values_job)
        state = st.sidebar.selectbox('State', data_values_state)
        city = st.sidebar.selectbox('City', data_values_city)
        age = st.sidebar.number_input('Age', min_value=0, max_value=120, value=30, placeholder="Type an age...")
        amount = st.sidebar.number_input('Amount', min_value=0.0, placeholder="Type the amount...")

        # Create a dictionary for user input
        user_input = {
            'merchant': merchant,
            'category': category,
            'job': job,
            'age': age,
            'state': state,
            'city': city,
            'amount': amount,
        }

        return user_input

    user_input = user_input_features()  # Call the function to get user input

    user_data = pd.DataFrame([user_input])
    categorical_columns = ['merchant', 'category', 'job', 'state', 'city']
    encoder = ce.BinaryEncoder(cols=categorical_columns)
    encoder.fit(training_dataset)
    encoded_data = encoder.transform(user_data)

    # Button to trigger predictions
    if st.button("Predict"):
        # Prepare the input data based on your model's requirements
        prediction = model.predict(encoded_data)

        if prediction[0] == 0:
            st.success('This transaction entered is NON-FRAUDULENT! ✅')
            st.write('Model Accuracy : 99.5%')
        elif prediction[0] == 1:
            st.error('This transaction entered is FRAUDULENT! 🚨')
            st.write('Model Accuracy : 99.5%')
        else:
            st.warning('Unknown Prediction! ⚠️')

if __name__ == '__main__':
    main()


# In[ ]:




