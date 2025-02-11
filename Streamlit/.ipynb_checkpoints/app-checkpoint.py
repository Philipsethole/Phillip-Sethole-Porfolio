import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Set page title and theme
st.set_page_config(page_title="Phillip Sethole | Machine Learning Portfolio", layout="wide")

# Apply custom styling
st.markdown(
    """
    <style>
        .big-title { font-size: 50px; font-weight: bold; color: #4CAF50; text-align: center; }
        .subheader { font-size: 20px; color: #A0A0A0; text-align: center; }
        .project-card { background: #1E1E1E; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0px 0px 10px rgba(0, 255, 0, 0.5); }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 5px; padding: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Avocado Prices"])

# Home Page
if page == "Home":
    st.markdown('<p class="big-title">Phillip Sethole</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Data Scientist | Machine Learning Enthusiast</p>', unsafe_allow_html=True)
    st.write("🚀 I specialize in **data cleaning, exploratory data analysis, and machine learning.**")

    st.write("### Contact Me")
    st.write("📧 Email: your_email@example.com")
    st.write("[GitHub](https://github.com/yourgithub) | [LinkedIn](https://linkedin.com/in/yourprofile)")

# Projects Page
elif page == "Projects":
    st.write("## My Projects")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### Avocado Prices Analysis 🥑")
        st.write("Analysis of avocado price trends using visualization and statistics.")
        st.markdown("[View Project](https://github.com/yourgithub/avocado-analysis)")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.markdown("### News Classification with ML 📰")
        st.write("Machine learning model to classify news articles into categories.")
        st.markdown("[View Project](https://github.com/yourgithub/news-classification)")
        st.markdown('</div>', unsafe_allow_html=True)

# Avocado Prices Interactive Chart
elif page == "Avocado Prices":
    st.write("## Avocado Prices Analysis 📊")
    
    # Sample Data
    months = ["Jan", "Feb", "Mar", "Apr"]
    prices = [1.2, 1.4, 1.3, 1.5]
    df = pd.DataFrame({"Month": months, "Price": prices})

    # Matplotlib Chart
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Price"], marker="o", linestyle="-", color="lime")
    ax.set_xlabel("Month")
    ax.set_ylabel("Price (USD)")
    ax.set_facecolor("#1E1E1E")
    st.pyplot(fig)

    # Plotly Interactive Chart
    fig_plotly = px.line(df, x="Month", y="Price", title="Avocado Prices Over Time", template="plotly_dark")
    st.plotly_chart(fig_plotly)

