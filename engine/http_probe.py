import aiohttp
import re
from termcolor import colored

async def fetch(session, url):
    try:
        async with session.get(url, timeout=8, allow_redirects=True) as r:
            body = await r.text(errors="ignore")
            title = re.search(r"<title>(.*?)</title>", body, re.I)
            return r.status, url, title.group(1) if title else ""
    except:
        return None

async def http_probe(subdomains):
    print(colored("\n[HTTP] Probing alive hosts", "cyan"))

    async with aiohttp.ClientSession() as session:
        tasks = []
        for sub in subdomains:
            tasks.append(fetch(session, f"http://{sub}"))
            tasks.append(fetch(session, f"https://{sub}"))

        results = await asyncio.gather(*tasks)

    for r in results:
        if not r:
            continue

        status, url, title = r
        tag = "NOT FOUND" if status == 404 else "ALIVE"
        color = "green" if status == 200 else "yellow" if status != 404 else "red"

        print(colored(f"[{status}] {tag} {url} | {title}", color))
