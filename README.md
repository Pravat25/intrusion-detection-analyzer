 Intrusion Detection Log Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Tool-Intrusion%20Detection-red)
![Status](https://img.shields.io/badge/Status-Active-success)

## Overview

Intrusion Detection Log Analyzer is a Python-based tool that analyzes authentication logs to detect suspicious login attempts and potential brute-force attacks.

This project simulates basic detection rules used in Security Operations Centers (SOC).

## Features

- Detect brute-force login attempts
- Identify suspicious IP addresses
- Analyze authentication logs
- Generate intrusion alerts

## Project Structure


intrusion-detection-analyzer
│
├── ids_analyzer.py
├── auth_log_sample.txt
└── README.md


## How to Run

Clone repository


git clone https://github.com/Pravat25/intrusion-detection-analyzer.git


Navigate to folder


cd intrusion-detection-analyzer


Run script


python ids_analyzer.py


Enter log file


auth_log_sample.txt


## Example Output


===== Intrusion Detection Report =====

 ALERT: Possible brute-force attack from 192.168.1.10 (5 attempts)

 Suspicious activity from 10.0.0.5 (3 attempts)


## Disclaimer

Educational purposes only.
