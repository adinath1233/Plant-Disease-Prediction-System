# Plant Disease Prediction System

## Project Overview
This project predicts plant diseases based on an input image of a plant or leaf. The system uses a machine learning model to identify diseases and provides:
- The name of the disease.
- A description of how the disease occurs.
- Suggestions on how to prevent or treat the disease.

The project is a **prototype** created for academic purposes to demonstrate the application of computer vision in agriculture.

## Diseases Predicted
The system can predict the following plant diseases:

### Apple
- Apple___Apple_scab
- Apple___Black_rot
- Apple___Cedar_apple_rust
- Apple___healthy

### Blueberry
- Blueberry___healthy

### Cherry (including sour)
- Cherry_(including_sour)__Powdery_mildew
- Cherry_(including_sour)___healthy

### Corn (maize)
- Corn_(maize)__Cercospora_leaf_spot Gray_leaf_spot
- Corn_(maize)_Common_rust
- Corn_(maize)__Northern_Leaf_Blight
- Corn_(maize)___healthy

### Grape
- Grape___Black_rot
- Grape___Esca_(Black_Measles)
- Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
- Grape___healthy

### Orange
- Orange___Haunglongbing_(Citrus_greening)

### Peach
- Peach___Bacterial_spot
- Peach___healthy

### Pepper (bell)
- Pepper,_bell___Bacterial_spot
- Pepper,_bell___healthy

### Potato
- Potato___Early_blight
- Potato___Late_blight
- Potato___healthy

### Raspberry
- Raspberry___healthy

### Soybean
- Soybean___healthy

### Squash
- Squash___Powdery_mildew

### Strawberry
- Strawberry___Leaf_scorch
- Strawberry___healthy

### Tomato
- Tomato___Bacterial_spot
- Tomato___Early_blight
- Tomato___Late_blight
- Tomato___Leaf_Mold
- Tomato___Septoria_leaf_spot
- Tomato___Spider_mites_Two-spotted_spider_mite
- Tomato___Target_Spot
- Tomato___Tomato_Yellow_Leaf_Curl_Virus
- Tomato___Tomato_mosaic_virus
- Tomato___healthy

## System Requirements
- **Anaconda Environment** with Python 3.10 version
- **Required Libraries**: All dependencies are specified in the `requirements.txt` file.

## Installation Instructions

1. **Create a Conda environment** with Python 3.10:
    ```bash
    conda create --name plant-disease-prediction python=3.10
    ```

2. **Activate the Conda environment**:
    ```bash
    conda activate plant-disease-prediction
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirments.txt
    ```

4. **Run the Flask application**:
    ```bash
    python app.py
    ```

    This will start the Flask server, and you can access the application in your browser at `http://127.0.0.1:5000`.

## Dataset Information
The dataset used for training the model is available on Kaggle. It contains images of various plants and their respective diseases, enabling the model to accurately identify diseases based on image input.

- **Dataset source**: [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

## Credits

- **Model**: The model used in this project is based on **PyTorch ResNet**, a widely used deep learning architecture for image classification tasks.
- **Dataset**: [New Plant Diseases Dataset on Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset).
- This project was created for academic purposes to demonstrate plant disease prediction using machine learning and Flask.

## License

This project is for academic purposes only. The PyTorch ResNet model has been used as the foundation for disease prediction and is credited to the PyTorch development team and contributors. Use of this project for commercial purposes is not permitted without proper permissions.
