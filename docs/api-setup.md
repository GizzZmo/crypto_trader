# API Setup Guide

This guide will help you set up API keys for Binance and Google Gemini to use with the trading bot.

## Table of Contents
1. [Binance API Setup](#binance-api-setup)
2. [Binance Testnet Setup](#binance-testnet-setup)
3. [Google Gemini API Setup](#google-gemini-api-setup)
4. [Security Best Practices](#security-best-practices)
5. [Troubleshooting](#troubleshooting)

---

## Binance API Setup

### Prerequisites
- Active Binance account
- Completed identity verification (KYC)
- Two-factor authentication (2FA) enabled

### Step 1: Access API Management

1. Log in to [Binance](https://www.binance.com)
2. Hover over your profile icon (top right)
3. Click on **"API Management"**
4. Or directly visit: https://www.binance.com/en/my/settings/api-management

### Step 2: Create API Key

1. Click **"Create API"** button
2. Choose **"System Generated"** (recommended)
3. Enter a label/name for your API key:
   - Example: "Grid Trading Bot"
   - Use a descriptive name
4. Complete 2FA verification:
   - Enter your Google Authenticator code
   - Enter SMS code (if enabled)
   - Confirm via email

### Step 3: Save Your Credentials

**Important:** You'll only see the API Secret once!

1. **Copy API Key**
   - Click the copy icon
   - Save to a secure location
   
2. **Copy Secret Key**
   - Click "Show" to reveal
   - Click copy icon
   - Save to a secure location
   - **You cannot view this again!**

**Recommended:** Save in a password manager like:
- 1Password
- LastPass
- Bitwarden
- KeePass

### Step 4: Configure API Key Restrictions

**IP Access Restriction (Recommended):**
1. Click "Edit" on your API key
2. Select **"Restrict access to trusted IPs only"**
3. Click "Confirm"
4. Add your IP address:
   - Find your IP: https://whatismyipaddress.com/
   - Enter IP address
   - Save changes

**Note:** If you have a dynamic IP, you may need to use "Unrestricted" but enable IP whitelist when possible.

### Step 5: Set API Key Permissions

**For Grid Trading Bot, enable:**
- ✅ **Enable Spot & Margin Trading** - Required for trading
- ✅ **Enable Reading** - Required for market data

**DO NOT enable:**
- ❌ **Enable Withdrawals** - Not needed and dangerous
- ❌ **Enable Internal Transfer** - Not needed
- ❌ **Enable Futures** - Not supported by this bot

**Permission Settings:**
1. Click "Edit" on your API key
2. Check only necessary permissions
3. Click "Save"
4. Complete 2FA verification

### Step 6: Test API Connection

1. Launch the bot
2. Enter API Key and Secret
3. Select "Demo (Testnet)" first
4. Check for connection errors

---

## Binance Testnet Setup

**Purpose:** Risk-free testing with fake cryptocurrency

### Why Use Testnet?

- ✅ No real money at risk
- ✅ Test bot functionality
- ✅ Learn grid trading
- ✅ Debug issues
- ✅ Perfect for beginners

### Step 1: Access Binance Testnet

1. Visit [Binance Testnet](https://testnet.binance.vision/)
2. No account creation needed
3. Free testnet API keys available

### Step 2: Get Testnet API Keys

1. Click **"Generate HMAC_SHA256 Key"**
2. Save the API Key
3. Save the Secret Key
4. No verification required

**Testnet Features:**
- Unlimited API keys
- No trading fees (or very low)
- Fake USDT and BTC
- Simulated market data
- May have different prices than live market

### Step 3: Get Test Funds

Testnet accounts usually come with test funds:
- Check your testnet wallet
- Should have test BTC, ETH, USDT, etc.
- If not, request from testnet faucet

### Step 4: Use Testnet in Bot

1. Launch the bot
2. Enter **testnet API key and secret**
3. Select **"Demo (Testnet)"** mode
4. Start trading with fake money

**Important:** Don't mix testnet and mainnet API keys!

---

## Google Gemini API Setup

**Purpose:** Enable AI-powered market analysis

### Step 1: Access Google AI Studio

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. No credit card required (free tier available)

### Step 2: Create API Key

1. Click **"Create API Key"**
2. Select or create a Google Cloud project
3. API key will be generated automatically
4. Click **"Copy"** to copy the key

### Step 3: Save Your API Key

Save the API key securely:
- It starts with `AI...`
- Keep it confidential
- Don't share publicly
- Store in password manager

### Step 4: Understand Usage Limits

**Free Tier:**
- 60 requests per minute
- Generous monthly quota
- Sufficient for most users

**If you need more:**
- Upgrade to paid plan
- Check [Google AI Pricing](https://ai.google.dev/pricing)

### Step 5: Use in Bot

1. Launch the bot
2. Find "AI Strategy Assistant" section
3. Enter your Gemini API Key
4. Click "Find Best Opportunity" to test

---

## Security Best Practices

### API Key Security

**DO:**
- ✅ Store keys in password manager
- ✅ Use environment variables for automation
- ✅ Enable IP whitelist when possible
- ✅ Disable withdrawals on Binance API
- ✅ Use testnet for development
- ✅ Rotate keys regularly (every 3-6 months)
- ✅ Create separate keys for different purposes
- ✅ Monitor API usage regularly

**DON'T:**
- ❌ Share keys publicly
- ❌ Commit keys to version control (Git)
- ❌ Store keys in plain text files
- ❌ Enable withdrawal permissions
- ❌ Use same key across multiple applications
- ❌ Leave unused keys active
- ❌ Screenshot keys and post online
- ❌ Email keys to anyone

### Binance Account Security

1. **Enable 2FA:**
   - Google Authenticator (recommended)
   - SMS backup
   - Security key (YubiKey)

2. **Use Strong Password:**
   - 12+ characters
   - Mix of letters, numbers, symbols
   - Unique to Binance

3. **Enable Anti-Phishing Code:**
   - Settings → Security
   - Set anti-phishing code
   - Verify in all Binance emails

4. **Enable Withdrawal Whitelist:**
   - Only allow withdrawals to saved addresses
   - Settings → Security

5. **Monitor Login Activity:**
   - Check login history regularly
   - Log out unknown devices

### What to Do If Compromised

**If you suspect your API key is compromised:**

1. **Immediately delete the API key:**
   - Binance → API Management
   - Click delete on compromised key
   - Confirm deletion

2. **Check account activity:**
   - Review recent trades
   - Check withdrawal history
   - Look for unauthorized access

3. **Change your password:**
   - Use a new, strong password
   - Enable 2FA if not already active

4. **Create new API key:**
   - Follow setup steps again
   - Use different permissions
   - Enable IP whitelist

5. **Contact Binance support:**
   - If unauthorized trades occurred
   - Report the incident
   - Follow their guidance

---

## Troubleshooting

### Common Issues

#### "Invalid API Key"

**Causes:**
- Incorrect key or secret
- Spaces in copied key
- Wrong environment (testnet vs mainnet)

**Solutions:**
1. Verify key and secret are correct
2. Remove any spaces before/after
3. Check you're using correct environment
4. Regenerate API key if needed

#### "IP Not Whitelisted"

**Causes:**
- IP restriction enabled
- Your IP changed
- VPN/proxy in use

**Solutions:**
1. Check your current IP
2. Add IP to whitelist in Binance
3. Temporarily disable IP restriction
4. Disable VPN/proxy

#### "Permission Denied"

**Causes:**
- Insufficient API permissions
- Trading not enabled
- Margin trading disabled

**Solutions:**
1. Edit API key permissions
2. Enable "Spot & Margin Trading"
3. Enable "Reading"
4. Save and try again

#### "API Rate Limit Exceeded"

**Causes:**
- Too many requests
- Multiple bots using same key
- Heavy market data queries

**Solutions:**
1. Wait a few minutes
2. Reduce request frequency
3. Use separate keys for different bots
4. Check Binance API limits

#### "Gemini API Error"

**Causes:**
- Invalid API key
- Quota exceeded
- Service unavailable

**Solutions:**
1. Verify Gemini key is correct
2. Check quota at AI Studio
3. Wait and retry
4. Use manual configuration instead

### Testing Your API Setup

**Binance API Test:**
```python
from binance.client import Client

api_key = "your_api_key"
api_secret = "your_secret_key"

client = Client(api_key, api_secret, testnet=True)  # Use testnet=False for mainnet

# Test connection
server_time = client.get_server_time()
print(f"Connected! Server time: {server_time}")

# Test account access
account = client.get_account()
print(f"Account status: {account['accountType']}")
```

**Gemini API Test:**
```python
import google.generativeai as genai

genai.configure(api_key="your_gemini_key")
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Hello!")
print(response.text)
```

---

## API Key Management Checklist

Before using the bot:

- [ ] Created Binance API key
- [ ] Saved API key and secret securely
- [ ] Configured proper permissions (trading + reading only)
- [ ] Disabled withdrawal permission
- [ ] Enabled IP whitelist (if stable IP)
- [ ] Tested API connection
- [ ] Created testnet API key for testing
- [ ] Created Gemini API key (optional)
- [ ] Tested all API connections
- [ ] Documented where keys are stored
- [ ] Set calendar reminder to rotate keys

---

## Next Steps

After setting up your API keys:

1. **Test in Testnet First**: Use testnet keys in demo mode
2. **Read Configuration Guide**: [Configuration Guide](configuration.md)
3. **Review Security**: Read [SECURITY.md](../SECURITY.md)
4. **Start Trading**: Follow [User Guide](user-guide.md)

## Additional Resources

- [Binance API Documentation](https://binance-docs.github.io/apidocs/)
- [Google Gemini AI Documentation](https://ai.google.dev/docs)
- [Binance API Best Practices](https://www.binance.com/en/support/faq/360002502072)

---

**Stay Safe! 🔒** Always prioritize security when handling API keys.
