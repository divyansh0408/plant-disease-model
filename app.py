#     # well working flask file
# from flask import Flask, request, jsonify, render_template
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image

# app = Flask(__name__)

# model = load_model('divyansh.h5')  
# class_names = ['healthy', 'powdery', 'rust']  

# # Define a route to render the HTML front-end
# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/get_started')
# def get_started():
#      return render_template('main.html')

# # Define a route to handle image upload and prediction
# @app.route('/predict', methods=['POST'])
# def predict():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'})

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'})

#     try:
#         # Open and preprocess the uploaded image
#         img = Image.open(file)
#         img = img.resize((64, 64))  # Resize image to match model input size
#         img_array = np.array(img) / 255.0  # Normalize image
#         img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#         # Predict class
#         predictions = model.predict(img_array)
#         predicted_class = class_names[np.argmax(predictions)]
#         confidence = np.max(predictions)

# #trial code here
#         if predicted_class=="healthy":
#             predicted_class="Healthy"
#         elif predicted_class=="rust":
#             predicted_class="Rusty"
#         elif predicted_class=="powdery":
#             predicted_class="Powdery"



#  #trial code ends here  
#         ## if trial code doesnt works then remove all the code between trial and directly run the return jsonify line below   

#         return jsonify({'class': predicted_class, 'confidence': float(confidence)})

#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)











    # well working flask file
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)

model = load_model('disease_detection_model.h5')  
class_names = ['American Bollworm on Cotton', 'Anthracnose on Cotton', 'Army worm', 'Becterial Blight in Rice', 'Brownspot', 'Common_Rust', 'Cotton Aphid', 'Flag Smut', 'Gray_Leaf_Spot', 'Healthy Maize', 'Healthy Wheat', 'Healthy cotton', 'Leaf Curl', 'Leaf smut', 'Mosaic sugarcane', 'RedRot sugarcane', 'RedRust sugarcane', 'Rice Blast', 'Sugarcane Healthy', 'Tungro', 'Wheat Brown leaf Rust', 'Wheat Stem fly', 'Wheat aphid', 'Wheat black rust', 'Wheat leaf blight', 'Wheat mite', 'Wheat powdery mildew', 'Wheat scab', 'Wheat___Yellow_Rust', 'Wilt', 'Yellow Rust Sugarcane', 'bacterial_blight in Cotton', 'bollrot on Cotton', 'bollworm on Cotton', 'cotton mealy bug', 'cotton whitefly', 'maize ear rot', 'maize fall armyworm', 'maize stem borer', 'pink bollworm in cotton', 'red cotton bug', 'thirps on  cotton']  


# Define a route to render the HTML front-end
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_started')
def get_started():
     return render_template('main.html')

# Define a route to handle image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    try:
        # Open and preprocess the uploaded image
        img = Image.open(file)
        img = img.resize((64, 64))  # Resize image to match model input size
        img_array = np.array(img) / 255.0  # Normalize image
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict class
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions)
        # disease_cure = disease_cures.get(predicted_class, "No cure information available.")


#trial code here
        if predicted_class == "American Bollworm on Cotton":
            predicted_class = "American Bollworm on Cotton"
        elif predicted_class == "Anthracnose on Cotton":
            predicted_class = "Anthracnose on Cotton"
        elif predicted_class == "Army worm":
            predicted_class = "Army Worm"
        elif predicted_class == "Becterial Blight in Rice":
            predicted_class = "Bacterial Blight in Rice"
        elif predicted_class == "Brownspot":
            predicted_class = "Brown Spot"
        elif predicted_class == "Common_Rust":
            predicted_class = "Common Rust"
        elif predicted_class == "Cotton Aphid":
            predicted_class = "Cotton Aphid"
        elif predicted_class == "Flag Smut":
            predicted_class = "Flag Smut"
        elif predicted_class == "Gray_Leaf_Spot":
            predicted_class = "Gray Leaf Spot"
        elif predicted_class == "Healthy Maize":
            predicted_class = "Healthy Maize"
        elif predicted_class == "Healthy Wheat":
            predicted_class = "Healthy Wheat"
        elif predicted_class == "Healthy cotton":
            predicted_class = "Healthy Cotton"
        elif predicted_class == "Leaf Curl":
            predicted_class = "Leaf Curl"
        elif predicted_class == "Leaf smut":
            predicted_class = "Leaf Smut"
        elif predicted_class == "Mosaic sugarcane":
            predicted_class = "Mosaic Sugarcane"
        elif predicted_class == "RedRot sugarcane":
            predicted_class = "Red Rot Sugarcane"
        elif predicted_class == "RedRust sugarcane":
            predicted_class = "Red Rust Sugarcane"
        elif predicted_class == "Rice Blast":
            predicted_class = "Rice Blast"
        elif predicted_class == "Sugarcane Healthy":
            predicted_class = "Healthy Sugarcane"
        elif predicted_class == "Tungro":
            predicted_class = "Tungro"
        elif predicted_class == "Wheat Brown leaf Rust":
            predicted_class = "Wheat Brown Leaf Rust"
        elif predicted_class == "Wheat Stem fly":
            predicted_class = "Wheat Stem Fly"
        elif predicted_class == "Wheat aphid":
            predicted_class = "Wheat Aphid"
        elif predicted_class == "Wheat black rust":
            predicted_class = "Wheat Black Rust"
        elif predicted_class == "Wheat leaf blight":
            predicted_class = "Wheat Leaf Blight"
        elif predicted_class == "Wheat mite":
            predicted_class = "Wheat Mite"
        elif predicted_class == "Wheat powdery mildew":
            predicted_class = "Wheat Powdery Mildew"
        elif predicted_class == "Wheat scab":
            predicted_class = "Wheat Scab"
        elif predicted_class == "Wheat___Yellow_Rust":
            predicted_class = "Wheat Yellow Rust"
        elif predicted_class == "Wilt":
            predicted_class = "Wilt"
        elif predicted_class == "Yellow Rust Sugarcane":
            predicted_class = "Yellow Rust Sugarcane"
        elif predicted_class == "bacterial_blight in Cotton":
            predicted_class = "Bacterial Blight in Cotton"
        elif predicted_class == "bollrot on Cotton":
            predicted_class = "Boll Rot on Cotton"
        elif predicted_class == "bollworm on Cotton":
            predicted_class = "Bollworm on Cotton"
        elif predicted_class == "cotton mealy bug":
            predicted_class = "Cotton Mealy Bug"
        elif predicted_class == "cotton whitefly":
            predicted_class = "Cotton Whitefly"
        elif predicted_class == "maize ear rot":
            predicted_class = "Maize Ear Rot"
        elif predicted_class == "maize fall armyworm":
            predicted_class = "Maize Fall Armyworm"
        elif predicted_class == "maize stem borer":
            predicted_class = "Maize Stem Borer"
        elif predicted_class == "pink bollworm in cotton":
            predicted_class = "Pink Bollworm in Cotton"
        elif predicted_class == "red cotton bug":
            predicted_class = "Red Cotton Bug"
        elif predicted_class == "thirps on  cotton":
            predicted_class = "Thrips on Cotton"




 #trial code ends here  
        ## if trial code doesnt works then remove all the code between trial and directly run the return jsonify line below   

        return jsonify({'class': predicted_class, 'confidence': float(confidence)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
