#!/bin/python3

import dns.resolver,re,sys

def get_mx_record(domain):

    resolver = dns.resolver.Resolver()

    # Specify the nameserver(s)
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Google public DNS servers

    # Perform a DNS query
    result = resolver.resolve(domain, 'MX')

    # Prints the MX record
    for rdata in result:
         print(rdata)

domain = sys.argv[1]

get_mx_record(domain)
