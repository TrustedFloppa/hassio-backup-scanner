import os
import tarfile
import json

# Function to scan all .tar files in a directory and extract backup information
def scan_backups(directory):
    backups = []  # List to store information about backups

    # Loop through all files in the specified directory
    for file in os.listdir(directory):
        if file.endswith(".tar"):  # Check if the file has a .tar extension
            file_path = os.path.join(directory, file)  # Get the full file path
            try:
                # Open the tar file for reading
                with tarfile.open(file_path, "r") as tar:
                    # Log the tar file being inspected
                    print(f"Inspecting {file}")

                    # Look for backup.json in the tar archive
                    for member in tar.getmembers():
                        if os.path.basename(member.name) == "backup.json":
                            # Extract and read the backup.json file
                            with tar.extractfile(member) as f:
                                backup_data = json.load(f)  # Parse the JSON content
                                # Append relevant information to the backups list
                                backups.append({
                                    "file": file,  # File name of the backup
                                    "name": backup_data.get("name", "Unknown"),  # Backup name
                                    "date": backup_data.get("date", "Unknown"),  # Date of the backup
                                    "type": backup_data.get("type", "Unknown"),  # Type of backup (e.g., full, partial)
                                    "size": member.size  # Size of the backup.json file
                                })
                            break  # Stop searching after finding backup.json
                    else:
                        # Print a message if backup.json is not found in the archive
                        print(f"backup.json not found in {file}")
            except Exception as e:
                # Handle exceptions and print an error message
                print(f"Failed to read {file}: {e}")

    return backups  # Return the list of backups found

# Main function to interact with the user and display backup information
def main():
    # Prompt the user to enter the directory containing backups
    directory = input("Enter the directory containing backups: ").strip()
    if not os.path.isdir(directory):  # Validate that the input is a valid directory
        print("Invalid directory")
        return

    # Scan the directory for backups
    backups = scan_backups(directory)

    # Display the found backups or a message if none are found
    if backups:
        print("\nBackups found:")
        for backup in backups:
            print(f"File: {backup['file']}\n  Name: {backup['name']}\n  Date: {backup['date']}\n  Type: {backup['type']}\n  Size: {backup['size']} bytes\n")
    else:
        print("No valid backups found.")

# Entry point of the script
if __name__ == "__main__":
    main()
