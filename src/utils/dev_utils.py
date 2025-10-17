import os
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ImportFormat
from typing import Any

def is_running_in_databricks():
    """Detect if code is running in Databricks workspace"""
    # Check for Databricks environment variables
    databricks_env_vars = [
        "DB_CLUSTER_ID",
        "DB_IS_DRIVER",
        "DB_DRIVER_IP",
        "DATABRICKS_RUNTIME_VERSION",
    ]

    for var in databricks_env_vars:
        if var in os.environ:
            return True

    return False


def upload_file_to_dbx(
    w: WorkspaceClient,
    local_path: str,
    dest_path: str,
    import_format: ImportFormat = ImportFormat.AUTO,
    overwrite: bool = True,
) -> None:
    """
    Upload a file from local_path to Databricks workspace or volume at dest_path.

    Args:
        w: WorkspaceClient instance.
        local_path: Path to the local file.
        dest_path: Destination path in Databricks workspace or volume.
        import_format: ImportFormat for the file upload.
        overwrite: Whether to overwrite the file if it exists.
    """
    with open(local_path, "rb") as f:
        file_bytes: bytes = f.read()
    
    # Check if destination is a volume path (starts with /Volumes/) or workspace path
    if dest_path.startswith("/Volumes/"):
        # Use files API for volume uploads
        if overwrite:
            w.files.upload(dest_path, file_bytes, overwrite=True)
        else:
            w.files.upload(dest_path, file_bytes)
        print(f"Copied {local_path} to {dest_path} in Databricks volume.")
    else:
        # Use workspace API for workspace uploads
        w.workspace.upload(dest_path, file_bytes, format=import_format, overwrite=overwrite)
        print(f"Copied {local_path} to {dest_path} in Databricks workspace.")