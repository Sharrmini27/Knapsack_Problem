import numpy as np
import streamlit as st

def load_instance(file_path, target_idx):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # This is a 'Dummy' generator for now to ensure your app OPENS.
        # It creates 500 items so you can test the UI first.
        data = {
            "values": np.random.randint(50, 500, 500),
            "w1": np.random.randint(10, 100, 500),
            "w2": np.random.randint(10, 100, 500),
            "capacity": 15000
        }
        return data
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None
