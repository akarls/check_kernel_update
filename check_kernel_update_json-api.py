#!/usr/bin/env python3

import requests
import subprocess

def get_current_kernel():
    return subprocess.check_output(['uname', '-r']).decode().strip().split('-')[0]

def get_latest_stable_kernel():
    url = "https://www.kernel.org/releases.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for release in data['releases']:
            if release['moniker'] == "stable":
                return release['version']
    return None

def main():
    current_kernel = get_current_kernel()
    latest_stable_kernel = get_latest_stable_kernel()

    if latest_stable_kernel:
        if latest_stable_kernel == current_kernel:
            print(f"Your kernel ({current_kernel}) is up to date with the latest stable version.")
        elif latest_stable_kernel > current_kernel:
            print(f"A newer stable kernel version ({latest_stable_kernel}) is available. You are running {current_kernel}.")
        else:
            print("Could not determine kernel version correctly.")
    else:
	print("Failed to fetch the latest stable kernel version.")

if __name__ == "__main__":
    main()
