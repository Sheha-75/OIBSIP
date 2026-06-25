from datetime import datetime
import hashlib
import json
from pathlib import Path

# Folder to monitor
MONITOR_FOLDER = Path("test_files")

# Baseline hash database
BASELINE_FILE = Path("baseline_hashes.json")

def calculate_sha256(file_path):
    """
    Calculate and return the SHA-256 hash of a file.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_files():
    """
    Scan all files in the monitored folder
    and return their SHA-256 hashes.
    """

    hashes = {}

    for file_path in MONITOR_FOLDER.rglob("*"):

        if file_path.is_file():

            file_hash = calculate_sha256(file_path)

            if file_hash:
                hashes[file_path.name] = file_hash

    return hashes
def save_baseline(hashes, message="Baseline saved successfully."):
    """
    Save file hashes to the baseline JSON file.
    """

    with open(BASELINE_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

    print(message)

def load_baseline():
    """
    Load the baseline hashes from the JSON file.
    """

    if not BASELINE_FILE.exists():
        return None

    with open(BASELINE_FILE, "r") as file:
        return json.load(file)

def save_scan_report(modified, new_files, deleted_files):
    """
    Save scan results to a text report.
    """

    with open("scan_report.txt", "w") as report:

        report.write("=" * 50 + "\n")
        report.write("FILE INTEGRITY MONITOR REPORT\n")
        report.write("=" * 50 + "\n\n")

        report.write(
            f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        if not modified and not new_files and not deleted_files:
            report.write("No changes detected.\n")

        if modified:
            report.write("Modified Files:\n")
            for file in modified:
                report.write(f" - {file}\n")
            report.write("\n")

        if new_files:
            report.write("New Files:\n")
            for file in new_files:
                report.write(f" - {file}\n")
            report.write("\n")

        if deleted_files:
            report.write("Deleted Files:\n")
            for file in deleted_files:
                report.write(f" - {file}\n")

    print("\n📄 Scan report saved as scan_report.txt")

def compare_hashes(old_hashes, new_hashes):
    """
    Compare baseline hashes with current hashes.
    """

    modified = []
    new_files = []
    deleted_files = []

    # Check for modified and new files
    for filename, current_hash in new_hashes.items():

        if filename not in old_hashes:
            new_files.append(filename)

        elif old_hashes[filename] != current_hash:
            modified.append(filename)

    # Check for deleted files
    for filename in old_hashes:

        if filename not in new_hashes:
            deleted_files.append(filename)

    return modified, new_files, deleted_files

if __name__ == "__main__":

    current_hashes = scan_files()

    baseline = load_baseline()

    if baseline is None:

        save_baseline(current_hashes)

    else:

        modified, new_files, deleted_files = compare_hashes(
            baseline,
            current_hashes
        )

        save_scan_report(modified, new_files, deleted_files)

        print("\n" + "=" * 50)
        print("      FILE INTEGRITY MONITOR REPORT")
        print("=" * 50)

        print(f"Scan Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        if not modified and not new_files and not deleted_files:
            print("No changes detected.")

        else:

            if modified:
                print("Modified Files")
                print("-" * 30)
                for file in modified:
                    print(f"• {file}")
                print()

            if new_files:
                print("New Files")
                print("-" * 30)
                for file in new_files:
                    print(f"• {file}")
                print()

            if deleted_files:
                print("Deleted Files")
                print("-" * 30)
                for file in deleted_files:
                    print(f"• {file}")

        print("\n" + "=" * 50)
        print("Scan Completed")
        print("=" * 50)

        choice = input("\nUpdate baseline with current file state? (y/n): ").lower()

        if choice == "y":
            save_baseline(current_hashes)
            print("Baseline updated successfully.")
        else:
            print("Baseline was not changed.")
