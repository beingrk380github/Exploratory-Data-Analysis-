# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import time

# ------------------------
# 🚀 Page Configuration
# ------------------------
st.set_page_config(
    page_title="🔥 EDA Visualizer | Streamlit",
    layout="wide",
    page_icon="📊"
)

# ------------------------
# 🎨 Custom Theme + Logo
# ------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

    html, body, [class*="css"] {
        background-color: #0d0d0d !important;
        color: #e6e6e6 !important;
        font-family: 'Orbitron', sans-serif;
    }

    .stApp {
        background: linear-gradient(to bottom right, #000000, #1c1c1c);
    }

    h1, h2, h3, h4 {
        color: #ff3333;
        text-shadow: 0 0 10px #ff4d4d;
    }

    .css-1rs6os.edgvbvh3 {
        color: #e6e6e6;
    }

    .reportview-container .main footer {
        visibility: hidden;
    }

    /* File uploader */
    .stFileUploader label {
        color: #ff4d4d;
        font-weight: bold;
    }

    /* Loader animation */
    #loader {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100px;
        margin-top: 20px;
    }

    .loader-text {
        font-size: 26px;
        color: #ff3333;
        text-align: center;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0% { opacity: 0.2; }
        50% { opacity: 1; }
        100% { opacity: 0.2; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------
# 🔥 Logo + Title
# ------------------------
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://hammond-design.co.uk/wp-content/uploads/2016/01/EDA-logo-banner3-new.jpg" width="100" />
        <h1>EDA Visualizer 🚀</h1>
        <p style="color:#bbbbbb;">A modern Exploratory Data Analysis web app built with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------
# 📂 File Upload
# ------------------------
uploaded_file = st.file_uploader("📂 Upload your CSV file here", type=["csv"])

if uploaded_file is not None:
    # Loader animation
    with st.spinner("Analyzing data..."):
        time.sleep(1)
        df = pd.read_csv(uploaded_file)

    st.success("✅ File Uploaded and Analyzed Successfully!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    st.subheader("📌 Correlation Heatmap (Numerical Features Only)")
    corr = df.select_dtypes(include='number').corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="Reds", fmt=".2f", ax=ax)
    st.pyplot(fig)

    st.subheader("📈 Histograms of Numerical Features")
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if numeric_cols:
        selected_num_col = st.selectbox("Select a numerical column for histogram", numeric_cols)
        if selected_num_col:
            fig = px.histogram(df, x=selected_num_col, nbins=30, title=f"Histogram of {selected_num_col}",
                               color_discrete_sequence=['#ff3333'])
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("⚠️ No numerical columns found in the dataset.")

    st.subheader("📦 Boxplot for Outliers")
    if numeric_cols:
        selected_box_col = st.selectbox("Select a column for boxplot", numeric_cols, key="boxplot")
        if selected_box_col:
            fig = px.box(df, y=selected_box_col, title=f"Boxplot of {selected_box_col}",
                         color_discrete_sequence=['#ff0000'])
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("🧮 Value Counts of Categorical Columns")
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    if cat_cols:
        selected_cat_col = st.selectbox("Select a categorical column", cat_cols)
        if selected_cat_col:
            cat_df = df[selected_cat_col].value_counts().reset_index()
            cat_df.columns = [selected_cat_col, 'Count']
            fig = px.bar(cat_df, x=selected_cat_col, y='Count',
                         title=f"Value Counts of {selected_cat_col}",
                         color_discrete_sequence=['#ff4d4d'])
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("⚠️ No categorical columns found in the dataset.")
else:
    st.warning("👆 Please upload a CSV file to get started.")

# ------------------------
# 🧾 Animated Footer
# ------------------------
st.markdown(
    """
    <div class="footer">
        <hr style="border-top: 1px solid #ff3333; margin-top: 40px;">
        <p style="text-align: center; color: #777;">
            Made with ❤️ by <a style="color: #ff3333;" href="https://www.linkedin.com/in/rambabukumargiri/" target="_blank">Rambabu Kumar</a> | © 2025
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
