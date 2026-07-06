import os
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account

class GCPPipeline:
    def __init__(self, project_id=None, credentials_path=None):
        # Use provided project_id or fallback to environment variable FRAUDLENS_PROJECT_ID
        self.project_id = project_id or os.getenv("FRAUDLENS_PROJECT_ID")
        self.credentials = None
        if credentials_path and os.path.exists(credentials_path):
            self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
            self.storage_client = storage.Client(credentials=self.credentials, project=project_id)
            self.bq_client = bigquery.Client(credentials=self.credentials, project=project_id)
            self.is_mock = False
        else:
            print("WARNING: GCP credentials not found. Running in MOCK mode.")
            self.is_mock = True

    def upload_to_gcs(self, bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        if self.is_mock:
            print(f"[MOCK] Uploaded {source_file_name} to gs://{bucket_name}/{destination_blob_name}")
            return f"gs://{bucket_name}/{destination_blob_name}"

        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
        return f"gs://{bucket_name}/{destination_blob_name}"

    def load_gcs_to_bigquery(self, gcs_uri, dataset_id, table_id):
        """Loads a CSV from GCS to BigQuery."""
        if self.is_mock:
            print(f"[MOCK] Loaded data from {gcs_uri} into BigQuery {dataset_id}.{table_id}")
            return True

        table_ref = self.bq_client.dataset(dataset_id).table(table_id)
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
        )

        load_job = self.bq_client.load_table_from_uri(
            gcs_uri, table_ref, job_config=job_config
        )
        load_job.result()
        print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
        return True

    def query_bigquery(self, query):
        """Executes a query and returns a pandas DataFrame."""
        if self.is_mock:
            print(f"[MOCK] Executing BigQuery: {query[:50]}...")
            # For mock, we just load the local CSV if it exists
            local_path = "../data/transactions.csv"
            if os.path.exists(local_path):
                return pd.read_csv(local_path)
            else:
                return pd.DataFrame()
        
        query_job = self.bq_client.query(query)
        return query_job.to_dataframe()

if __name__ == "__main__":
    pipeline = GCPPipeline()
    # Example usage (will mock without creds):
    # gcs_uri = pipeline.upload_to_gcs("my-bucket", "../data/transactions.csv", "raw/transactions.csv")
    # pipeline.load_gcs_to_bigquery(gcs_uri, "fraud_dataset", "transactions")
