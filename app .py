import streamlit as st
import de_optimizer
import pandas as pd
import plotly.express as px

st.title("📦 Multi-Objective Knapsack - DE Algorithm")

# Sidebar for user inputs
st.sidebar.header("Settings")
instance_idx = st.sidebar.selectbox("Select Instance", [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
gen = st.sidebar.slider("Generations", 10, 500, 100)

if st.button("Run Optimization"):
    # Call the DE algorithm
    results, history = de_optimizer.run_de(instance_data)
    
    # Visualization
    st.subheader("Convergence Curve")
    st.line_chart(history)
    
    st.subheader("Pareto Front (Profit vs W2)")
    # Plotly Scatter Chart
