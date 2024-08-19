import json

# Path to the file containing the list of domains
domains_file_path = 'domains.txt'

def read_domains(file_path):
    with open(file_path, 'r') as file:
        # Read lines and strip any surrounding whitespace
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
    # Read domains from file
    domains = read_domains(domains_file_path)
    
    # Generate rules for each domain
    rules = [create_rule(domain) for domain in domains]

    # Convert to JSON and print or save to file
    rules_json = json.dumps(rules, indent=4)
    print(rules_json)

    # Optionally save to a file
    with open('rules.json', 'w') as f:
        f.write(rules_json)

if __name__ == "__main__":
    main()
