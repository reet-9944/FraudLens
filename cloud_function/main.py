# cloud_function/main.py
import subprocess
import os

def fraudlens_retrain(request):
    """Cloud Function entry point that runs the model training script.
    Assumes the repository is mounted at /workspace (the default for GCF 2nd gen).
    """
    try:
        # Change to project root where src/ exists
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        result = subprocess.run(["python", "src/model_training.py"], cwd=cwd, capture_output=True, text=True, check=True)
        return {
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr,
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "stdout": e.stdout,
            "stderr": e.stderr,
            "returncode": e.returncode,
        }
