# SQL Injection Demonstration Using DVWA

## Objective

The objective of this task is to understand how SQL injection vulnerabilities occur and how they can be identified and mitigated in web applications.

## Lab Environment

* Kali Linux
* Docker
* DVWA (Damn Vulnerable Web Application)
* Firefox Browser

## Setup Procedure

1. Installed Docker on Kali Linux.
2. Downloaded and started the DVWA container.
3. Opened DVWA in the browser using `http://localhost:8080`.
4. Created and initialized the database.
5. Logged in using the default credentials.
6. Set the DVWA security level to **Low**.

## Normal Application Behavior

A valid User ID was entered into the SQL Injection module.

The application returned the corresponding user information from the database.

## Vulnerability Overview

The application directly incorporates user input into SQL queries without proper validation or parameterization.

This allows an attacker to manipulate the query logic and access unintended data.

## Impact

SQL injection vulnerabilities can lead to:

* Unauthorized access to sensitive information
* Data leakage
* Authentication bypass
* Data modification or deletion
* Complete database compromise

## Mitigation Techniques

* Use prepared statements
* Implement parameterized queries
* Validate and sanitize user input
* Apply the principle of least privilege
* Use Web Application Firewalls (WAFs)

## Conclusion

This task demonstrated how improper handling of user input can introduce SQL injection vulnerabilities. Understanding these issues helps developers build secure applications and enables security professionals to identify and mitigate risks effectively.
