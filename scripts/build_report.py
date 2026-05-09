import json


with open("reports/final/comparison.json") as f:
    data = json.load(f)


html = f"""
<html>

<head>

    <title>Audit Hardening Report</title>

    <style>

        body {{
            font-family: Arial;
            margin: 40px;
            background-color: #f4f4f4;
            color: #222;
        }}

        h1 {{
            color: #111;
        }}

        h2 {{
            margin-top: 40px;
            color: #333;
        }}

        .good {{
            color: green;
            font-weight: bold;
        }}

        .bad {{
            color: red;
            font-weight: bold;
        }}

        .score {{
            font-size: 24px;
            font-weight: bold;
        }}

        table {{
            border-collapse: collapse;
            width: 90%;
            background: white;
            margin-top: 20px;
        }}

        td, th {{
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
        }}

        th {{
            background-color: #e8e8e8;
        }}

    </style>

</head>

<body>

<h1>Audit & Hardening Report</h1>

<p>
Automated Linux hardening and security audit using
Docker, Ansible and Lynis.
</p>

<h2>Lynis Hardening Score</h2>

<table>

<tr>
    <th>State</th>
    <th>Score</th>
</tr>

<tr>
    <td>Before Hardening</td>
    <td class="bad score">
        {data['before']['lynis_score']}
    </td>
</tr>

<tr>
    <td>After Hardening</td>
    <td class="good score">
        {data['after']['lynis_score']}
    </td>
</tr>

</table>

<h2>Security Controls Validation</h2>

<table>

<tr>
    <th>Security Control</th>
    <th>Before</th>
    <th>After</th>
</tr>

<tr>
    <td>Root SSH Login Disabled</td>
    <td class="bad">
        {data['before']['root_login_disabled']}
    </td>
    <td class="good">
        {data['after']['root_login_disabled']}
    </td>
</tr>

<tr>
    <td>Password Authentication Disabled</td>
    <td class="bad">
        {data['before']['password_auth_disabled']}
    </td>
    <td class="good">
        {data['after']['password_auth_disabled']}
    </td>
</tr>

<tr>
    <td>Firewall Active</td>
    <td class="bad">
        {data['before']['firewall_active']}
    </td>
    <td class="good">
        {data['after']['firewall_active']}
    </td>
</tr>

<tr>
    <td>Audit Rules Present</td>
    <td class="bad">
        {data['before']['audit_rules_present']}
    </td>
    <td class="good">
        {data['after']['audit_rules_present']}
    </td>
</tr>

</table>

<h2>Implemented Security Measures</h2>

<ul>
    <li>SSH root login disabled</li>
    <li>Password authentication disabled</li>
    <li>UFW firewall configured with deny-all incoming policy</li>
    <li>Audit rules added for sensitive files</li>
    <li>Vulnerable services removed</li>
    <li>Automated hardening with Ansible</li>
</ul>

<h2>Technologies Used</h2>

<ul>
    <li>Docker</li>
    <li>Ansible</li>
    <li>Python</li>
    <li>Lynis</li>
    <li>UFW</li>
    <li>auditd</li>
</ul>

</body>

</html>
"""


with open("reports/final/report.html", "w") as f:
    f.write(html)

print("HTML report generated.")