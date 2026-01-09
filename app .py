import streamlit as st
import data_loader
import de_optimizer
import plotly.express as px

st.set_page_config(page_title="DE Knapsack Solver", layout="wide")

st.title("🧬 Differential Evolution: Multi-Objective Knapsack")
st.write("Solving OR-Library mknapcb3 (10 Instances)")

# Sidebar
st.sidebar.header("Configuration")
inst = st.sidebar.selectbox("Select Instance ID", [0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
f_param = st.sidebar.slider("Mutation Factor (F)", 0.1, 1.0, 0.5)
cr_param = st.sidebar.slider("Crossover Rate (CR)", 0.1, 1.0, 0.7)

if st.button("Run Optimization"):
    # 1. Load Data
    data = data_loader.load_instance("mknapcb3.txt", inst)
    
    # 2. Run Algorithm
    with st.spinner("Evolution in progress..."):
        history, final_pop = de_optimizer.run_de(data, F=f_param, CR=cr_param)
    
    # 3. Visuals
    st.success("Optimization Finished!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Convergence (Profit over Generations)")
        st.line_chart(history)
    
    with col2:
        st.subheader("Pareto Analysis (Objective Trade-offs)")
        st.info("This scatter plot shows the trade-off between Profit and Resource w2.")
        # Logic to plot Pareto Front would go here
