#daily health checkup app

import streamlit as st

st.set_page_config(
    page_title="Daily Health Checker",
    page_icon="💕",
    layout="centered"
)
# Application title
st.title("❤️ Daily Health Checker")
st.write("Welcome! Check your basic health measurements.")

st.info(
    "This application is for general health awareness only. "
    "It does not provide medical diagnosis."
)

# User information
st.header("👤 Personal Information")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)

st.divider()

# Health measurements
st.header("🩺 Enter Your Health Details")

weight = st.number_input(
    "Weight (kg)", min_value=1.0, max_value=300.0, value=65.0
)

height = st.number_input(
    "Height (cm)", min_value=50.0, max_value=250.0, value=170.0
)

heart_rate = st.number_input(
    "Heart Rate (beats per minute)",
    min_value=20, max_value=250, value=75
)

temperature = st.number_input(
    "Body Temperature (°C)",
    min_value=30.0, max_value=45.0, value=36.8
)

systolic = st.number_input(
    "Systolic Blood Pressure (mmHg)",
    min_value=50, max_value=250, value=120
)

diastolic = st.number_input(
    "Diastolic Blood Pressure (mmHg)",
    min_value=30, max_value=150, value=80
)

# Health check button
if st.button("Check My Health ❤️", use_container_width=True):

    bmi = weight / ((height / 100) ** 2)

    st.divider()
    st.header("📊 Your Health Report")

    if name.strip():
        st.success(f"Hello, {name}! Here is your report.")
    else:
        st.success("Here is your health report.")

    st.metric("Your BMI", f"{bmi:.2f}")

    # BMI interpretation for adults
    if age >= 20:
        if bmi < 18.5:
            st.warning("BMI category: Underweight")
        elif bmi < 25:
            st.success("BMI category: Healthy weight range")
        elif bmi < 30:
            st.warning("BMI category: Overweight")
        else:
            st.warning("BMI category: Obesity range")
    else:
        st.info(
            "BMI for children and teenagers requires "
            "age- and sex-specific growth charts."
        )

    # Heart rate
    st.subheader("❤️ Heart Rate")

    if 60 <= heart_rate <= 100:
        st.success(f"Heart rate: {heart_rate} BPM")
    else:
        st.warning(
            f"Heart rate: {heart_rate} BPM. "
            "This is outside the typical adult resting range."
        )

    # Temperature
    st.subheader("🌡️ Body Temperature")

    if 36.1 <= temperature <= 37.2:
        st.success(f"Temperature: {temperature} °C")
    elif temperature >= 38:
        st.warning(
            f"Temperature: {temperature} °C. "
            "This may indicate a fever."
        )
    else:
        st.warning(
            f"Temperature: {temperature} °C. "
            "This is outside the typical range."
        )

    # Blood pressure
    st.subheader("🩸 Blood Pressure")

    if systolic >= 180 or diastolic >= 120:
        st.error(
            "Very high blood pressure reading. "
            "Seek urgent medical assessment. If you have chest pain, "
            "breathlessness, weakness, vision changes or severe headache, "
            "seek emergency care immediately."
        )
    elif systolic >= 140 or diastolic >= 90:
        st.warning("Blood pressure is in a high range.")
    elif systolic >= 130 or diastolic >= 80:
        st.warning("Blood pressure is above the ideal range.")
    elif systolic < 90 or diastolic < 60:
        st.warning("Blood pressure is on the low side.")
    else:
        st.success("Blood pressure reading is within a typical range.")

    st.divider()

    st.subheader("💡 Healthy Lifestyle Tips")

    st.write("✅ Drink enough water.")
    st.write("✅ Eat a balanced and nutritious diet.")
    st.write("✅ Exercise regularly.")
    st.write("✅ Get sufficient sleep.")
    st.write("✅ Monitor your health regularly.")

    st.caption(
        "Note: These measurements are screening information, "
        "not a diagnosis. Interpretations vary by age, health status "
        "and measurement conditions. Consult a healthcare professional "
        "for medical advice."
    )

# Footer
st.divider()
st.caption("Daily Health Checker | Built with Python and Streamlit ❤️")



