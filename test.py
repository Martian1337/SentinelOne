import json
import argparse
import os

def read_domains(file_path):
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def create_rule(domain):
    return {
        "action": "Block",
        "application": [],
        "application_type": "any",
        "description": None,
        "direction": "inbound",
        "local_host": [],
        "local_host_type": "any",
        "local_port": [],
        "local_port_type": "any",
        "location_ids": [],
        "location_type": "all",
        "name": f"block {domain} ITS-114",
        "os_types": ["osx", "windows"],
        "profile": "any",
        "protocol": None,
        "remote_host": [domain],
        "remote_host_type": "fqdn",
        "remote_hosts": [{"type": "fqdn", "values": [domain]}],
        "remote_port": [],
        "remote_port_type": "any",
        "rule_type": "custom",
        "scope": "site",
        "service": None,
        "status": "Enabled",
        "tag_ids": [],
        "tag_names": []
    }

def main():
    parser = argparse.ArgumentParser(description='Generate configuration rules from a list of domain names.')
    parser.add_argument(
        'domains_file',
        type=str,
        nargs='?',
        default=None,
        help='Path to the file containing the list of domains (optional). If not provided, defaults to "domains.txt".'
    )
    args = parser.parse_args()
    
    if args.domains_file is None:
        args.domains_file = 'domains.txt'
    
    if not os.path.isfile(args.domains_file):
        print(f"Error: The file '{args.domains_file}' does not exist.")
        return

    domains = read_domains(args.domains_file)
    rules = [create_rule(domain) for domain in domains]
    rules_json = json.dumps(rules, indent=4)
    print(rules_json)

    with open('rules.json', 'w') as f:
        f.write(rules_json)

if __name__ == "__main__":
    main()
