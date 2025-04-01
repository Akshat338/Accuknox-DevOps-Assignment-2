import os
import subprocess
import logging
from datetime import datetime

# Set up logging for backup reports
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("backup_report.log"),
        logging.StreamHandler()
    ]
)

# Configuration
LOCAL_DIRECTORY = "/path/to/local/directory"  # Replace with the directory to back up
REMOTE_SERVER = "user@remote_server_ip"  # Replace with your remote server's username and IP
REMOTE_DIRECTORY = "/path/to/remote/directory"  # Replace with the directory on the remote server

def backup_directory():
    try:
        # Construct the rsync command
        command = [
            "rsync",
            "-avz",  # Archive mode, verbose, compressed
            LOCAL_DIRECTORY,
            f"{REMOTE_SERVER}:{REMOTE_DIRECTORY}"
        ]
        
        # Run the rsync command
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Log success
        logging.info(f"Backup completed successfully:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        # Log failure
        logging.error(f"Backup failed:\n{e.stderr}")

if __name__ == "__main__":
    logging.info("Starting backup process...")
    backup_directory()
