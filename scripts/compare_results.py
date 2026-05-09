import json
import re


def extract_ssh_status(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    result = {
        "root_login_disabled": "PermitRootLogin no" in content,
        "password_auth_disabled": "PasswordAuthentication no" in content,
        "firewall_active": "Status: active" in content,
        "audit_rules_present": "-w /etc/passwd" in content,
    }

    return result


def build_comparison():
    before = {
        "root_login_disabled": False,
        "password_auth_disabled": False,
        "firewall_active": False,
        "audit_rules_present": False,
    }

    after = extract_ssh_status(
        "reports/after/validation_report.txt"
    )

    comparison = {
        "before": before,
        "after": after
    }

    return comparison


if __name__ == "__main__":

    results = build_comparison()

    with open(
        "reports/final/comparison.json",
        "w"
    ) as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))