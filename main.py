import re
import json
import requests
import dns.resolver

url = "https://hooks.arcemtene.com/wireguard/allowedips"
allowed = ["0.0.0.0/0", "::/0"]
resolver = dns.resolver.Resolver(configure=True)

resolver.nameservers = ['8.8.8.8', '1.0.0.1', '1.1.1.1']

# reading input.txt
with open("input.txt", "r") as f:
    lines = f.readlines()
    disallowed = []

    # dig
    for line in lines:
        line = line.replace("\n", "")

        if len(line.strip()) < 3:
            continue

        if re.match(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", line):
            disallowed.append(line)
            continue

        print(f"-@ Resolving '{line}'")
        res = resolver.resolve(line, 'A')

        ips = []
        for a in res:
            disallowed.append(str(a))
            ips.append(str(a))
        print(" ".join(ips))
        print()

    # api
    res = requests.get(url, params=(('allowed', ", ".join(allowed)), ('disallowed', ", ".join(disallowed)))).text
    res = json.loads(res)

    s = f"AllowedIPs = {', '.join([x['id'] for x in res['data']])}"

    print(s)

    with open('./allowed.ips', 'w') as f:
        f.write(s + "\n")
