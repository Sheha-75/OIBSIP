# Basic Network Scanning with Nmap

## Objective

The objective of this task is to perform a basic network scan using Nmap to identify open ports and services on a target machine within a controlled environment.

## Tools Used

* Nmap 7.95
* Kali Linux
* Windows 11
* Virtual Machine (if applicable)

## Lab Setup

| Machine    | IP Address      | Role    |
| ---------- | --------------- | ------- |
| Kali Linux | 192.168.159.134 | Scanner |
| Windows 11 | 192.168.159.13  | Target  |

## Commands Used

```bash
nmap --version
hostname -I
ipconfig
nmap 192.168.159.13
nmap 192.168.159.13 -oN nmap_scan_results.txt
```

## Scan Results

The target host was successfully identified as active on the network.

Nmap scanned the top 1000 TCP ports and reported that all ports were in a filtered state.

```text
Host is up.

All 1000 scanned ports on 192.168.159.13 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
```

## Analysis

The scan results indicate that the target system is protected by a firewall.

Filtered ports mean that Nmap did not receive a response from the target ports because firewall rules or packet filtering mechanisms blocked the scan requests.

No publicly accessible services were detected during the assessment.

## Security Recommendations

* Keep Windows Defender Firewall enabled.
* Disable unnecessary network services.
* Periodically perform network scans to identify exposed services.
* Ensure operating systems and applications are updated regularly.

## Conclusion

The Nmap scan successfully discovered the target host and confirmed that network filtering controls were in place. Although no open ports were identified, the task demonstrated essential reconnaissance techniques, including host discovery, port scanning, and attack surface analysis.
