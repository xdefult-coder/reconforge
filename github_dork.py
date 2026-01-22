import aiohttp
from termcolor import colored

DORKS = [
    "AWS_SECRET_ACCESS_KEY",
    "AWS_ACCESS_KEY_ID",
    "password",
    "secret",
    "apikey",
    "token",
    "s3.amazonaws.com"
]

async def github_dork(domains):
    print(colored("\n[GITHUB] Dorking started", "cyan"))

    async with aiohttp.ClientSession() as session:
        for domain in domains:
            for dork in DORKS:
                url = f"https://github.com/search?q={dork}+{domain}&type=code"
                try:
                    async with session.get(url, timeout=10) as r:
                        if r.status == 200:
                            print(colored(f"[GITHUB] {dork} {domain}", "green"))
                except:
                    pass
