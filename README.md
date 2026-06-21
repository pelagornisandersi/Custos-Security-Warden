# Custos - Security Warden

## Overview

Custos is a lightweight cybersecurity dashboard for Linux that provides real-time system monitoring, process analysis, file integrity monitoring, port scanning, and network connection visibility.

## Features

- Real-time CPU, RAM, and Disk monitoring
- Security score calculation
- Process monitoring and risk classification
- File integrity monitoring
- Security alerts system
- Localhost port scanning
- Active network connection monitoring

## Technologies

- Python
- CustomTkinter
- psutil
- socket
- hashlib

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/custos-security-warden.git
cd custos-security-warden
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Linux/macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

---

## Requirements

- Python 3.10+
- Linux (developed and tested on Fedora)
- CustomTkinter
- psutil

---

## Project Structure

```text
custos/
├── core/
│   ├── file_monitor.py
│   ├── network_monitor.py
│   ├── port_scanner.py
│   ├── process_monitor.py
│   └── security_score.py
│
├── widgets/
│   ├── metric_card.py
│   ├── process_panel.py
│   ├── network_panel.py
│   ├── alert_panel.py
│   └── security_score_card.py
│
├── assets/
│   └── dashboard.png
│
├── main.py
├── requirements.txt
└── README.md
```

## Features

- Real-time CPU, RAM, and Disk monitoring
- Security score calculation
- Process monitoring and risk classification
- File Integrity Monitoring (FIM)
- Port scanning
- Network connection monitoring
- Security alert system

...

## Screenshots

![Dashboard](assets/dashboard.png)
...

## Future Improvements

- PDF security reports
- Threat intelligence integration
- VirusTotal API support
- Suspicious IP detection
