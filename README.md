# MalluScanner - File Scanning with Python

![Security](https://img.shields.io/badge/Security-Cyber%20Defense-brightgreen)
![Language](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-orange)

## Overview

This Python script provides a basic implementation of file and directory scanning for potential threats using SHA-256 hashing and fake malware detection. It's designed for educational purposes and serves as a starting point for building more robust security solutions.

## Features

- Supports scanning of multiple file extensions.
- Calculates the SHA-256 hash of files.
- Simulates a malware database for demonstration purposes.
- Recursively scans directories for files.
- Utilizes the `termcolor` library for colorful console output.

## Usage

1. Clone or download the repository to your local machine:
   ```bash
   git clone https://github.com/AbhishekNair1289/MalluScanner.git
   ```
2. Make sure you have Python installed (Python 3.6 or higher is recommended).
3. Install the `termcolor` library using pip:

   ```bash
   pip install termcolor
   ```

4. Modify the `allowed_extensions` list with the file extensions you want to scan.
5. Run the script:

   ```bash
   python malluscanner.py
   ```

6. Enter the directory path you want to scan when prompted.

## Example Output

The script will display the results of the file scan in your console. It will show whether a file is skipped due to an unsupported file type, if malware is detected, or if no threats are found.

## Disclaimer

This code is provided for educational and demonstrative purposes only. It is not a complete or production-ready security solution. For real-world applications, consider integrating with a reputable antivirus or security software.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, suggest improvements, or report issues. Your feedback is highly appreciated! 🚀🔒
