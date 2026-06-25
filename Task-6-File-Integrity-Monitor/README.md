# File Integrity Monitor

## Overview

This project is a Python-based File Integrity Monitoring (FIM) tool developed as part of the Oasis Infobyte Cyber Security Internship.

The application monitors files within a specified directory by generating SHA-256 hashes and comparing them against a trusted baseline. It detects unauthorized file modifications, newly created files, and deleted files, helping maintain the integrity of critical system files.

---

## Objectives

* Monitor file integrity using cryptographic hashing.
* Detect unauthorized file modifications.
* Identify newly added files.
* Detect deleted files.
* Generate a scan report for security monitoring.
* Maintain a trusted baseline for comparison.

---

## Features

* SHA-256 file hashing
* Automatic baseline creation
* Baseline loading from JSON
* Detection of modified files
* Detection of newly added files
* Detection of deleted files
* Recursive directory scanning
* Timestamped scan reports
* Interactive baseline update option
* Clean and readable console output

---

## Technologies Used

* Python 3
* hashlib
* json
* pathlib
* datetime

---

## Project Structure

```text
Task-6-File-Integrity-Monitor/
│
├── baseline_hashes.json
├── file_integrity_monitor.py
├── scan_report.txt
├── README.md
│
├── screenshots/
│
└── test_files/
    ├── test1.txt
    ├── test3.txt
```

---

## How It Works

1. Scan all files inside the monitored directory.
2. Calculate the SHA-256 hash for each file.
3. Load the trusted baseline.
4. Compare current hashes with the baseline.
5. Detect:

   * Modified files
   * New files
   * Deleted files
6. Display the results.
7. Save the scan report.
8. Optionally update the baseline.

---

## Running the Program

```bash
python3 file_integrity_monitor.py
```

---

## Sample Output

```
==================================================
      FILE INTEGRITY MONITOR REPORT
==================================================

Scan Time : 2026-06-25 10:20:56

No changes detected.

==================================================
Scan Completed
==================================================
```

When file changes are detected:

```
Modified Files
--------------
• test1.txt

New Files
---------
• test3.txt

Deleted Files
-------------
• test2.txt
```

---

## Security Benefits

* Detects unauthorized file modifications.
* Helps identify potential malware activity.
* Supports system integrity monitoring.
* Provides a trusted baseline for verification.
* Improves security monitoring and incident detection.

---

## Future Enhancements

* Email alerts for detected changes.
* Real-time monitoring using filesystem events.
* Logging to a database.
* Graphical User Interface (GUI).
* Monitoring multiple directories.
* Export reports in PDF or CSV format.

---

## Author

**Shehani Lakshika Chandrakumar**

BSc (Hons) in Information Technology (Cyber Security)

Oasis Infobyte Cyber Security Internship
