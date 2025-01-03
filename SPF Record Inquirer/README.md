# SPF Record Inquirer  

This python script queries the specified DNS server(s) for text records that contain 'v=spf1' and prints them to the console.


### Usage:
To use the script, run it at the command line using the folling syntax:  
`./spf_inquire.py example.org`  



### Requirements:
This script requires the following to be install on the system running the script:  
1) Python3  
2) pip  
3) The dns.resolver Python module  

**To install Python3:**  
- On RHEL and compatible systems: `sudo dnf install python3`  
- On Debain and compatible systems: `sudo apt-get install python3`  


**To install pip:**  
- On RHEL and compatible systems: `sudo dnf install pip`
- On Debian and compatible systems: `sudo apt-get install pip`


**To install the dns.resolver Python module:**
- `pip install dnspython`
