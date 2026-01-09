import re

def parse_mknapcb3(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split by instance markers (typically numbers like '1', '2'...)
    # For mknapcb3, instances are separated by problem headers
    instances_raw = re.split(r'\n\s*\d+\s+\d+\s*\n', content)
    instances = []
    
    # We only want instances 0, 3, 6, 9, 12, 15, 18, 21, 24, 27
    target_ids = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    
    for i in target_ids:
        # Simplified parsing logic for 500 items, 5 weights
        # Logic: Extract Profit (Value), Weight1, Weight2, and Capacity
        # ... (Parsing implementation)
        pass 
    return instances
