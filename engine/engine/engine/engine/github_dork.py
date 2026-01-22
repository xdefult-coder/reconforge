import aiohttp
from termcolor import colored

DORKS = [
    "AWS_SECRET_ACCESS_KEY",
    "AWS_ACCESS_KEY_ID",
    "password",
    "secret",
    "token",
    "apikey",
    "s3.amazonaws.com"
]

async def run_github_dorking(domains):
    print(colored("\n[GITHUB] Dorking", "cyan"))
    async with aiohttp.ClientSession() as s:
        for d in domains:
            for dk in DORKS:
                url = f"https://github.com/search?q={dk}+{d}&type=code"
                async with s.get(url) as r:
                    if r.status == 200:
                        print(colored(f"[GITHUB] {dk} {d}", "green"))
