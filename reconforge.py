import argparse
import asyncio
from termcolor import colored

from engine.subdomain import enumerate_subdomains
from engine.http_probe import http_probe
from engine.s3_scanner import s3_scan
from engine.github_dork import github_dork

async def run(domains, wordlist):
    print(colored("\n[ ReconForge Started ]\n", "cyan"))

    subs = await enumerate_subdomains(domains, wordlist)
    await http_probe(subs)
    await s3_scan(domains)
    await github_dork(domains)

def main():
    parser = argparse.ArgumentParser(
        description="ReconForge - Ultra Deep Bug Bounty Recon Tool"
    )

    parser.add_argument(
        "-d", "--domain",
        help="Single domain (example.com)"
    )

    parser.add_argument(
        "-D", "--domains",
        help="File with domains (.txt)"
    )

    parser.add_argument(
        "-w", "--wordlist",
        help="Subdomain wordlist"
    )

    args = parser.parse_args()

    targets = []

    if args.domain:
        targets.append(args.domain.strip())

    if args.domains:
        with open(args.domains) as f:
            targets += [x.strip() for x in f if x.strip()]

    if not targets:
        parser.print_help()
        return

    asyncio.run(run(targets, args.wordlist))

if __name__ == "__main__":
    main()
