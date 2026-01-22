import aiohttp, asyncio
from termcolor import colored

async def run_s3_scan(domains):
    print(colored("\n[S3] Scanning buckets", "cyan"))
    async with aiohttp.ClientSession() as s:
        for d in domains:
            bucket = d.replace(".", "-")
            url = f"http://{bucket}.s3.amazonaws.com/"
            try:
                async with s.get(url, timeout=6) as r:
                    if r.status == 200:
                        print(colored(f"[S3] PUBLIC READ {bucket}", "green"))
                    elif r.status == 403:
                        print(colored(f"[S3] EXISTS {bucket}", "yellow"))
            except:
                pass
