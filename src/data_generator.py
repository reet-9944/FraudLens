try:
    import cudf.pandas
    cudf.pandas.install()
    print("🚀 NVIDIA RAPIDS (cudf.pandas) enabled for ultra-fast data generation.")
except ImportError:
    pass

import pandas as pd
import numpy as np
import os
import argparse
from datetime import datetime, timedelta

def resolve_path(rel_path):
    """Resolve relative path dynamically by searching candidate folders."""
    filename = os.path.basename(rel_path)
    parent_dir = os.path.basename(os.path.dirname(rel_path))
    
    candidates = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", parent_dir)),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", parent_dir)),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fraudlens", parent_dir)),
        os.path.abspath(os.path.join(".", parent_dir)),
        os.path.abspath(os.path.join("..", parent_dir)),
    ]
    
    for c in candidates:
        full_path = os.path.join(c, filename)
        if os.path.exists(full_path):
            return full_path
            
    # Fallback to creating/using the first candidate
    for c in candidates:
        try:
            os.makedirs(c, exist_ok=True)
            return os.path.join(c, filename)
        except Exception:
            continue
            
    return os.path.abspath(rel_path)

def generate_data(num_records=1_000_000, output_path=None):
    if output_path is None:
        output_path = resolve_path('../data/transactions.csv')
    else:
        output_path = resolve_path(output_path)
        
    print(f"Generating {num_records} synthetic transactions...")
    np.random.seed(42)

    # Generate basic fields
    transaction_ids = [f"TXN{i:08d}" for i in range(num_records)]
    
    # 5000 users, 1000 merchants
    user_ids = np.random.randint(1000, 6000, size=num_records)
    merchant_ids = np.random.randint(1, 1000, size=num_records)
    
    # Amounts: most are small, some are very large
    base_amounts = np.random.exponential(scale=50, size=num_records)
    
    # Timestamps over 30 days
    start_date = datetime.now() - timedelta(days=30)
    seconds_add = np.random.randint(0, 30*24*60*60, size=num_records)
    timestamps = [start_date + timedelta(seconds=int(s)) for s in seconds_add]
    
    # Transaction types
    tx_types = np.random.choice(['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'], 
                                size=num_records, 
                                p=[0.35, 0.1, 0.35, 0.05, 0.15])
                                
    # Create DataFrame
    df = pd.DataFrame({
        'transaction_id': transaction_ids,
        'timestamp': timestamps,
        'user_id': user_ids,
        'merchant_id': merchant_ids,
        'amount': base_amounts,
        'tx_type': tx_types,
        'location_id': np.random.randint(1, 100, size=num_records)
    })
    
    # Introduce fraud patterns
    # 1. Very large transfers are more likely to be fraud
    df['is_fraud'] = 0
    
    # Pattern A: High amount transfers
    mask_a = (df['tx_type'] == 'TRANSFER') & (df['amount'] > 300)
    df.loc[mask_a, 'is_fraud'] = np.random.choice([0, 1], size=mask_a.sum(), p=[0.2, 0.8])
    
    # Pattern B: Multiple transactions from same user in short time (velocity)
    # To simulate simply, we just assign random fraud to certain user/merchant combos
    fraud_merchants = np.random.choice(range(1, 1000), size=20, replace=False)
    mask_b = df['merchant_id'].isin(fraud_merchants)
    df.loc[mask_b, 'is_fraud'] = np.random.choice([0, 1], size=mask_b.sum(), p=[0.5, 0.5])
    
    # Noise fraud
    mask_c = df['is_fraud'] == 0
    df.loc[mask_c, 'is_fraud'] = np.random.choice([0, 1], size=mask_c.sum(), p=[0.99, 0.01])
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV
    print(f"Saving to {output_path}...")
    df.sort_values('timestamp', inplace=True)
    df.to_csv(output_path, index=False)
    print("Done! Fraud rate:", df['is_fraud'].mean())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic transaction data")
    parser.add_argument("--rows", type=int, default=100_000, help="Number of rows to generate")
    parser.add_argument("--output", type=str, default=None, help="Output CSV path")
    args = parser.parse_args()
    
    generate_data(args.rows, args.output)
