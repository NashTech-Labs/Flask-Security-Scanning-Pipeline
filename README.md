 # Security Compliance Workshop-day2-anshikavarshney

## Overview
This project demonstrates a **security scanning pipeline** for a sample Flask application using multiple tools:

- **Bandit** – Python static code analysis for security issues  
- **Semgrep** – Static analysis for patterns, bugs, and vulnerabilities  
- **Gitleaks** – Detect secrets and credentials in the repository  
- **OWASP ZAP** – Dynamic application security testing (DAST)  

The pipeline is implemented via **GitHub Actions**, generating reports as artifacts.

---

## 1. Pipeline Setup & Execution 

- **Workflow File**: `.github/workflows/day3-scan.yaml`  
- **Pipeline Steps**:
  1. Checkout repository
  2. Setup Python environment
  3. Install scanning tools (Bandit, Semgrep)
  4. Run Bandit and Semgrep
  5. Install and run Gitleaks
  6. Build and run Flask Docker container
  7. Run ZAP full scan
  8. Upload all reports as artifacts  

- **Artifacts Generated**:
  - `reports/bandit-report.html`  
  - `reports/semgrep-report.json`  
  - `reports/gitleaks-report.json`  
  - ZAP reports (`report_html.html`, `report_md.md`, `report_json.json`)  

**Pipeline successfully executes and uploads all reports.**

---

## 2. Vulnerability Identification
During the scans, the following vulnerabilities/secrets were identified:

| Vulnerability                                  | Impact                                      | Recommended Fix                                      |
|------------------------------------------------|--------------------------------------------|------------------------------------------------------|
| Hardcoded secret in `app.py` (example API key)| Exposed secrets can be stolen from the repo, leading to unauthorized access | Move secret to environment variable or use GitHub Secrets |
| Use of outdated Flask version (`1.0`)         | Older versions may have known CVEs and security flaws (XSS, SSRF) | Upgrade Flask to latest stable version (e.g., `Flask>=2.3.2`) |

**Evidence**: Reports are available in the pipeline artifacts and in reports  and screenshorts folder.

---

## 3. Fix Demonstration 

- **Fix Applied**:  
  - Updated Flask version in `requirements.txt` from `Flask==1.0` → `Flask>=2.3.2`  
  - Removed any hardcoded secrets and replaced with environment variables

- **Pipeline Re-run**:
  - Bandit, Semgrep, Gitleaks, and ZAP scans were executed again  
  - Vulnerabilities from previous run were resolved  
  - Updated reports uploaded as artifacts

---
**Evidence**: Reports are available in the pipeline artifacts and in reports-after-fix folder

## Running the Application Locally

               git clone <repo-url>
               cd security-compliance-workshop/day3
               docker build -t day3-flask .
               docker run -d -p 5001:5000 --env-file .env day3-flask 
               curl http://127.0.0.1:5001/
               curl "http://127.0.0.1:5001/calc?expr=5*10"


