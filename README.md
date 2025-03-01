# Social Media Link Extractor | Bug Bounty Tool  

**Author:** XABIT  

## 📌 About  
This **Social Media Link Extractor** is a high-performance Python tool designed for **bug bounty hunters**, **pentesters**, and **OSINT researchers**. It automatically scrapes social media links from a list of subdomains and saves them in structured output files for easy analysis.  

## 🚀 Features  
✅ **Multithreaded (500 threads)** for ultra-fast processing  
✅ **Extracts links from popular social platforms** (YouTube, Twitter, Facebook, GitHub, etc.)  
✅ **Automatically formats URLs** (adds `https://` if missing)  
✅ **Saves results in two files:**  
   - `social.txt` → Contains all extracted social media links  
   - `p_social.txt` → Stores links in a structured format:  
     ```
     SOURCE URL: <subdomain>
     Extracted Links:
     <social media link 1>
     <social media link 2>
     ```  
✅ **Minimal output** (only displays source URLs and valid social media links)  
✅ **Stylish banner** with sky-blue theme  

## 🔧 Installation  
```bash
git clone https://github.com/yourusername/Social-Media-Extractor.git
cd Social-Media-Extractor
pip install -r requirements.txt
```

## ▶️ Usage  
```bash
python extractor.py
```
Enter the filename containing the subdomains when prompted.

## 📂 Example Output  
**p_social.txt:**  
```
SOURCE URL: https://example.com
https://twitter.com/example
https://github.com/example
```

## 🛠 Requirements  
- Python 3.x  
- `requests`  
- `beautifulsoup4`  
- `concurrent.futures`  
