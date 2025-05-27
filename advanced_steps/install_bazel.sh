#!/bin/bash

# Define the Bazel version to install.
# TensorFlow 2.19.0 (Python 3.12) requires Bazel 6.5.0
BAZEL_VERSION=6.5.0

# Download the Bazel installer
wget https://github.com/bazelbuild/bazel/releases/download/${BAZEL_VERSION}/bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh

# Make the installer executable
chmod +x bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh

# Run the installer
./bazel-${BAZEL_VERSION}-installer-linux-x86_64.sh --user

$HOME/.bazel/bin/bazel --version
~/bin/bazel --version

# add bazel you the shell
# Open it
# vi ~/.bashrc
# Add this line at the end
# export PATH="$HOME/bin:$PATH"
# Apply the changes
# source ~/.bashrc
# Now try 
# bazel --version
