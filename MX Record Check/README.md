# MX Record Check

This python script queries the specified DNS server(s) for all MX records for a given domain.

### Usage:
To use the script, run it at the command line using the folling syntax:  
`./mx_check.py example.org`  

### Requirements:
This script requires the following:
1) Installation of Python3  
2) Installation of pip  
3) Instalaion of The dns.resolver Python module
4) Mark the script as executable  

**To install Python3:**  
- On RHEL and compatible systems: `sudo dnf install python3`  
- On Debain and compatible systems: `sudo apt-get install python3`  


**To install pip:**  
- On RHEL and compatible systems: `sudo dnf install pip`
- On Debian and compatible systems: `sudo apt-get install pip`


**To install the dns.resolver Python module:**
- `pip install dnspython`

**To mark the script as executable:**
- `chmod +x mx_check.py`
