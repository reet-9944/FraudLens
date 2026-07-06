# Looker Studio Integration Guide

FraudLens is designed to integrate seamlessly with Google Cloud's data ecosystem, including **Looker** and **Looker Studio**. 

By utilizing the provided `looker_schema.json`, risk analysts can instantly generate enterprise-grade dashboards on top of the BigQuery enriched transaction data.

## Steps to Deploy in Looker:

### 1. Ensure BigQuery Data is Populated
Run the Dataproc Spark RAPIDS job or the native GCP Pipeline script to ensure your BigQuery dataset `fraud_dataset.transactions_enriched` is fully populated.

### 2. Connect Looker to BigQuery
1. Navigate to your Looker instance (Admin -> Database -> Connections).
2. Add a new connection named `bigquery_fraudlens_conn`.
3. Authenticate using the Service Account JSON used by the FraudLens application.

### 3. Import the LookML Schema
1. In your Looker IDE, create a new project called `FraudLens`.
2. Upload the `looker_schema.json` file provided in the repository root. Looker can auto-parse this JSON structure into native LookML views and explores.
3. Commit and push to your production branch.

### 4. Build the Dashboard
Navigate to the Explore menu and select **FraudLens Risk Analysis**. 
You can now build interactive charts using the pre-calculated metrics:
* `Value at Risk`
* `Fraud Rate`
* `ML Risk Score`

### 5. Embed in Streamlit (Optional)
If you wish to embed the Looker dashboard directly inside the FraudLens Streamlit UI:
1. Generate an SSO Embed URL in Looker.
2. In `app/dashboard.py`, add the following Streamlit component:
```python
import streamlit.components.v1 as components
components.iframe("YOUR_LOOKER_EMBED_URL", height=800, scrolling=True)
```
