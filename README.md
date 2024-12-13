# Hass.io Backup Scanner

This Python script scans a specified directory for `.tar` backup files created by Home Assistant (`Hass.io`). It looks for a `backup.json` file inside each `.tar` archive, extracts relevant information from it, and presents a summary of the backups, including the backup name, date, type, and size.

## Features

- Scans a directory for `.tar` backup files.
- Searches for `backup.json` inside each `.tar` archive.
- Extracts and displays important information from `backup.json`:
  - **Name**: The name of the backup.
  - **Date**: The date when the backup was created.
  - **Type**: The type of the backup (Full, Snapshot, etc.).
  - **Size**: The size of the backup archive.
- Gracefully handles errors during file extraction.
- Outputs a summary of valid backups found in the directory.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/TrustedFloppa/hassio-backup-scanner.git
Navigate to the project directory:

bash
Skopiuj kod
cd hassio-backup-scanner
Ensure Python 3 is installed on your system.

Install required Python libraries:

```bash
pip install json
```
Usage
Run the script:


```bash
python backup_scanner.py
```
When prompted, enter the directory path where your .tar backup files are stored. 

This could be the folder containing Home Assistant backups, often found under /mnt/backup or a custom directory.

The script will scan the directory for .tar files, extract backup.json if available, and display the backup details.

Example Output:
```
Enter the directory containing backups: /mnt/backup

Inspecting backup1.tar
backup.json found in backup1.tar
Inspecting backup2.tar
backup.json not found in backup2.tar

Backups found:
File: backup1.tar
  Name: Home Assistant Full Backup
  Date: 2024-12-01
  Type: Full
  Size: 12345678 bytes
```
