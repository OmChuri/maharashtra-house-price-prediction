# maharashtra-house-price-prediction
Machine Learning-based web application using Streamlit to predict house prices in Maharashtra based on location, area, and BHK configuration.

This project is a Machine Learning-based web application that predicts house prices across various locations in Maharashtra. It uses a trained regression model and provides an interactive user interface built with Streamlit for real-time predictions.

##Key Features##
Predict house prices based on location, area (in square feet), and BHK configuration
*Interactive and user-friendly web interface using Streamlit
*Real-time prediction using a trained machine learning model
*Integrated dataset and preprocessing workflow
*Clean and structured project design

##Tech Stack##
Python
Pandas
NumPy
Scikit-learn
Streamlit
Pickle

##Project Structure##

*
house_price_prediction_maharashtra/
│
├── maharashtra_house_price_prediction.py   # Streamlit application
├── maharashtra_region_model.pickle         # Trained model
├── column.json                             # Feature columns
├── analysis_data.csv                       # Dataset
├── data_model_cleaning.ipynb               # Data preprocessing and model training
├── util.py                                 # Utility functions
├── animation.json                          # UI animation
├── requirements.txt                        # Dependencies
└── README.md                               # Documentation


##Installation##

1. Clone the repository ----  git clone https://github.com/your-username/maharashtra-house-price-prediction.git
cd maharashtra-house-price-prediction

2. Install dependencies --- pip install -r requirements.txt
3. Running the Application --- python -m streamlit run maharashtra_house_price_prediction.py

##How It Works##

1]The dataset is preprocessed and used to train a regression model
2]Input features such as location, area, and BHK are encoded into a feature vector
3]he trained model predicts the estimated house price
4]The result is displayed instantly through the Streamlit interface

##Output##
*Web-based interactive interface
*Real-time house price predictions
*Structured and responsive layout

