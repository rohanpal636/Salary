import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.markdown(
    """
    <style>
    .css-1d391kg, .css-1p0j8nk {
        max-width: 80%;
        margin: auto;
    }
    img {
        max-width: 100%;
        height: auto;
    }
    .plotly-container {
        width: 100% !important;
        height: auto !important;
    }
    h1 {
        font-size: min(4vw, 30px);
        white-space: nowrap;
        text-align: center;
    }
    .contact-item {
        font-size: 16px;
        margin-bottom: 10px;
    }
    .contact-item i {
        font-size: 18px;
        margin-right: 8px;
    }
    .contact-item a {
        text-decoration: none;
        color: #1e90ff;  /* Blue color for links */
        margin-left: 8px;
    }
    .contact-item a:hover {
        text-decoration: underline;
    }
    .linkedin, .instagram {
        color: white; /* White color for text */
    }
    .linkedin a, .instagram a {
        color: #1e90ff; /* Blue color for links */
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True
)

data = pd.read_csv("Data//Salary_Data.csv")

st.title("Salary Predictor App by Rohan")

navigation = st.sidebar.radio("Menu", ["Home", "Prediction", "Contribute", "Contact"])

if navigation == "Home":
    st.image("Data//Salary.jpg", use_column_width=True)
    if st.checkbox("Show Table"):
        st.table(data)
    
    graph = st.selectbox("Choose a graph:", ["None", "Non-Interactive", "Interactive", "Both"])
    
    if graph in ["Non-Interactive", "Both"]:
        plt.figure(figsize=(10, 5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("YearsExperience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
    
    if graph in ["Interactive", "Both"]:
        layout = go.Layout(
            xaxis=dict(title="Years of Experience", range=[0, 15]),
            yaxis=dict(title="Salary", range=[0, 210000]),
            autosize=True,
            width=None,
            height=None
        )
        fig = go.Figure(
            data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),
            layout=layout
        )
        st.plotly_chart(fig, use_container_width=True)

if navigation == "Prediction":
    st.header("Predict Your Salary")
    X = data[["YearsExperience"]]
    y = data["Salary"]
    model = LinearRegression()
    model.fit(X, y)
    exp_input = st.number_input("Enter your years of experience:", min_value=0.0, max_value=50.0, step=0.1)
    if st.button("Predict Salary"):
        pred_salary = model.predict(np.array([[exp_input]]))[0]
        st.success(f"The predicted salary for {exp_input} years of experience is: ${pred_salary:,.2f}")

if navigation == "Contribute":
    st.header("Contribute to the Salary Predictor App")

    st.subheader("Add Your Data")
    new_exp = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)
    new_salary = st.number_input("Salary", min_value=0, step=1000)
    if st.button("Submit Data"):
        if new_exp > 0 and new_salary > 0:
            new_data = pd.DataFrame({"YearsExperience": [new_exp], "Salary": [new_salary]})
            data = pd.concat([data, new_data], ignore_index=True)
            data.to_csv("Data//Salary_Data.csv", index=False)
            st.success("Thank you for your contribution! Your data has been recorded.")
        else:
            st.error("Please provide valid input for both fields.")
    
    with st.expander("Feedback and Suggestions"):
        feedback = st.text_area("Please share your feedback or suggestions:")
        if st.button("Submit Feedback"):
            if feedback:
                st.success("Thank you for your feedback!")
            else:
                st.error("Feedback cannot be empty.")
    
    with st.expander("Share a Resource"):
        resource_link = st.text_input("Resource URL")
        resource_description = st.text_area("Description of the Resource")
        if st.button("Submit Resource"):
            if resource_link and resource_description:
                st.success("Thank you for sharing this resource!")
            else:
                st.error("Please provide both a URL and a description.")

if navigation == "Contact":
    st.title("Contact Me")

    st.markdown("""
        <div class="contact-item linkedin">
            <i class="fab fa-linkedin"></i>
            LinkedIn: <a href="https://www.linkedin.com/in/rohanpal636" >https://www.linkedin.com/in/rohanpal636</a>
        </div>
        <div class="contact-item github">
            <i class="fab fa-github"></i>
            Github: <a href="https://github.com/rohanpal636">https://github.com/rohanpal636</a>
        </div>
        <div class="contact-item instagram">
            <i class="fab fa-instagram"></i>
            Instagram: <a href="https://www.instagram.com/rohan.forreal">https://www.instagram.com/rohan.forreal</a>
        </div>
        <div class="contact-item instagram">
            <i class="fab fa-instagram"></i>
            Instagram: <a href="https://www.instagram.com/rohanpal636">https://www.instagram.com/rohanpal636</a>
        <div class="contact-item">
            <i class="fas fa-envelope"></i>
            Email: <a href="mailto:rohanpal636@gmail.com">rohanpal636@gmail.com</a>
        
    """, unsafe_allow_html=True)
