import aiohttp, asyncio, re
from termcolor import colored

async def fetch(s, url):
    try:
        async with s.get(url, timeout=8, allow_redirects=True) as r:
            text = await r.text(errors="ignore")
            title = re.search(r"<title>(.*?)</title>", text, re.I)
            return r.status, url, title.group(1) if title else ""
    except:
        return None

async def run_http_probe(subs):
    print(colored("\n[HTTP] Probing", "cyan"))
    async with aiohttp.ClientSession() as s:
        tasks = []
        for sub in subs:
            tasks.append(fetch(s, f"http://{sub}"))
            tasks.append(fetch(s, f"https://{sub}"))

        for r in await asyncio.gather(*tasks):
            if not r:
                continue
            status, url, title = r
            tag = "NOT FOUND" if status == 404 else "ALIVE"
            color = "green" if status == 200 else "yellow" if status != 404 else "red"
            print(colored(f"[{status}] {tag} {url} | {title}", color))
