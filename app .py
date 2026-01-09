import streamlit as st
import data_loader
import de_optimizer
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="DE Knapsack Solver", layout="wide")

# 2. Sidebar Setup
st.sidebar.header("Step 1: Setup Parameters")
inst_id = st.sidebar.selectbox("Choose Instance", [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
pop_size = st.sidebar.slider("Population Size", 10, 100, 50)
iters = st.sidebar.slider("Generations", 10, 200, 50)

# 3. Main UI
st.title("📦 Differential Evolution: Multi-Objective Knapsack")
st.info("If the screen is black, please check your 'requirements.txt' file on GitHub.")

if st.button("🚀 Start Optimization"):
    # Load the data
    data = data_loader.load_instance("mknapcb3.txt", inst_id)
    
    if data:
        st.write(f"Running optimization for Instance {inst_id} with 500 items...")
        
        # Run Algorithm
        progress_bar = st.progress(0)
        history, final_pop = de_optimizer.run_de(data, pop_size, iters)
        progress_bar.progress(100)
        
        # Show Results
        st.subheader("Convergence Graph")
        st.line_chart(history)
        st.success(f"Final Best Profit: {max(history)}")
    else:
        st.error("Data could not be loaded. Check if mknapcb3.txt exists in your GitHub.")
