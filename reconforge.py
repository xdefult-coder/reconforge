import argparse, asyncio
from termcolor import colored

from engine.subdomain import run_subdomain
from engine.http_probe import run_http_probe
from engine.s3_scanner import run_s3_scan
from engine.passive import run_passive
from engine.github_dork import run_github_dorking

async def run(domain, file, wordlist):
    domains = []

    if domain:
        domains.append(domain)

    if file:
        with open(file) as f:
            domains += [x.strip() for x in f if x.strip()]

    print(colored(f"\n[+] ReconForge started on {len(domains)} domain(s)\n", "cyan"))

    subs = await run_subdomain(domains, wordlist)
    await run_http_probe(subs)
    await run_s3_scan(domains)
    await run_passive(domains)
    await run_github_dorking(domains)

def main():
    parser = argparse.ArgumentParser(
        description="ReconForge – Ultra Deep Bug Bounty Recon"
    )

    parser.add_argument("-d", "--domain", help="Single domain")
    parser.add_argument("-D", "--domains", help="Domains file (.txt)")
    parser.add_argument("-w", "--wordlist", help="Subdomain wordlist")

    args = parser.parse_args()

    if not args.domain and not args.domains:
        parser.print_help()
        return

    asyncio.run(run(args.domain, args.domains, args.wordlist))

if __name__ == "__main__":
    main()
