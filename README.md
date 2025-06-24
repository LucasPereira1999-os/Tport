# 💫 About Me:
👨‍💻 About Me<br><br>Hi there! 👋<br>I'm an aspiring ethical hacker passionate about everything offensive security — especially Web Exploitation 🌐 and Malware Development 🐍💣.<br><br>Currently sharpening my skills through hands-on learning at platforms like:<br><br>🧠 Hack The Box<br><br>🛡️ PortSwigger Web Security Academy<br><br>🔍 APISEC University<br><br><br>I enjoy breaking (and fixing) things to better understand how systems work from the inside. Whether it’s bypassing filters, crafting payloads, or analyzing malware behavior, I’m always exploring and learning more every day.<br><br>🔧 Interests<br><br>Web application vulnerabilities (XSS, SSRF, IDOR, etc.)<br><br>Malware analysis and AV/EDR evasion techniques<br><br>Automation, scripting, and red team tooling<br><br><br>🧠 Mindset<br><br>> "Learn. Break. Understand. Repeat."


## 🌐 Socials:
[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white)](https://discord.gg/@james_carter11) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/www.linkedin.com/in/alwi-muzakki-62443b360) [![email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:blazeice628@gmail.com) 

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=LucasPereira1999-os&theme=tokyonight&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://nirzak-streak-stats.vercel.app/?user=LucasPereira1999-os&theme=tokyonight&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=LucasPereira1999-os&theme=tokyonight&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

---
[![](https://visitcount.itsvg.in/api?id=LucasPereira1999-os&icon=4&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

![Tscan     ](https://github.com/user-attachments/assets/513bc686-1751-4f44-a36e-49ed15c215be)

# 🔎 Tscan — Multi-threaded Port Scanner with TOR Support

Tscan is a simple multi-threaded port scanner written in Python. It can optionally use TOR to anonymize your scan traffic. The scan results are saved in a scan_file.txt.

## 📦 Features

- Multi-threaded for faster scanning.
- TOR SOCKS5 proxy support.
- Randomized port scanning.
- Saves output to a file (scan_file.txt).
- Optional HTTP GET request to open ports.

## 🧰 Requirements

- Python 3.7+
- Optional: [TOR service](https://www.torproject.org/)

## 🚀 Installation

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/Tscan.git
cd Tscan

# 2. (Recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/macOS

# 3. Install required packages
pip install -r requirements.txt

🧪 Usage

# Basic scan using TOR (default)
python Tscan.py -d example.com

# Scan without TOR
python Tscan.py -d example.com --not_tor

> ❗ Make sure TOR is running on your system if using the default mode.



📂 Output

Results will be saved to scan_file.txt in the current directory, showing open ports like:

Port : 80 | OPEN
Port : 443 | OPEN

🛡️ Legal Disclaimer

This tool is intended for educational and authorized security testing only. Unauthorized scanning is illegal. The developer is not responsible for misuse or illegal activity.


📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
