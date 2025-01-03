#!/bin/python3

import dns.resolver,re,sys

def get_ns_record(domain):

    resolver = dns.resolver.Resolver()

    # Specify the nameserver(s)
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Cloudflare public DNS server

    # Perform a DNS query
    result = resolver.resolve(domain, 'NS')

    # Prints the NS records
    for rdata in result:
         print(rdata)

domain = sys.argv[1]

get_ns_record(domain)
