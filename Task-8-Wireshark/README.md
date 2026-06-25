# Network Traffic Capture and Analysis with Wireshark

## Overview

This project demonstrates how to capture and analyze network traffic using **Wireshark**, one of the most widely used network protocol analyzers. The objective is to observe network communication, filter HTTP traffic, and examine packet details to better understand how data is transmitted across a network.

This task was completed as part of the **Oasis Infobyte Cyber Security Internship**.

---

## Objective

* Capture network traffic using Wireshark.
* Filter and analyze HTTP packets.
* Understand the structure of network communication.
* Learn how packet analysis supports network troubleshooting and security investigations.

---

## Tools Used

* Kali Linux
* Wireshark 4.6.0
* Firefox Web Browser
* DVWA (Damn Vulnerable Web Application) running locally via Docker

---

## Project Structure

```text
Task-8-Wireshark/
│
├── wireshark_capture.pcap
├── README.md
└── screenshots/
    ├── interface_selection.png
    ├── capture_running.png
    ├── http_filter.png
    ├── packet_details.png
    └── project_structure.png
```

---

## Procedure

1. Verified that Wireshark was installed.
2. Launched Wireshark.
3. Selected the active network interface.
4. Started packet capture.
5. Generated HTTP traffic by accessing the local DVWA application (`http://localhost:8080`).
6. Stopped the capture after collecting traffic.
7. Applied the **http** display filter.
8. Examined the captured HTTP packets.
9. Saved the capture as **wireshark_capture.pcap**.

---

## Packet Analysis

The captured packets contained HTTP communication between the client and the local web server.

The analysis included:

* HTTP GET requests
* HTTP responses
* Source and destination IP addresses
* Source and destination ports
* Host information
* Request URI
* User-Agent header

These details demonstrate how a web browser communicates with a web application over the HTTP protocol.

---

## Protocols Observed

During packet capture, the following protocols were observed:

* Ethernet
* IPv4
* TCP
* HTTP
* ARP

Each protocol performs a different role within the network communication process.

---

## Security Importance

Network traffic analysis is an essential skill for cybersecurity professionals because it helps:

* Detect suspicious network activity.
* Troubleshoot communication issues.
* Investigate security incidents.
* Identify malicious connections.
* Monitor application behavior.

Packet analysis is widely used in Security Operations Centers (SOCs), Digital Forensics, Incident Response (DFIR), and Threat Hunting.

---

## Conclusion

Wireshark successfully captured and analyzed HTTP traffic generated between a client and a locally hosted web application. This exercise demonstrates the fundamentals of packet capture and protocol analysis, providing valuable insight into how network communication occurs and how packet analysis supports cybersecurity investigations.

---

## Deliverables

* wireshark_capture.pcap
* README.md
* Screenshots

---

## Author

**Shehani Lakshika Chandrakumar**

BSc (Hons) in Information Technology (Cyber Security)

Oasis Infobyte Cyber Security Internship
