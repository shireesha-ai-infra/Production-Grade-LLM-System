import mlflow

def log_run(metrics, params):
    mlflow.log_metrics(metrics)
    mlflow.log_params(params)