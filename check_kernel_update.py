#!/usr/bin/env python3

import requests
import re
import subprocess

def get_current_kernel():
    return subprocess.check_output(['uname', '-r']).decode().strip().split('-')[0]

def get_latest_kernel():
    response = requests.get("https://www.kernel.org/")
    if response.status_code == 200:
        match = re.search(r'(?<=strong>)(\d+\.\d+\.\d+)', response.text)
        if match:
            return match.group(0)
    return None

def main():
    current_kernel = get_current_kernel()
    latest_kernel = get_latest_kernel()
    
    if latest_kernel:
        if latest_kernel == current_kernel:
            print(f"Your kernel ({current_kernel}) is up to date.")
        elif latest_kernel > current_kernel:
            print(f"A newer kernel version ({latest_kernel}) is available. You are running {current_kernel}. Run: sudo dnf install kernel --best")
        else:
            print("Could not determine kernel version correctly.")
    else:
        print("Failed to fetch latest kernel version.")

if __name__ == "__main__":
    main()
