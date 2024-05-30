# Title: Online Payment Fraud Detection using Machine Learning

# Overview:

This project is a web application for detecting fraudulent online payments using a machine learning model. It leverages Flask for the web interface and a pre-trained machine learning model to predict whether a given transaction is fraudulent or not.

# Background:

In the digital age, the prevalence of online payments has increased significantly, providing convenience and efficiency in transactions. However, this surge in online transactions has also led to a rise in fraudulent activities. Detecting fraudulent transactions is crucial for financial institutions and businesses to protect their customers and maintain trust.

# Objective:

The objective of this project is to develop a machine learning-based web application that can accurately detect fraudulent online payment transactions. The application should provide an easy-to-use interface where users can input transaction details and receive real-time predictions on whether the transaction is fraudulent or not.

# Phases:

1. Data Collection and Preprocessing:

Use a pre-existing dataset containing transaction details and labels indicating fraudulent or non-fraudulent transactions.
Preprocess the data to make it suitable for training a machine learning model.

2. Model Training:

Train a machine learning model using the preprocessed data.
Evaluate the model to ensure it has acceptable accuracy and performance metrics.

3. Web Application Development:

Develop a web interface using Flask where users can input transaction details.
Integrate the trained machine learning model to make predictions based on user inputs.
Display the prediction results clearly to the user.

# Features

1. User Input Form: A web form to collect transaction details, including payment type, amount, old balance, and new balance for both the origin and destination accounts.
2. Prediction Result: Real-time display of the prediction result, indicating whether the transaction is "Fraud" or "Not Fraud".
3. Model Integration: Seamless integration of the trained machine learning model to provide accurate predictions.
