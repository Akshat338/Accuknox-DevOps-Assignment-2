# Accuknox-DevOps-Assessment-2

# Problem Statement 2: 

# 1. System Health Monitoring Script: 
Develop a script that monitors the health of a Linux system. It should check CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script should send an alert to the console or a log file.

## Solution:
Python script that monitors the health of a Linux system. It checks CPU usage, memory usage, disk space, and the number of running processes. If any of the metrics exceed predefined thresholds, it logs the alert in a file and displays it in the console:

import psutil
import logging

# Set up logging to a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("system_health.log"),
        logging.StreamHandler()
    ]
)

# Define thresholds
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 80  # Percentage
PROCESS_THRESHOLD = 200  # Number of processes

def monitor_system():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")

    # Check memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")

    # Check disk space usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High disk usage detected: {disk_usage}%")

    # Check number of running processes
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f"High number of processes detected: {process_count}")

if __name__ == "__main__":
    while True:
        monitor_system()

# Explaination:        
psutil: A library used to fetch system metrics like CPU, memory, disk usage, and processes. It must be installed (pip install psutil) to use this script.

Thresholds: You can adjust CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, and PROCESS_THRESHOLD as needed for your monitoring requirements.

Logging: Alerts are both logged to the console and saved in a file called system_health.log.

Continuous Monitoring: The script runs indefinitely, checking system health at regular intervals.

# 2.Automated Backup Solution: 
Write a script to automate the backup of a specified directory to a remote server or a cloud storage solution. The script should provide a report on the success or failure of the backup operation. 

## Solution
Python script that automates the backup of a specified directory to a remote server using the rsync command over SSH. The script also generates a report indicating whether the operation succeeded or failed:

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

## Explanation:

How It Works:
### 1.Configuration:

Replace LOCAL_DIRECTORY with the path of the directory you want to back up.

Replace REMOTE_SERVER with your remote server's username and IP address.

Replace REMOTE_DIRECTORY with the path to the directory on the remote server where the backup will be stored.

### 2.rsync Command:

The rsync command efficiently syncs files and directories from the local machine to the remote server.

It uses the -avz flags for archive mode (preserves file permissions), verbosity, and compression.

### 3.Logging:

Logs all backup results in backup_report.log.

Indicates success with detailed output or logs any errors if the operation fails.

### 4.SSH Authentication:

Ensure that passwordless authentication is set up between your local machine and the remote server for rsync to work seamlessly. You can do this by generating SSH keys using ssh-keygen and copying the public key to the remote server using ssh-copy-id.


