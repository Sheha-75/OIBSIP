# Network Security Assessment Report

## Executive Summary

This security assessment was conducted on the local test environment using Nmap and Wireshark. The objective was to identify active network services, analyze captured network traffic, and evaluate potential security risks. The assessment identified two active services: SSH and an Apache web server hosting the DVWA application.

---

# Objective

Perform a basic network security assessment by:

* Discovering active network services.
* Capturing network traffic.
* Identifying potential security risks.
* Providing security recommendations.

---

# Scope

**Target Host**

* Hostname: localhost
* IP Address: 127.0.0.1

This assessment was performed in a controlled laboratory environment for educational purposes.

---

# Tools Used

* Kali Linux
* Nmap 7.95
* Wireshark 4.6.0
* Docker
* DVWA (Damn Vulnerable Web Application)

---

# Nmap Scan Results

The following command was used:

```bash
nmap -sV localhost
```

### Open Services

| Port | Service | Version                 | Status |
| ---- | ------- | ----------------------- | ------ |
| 22   | SSH     | OpenSSH 10.2p1 (Debian) | Open   |
| 8080 | HTTP    | Apache 2.4.25 (Debian)  | Open   |

### Analysis

### SSH Service (Port 22)

The SSH service allows secure remote administration of the system.

**Observation**

* SSH is enabled.
* OpenSSH version 10.2p1 was detected.

**Risk**

Leaving SSH exposed may allow unauthorized login attempts if weak credentials or poor access controls are used.

**Recommendation**

* Use strong passwords or SSH keys.
* Disable root login.
* Restrict SSH access using firewall rules.
* Keep OpenSSH updated.

---

### Apache Web Server (Port 8080)

Apache HTTP Server is running on port 8080 and is hosting the DVWA web application.

**Observation**

* HTTP service detected.
* Apache version 2.4.25 identified.

**Risk**

The application is accessible over HTTP rather than HTTPS. HTTP traffic is transmitted without encryption, making sensitive information vulnerable to interception in a real network environment.

Apache version information is also exposed, which could assist attackers in identifying known vulnerabilities.

**Recommendation**

* Enable HTTPS using TLS certificates.
* Keep Apache updated.
* Hide server version information.
* Disable unnecessary modules.

---

# Wireshark Traffic Analysis

Network traffic was captured using Wireshark while accessing the DVWA application hosted on localhost.

The capture included HTTP communication between the client browser and the Apache web server.

Protocols observed include:

* Ethernet
* IPv4
* TCP
* HTTP
* ARP

The HTTP packets contained:

* GET requests
* HTTP responses
* Source and destination IP addresses
* Source and destination ports
* Host information
* User-Agent information

This confirms successful communication between the client and the web application.

---

# Security Findings

| Finding                               | Risk   |
| ------------------------------------- | ------ |
| SSH service exposed                   | Medium |
| Apache version disclosure             | Medium |
| HTTP communication without encryption | High   |
| Web server accessible on port 8080    | Low    |

---

# Recommendations

* Upgrade Apache to the latest supported version.
* Replace HTTP with HTTPS.
* Limit SSH access to trusted users.
* Configure firewall rules to restrict unnecessary access.
* Remove unnecessary services.
* Perform regular vulnerability assessments.
* Continuously monitor network traffic for suspicious activity.

---

# Conclusion

The assessment identified two active services running on the target system: SSH and an Apache web server. Network traffic analysis confirmed successful HTTP communication between the client and the server. While this assessment was conducted within a controlled laboratory environment, it demonstrates common security considerations such as service exposure, software version management, and the importance of encrypted communications.

This assessment highlights the value of combining network scanning and packet analysis to evaluate the security posture of a system.

---

# Deliverables

* network_security_assessment.md
* nmap_results.txt
* wireshark_capture.pcap

---

# Author

**Shehani Lakshika Chandrakumar**

BSc (Hons) Information Technology (Cyber Security)

Oasis Infobyte Cyber Security Internship
