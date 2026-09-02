import streamlit as st

st.title("Hello, Streamlit!")
st.write("My first Streamlit app.")
st.balloons()

# Title and headers
st.title("Main Title")          # H1
st.header("Section Header")     # H2
st.subheader("Subsection")      # H3
# Body text
st.write("Auto-formats anything!")
st.markdown("**Bold**, *italic*, `code`")
st.latex(r"E = mc^2")
st.code("print('hello')", language="python")
st.caption("Small grey caption")

import pandas as pd
df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Score': [92, 85]})
st.dataframe(df)        # Interactive – sortable, scrollable
st.table(df)            # Static – full display
st.metric("Accuracy", "92%", "+2%")   # KPI card with delta
st.json({"model": "XGBoost", "accuracy": 0.92})

import numpy as np
rng = np.random.default_rng(12)
dates = pd.date_range("2024-01-01", periods=60, freq="D")
data = pd.DataFrame(
    {
        "date": dates,
        "product_A": rng.integers(50, 200, size=60).cumsum(),
        "product_B": rng.integers(30, 150, size=60).cumsum(),
        "product_C": rng.integers(20, 100, size=60).cumsum(),
    }
).set_index("date")
# line chart
st.title("Sales Trends Over Time")
st.line_chart(data)
# bar chart
st.title("Total Sales by Product")
total_sales = data.sum()
st.bar_chart(total_sales)

import plotly.express as px
# pie chart
st.title("Sales Share by Product")
fig_pie = px.pie(
    values=total_sales.values,
    names=total_sales.index,
    title="Total Sales Distribution",
)
st.plotly_chart(fig_pie)
# plotly line chart
st.title("Sales Trends Over Time (Plotly)")
fig_line = px.line(
    data.reset_index(),
    x="date",
    y=["product_A", "product_B", "product_C"],
    title="Sales Trends (Plotly)",
)
st.plotly_chart(fig_line)

# Text inputs
name = st.text_input("Your name")
bio  = st.text_area("About you")
# Numeric inputs
age    = st.number_input("Age", 18, 100)
rating = st.slider("Rating", 1, 10, 7)
# Selection inputs
model    = st.selectbox("Model", ["RF", "XGBoost", "SVM"])
features = st.multiselect("Features", ["Age", "Income", "Education"])
# Boolean & file
show = st.checkbox("Show raw data")
file = st.file_uploader("Upload CSV")
# Action
if st.button("Train Model"):
    st.write("Training...")

# Sidebar
with st.sidebar:
    page = st.radio("Go to", ["Home", "Projects", "Contact"])
# Columns
col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "92%")
# Tabs
tab1, tab2 = st.tabs(["EDA", "Model"])
with tab1:
    st.write("EDA content...")
# Expander (collapsible)
with st.expander("Show code"):
    st.code("model.fit(X, y)")

st.set_page_config(
    page_title="John | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)
