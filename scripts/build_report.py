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
        }}

        h1 {{
            color: #222;
        }}

        .good {{
            color: green;
            font-weight: bold;
        }}

        .bad {{
            color: red;
            font-weight: bold;
        }}

        table {{
            border-collapse: collapse;
            width: 80%;
            background: white;
        }}

        td, th {{
            border: 1px solid #ccc;
            padding: 10px;
        }}
    </style>
</head>

<body>

<h1>Audit & Hardening Report</h1>

<table>
<tr>
    <th>Security Control</th>
    <th>Before</th>
    <th>After</th>
</tr>

<tr>
    <td>Root SSH Login Disabled</td>
    <td class="bad">{data['before']['root_login_disabled']}</td>
    <td class="good">{data['after']['root_login_disabled']}</td>
</tr>

<tr>
    <td>Password Authentication Disabled</td>
    <td class="bad">{data['before']['password_auth_disabled']}</td>
    <td class="good">{data['after']['password_auth_disabled']}</td>
</tr>

<tr>
    <td>Firewall Active</td>
    <td class="bad">{data['before']['firewall_active']}</td>
    <td class="good">{data['after']['firewall_active']}</td>
</tr>

<tr>
    <td>Audit Rules Present</td>
    <td class="bad">{data['before']['audit_rules_present']}</td>
    <td class="good">{data['after']['audit_rules_present']}</td>
</tr>

</table>

</body>
</html>
"""


with open("reports/final/report.html", "w") as f:
    f.write(html)

print("HTML report generated.")