import requests
import concurrent.futures
from bs4 import BeautifulSoup
import os

# Sky Blue Banner with Styled Font
BANNER = """
\033[94m
▒██   ██▒ ▄▄▄       ▄▄▄▄    ██▓▄▄▄█████▓
▒▒ █ █ ▒░▒████▄    ▓█████▄ ▓██▒▓  ██▒ ▓▒
░░  █   ░▒██  ▀█▄  ▒██▒ ▄██▒██▒▒ ▓██░ ▒░
 ░ █ █ ▒ ░██▄▄▄▄██ ▒██░█▀  ░██░░ ▓██▓ ░ 
▒██▒ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓░██░  ▒██▒ ░ 
▒▒ ░ ░▓ ░ ▒▒   ▓▒█░░▒▓███▀▒░▓    ▒ ░░   
░░   ░▒ ░  ▒   ▒▒ ░▒░▒   ░  ▒ ░    ░    
 ░    ░    ░   ▒    ░    ░  ▒ ░  ░      
 ░    ░        ░  ░ ░       ░           
                         ░              
\033[0m
    \033[1;94mSocial Media Link Extractor | BUG BOUNTY \033[0m
         \033[93mAuthor: XABIT\033[0m
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
print(BANNER)

# Social Media Platforms
SOCIAL_MEDIA_SITES = [
    "youtube.com", "twitter.com", "instagram.com", "medium.com", "discord.com", 
    "reddit.com", "facebook.com", "pinterest.com", "snapchat.com", "linkedin.com", 
    "twitch.tv", "tumblr.com", "github.com"
]

def format_url(url):
    if not url.startswith("http"):
        return "https://" + url
    return url

# Extract social media links from a page
def extract_social_links(url):
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a["href"] for a in soup.find_all("a", href=True)]
        social_links = [link for link in links if any(site in link for site in SOCIAL_MEDIA_SITES)]
        return social_links
    except:
        return []

# Process each subdomain
def process_subdomain(subdomain):
    subdomain = format_url(subdomain)
    social_links = extract_social_links(subdomain)
    if social_links:
        with open("p_social.txt", "a") as pf, open("social.txt", "a") as sf:
            pf.write(f"\n\033[92mSOURCE URL:\033[0m {subdomain}\n")
            for link in social_links:
                pf.write(f"{link}\n")
                sf.write(f"{link}\n")
        print(f"\n\033[92mSOURCE URL:\033[0m {subdomain}")
        for link in social_links:
            print(f"\033[96m{link}\033[0m")

# Load input file
input_file = input("Enter the file containing subdomains: ").strip()
with open(input_file, "r") as f:
    subdomains = [line.strip() for line in f.readlines()]

# Multithreading execution
with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
    executor.map(process_subdomain, subdomains)

print("\n\033[92m✅ Extraction Completed! Check social.txt & p_social.txt for results.\033[0m")
