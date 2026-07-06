import os
import argparse
from google.cloud import aiplatform

def deploy_to_vertex_ai(project_id, location, model_display_name, model_artifact_uri, serving_container_image_uri):
    """
    Registers and deploys an XGBoost model to Google Cloud Vertex AI.
    
    Args:
        project_id: GCP Project ID
        location: GCP Region (e.g., 'us-central1')
        model_display_name: Name of the model in Vertex AI Model Registry
        model_artifact_uri: GCS URI where the `xgboost_fraud_model.pkl` is stored (e.g., gs://my-bucket/models/)
        serving_container_image_uri: Container image for serving (e.g., 'us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.1-7:latest')
    """
    print(f"Initializing Vertex AI for project '{project_id}' in region '{location}'...")
    aiplatform.init(project=project_id, location=location)

    # 1. Upload the Model to Model Registry
    print(f"Uploading model '{model_display_name}' to Vertex AI Model Registry...")
    model = aiplatform.Model.upload(
        display_name=model_display_name,
        artifact_uri=model_artifact_uri,
        serving_container_image_uri=serving_container_image_uri,
    )
    print(f"Model uploaded successfully! Model Resource Name: {model.resource_name}")

    # 2. Create an Endpoint
    endpoint_display_name = f"{model_display_name}-endpoint"
    print(f"Creating Endpoint '{endpoint_display_name}'...")
    endpoint = aiplatform.Endpoint.create(display_name=endpoint_display_name)
    print(f"Endpoint created! Endpoint Resource Name: {endpoint.resource_name}")

    # 3. Deploy the Model to the Endpoint
    print(f"Deploying model to endpoint (this may take 10-15 minutes)...")
    model.deploy(
        endpoint=endpoint,
        machine_type="n1-standard-4",
        min_replica_count=1,
        max_replica_count=3,
        traffic_split={"0": 100},
        sync=True
    )
    
    print("Deployment complete! The model is now ready to receive online predictions.")
    print(f"Endpoint ID for predictions: {endpoint.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy FraudLens XGBoost model to Vertex AI")
    parser.add_argument("--project_id", type=str, required=True, help="Google Cloud Project ID")
    parser.add_argument("--location", type=str, default="us-central1", help="Vertex AI region")
    parser.add_argument("--model_name", type=str, default="fraudlens-xgboost-v1", help="Display name for the model")
    parser.add_argument("--artifact_uri", type=str, required=True, help="GCS URI containing model.pkl (e.g., gs://my-bucket/models/)")
    # Using the pre-built XGBoost serving container from Google Cloud
    parser.add_argument("--container_uri", type=str, default="us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.1-7:latest", help="Serving container URI")
    
    args = parser.parse_args()
    
    deploy_to_vertex_ai(
        project_id=args.project_id,
        location=args.location,
        model_display_name=args.model_name,
        model_artifact_uri=args.artifact_uri,
        serving_container_image_uri=args.container_uri
    )
