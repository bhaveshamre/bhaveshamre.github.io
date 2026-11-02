#!/usr/bin/env python3
"""
Portfolio Photo Setup Script
This script helps you set up your profile photo for your portfolio
"""

import os
import shutil
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
images_dir = script_dir / "images"

print("=" * 60)
print("📸 Portfolio Photo Setup Script")
print("=" * 60)

# Create images directory if it doesn't exist
if not images_dir.exists():
    images_dir.mkdir()
    print(f"✅ Created 'images' folder at: {images_dir}")
else:
    print(f"✅ 'images' folder already exists at: {images_dir}")

print("\n" + "=" * 60)
print("📋 Instructions:")
print("=" * 60)
print(f"""
1. Locate your profile photo (the green outfit photo)
2. Copy it to this location and rename it to: profile.jpg

   Path: {images_dir / 'profile.jpg'}

3. Alternatively, you can drag & drop your photo to the 'images' folder
4. Make sure the filename is exactly: profile.jpg
5. Open index.html in your browser to see your portfolio with the photo

File format: JPG, PNG, or WebP (recommended: JPG)
Recommended size: Square image (1:1 aspect ratio) works best for circular display
""")

print("=" * 60)
print(f"✅ Images folder is ready at: {images_dir}")
print("=" * 60)

# Check if profile.jpg exists
profile_path = images_dir / "profile.jpg"
if profile_path.exists():
    print(f"✅ Photo found at: {profile_path}")
    print("✅ Your portfolio is ready! Open index.html to see it.")
else:
    print(f"⏳ Waiting for photo at: {profile_path}")
    print("   Please copy your photo there.")

print("\n")
