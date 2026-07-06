import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score
import time
import pickle
import os
import json

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

def prepare_data(df):
    """Basic feature engineering using pandas (simulating the pipeline)."""
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Feature Engineering
    user_stats = df.groupby('user_id').agg({
        'amount': ['mean', 'std', 'max'],
        'transaction_id': 'count'
    }).reset_index()
    user_stats.columns = ['user_id', 'user_mean_amt', 'user_std_amt', 'user_max_amt', 'user_txn_count']
    
    # Fill NAs
    user_stats.fillna(0, inplace=True)
    
    df = df.merge(user_stats, on='user_id', how='left')
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    
    # Drop non-numeric/unnecessary columns
    cols_to_drop = ['transaction_id', 'timestamp']
    df = df.drop(columns=cols_to_drop)
    
    # One-hot encode categorical
    df = pd.get_dummies(df, columns=['tx_type'], drop_first=True)
    
    # Target
    y = df['is_fraud']
    X = df.drop(columns=['is_fraud'])
    
    return X, y

def train_model(data_path=None, model_path=None):
    if data_path is None:
        data_path = resolve_path("../data/transactions.csv")
    else:
        data_path = resolve_path(data_path)
        
    if model_path is None:
        model_path = resolve_path("../data/xgboost_fraud_model.pkl")
    else:
        model_path = resolve_path(model_path)

    print(f"Loading data from {data_path}...")
    if not os.path.exists(data_path):
        from data_generator import generate_data
        generate_data(num_records=100_000, output_path=data_path)
        
    df = pd.read_csv(data_path)
    print(f"Data loaded: {len(df)} rows.")
    
    X, y = prepare_data(df)
    
    # Ensure all categorical columns are present or set defaults
    for col in ['tx_type_TRANSFER', 'tx_type_CASH_OUT', 'tx_type_DEBIT', 'tx_type_CASH_IN']:
        if col not in X.columns:
            X[col] = 0
            
    # Keep column order consistent
    X = X.reindex(sorted(X.columns), axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"Training set shape: {X_train.shape}")
    
    # Attempt GPU acceleration
    use_gpu = False
    try:
        import subprocess
        # Quick check for nvidia-smi
        subprocess.check_output('nvidia-smi', shell=True)
        use_gpu = True
    except Exception:
        pass
        
    params = {
        'objective': 'binary:logistic',
        'max_depth': 6,
        'learning_rate': 0.1,
        'n_estimators': 100,
        'eval_metric': 'auc'
    }
    
    start_time = time.time()
    
    if use_gpu:
        print("GPU found! Using NVIDIA RAPIDS XGBoost (device='cuda')...")
        params['tree_method'] = 'hist'
        params['device'] = 'cuda'
        
        clf = xgb.XGBClassifier(**params)
        clf.fit(X_train, y_train)
        training_time = time.time() - start_time
        print(f"GPU Training Time: {training_time:.2f} seconds")
    else:
        print("No GPU found. Falling back to CPU training (this would be much slower on big data)...")
        clf = xgb.XGBClassifier(**params)
        clf.fit(X_train, y_train)
        training_time = time.time() - start_time
        print(f"CPU Training Time: {training_time:.2f} seconds")

    # Evaluate
    preds = clf.predict(X_test)
    preds_proba = clf.predict_proba(X_test)[:, 1]
    
    auc = roc_auc_score(y_test, preds_proba)
    precision = precision_score(y_test, preds)
    recall = recall_score(y_test, preds)
    
    print(f"Validation AUC: {auc:.4f}")
    print(f"Precision: {precision:.4f} | Recall: {recall:.4f}")
    
    # Save model
    with open(model_path, 'wb') as f:
        pickle.dump(clf, f)
    print(f"Model saved to {model_path}")
    
    # Save features for frontend
    features_path = resolve_path("../data/model_features.json")
    with open(features_path, "w") as f:
        json.dump(list(X.columns), f)
    print(f"Model features saved to {features_path}")
        
    return {
        'auc': round(auc, 4),
        'precision': round(precision, 4),
        'recall': round(recall, 4),
        'training_time': round(training_time, 2),
        'accelerated': use_gpu
    }

if __name__ == "__main__":
    train_model()
