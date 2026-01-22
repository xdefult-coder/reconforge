import aiohttp
import dns.resolver
from termcolor import colored

async def crtsh(domain):
    subs = set()
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=15) as r:
                data = await r.json()
                for entry in data:
                    subs.add(entry["name_value"].strip())
    except:
        pass
    return subs

def brute(domain, words):
    found = set()
    resolver = dns.resolver.Resolver()
    for w in words:
        sub = f"{w}.{domain}"
        try:
            resolver.resolve(sub, "A")
            found.add(sub)
        except:
            pass
    return found

async def enumerate_subdomains(domains, wordlist):
    print(colored("[SUBDOMAIN] Enumerating", "cyan"))
    all_subs = set()

    for domain in domains:
        subs = await crtsh(domain)
        all_subs |= subs

        if wordlist:
            with open(wordlist) as f:
                words = [x.strip() for x in f if x.strip()]
            all_subs |= brute(domain, words)

    for s in all_subs:
        print(colored(f"[SUB] {s}", "green"))

    return list(all_subs)
