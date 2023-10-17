#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit


# In[2]:


#pip install joblib


# In[3]:


import streamlit as st
import joblib  # Import joblib to load the model

# Load the pre-trained model
model = joblib.load("random_forest_model.pkl")  # Replace with the actual filename

# Streamlit app title
st.title("Model-Specific Streamlit App")

# Add user input fields (customize based on your model's input requirements)
user_input = st.number_input("Input Feature", value=0.0)

# Make predictions using the loaded model
if st.button("Predict"):
    input_data = [user_input]  # Prepare the input data based on your model's requirements
    prediction = model.predict(input_data)
    st.write("Prediction:", prediction[0])


# In[ ]:




