import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("Unit Converter")
st.write("Easily convert different measurement units in real-time.")

st.sidebar.markdown("### Select a category")
category = st.sidebar.selectbox("Choose a Category", ["Length", "Weight", "Temperature", "Time", "Data"])

def length_converter():
    st.header("Length Converter")
    units = {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    }

    with st.form(key="length_form"):
        from_unit = st.selectbox("From", list(units.keys()), key="length_from")
        to_unit = st.selectbox("To", list(units.keys()), key="length_to")
        value = st.number_input("Enter value:", min_value=0.0, format="%.4f", key="length_value")

        convert_btn = st.form_submit_button("Convert")

        if convert_btn:
            result = value * (units[to_unit] / units[from_unit])
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

def weight_converter():
    st.header("Weight Converter")
    units = {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1e6, "Pounds": 2.20462, "Ounces": 35.274
    }

    with st.form(key="weight_form"):
        from_unit = st.selectbox("From", list(units.keys()), key="weight_from")
        to_unit = st.selectbox("To", list(units.keys()), key="weight_to")
        value = st.number_input("Enter value:", min_value=0.0, format="%.4f", key="weight_value")

        convert_btn = st.form_submit_button("Convert")

        if convert_btn:
            result = value * (units[to_unit] / units[from_unit])
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

def temperature_converter():
    st.header("Temperature Converter")
    temp_scales = ["Celsius", "Fahrenheit", "Kelvin"]

    with st.form(key="temperature_form"):
        from_unit = st.selectbox("From", temp_scales, key="temp_from")
        to_unit = st.selectbox("To", temp_scales, key="temp_to")
        value = st.number_input("Enter Temperature:", format="%.2f", key="temp_value")

        convert_btn = st.form_submit_button("Convert")

        if convert_btn:
            if from_unit == to_unit:
                result = value
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

def time_converter():
    st.header("Time Converter")
    units = {
        "Seconds": 1, "Minutes": 60, "Hours": 3600, "Days": 86400
    }

    with st.form(key="time_form"):
        from_unit = st.selectbox("From", list(units.keys()), key="time_from")
        to_unit = st.selectbox("To", list(units.keys()), key="time_to")
        value = st.number_input("Enter value:", min_value=0.0, format="%.2f", key="time_value")

        convert_btn = st.form_submit_button("Convert")

        if convert_btn:
            result = value * (units[from_unit] / units[to_unit])
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

def data_converter():
    st.header("Data Converter")
    units = {
        "Bytes": 1, "Kilobytes": 1024, "Megabytes": 1048576, "Gigabytes": 1073741824, "Terabytes": 1099511627776
    }

    with st.form(key="data_form"):
        from_unit = st.selectbox("From", list(units.keys()), key="data_from")
        to_unit = st.selectbox("To", list(units.keys()), key="data_to")
        value = st.number_input("Enter value:", min_value=0.0, format="%.2f", key="data_value")

        convert_btn = st.form_submit_button("Convert")

        if convert_btn:
            result = value * (units[from_unit] / units[to_unit])
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

if category == "Length":
    length_converter()
elif category == "Weight":
    weight_converter()
elif category == "Temperature":
    temperature_converter()
elif category == "Time":
    time_converter()
elif category == "Data":
    data_converter()
