import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Laptop Price Predictor")



brand = st.text_input("Brand name")
Processor = st.text_input("Processor Name")
ram = st.number_input("RAM (GB)", min_value=2, max_value=64)
Storage_GB = st.number_input("Storage (GB)")
Operating_System = st.text_input("OS Version")
Gpu = st.text_input("GPU Version")
Rating = st.number_input("Rating")




brand_map = {
"MSI":0,
"Lenovo":1,
"Asus":2,
"Dell":3,
"Acer":4,
"Apple":5,
"HP":6
}

processor_map = {
"AMD Ryzen 3":0,
"Intel i7":1,
"AMD Ryzen 7":2,
"Intel i5":3,
"Intel i3":4,
"AMD Ryzen 5":5
}

os_map = {
"macOS":0,
"Windows 10":1,
"Windows 11":2
}

gpu_map = {
"AMD Radeon":0,
"NVIDIA GTX 1650":1,
"Integrated":2,
"NVIDIA RTX 3050":3
}

if st.button("Predict Price"):

    brand_num = brand_map.get(brand)
    processor_num = processor_map.get(Processor)
    os_num = os_map.get(Operating_System)
    gpu_num = gpu_map.get(Gpu)

    features = np.array([[brand_num, processor_num, ram, Storage_GB, os_num, gpu_num, Rating]])

    prediction = model.predict(features)

    st.success(f"Estimated Laptop Price: ₹{prediction[0]:,.2f}")