# Installation Guide

This guide will walk you through the installation process for the AI-Powered Binance Grid Trading Bot.

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: Version 3.8 or higher
- **RAM**: 2 GB minimum
- **Disk Space**: 500 MB free space
- **Internet**: Stable internet connection required

### Recommended Requirements
- **Operating System**: Windows 11, macOS 12+, or Linux (Ubuntu 22.04+)
- **Python**: Version 3.10 or higher
- **RAM**: 4 GB or more
- **Disk Space**: 1 GB free space
- **Internet**: High-speed internet connection

## Prerequisites

### 1. Python Installation

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH"
4. Verify installation:
   ```cmd
   python --version
   ```

#### macOS
Using Homebrew:
```bash
brew install python@3.10
python3 --version
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

### 2. Git Installation (Optional)

#### Windows
Download from [git-scm.com](https://git-scm.com/downloads)

#### macOS
```bash
brew install git
```

#### Linux
```bash
sudo apt install git
```

## Installation Methods

### Method 1: Installation from Source (Recommended)

#### Step 1: Clone the Repository

Using Git:
```bash
git clone https://github.com/GizzZmo/crypto_trader.git
cd crypto_trader
```

Or download ZIP:
1. Visit [repository page](https://github.com/GizzZmo/crypto_trader)
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Navigate to the extracted folder

#### Step 2: Create Virtual Environment

**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Wait for all packages to install. This may take a few minutes.

#### Step 4: Verify Installation

```bash
python bot.py
```

The GUI should launch. If you see the bot interface, installation was successful!

### Method 2: Installation from Release Package

#### Step 1: Download Release

1. Visit [Releases page](https://github.com/GizzZmo/crypto_trader/releases)
2. Download the latest release:
   - `crypto-trader-bot-vX.X.X-source.tar.gz` (Linux/macOS)
   - `crypto-trader-bot-vX.X.X-source.zip` (Windows)

#### Step 2: Extract Archive

**Windows:**
- Right-click the ZIP file
- Select "Extract All"

**macOS/Linux:**
```bash
tar -xzf crypto-trader-bot-vX.X.X-source.tar.gz
cd release-package
```

#### Step 3: Install

Create virtual environment and install dependencies (same as Method 1, Steps 2-4).

### Method 3: Installation via pip (Future Release)

**Note:** This method is not yet available. The package name `crypto-trader-bot` will be published to PyPI in a future release.

Once available, installation will be:

```bash
pip install crypto-trader-bot
```

## Post-Installation Setup

### 1. Verify GUI Dependencies

The bot uses tkinter for the GUI. Verify it's working:

```bash
python -c "import tkinter; tkinter.Tk()"
```

If a blank window appears, tkinter is working correctly.

#### Troubleshooting tkinter

**Ubuntu/Debian:**
```bash
sudo apt install python3-tk
```

**Fedora/CentOS:**
```bash
sudo dnf install python3-tkinter
```

**macOS:**
tkinter is included with Python from python.org

### 2. Test Imports

Verify all dependencies are installed:

```bash
python -c "import customtkinter; import pandas; import numpy; import google.generativeai; print('All imports successful!')"
```

### 3. Create Configuration Directory (Optional)

For organizing your settings:

```bash
mkdir config
```

## Updating the Bot

### From Git Repository

```bash
cd crypto_trader
git pull origin main
pip install --upgrade -r requirements.txt
```

### From Release Package

Download the new release and follow installation steps again.

## Uninstallation

### Step 1: Deactivate Virtual Environment

```bash
deactivate
```

### Step 2: Remove Files

**Windows:**
```cmd
rmdir /s /q crypto_trader
```

**macOS/Linux:**
```bash
rm -rf crypto_trader
```

### Step 3: Remove Virtual Environment

If you created it separately:
```bash
rm -rf venv
```

## Common Installation Issues

### Issue: "python: command not found"

**Solution:** 
- Windows: Use `py` instead of `python`
- Linux/macOS: Use `python3` instead of `python`

### Issue: "pip: command not found"

**Solution:**
```bash
python -m pip install --upgrade pip
```

### Issue: "Permission denied" on Linux/macOS

**Solution:**
Don't use `sudo` with pip. Use virtual environments instead.

### Issue: Import errors for tkinter

**Solution:**
Install system tkinter package:
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

### Issue: SSL Certificate Errors

**Solution:**
Update certificates:
```bash
pip install --upgrade certifi
```

### Issue: Slow Installation

**Solution:**
Use a faster mirror:
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Verifying Installation

Run these commands to verify everything is set up correctly:

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check installed packages
pip list

# Test bot startup
python bot.py
```

## Next Steps

After successful installation:

1. **Configure API Keys**: See [Configuration Guide](configuration.md)
2. **Set Up Binance Account**: See [API Setup Guide](api-setup.md)
3. **Learn to Use the Bot**: See [User Guide](user-guide.md)

## Getting Help

If you encounter issues:

1. Check [Common Issues](#common-installation-issues)
2. Search [GitHub Issues](https://github.com/GizzZmo/crypto_trader/issues)
3. Create a new issue with:
   - Your OS and Python version
   - Complete error message
   - Steps you've already tried

## Directory Structure After Installation

```
crypto_trader/
├── bot.py                 # Main application
├── requirements.txt       # Python dependencies
├── README.md             # Project overview
├── CONTRIBUTING.md       # Contribution guide
├── ROADMAP.md           # Development roadmap
├── SECURITY.md          # Security policy
├── CHANGELOG.md         # Version history
├── LICENSE              # License information
├── .gitignore           # Git ignore rules
├── docs/                # Documentation
└── .github/             # GitHub templates and workflows
```

---

**Installation complete!** 🎉

Continue to the [Configuration Guide](configuration.md) to set up your API keys.
