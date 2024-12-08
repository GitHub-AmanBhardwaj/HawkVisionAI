#!/usr/bin/env python3
import os
import subprocess
import sys
import platform

# List of common packages to install
packages = [
    'streamlit',
    'opencv-python',
    'pillow',
    'numpy',
    'onnx',
    'onnxruntime',  # Ensure CPU version is installed
    'insightface',
    'psutil',
    'tk',
    'customtkinter',
    'tensorflow',
    'opennsfw2',
    'protobuf',
    'tqdm',
    'gfpgan'
]

# Platform-specific installs
def platform_specific_install():
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinterdnd2-universal"])
    elif platform.system() != "Darwin" and platform.machine() != "arm64":
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tkinterdnd2"])

# Function to install a package
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")

# Install platform-specific packages
platform_specific_install()

# Install common packages
for package in packages:
    install_package(package)

from roop import core

if __name__ == '__main__':
    core.run()
