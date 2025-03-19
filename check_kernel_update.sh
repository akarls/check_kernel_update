#!/bin/bash

# Get the current kernel version
CURRENT_KERNEL=$(uname -r | cut -d'-' -f1)

# Fetch the latest stable kernel version from kernel.org
LATEST_KERNEL=$(curl -s https://www.kernel.org/ | grep -oP '(?<=strong>)[0-9]+\.[0-9]+\.[0-9]+' | head -1)

# Compare versions
if [ "$LATEST_KERNEL" == "$CURRENT_KERNEL" ]; then
    echo "Your kernel ($CURRENT_KERNEL) is up to date."
elif [ "$LATEST_KERNEL" > "$CURRENT_KERNEL" ]; then
    echo "A newer kernel version ($LATEST_KERNEL) is available. You are running $CURRENT_KERNEL."
else
    echo "Could not determine kernel version correctly."
fi
