# src/gemini_agent.py
"""A very small stub that shows how FraudLens could be exposed as a Gemini Enterprise Agent.
In a real deployment you would package this as a Docker image, register it with the Gemini
platform and define an OpenAPI spec. For the hackathon a simple Python class is enough.
"""

import os
import pickle
import json
from typing import Dict, Any

class FraudLensAgent:
    def __init__(self, model_path: str = os.path.abspath(os.path.join(__file__, "../../data/xgboost_fraud_model.pkl"))):
        if os.path.exists(model_path):
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            raise FileNotFoundError(f"Model file not found at {model_path}")

    def predict(self, payload: Dict[str, Any]) -> Dict[str, float]:
        """Accept a JSON payload with a single record of features and return a fraud risk score.
        The payload format is expected to match the column order used in `model_training.py`.
        Example:
        {
            "features": {
                "user_id": 1234,
                "merchant_id": 56,
                "amount": 124.5,
                "tx_type_CASH_OUT": 0,
                "tx_type_DEBIT": 1,
                ...
            }
        }
        """
        features = payload.get("features")
        if not features:
            raise ValueError("Payload must contain a 'features' dictionary")

        # Convert to DataFrame with the same column order the model expects
        import pandas as pd
        df = pd.DataFrame([features])
        prob = self.model.predict_proba(df)[0, 1]
        return {"risk_score": float(prob)}

# If this file is executed directly we expose a tiny Flask endpoint for demo purposes
if __name__ == "__main__":
    from flask import Flask, request, jsonify
    app = Flask(__name__)
    agent = FraudLensAgent()

    @app.route("/predict", methods=["POST"])
    def predict():
        payload = request.get_json(force=True)
        try:
            result = agent.predict(payload)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    app.run(host="0.0.0.0", port=8080)
