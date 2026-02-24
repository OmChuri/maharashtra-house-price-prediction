import streamlit as st
import pickle
import json
import numpy as np
import requests
from streamlit_lottie import st_lottie

__data_columns = None
__locations = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    with open("column.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[2:]

    if __model is None:
        with open("maharashtra_region_model.pickle", "rb") as f:
            __model = pickle.load(f)

def get_estimated_price(location, sqft, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_lottiefile(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

load_saved_artifacts()

animation = load_lottiefile("animation.json")
st_lottie(animation, height=200)

st.markdown("""
<div style="background:#025246;padding:15px;border-radius:10px">
<h1 style="color:white;text-align:center;">
🏠 Maharashtra House Price Prediction
</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center; margin-top:10px;">
<a href="https://www.linkedin.com/in/om-churi" target="_blank">
<button style="
    background-color:#0077b5;
    color:white;
    padding:10px 20px;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-size:16px;">
    🔗 Connect on LinkedIn
</button>
</a>
</div>
""", unsafe_allow_html=True)

sqft = st.number_input("📏 Enter Area (sqft)", min_value=375, max_value=15000, step=50)
bhk = st.select_slider("🏢 Select BHK", options=[1, 2, 3, 4, 5])
location = st.selectbox("📍 Select Location", __locations)

if st.button("💰 Predict House Price"):
    price = get_estimated_price(location, sqft, bhk)
    st.success(f"Estimated Price: ₹ {price:,.2f}")

st.markdown("""
<style>
@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}

.footer {
    text-align: center;
    font-size: 14px;
    color: grey;
    margin-top: 30px;
    animation: fadeIn 3s ease-in-out;
}
</style>

<div class="footer">
    ✨ Created by <b>Om Churi</b>
</div>
""", unsafe_allow_html=True)