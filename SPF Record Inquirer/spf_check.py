#!/bin/python3

import dns.resolver,re,sys

def get_spf_record(domain):
  
    # Specifies resolver    
    resolver = dns.resolver.Resolver()

    # Specify the nameserver(s)
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']

    # Performs a DNS query for the a txt record against the specified domain
    result = resolver.resolve(domain, 'TXT')

    # Prints only text records with 'v=spf1' in them and removes leading and trailing quotation marks
    for rdata in result:
        if re.search('v=spf1', (str(rdata))):
        print((str(rdata)).strip("\""))

# Accesses first argument sent to this script
domain = sys.argv[1] 

get_spf_record(domain)READ
