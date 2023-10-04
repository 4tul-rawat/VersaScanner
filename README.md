# VersaScanner

A security tool that performs scans on a target using OpenVAS, Zap, and Nexpose, then compiles and combines the scan findings.

---

## Usage

### Start a scan against a Target

`./main.py --scan-name <scan-name> --target <url>`


### Get scan result

`./main.py --scan-name <scan-name>`


### Pause/Resume a scan result

- `./main.py --scan-name <scan-name> --pause`
- `./main.py --scan-name <scan-name> --resume`

---

## Prerequisites

- Python 3
- Zap
- Nexpose
- OpenVAS

---

## Installation

`pip3 install -r requirements.txt`

OR

Run in Virtual Env:

```console
python3 -m venv .venv

source .venv/bin/activate

pip3 install -r requirements.txt
```

---

## Configuration

The configuration of scanners will be in Environment File `.env`. There is sample `.env.example` file in the codebase, update the values with the proper API Keys and Credentials details before using. Rename it to `.env`.

---

## Targets to Test
- http://scanme.nmap.org
- http://webscantest.com

---

## ToDo
- [ ] Dockerize
- [ ] Add Nessus
- [ ] Error Stack
- [ ] auto reload
- [ ] Remove logs
- [ ] Save to CSV
- [ ] Make it interactive
- [ ] OOPs
- [ ] Improve Scan Results and Output
- [ ] Color logging

---

### Scanner Interface:

- start
- scan
- get_scan_status
- get_scan_results
- is_valid_scan
- list_scans
- pause
- resume
- stop
