# pyploit.py
"""
PyPloit Framework - Metasploit-style Python Exploit Loader
Author: Aram
"""

import os

# === Exploit Class === #
class Exploit:
    def __init__(self):
        self.options = {
            'RHOST': None,
            'RPORT': '22',
            'USER_FILE': None,
            'PASS_FILE': None
        }

    def set_option(self, key, value):
        key = key.upper()
        if key in self.options:
            self.options[key] = value
        else:
            print(f"[!] Unknown option: {key}")

    def show_options(self):
        print("\n[+] Current Options:")
        for key, val in self.options.items():
            print(f"   {key:<12} => {val}")
        print("")

    def run(self):
        rhost = self.options['RHOST']
        rport = self.options['RPORT']
        user_file = self.options['USER_FILE']
        pass_file = self.options['PASS_FILE']

        if not all([rhost, user_file, pass_file]):
            print("[!] Missing required options. Use `show options` to verify.")
            return

        print(f"\n[+] Starting brute-force attack on {rhost}:{rport}\n")

        try:
            with open(user_file, 'r') as uf, open(pass_file, 'r') as pf:
                users = [u.strip() for u in uf.readlines()]
                passwords = [p.strip() for p in pf.readlines()]

                for user in users:
                    for pwd in passwords:
                        print(f"[*] Trying {user}:{pwd}")
                        # Simulated success condition
                        if user == "admin" and pwd == "admin123":
                            print(f"\n[✔] SUCCESS: Valid credentials found: {user}:{pwd}\n")
                            return

                print("\n[✘] Brute-force finished. No valid credentials found.\n")

        except FileNotFoundError:
            print("[!] User or password file not found.")


# === PyPloit Framework === #
class PyPloitFramework:
    def __init__(self):
        self.modules = {
            'exploit/custom/david/python_bruter': Exploit()
        }
        self.current_module = None

    def start(self):
        print("\nPyPloit v1.0 by Aram - Custom Exploit Framework\n")
        while True:
            prompt = "pyploit> " if not self.current_module else "pyploit(module)> "
            cmd = input(prompt).strip()

            if cmd == "exit":
                break
            elif cmd.startswith("use "):
                module = cmd[4:]
                if module in self.modules:
                    self.current_module = self.modules[module]
                    print(f"[+] Loaded module: {module}")
                else:
                    print("[!] Module not found.")
            elif cmd.startswith("set ") and self.current_module:
                try:
                    _, key, value = cmd.split(maxsplit=2)
                    self.current_module.set_option(key, value)
                except ValueError:
                    print("[!] Usage: set OPTION VALUE")
            elif cmd == "show options" and self.current_module:
                self.current_module.show_options()
            elif cmd == "run" and self.current_module:
                self.current_module.run()
            elif cmd == "back":
                self.current_module = None
            elif cmd == "help":
                print("""
Available Commands:
  use <module>        Load a module (e.g., use exploit/custom/david/python_bruter)
  set <opt> <val>     Set module option (e.g., set RHOST 192.168.1.10)
  show options        Display current module options
  run                 Execute the module
  back                Unload the current module
  exit                Exit the framework
""")
            else:
                print("[?] Unknown command. Type 'help' for options.")


# === Entry Point === #
if __name__ == "__main__":
    PyPloitFramework().start()

