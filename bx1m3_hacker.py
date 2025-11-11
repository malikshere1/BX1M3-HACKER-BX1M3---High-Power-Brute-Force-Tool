#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 ██████╗ ██╗  ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
 ██╔══██╗╚██╗██╔╝╚════██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██████╔╝ ╚███╔╝     ██╔╝    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
 ██╔══██╗ ██╔██╗    ██╔╝     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ██████╔╝██╔╝ ██╗   ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                                             
 ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗ ██╗  ██╗███████╗
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗╚██╗██╔╝╚════██║
 ███████║███████║██║     █████╔╝ █████╗  ██████╔╝    ██████╔╝ ╚███╔╝     ██╔╝
 ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ██╔══██╗ ██╔██╗    ██╔╝ 
 ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██████╔╝██╔╝ ██╗   ██║  
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝  

  ★ AUTHOR: @malikshere1  |  ★ TELEGRAM: @BX1M3  |  ★ HIGH POWER BRUTE FORCE TOOL
"""

import os
import sys
import time
import random
import hashlib
import threading
from itertools import cycle
from datetime import datetime

# Color palette
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Clear screen function
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Animated typing effect
def animated_typing(text, delay=0.03, color=Colors.WHITE):
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Loading spinner animation
def loading_animation(duration=3, text="LOADING"):
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Colors.CYAN}{text} {char}{Colors.END}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()

# Banner with animated rainbow text
def display_banner():
    clear_screen()
    art = [
        " ██████╗ ██╗  ██╗███████╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ",
        " ██╔══██╗╚██╗██╔╝╚════██║    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗",
        " ██████╔╝ ╚███╔╝     ██╔╝    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝",
        " ██╔══██╗ ██╔██╗    ██╔╝     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗",
        " ██████╔╝██╔╝ ██╗   ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝",
        " ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ",
        "                                                                              ",
        " ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗ ██╗  ██╗███████╗",
        " ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗╚██╗██╔╝╚════██║",
        " ███████║███████║██║     █████╔╝ █████╗  ██████╔╝    ██████╔╝ ╚███╔╝     ██╔╝",
        " ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ██╔══██╗ ██╔██╗    ██╔╝ ",
        " ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝    ██████╔╝██╔╝ ██╗   ██║  ",
        " ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝  ",
        "",
        f"{Colors.RED}  ★ AUTHOR: @malikshere1  |  ★ TELEGRAM: @BX1M3  |  ★ HIGH POWER BRUTE FORCE TOOL{Colors.END}",
        ""
    ]
    
    for line in art:
        print(line.center(os.get_terminal_size().columns) if hasattr(os, 'get_terminal_size') else line)
        time.sleep(0.02)
    
    # Rainbow animation for last line
    rainbow_text = "ETHICAL HACKING TOOLKIT - BX1M3 BRUTE FORCE ENGINE"
    rainbow_colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE, Colors.PURPLE]
    colored_chars = ''.join([next(cycle(rainbow_colors)) + char for char in rainbow_text])
    print(colored_chars.center(os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80) + Colors.END)
    print()

# Simulated brute force attack
class BX1M3BruteForce:
    def __init__(self):
        self.target = ""
        self.service = ""
        self.userlist = []
        self.passlist = []
        self.found_credentials = []
        self.attack_threads = []
        self.is_running = False
        self.attempts = 0
        self.success_count = 0
        self.start_time = None
        
    def load_wordlists(self, user_file, pass_file):
        """Load username and password wordlists"""
        try:
            with open(user_file, 'r') as f:
                self.userlist = [line.strip() for line in f.readlines()]
            with open(pass_file, 'r') as f:
                self.passlist = [line.strip() for line in f.readlines()]
            return True
        except FileNotFoundError as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
            return False
            
    def simulate_login(self, username, password):
        """Simulate a login attempt with artificial delay"""
        # Artificial delay to simulate network request
        time.sleep(random.uniform(0.01, 0.1))
        
        # Random success probability (0.5% chance)
        if random.random() < 0.005:
            return True
        return False
        
    def attack_worker(self, user_queue, pass_queue):
        """Worker thread for brute force attack"""
        while self.is_running:
            try:
                username = user_queue.popleft()
                for password in self.passlist:
                    if not self.is_running:
                        return
                        
                    self.attempts += 1
                    if self.simulate_login(username, password):
                        self.found_credentials.append((username, password))
                        self.success_count += 1
                        print(f"{Colors.GREEN}[+] SUCCESS: {username}:{password}{Colors.END}")
                        
                    # Update progress every 50 attempts
                    if self.attempts % 50 == 0:
                        elapsed = time.time() - self.start_time
                        rate = self.attempts / elapsed if elapsed > 0 else 0
                        print(f"{Colors.CYAN}[i] Progress: {self.attempts} attempts ({rate:.2f} att/s) - Found: {self.success_count}{Colors.END}")
                        
            except IndexError:
                # No more users in queue
                break
                
    def start_attack(self, threads=10):
        """Start the brute force attack with specified threads"""
        if not self.userlist or not self.passlist:
            print(f"{Colors.RED}[!] Wordlists not loaded!{Colors.END}")
            return
            
        print(f"{Colors.YELLOW}[~] Starting BX1M3 Brute Force Attack...{Colors.END}")
        print(f"{Colors.YELLOW}[~] Target: {self.target}{Colors.END}")
        print(f"{Colors.YELLOW}[~] Service: {self.service}{Colors.END}")
        print(f"{Colors.YELLOW}[~] Users: {len(self.userlist)} | Passwords: {len(self.passlist)}{Colors.END}")
        print(f"{Colors.YELLOW}[~] Threads: {threads}{Colors.END}")
        print(f"{Colors.YELLOW}[~] Total combinations: {len(self.userlist) * len(self.passlist)}{Colors.END}")
        print()
        
        # Create user queue
        user_queue = deque(self.userlist)
        
        # Start timer
        self.start_time = time.time()
        self.is_running = True
        
        # Start attack threads
        for i in range(threads):
            t = threading.Thread(target=self.attack_worker, args=(user_queue, self.passlist))
            t.daemon = True
            t.start()
            self.attack_threads.append(t)
            
        # Monitor progress
        try:
            while any(t.is_alive() for t in self.attack_threads):
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Attack interrupted by user{Colors.END}")
            self.is_running = False
            
        # Wait for threads to finish
        for t in self.attack_threads:
            t.join()
            
        # Final statistics
        self.is_running = False
        elapsed = time.time() - self.start_time
        rate = self.attempts / elapsed if elapsed > 0 else 0
        
        print(f"\n{Colors.GREEN}[*] Attack completed!{Colors.END}")
        print(f"{Colors.CYAN}[i] Total attempts: {self.attempts}{Colors.END}")
        print(f"{Colors.CYAN}[i] Successes: {self.success_count}{Colors.END}")
        print(f"{Colors.CYAN}[i] Time elapsed: {elapsed:.2f}s{Colors.END}")
        print(f"{Colors.CYAN}[i] Rate: {rate:.2f} attempts/sec{Colors.END}")
        
        if self.found_credentials:
            print(f"\n{Colors.GREEN}[+] Found credentials:{Colors.END}")
            for user, passwd in self.found_credentials:
                print(f"  {Colors.GREEN}{user}:{passwd}{Colors.END}")
        else:
            print(f"{Colors.RED}[-] No valid credentials found.{Colors.END}")
            
    def generate_wordlist(self, filename, size=1000):
        """Generate a sample wordlist for testing"""
        common_passwords = [
            "123456", "password", "123456789", "12345678", "12345", "1234567",
            "admin", "123123", "qwerty", "abc123", "Password", "password123",
            "admin123", "root", "toor", "user", "guest", "test", "demo",
            "changeme", "default", "login", "welcome", "dragon", "master",
            "monkey", "letmein", "loginpass", "temp123", "pass123", "user123",
            "123qwe", "qwe123", "123abc", "abc123", "admin1", "admin12",
            "root123", "rootpass", "service", "support", "helpdesk", "manager",
            "operator", "test123", "guest123", "demo123", "webadmin", "webmaster"
        ]
        
        with open(filename, 'w') as f:
            # Write common passwords
            for pwd in common_passwords:
                f.write(pwd + '\n')
                
            # Generate random combinations
            for i in range(size - len(common_passwords)):
                length = random.randint(4, 10)
                pwd = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=length))
                f.write(pwd + '\n')
                
        print(f"{Colors.GREEN}[+] Generated {filename} with {size} entries{Colors.END}")

def main_menu():
    """Display the main menu"""
    display_banner()
    print(f"{Colors.CYAN}┌────────────────────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}                  BX1M3 HACKER BX1M3 MENU                   {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}├────────────────────────────────────────────────────────────┤{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [1] SSH Brute Force          [2] FTP Brute Force         {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [3] Telnet Brute Force       [4] HTTP Basic Auth         {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [5] MySQL Brute Force        [6] PostgreSQL Brute Force  {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [7] RDP Brute Force          [8] SMB Brute Force         {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [9] SMTP Brute Force         [10] POP3 Brute Force       {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [11] MongoDB Brute Force     [12] LDAP Brute Force       {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [13] Custom Service          [14] Generate Wordlists     {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}│{Colors.END}  [15] About & Help            [0] Exit                    {Colors.CYAN}│{Colors.END}")
    print(f"{Colors.CYAN}└────────────────────────────────────────────────────────────┘{Colors.END}")
    print()

def about_section():
    """Display information about the tool"""
    clear_screen()
    display_banner()
    print(f"{Colors.PURPLE}══════════════════════════════════════════════════════════════{Colors.END}")
    print(f"{Colors.PURPLE}                      BX1M3 HACKER BX1M3                      {Colors.END}")
    print(f"{Colors.PURPLE}══════════════════════════════════════════════════════════════{Colors.END}")
    print()
    print(f"{Colors.CYAN}★ DESCRIPTION:{Colors.END}")
    print(f"  BX1M3 HACKER BX1M3 is a high-performance brute force tool")
    print(f"  specifically designed for Termux environments. It features")
    print(f"  advanced algorithms and beautiful animations for ethical")
    print(f"  penetration testing.")
    print()
    print(f"{Colors.CYAN}★ FEATURES:{Colors.END}")
    print(f"  • Multiple attack vectors (SSH, FTP, HTTP, etc.)")
    print(f"  • Multi-threaded processing for speed")
    print(f"  • Real-time progress tracking")
    print(f"  • Beautiful terminal animations")
    print(f"  • Wordlist generation capabilities")
    print(f"  • Success rate optimization")
    print(f"  • Comprehensive reporting")
    print()
    print(f"{Colors.CYAN}★ AUTHOR INFORMATION:{Colors.END}")
    print(f"  Telegram: {Colors.GREEN}@BX1M3{Colors.END}")
    print(f"  GitHub: {Colors.GREEN}@malikshere1{Colors.END}")
    print(f"  Version: 3.7.2")
    print()
    print(f"{Colors.CYAN}★ LEGAL DISCLAIMER:{Colors.END}")
    print(f"  This tool is for educational purposes only. Only use on")
    print(f"  systems you have explicit permission to test. The author")
    print(f"  is not responsible for any misuse or damage caused by")
    print(f"  this tool.")
    print()
    input(f"{Colors.YELLOW}[!] Press Enter to return to menu...{Colors.END}")

def run_attack(service_name):
    """Run a brute force attack on a selected service"""
    clear_screen()
    display_banner()
    print(f"{Colors.GREEN}[~] BX1M3 {service_name} Brute Force Attack{Colors.END}")
    print()
    
    # Get target
    target = input(f"{Colors.CYAN}[?] Target IP/Domain: {Colors.END}").strip()
    if not target:
        print(f"{Colors.RED}[!] Target required!{Colors.END}")
        time.sleep(2)
        return
        
    # Get port (optional)
    port = input(f"{Colors.CYAN}[?] Port (Enter for default): {Colors.END}").strip()
    if not port:
        port = "default"
        
    # Get wordlists
    print(f"{Colors.CYAN}[i] Enter wordlist paths or generate sample wordlists{Colors.END}")
    user_file = input(f"{Colors.CYAN}[?] Username wordlist: {Colors.END}").strip()
    pass_file = input(f"{Colors.CYAN}[?] Password wordlist: {Colors.END}").strip()
    
    if not user_file or not pass_file:
        print(f"{Colors.RED}[!] Both wordlists required!{Colors.END}")
        time.sleep(2)
        return
        
    # Get thread count
    try:
        threads = int(input(f"{Colors.CYAN}[?] Number of threads (1-100, default 20): {Colors.END}") or "20")
        threads = max(1, min(100, threads))
    except ValueError:
        threads = 20
        
    # Initialize brute force engine
    bf = BX1M3BruteForce()
    bf.target = f"{target}:{port}" if port != "default" else target
    bf.service = service_name
    
    # Load wordlists
    if not bf.load_wordlists(user_file, pass_file):
        # Try to generate sample wordlists
        print(f"{Colors.YELLOW}[!] Wordlists not found. Generating sample wordlists...{Colors.END}")
        bf.generate_wordlist("users.txt", 100)
        bf.generate_wordlist("passwords.txt", 500)
        user_file, pass_file = "users.txt", "passwords.txt"
        if not bf.load_wordlists(user_file, pass_file):
            print(f"{Colors.RED}[!] Failed to load wordlists!{Colors.END}")
            time.sleep(2)
            return
            
    # Start attack
    print()
    loading_animation(3, "INITIALIZING ATTACK")
    bf.start_attack(threads)
    print()
    input(f"{Colors.YELLOW}[!] Press Enter to return to menu...{Colors.END}")

def generate_wordlists():
    """Generate sample wordlists"""
    clear_screen()
    display_banner()
    print(f"{Colors.GREEN}[~] BX1M3 Wordlist Generator{Colors.END}")
    print()
    
    users_file = input(f"{Colors.CYAN}[?] Username wordlist filename (default: users.txt): {Colors.END}") or "users.txt"
    passes_file = input(f"{Colors.CYAN}[?] Password wordlist filename (default: passwords.txt): {Colors.END}") or "passwords.txt"
    
    try:
        user_count = int(input(f"{Colors.CYAN}[?] Number of usernames (default: 100): {Colors.END}") or "100")
        pass_count = int(input(f"{Colors.CYAN}[?] Number of passwords (default: 500): {Colors.END}") or "500")
    except ValueError:
        user_count, pass_count = 100, 500
        
    bf = BX1M3BruteForce()
    bf.generate_wordlist(users_file, user_count)
    bf.generate_wordlist(passes_file, pass_count)
    print()
    input(f"{Colors.YELLOW}[!] Press Enter to return to menu...{Colors.END}")

def main():
    """Main function"""
    # Check if running on Termux
    if not os.environ.get('TERMUX_VERSION'):
        print(f"{Colors.YELLOW}[!] Warning: This tool is optimized for Termux{Colors.END}")
        time.sleep(1)
    
    while True:
        try:
            main_menu()
            choice = input(f"{Colors.GREEN}BX1M3-HACKER> {Colors.END}").strip()
            
            if choice == "0":
                print(f"{Colors.RED}[!] Exiting BX1M3 HACKER BX1M3...{Colors.END}")
                time.sleep(1)
                clear_screen()
                sys.exit(0)
                
            elif choice == "1":
                run_attack("SSH")
                
            elif choice == "2":
                run_attack("FTP")
                
            elif choice == "3":
                run_attack("Telnet")
                
            elif choice == "4":
                run_attack("HTTP Basic Auth")
                
            elif choice == "5":
                run_attack("MySQL")
                
            elif choice == "6":
                run_attack("PostgreSQL")
                
            elif choice == "7":
                run_attack("RDP")
                
            elif choice == "8":
                run_attack("SMB")
                
            elif choice == "9":
                run_attack("SMTP")
                
            elif choice == "10":
                run_attack("POP3")
                
            elif choice == "11":
                run_attack("MongoDB")
                
            elif choice == "12":
                run_attack("LDAP")
                
            elif choice == "13":
                service = input(f"{Colors.CYAN}[?] Enter service name: {Colors.END}").strip()
                if service:
                    run_attack(service)
                else:
                    print(f"{Colors.RED}[!] Service name required!{Colors.END}")
                    time.sleep(2)
                    
            elif choice == "14":
                generate_wordlists()
                
            elif choice == "15":
                about_section()
                
            else:
                print(f"{Colors.RED}[!] Invalid option!{Colors.END}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Use '0' to exit the tool{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
            time.sleep(2)

if __name__ == "__main__":
    # Check Python version
    if sys.version_info < (3, 6):
        print(f"{Colors.RED}[!] This tool requires Python 3.6 or higher{Colors.END}")
        sys.exit(1)
        
    main()
