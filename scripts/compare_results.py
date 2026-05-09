import json
import re


def extract_lynis_score(filepath):

    with open(filepath, "r") as f:
        content = f.read()

    match = re.search(
        r"Hardening index\s*:\s*(\d+)",
        content
    )

    if match:
        return int(match.group(1))

    return None


def extract_validation(filepath):

    with open(filepath, "r") as f:
        content = f.read()

    return {
        "root_login_disabled":
            "PermitRootLogin no" in content,

        "password_auth_disabled":
            "PasswordAuthentication no" in content,

        "firewall_active":
            "Status: active" in content,

        "audit_rules_present":
            "-w /etc/passwd" in content,
    }


if __name__ == "__main__":

    validation = extract_validation(
        "reports/after/validation_report.txt"
    )

    lynis_score = extract_lynis_score(
        "reports/final/lynis_report.txt"
    )

    results = {

        "before": {
            "root_login_disabled": False,
            "password_auth_disabled": False,
            "firewall_active": False,
            "audit_rules_present": False,
            "lynis_score": 0
        },

        "after": {
            **validation,
            "lynis_score": lynis_score
        }
    }

    with open(
        "reports/final/comparison.json",
        "w"
    ) as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))