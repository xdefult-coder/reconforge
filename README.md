# ReconForge 🔥

Ultra-Fast & Ultra-Deep Bug Bounty Recon Tool.

## Features
- Advanced subdomain enumeration
- HTTP status + title detection
- 404 separation
- S3 bucket discovery
- GitHub dorking

## Installation
```bash
git clone https://github.com/YOURNAME/reconforge
cd reconforge
pip install -r requirements.txt

python reconforge.py -d example.com
python reconforge.py -D domains.txt -w wordlists/subdomains.txt


---

# 🚀 RUN & TEST

```bash
python reconforge.py -d google.com

[SUB] www.google.com
[200] ALIVE https://www.google.com | Google
[S3] EXISTS google-com
[GITHUB] AWS_SECRET_ACCESS_KEY google.com

git init
git add .
git commit -m "Initial ReconForge release"
git branch -M main
git remote add origin https://github.com/YOURNAME/reconforge.git
git push -u origin main

