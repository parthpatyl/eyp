import os
import time
import random
import hashlib
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin, unquote, parse_qs, urlparse

# Configuration
DOWNLOAD_DIR = "downloaded_pdfs"
DELAY_RANGE = (3, 6)

# Multiple search queries covering the full research landscape
SEARCH_QUERIES = [
    # Core topic
    "solar powered HALE UAV design pdf",
    "high altitude long endurance UAV solar energy pdf",
    # Energy & power
    "solar UAV energy management system pdf",
    "solar cell photovoltaic UAV efficiency pdf",
    "solar powered unmanned aircraft battery energy storage pdf",
    "MPPT solar UAV power optimization pdf",
    # Aerodynamics & structures
    "HALE UAV aeroelastic flexible wing design pdf",
    "lightweight composite structure HALE UAV pdf",
    "very flexible aircraft nonlinear aeroelasticity pdf",
    # Flight & mission
    "HALE UAV autonomous flight control pdf",
    "solar irradiance altitude UAV mission planning pdf",
    "perpetual endurance solar UAV flight pdf",
    # Propulsion
    "solar electric propulsion UAV motor propeller pdf",
    # Specific programs & vehicles
    "Zephyr solar HALE UAV Airbus pdf",
    "NASA Helios solar UAV research pdf",
    "AtlantikSolar ETH Zurich solar UAV pdf",
    # Conceptual design & sizing
    "solar UAV conceptual design sizing methodology pdf",
    "MALE HALE UAV configuration trade study pdf",
]

def get_random_user_agent():
    try:
        ua = UserAgent()
        return ua.random
    except Exception:
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def get_file_hash(filepath):
    """Calculates the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def download_file(url, destination_folder):
    """Downloads a file from a URL to the destination folder."""
    try:
        # Get filename from URL
        parsed = urlparse(url)
        filename = unquote(parsed.path.split("/")[-1])
        if not filename.lower().endswith(".pdf"):
            filename += ".pdf"
        
        # Sanitize filename - keep it readable
        filename = "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).strip()
        if not filename or filename == ".pdf":
            filename = hashlib.md5(url.encode()).hexdigest()[:12] + ".pdf"
        
        filepath = os.path.join(destination_folder, filename)

        if os.path.exists(filepath):
            print(f"  Skipping (already exists): {filename}")
            return False

        headers = {'User-Agent': get_random_user_agent()}
        response = requests.get(url, headers=headers, stream=True, timeout=30, allow_redirects=True)
        response.raise_for_status()

        temp_filepath = filepath + ".tmp"
        with open(temp_filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Check if file is a valid PDF (basic check)
        with open(temp_filepath, 'rb') as f:
            header = f.read(5)
            if not header.startswith(b'%PDF'):
                print(f"  Skipping (not a valid PDF): {filename}")
                os.remove(temp_filepath)
                return False

        # Check for duplicates by hash
        new_file_hash = get_file_hash(temp_filepath)
        for existing_file in os.listdir(destination_folder):
            existing_filepath = os.path.join(destination_folder, existing_file)
            if os.path.isfile(existing_filepath) and not existing_file.endswith('.tmp'):
                 if get_file_hash(existing_filepath) == new_file_hash:
                     print(f"  Skipping (duplicate content): {filename}")
                     os.remove(temp_filepath)
                     return False

        os.rename(temp_filepath, filepath)
        size_mb = os.path.getsize(filepath) / (1024 * 1024)
        print(f"  ✓ Downloaded: {filename} ({size_mb:.1f} MB)")
        return True

    except Exception as e:
        print(f"  ✗ Failed: {url[:80]}... ({e})")
        temp = filepath + ".tmp" if 'filepath' in dir() else None
        if temp and os.path.exists(temp):
             os.remove(temp)
        return False

def extract_ddg_url(href):
    """Extract actual URL from DuckDuckGo redirect link."""
    if "//duckduckgo.com/l/" in href or "/l/?" in href:
        try:
            parsed = urlparse(href)
            qs = parse_qs(parsed.query)
            if 'uddg' in qs:
                return unquote(qs['uddg'][0])
        except:
            pass
    return href

def duckduckgo_search_pdfs(query):
    """Scrapes DuckDuckGo HTML version for PDF links."""
    links = []
    base_url = "https://html.duckduckgo.com/html/"
    
    headers = {
        'User-Agent': get_random_user_agent(),
    }
    
    data = {'q': query}
    
    try:
        response = requests.post(base_url, data=data, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # DDG HTML results: look at ALL links, not just result__a
        for a in soup.find_all('a', href=True):
            href = a['href']
            
            # Extract real URL from DDG redirect
            real_url = extract_ddg_url(href)
            
            if real_url.lower().endswith(".pdf"):
                if real_url not in links:
                    links.append(real_url)
        
        # Also look for links in result snippets that might point to PDFs
        for a in soup.find_all('a', class_='result__url', href=True):
            href = extract_ddg_url(a['href'])
            if href.lower().endswith(".pdf") and href not in links:
                links.append(href)

    except Exception as e:
        print(f"  Error searching: {e}")

    return links

def main():
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    all_pdf_links = []
    
    print("=" * 60)
    print("Solar HALE UAV Research Paper Downloader")
    print("=" * 60)
    
    # Search across all queries
    for i, query in enumerate(SEARCH_QUERIES, 1):
        print(f"\n[{i}/{len(SEARCH_QUERIES)}] Searching: {query}")
        links = duckduckgo_search_pdfs(query)
        new_links = [l for l in links if l not in all_pdf_links]
        all_pdf_links.extend(new_links)
        print(f"  Found {len(links)} PDFs ({len(new_links)} new)")
        time.sleep(random.uniform(*DELAY_RANGE))
    
    print(f"\n{'=' * 60}")
    print(f"Total unique PDF links found: {len(all_pdf_links)}")
    print(f"{'=' * 60}\n")
    
    downloaded = 0
    for i, link in enumerate(all_pdf_links, 1):
        print(f"[{i}/{len(all_pdf_links)}] {link[:80]}...")
        if download_file(link, DOWNLOAD_DIR):
            downloaded += 1
        time.sleep(random.uniform(1, 3))

    print(f"\n{'=' * 60}")
    print(f"Download complete. {downloaded} new papers downloaded.")
    existing = len([f for f in os.listdir(DOWNLOAD_DIR) if f.endswith('.pdf')])
    print(f"Total papers in {DOWNLOAD_DIR}: {existing}")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
