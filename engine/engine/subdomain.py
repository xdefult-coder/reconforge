import asyncio, aiohttp, dns.resolver
from termcolor import colored

async def passive(domain):
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    subs = set()
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(url, timeout=15) as r:
                data = await r.json()
                for i in data:
                    subs.add(i["name_value"].strip())
    except:
        pass
    return subs

def brute(domain, words):
    found = set()
    res = dns.resolver.Resolver()
    for w in words:
        sub = f"{w}.{domain}"
        try:
            res.resolve(sub, "A")
            found.add(sub)
        except:
            pass
    return found

async def run_subdomain(domains, wordlist):
    print(colored("[SUB] Enumerating subdomains", "cyan"))
    final = set()

    for d in domains:
        final |= await passive(d)

        if wordlist:
            with open(wordlist) as f:
                words = [x.strip() for x in f]
            final |= brute(d, words)

    for s in final:
        print(colored(f"[SUB] {s}", "green"))

    return list(final)
