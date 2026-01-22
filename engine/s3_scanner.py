import aiohttp
from termcolor import colored

async def s3_scan(domains):
    print(colored("\n[S3] Checking buckets", "cyan"))

    async with aiohttp.ClientSession() as session:
        for d in domains:
            bucket = d.replace(".", "-")
            url = f"http://{bucket}.s3.amazonaws.com/"

            try:
                async with session.get(url, timeout=6) as r:
                    if r.status == 200:
                        print(colored(f"[S3] PUBLIC READ: {bucket}", "green"))
                    elif r.status == 403:
                        print(colored(f"[S3] EXISTS (Private): {bucket}", "yellow"))
            except:
                pass
