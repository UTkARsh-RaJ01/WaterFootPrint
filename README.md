
# **Jal Rakshak - Water Footprint Calculator**

**Jal Rakshak** is an innovative web-based application that calculates the water footprint of agricultural and food products. It leverages advanced technologies like Machine Learning (ML), Blockchain, and real-time data visualization to provide accurate insights into the water usage of consumable items. The platform is designed to promote awareness about water conservation, empower consumers to make informed decisions, and help industries and farmers optimize water consumption.

---

## **Table of Contents**
- [Problem Statement](#problem-statement)
- [Proposed Solution](#proposed-solution)
- [Key Features](#key-features)
- [Technical Overview](#technical-overview)
- [Technologies Used](#technologies-used)
- [Usage](#usage)


---

## **Problem Statement**

With agriculture accounting for nearly 70% of global freshwater consumption, understanding water usage is critical for sustainability. Despite this, consumers and businesses often lack the necessary tools to calculate the water footprint of food products. Jal Rakshak addresses this problem by providing an intuitive platform that helps users calculate and visualize their water footprint, promoting sustainable practices in food consumption and production.

---

## **Proposed Solution**

**Jal Rakshak** is designed to:
- Provide water footprint estimations for agricultural and processed food items.
- Help users visualize the water footprint in terms of relatable metrics (e.g., the number of 1L water bottles).
- Empower users to make informed decisions based on regional water availability, thus encouraging sustainable consumption habits.
- Assist industries and farmers in optimizing water use by tracking and managing the water footprint of their products.
- Use blockchain for data transparency and security, ensuring that the water footprint data is accurate and trustworthy.

---

## **Key Features**

- **Water Footprint Calculator**: Users can search for a product, input the quantity, and receive a water footprint estimation.
- **Image-Based Classification**: Upload an image, and the app will classify the item and provide an estimated water footprint using Machine Learning models.
- **Net Daily Water Footprint Chart**: Users can create a custom basket of food items and view the total water footprint in a pie chart.
- **Multilingual Support**: Available in multiple Indian languages, making it accessible to rural and vernacular users.
- **Blockchain Integration**: Secure and transparent storage of water footprint data using the Ethereum blockchain.
  
---

## **Technical Overview**

### **Machine Learning Models**
Jal Rakshak uses three distinct ML models for classifying different types of food items:
- **VGG16** for vegetables: Fine-tuned to capture subtle details of vegetable textures.
- **ResNet50** for fruits: Handles complex textures, shapes, and colors with its deep architecture.
- **Transfer Learning Models (EfficientNet/MobileNet)** for crops: Transfer learning allows the model to generalize across diverse crop types using smaller datasets.

### **Web Application Development**
The front-end is built using **Streamlit** for fast prototyping and intuitive data visualization. The back-end uses **FastAPI** to integrate the ML models and handle user requests efficiently.

### **Blockchain Integration**
Water footprint data is securely stored and verified on the **Ethereum blockchain**, ensuring data integrity and transparency through the use of smart contracts.

### **Multilingual Support**
Integration with the **Google Translate API** allows the platform to support multiple Indian languages, enhancing accessibility for rural and vernacular users.

---

## **Technologies Used**

- **Frontend**: Streamlit, HTML, CSS, JavaScript
- **Backend**: FastAPI, Python
- **Machine Learning**: TensorFlow, Keras, OpenCV, Scikit-Learn, Numpy, Pandas
- **Blockchain**: Ethereum, Solidity
- **Data Storage and Processing**: MongoDB, Google Cloud Storage
- **APIs**: Google Translate API
- **Visualization**: Matplotlib, Plotly

---

## **Installation**

### **Prerequisites**
- Python 3.x
- Node.js
- TensorFlow and Keras libraries

### **Steps to Install**


1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**

1. **Search for Products**: Use the search bar to input a food item and get the water footprint.
2. **Image Classification**: Upload an image, and the ML models will classify the product and estimate its water footprint.
3. **Custom Basket**: Create a custom basket of items, calculate the total daily water footprint, and visualize it using pie charts.
4. **Blockchain Verification**: View the verified water footprint data stored on the Ethereum blockchain.

---

---

**Jal Rakshak** aims to provide a solution to the pressing issue of water scarcity by making water footprint data accessible, easy to understand, and actionable. Join us in making water conservation a global priority!

---

This GitHub README includes a comprehensive overview of the project, installation instructions, usage guidance, and technical details.
