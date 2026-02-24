# maharashtra-house-price-prediction
Machine Learning-based web application using Streamlit to predict house prices in Maharashtra based on location, area, and BHK configuration.

Maharashtra House Price Prediction
Project Overview

This project uses a trained Machine Learning model to estimate property prices in Maharashtra. The application is built using Streamlit to provide an interactive and user-friendly interface for real-time predictions.

Tech Stack

Python

Pandas

NumPy

Scikit-learn

Streamlit

Pickle

Features

Select location from Maharashtra

Enter area in square feet

Choose number of BHK

Get instant house price prediction

Interactive web interface

Integrated professional profile link

Project Structure
house_price_prediction_maharashtra/
│
├── maharashtra_house_price_prediction.py
├── maharashtra_region_model.pickle
├── column.json
├── analysis_data.csv
├── data_model_cleaning.ipynb
├── util.py
├── animation.json
├── requirements.txt
└── README.md
Installation and Setup
1. Clone the repository
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
2. Install dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit pandas numpy scikit-learn streamlit-lottie requests
3. Run the application
python -m streamlit run maharashtra_house_price_prediction.py
How It Works

The model is trained using housing data from Maharashtra

User inputs (area, BHK, location) are converted into a feature vector

The trained model predicts the estimated house price

The result is displayed instantly on the web interface

Output

Interactive web-based application

Real-time price prediction

Clean and structured user interface

Future Improvements

Add data visualizations for price trends

Deploy the application online

Improve model accuracy with more data

Add advanced filters such as amenities and property type
