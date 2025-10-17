# Databricks Notebook Example for local development

## Dual Env Setup

```python
from utils import is_running_in_databricks
import os

if not is_running_in_databricks():
    print("Not running in Databricks")
    from databricks.connect import DatabricksSession
    #from dotenv import load_dotenv

    # Clear any conflicting environment variables if they exist
    if 'DATABRICKS_AUTH_TYPE' in os.environ:
        os.environ.pop('DATABRICKS_AUTH_TYPE')
    if 'DATABRICKS_METADATA_SERVICE_URL' in os.environ:
        os.environ.pop('DATABRICKS_METADATA_SERVICE_URL')
    if 'DATABRICKS_SERVERLESS_COMPUTE_ID' in os.environ:
        os.environ.pop('DATABRICKS_SERVERLESS_COMPUTE_ID')

    # Use the profile from $HOME/.databrickscfg to connect to Databricks
    profile = "my_profile"
    spark = DatabricksSession.builder.profile(profile).getOrCreate()
    print(f"Using Databricks profile: {profile}")

    # Alternatively use .env to connect to databricks
    # load_dotenv('./.env')
    # DATABRICKS_HOST = os.getenv('host')
    # DATABRICKS_TOKEN = os.getenv('token')
    # spark = DatabricksSession.builder.host(DATABRICKS_HOST).token(DATABRICKS_TOKEN).serverless().getOrCreate()
```