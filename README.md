# Lightweight API Security Testing Framework

A modular, signature-based Application Security Testing (AST) utility written in Python. This framework automates the discovery of critical vulnerabilities listed in the **OWASP API Security Top 10**, focusing on access control mechanisms and server infrastructure configurations.

## 🚀 Features
* **Broken Object Level Authorization (BOLA) Detection:** Simulates authorization bypass attempts by fuzzing resource identifiers to detect unauthorized data exposure.
* **Security Posture Auditing:** Evaluates HTTP response headers to flag missing defensive configurations (`X-Frame-Options`, `Content-Security-Policy`, `X-Content-Type-Options`).
* **Informative Security Alert System:** Generates clean, structured CLI alert notifications classifying structural risks (`[ALERT]`, `[WARN]`, `[OK]`).

## 🛠️ Architecture & Workflow



1. **Target Initialization:** Reads and validates the target RESTful API baseline URL.
2. **Payload Delivery:** Dispatches automated HTTP `GET` requests to targeted endpoint arrays.
3. **Response Parsing:** Analyzes network HTTP status codes and maps underlying response headers.
4. **Reporting:** Prints an actionable, terminal-based vulnerability assessment matrix.

## 📦 Installation & Usage

### Prerequisites
* Python 3.x Installed
* `requests` library

### Setup
1. Clone this repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install requests
## 🛡️ Ethical Disclaimer

This tool is developed strictly for educational, research, and authorized penetration testing evaluation purposes. Scanning target environments without explicit, prior written consent from the infrastructure asset owner is illegal and violates authorization policies. The developer assumes no liability for misuse or damage caused by this utility.
