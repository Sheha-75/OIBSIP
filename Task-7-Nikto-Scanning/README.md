# Vulnerability Scanning with Nikto

## Objective

The objective of this task is to perform a vulnerability assessment of a web server using Nikto and identify potential security weaknesses.

---

## Tools Used

* Kali Linux
* Nikto 2.5.0
* Docker
* DVWA (Damn Vulnerable Web Application)

---

## Target

* Host: localhost
* Port: 8080
* Web Server: Apache 2.4.25 (Debian)

---

## Scan Command

```bash
nikto -h http://localhost:8080 | tee nikto_scan_results.txt
```

---

## Key Findings

The vulnerability scan identified several security issues:

* Session cookies without the HttpOnly attribute.
* Missing X-Frame-Options header.
* Missing X-Content-Type-Options header.
* Outdated Apache web server version.
* Directory indexing enabled.
* Configuration directory accessible.
* Apache default files exposed.
* Publicly accessible `.gitignore` file.

---

## Risk Assessment

| Vulnerability                      | Risk Level |
| ---------------------------------- | ---------- |
| Outdated Apache Version            | High       |
| Accessible Configuration Directory | High       |
| Missing HttpOnly Cookies           | Medium     |
| Missing X-Frame-Options            | Medium     |
| Directory Indexing                 | Medium     |
| Exposed .gitignore                 | Medium     |
| Missing X-Content-Type-Options     | Low        |
| Apache Default Files               | Low        |

---

## Mitigation Recommendations

* Upgrade Apache to the latest supported version.
* Enable HttpOnly and Secure cookie attributes.
* Configure X-Frame-Options to prevent clickjacking.
* Configure X-Content-Type-Options to prevent MIME type sniffing.
* Disable directory indexing.
* Restrict access to sensitive configuration files.
* Remove unnecessary default files.
* Block access to development-related files such as `.gitignore`.

---

## Conclusion

Nikto successfully identified multiple security weaknesses within the intentionally vulnerable DVWA environment. This exercise demonstrates how automated vulnerability scanners help security professionals detect insecure configurations and prioritize remediation efforts.

---

## Deliverables

* nikto_scan_results.txt
* README.md

---

## Author

Shehani Lakshika Chandrakumar

BSc (Hons) Information Technology (Cyber Security)

Oasis Infobyte Cyber Security Internship
