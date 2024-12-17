import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from PIL import Image

# Load the model
model = load_model('divyansh.h5')  # Path to your trained model

# Define the class names (Adjust according to your dataset)
class_names = ['healthy', 'powdery', 'rust']

# Set up the Streamlit app layout
st.title('Plant Leaf Disease Detection')
st.write('Upload a plant leaf image to check if it is healthy, has powdery mildew, or rust.')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    img = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    
    # Preprocess the image before prediction
    img = img.resize((64, 64))  # Resize to match input shape (64, 64)
    img_array = np.array(img)  # Convert image to numpy array
    img_array = img_array / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict the class of the image
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]  # Get the class with the highest probability



    st.write(f'This is a {predicted_class} leaf ')
