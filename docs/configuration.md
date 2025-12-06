# Configuration Guide

This guide covers all configuration options for the AI-Powered Binance Grid Trading Bot.

## Overview

The bot can be configured through:
1. **GUI Interface** (recommended for most users)
2. **Configuration Files** (for advanced users - future feature)
3. **Environment Variables** (for automation)

## API Configuration

### Binance API Setup

You need Binance API credentials to use the bot. See [API Setup Guide](api-setup.md) for detailed instructions.

**Required Credentials:**
- API Key
- API Secret

**Where to Enter:**
1. Launch the bot: `python bot.py`
2. Find "Binance Credentials" section in the left panel
3. Enter your API Key
4. Enter your API Secret

**Security Notes:**
- ⚠️ Never share your API keys
- ⚠️ Never commit API keys to version control
- ⚠️ Use testnet keys for testing
- ⚠️ Restrict API key permissions (disable withdrawals)

### Google Gemini API Setup

For AI-powered market analysis features.

**Get API Key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

**Where to Enter:**
1. Find "AI Strategy Assistant" section
2. Enter your Gemini API Key

**Optional:** This is only needed if you want to use AI market analysis features.

## Trading Environment

### Demo Mode (Testnet)

**Purpose:** Risk-free testing with fake money

**When to Use:**
- First time using the bot
- Testing new strategies
- Learning how grid trading works
- Developing/debugging

**How to Select:**
1. Find "Environment Selection" in the GUI
2. Select "Demo (Testnet)"

**API Requirements:**
- Use Binance Testnet API keys
- Get testnet keys from [Binance Testnet](https://testnet.binance.vision/)

**Limitations:**
- Not real money
- Limited market data
- May have different liquidity than live market

### Live Trading Mode

**Purpose:** Real trading with actual cryptocurrency

**When to Use:**
- After thorough testing in demo mode
- When you understand the risks
- With money you can afford to lose

**How to Select:**
1. Find "Environment Selection" in the GUI
2. Select "Live Trading"

**API Requirements:**
- Use production Binance API keys
- Set appropriate permissions

**⚠️ Warning:**
- Real money is at risk
- Always start with small amounts
- Monitor regularly
- Use stop-loss strategies

## Grid Trading Parameters

### Trading Pair

**What:** The cryptocurrency pair to trade

**Format:** `BASEQUOTE` (e.g., BTCUSDT, ETHUSDT)
- BASE: The cryptocurrency you're trading (BTC, ETH)
- QUOTE: The currency you're using to buy (USDT, BUSD)

**Examples:**
- `BTCUSDT` - Bitcoin vs Tether
- `ETHUSDT` - Ethereum vs Tether
- `BNBUSDT` - Binance Coin vs Tether

**How to Choose:**
- High liquidity pairs work best
- Check 24h volume on Binance
- AI assistant can recommend pairs

**Where to Enter:**
GUI → Manual Configuration → Trading Pair

### Lower Price Boundary

**What:** Minimum price for grid placement

**Purpose:** Sets the bottom of your trading range

**How to Choose:**
1. Analyze recent price action
2. Identify support levels
3. Consider volatility
4. Leave margin for price drops

**Example:**
- Current BTC price: $42,000
- Recent low: $38,000
- Lower boundary: $38,000 (or slightly below)

**Best Practices:**
- Don't set too tight (price may break out)
- Don't set too wide (reduces profit per grid)
- Consider 24h trading range
- Review historical price charts

**Where to Enter:**
GUI → Manual Configuration → Lower Price Boundary

### Upper Price Boundary

**What:** Maximum price for grid placement

**Purpose:** Sets the top of your trading range

**How to Choose:**
1. Analyze recent highs
2. Identify resistance levels
3. Consider upside potential
4. Leave margin for price spikes

**Example:**
- Current BTC price: $42,000
- Recent high: $45,000
- Upper boundary: $45,000 (or slightly above)

**Best Practices:**
- Should be realistic for timeframe
- Consider market trend
- Leave room for profit taking
- Balance risk/reward

**Where to Enter:**
GUI → Manual Configuration → Upper Price Boundary

### Number of Grids

**What:** How many price levels between boundaries

**Purpose:** Determines grid spacing and trade frequency

**Typical Range:** 5-50 grids

**Factors to Consider:**
1. **Price Range:** Larger range = more grids
2. **Trading Fees:** More grids = more fees
3. **Volatility:** Higher volatility = fewer grids
4. **Capital:** More capital = more grids possible

**Examples:**

**Conservative (10-20 grids):**
- Wider spacing
- Fewer trades
- Lower fees
- Better for volatile markets

**Moderate (20-30 grids):**
- Balanced approach
- Good for most situations
- Reasonable fees

**Aggressive (30-50 grids):**
- Tight spacing
- More trades
- Higher fees
- Better for range-bound markets

**Formula:**
```
Grid Spacing = (Upper Boundary - Lower Boundary) / Number of Grids
```

**Example Calculation:**
```
Upper: $45,000
Lower: $38,000
Grids: 20
Spacing: ($45,000 - $38,000) / 20 = $350 per grid
```

**Where to Enter:**
GUI → Manual Configuration → Number of Grids

### Total Investment

**What:** Total capital to allocate to the strategy

**Currency:** Quote currency (usually USDT)

**How It's Distributed:**
- Divided equally across all grids
- Part in buy orders (below current price)
- Part in sell orders (above current price)

**Example:**
```
Total Investment: 1000 USDT
Number of Grids: 10
Investment per Grid: 100 USDT
```

**Best Practices:**
1. **Start Small:** Test with minimum amounts
2. **Risk Management:** Never use all your capital
3. **Diversification:** Don't put everything in one bot
4. **Emergency Fund:** Keep reserves for opportunities

**Recommended Starting Amounts:**
- **Testnet:** Any amount (it's fake)
- **First Live Trade:** $50-$100
- **After Testing:** $500-$1000
- **Experienced:** Based on your risk tolerance

**Where to Enter:**
GUI → Manual Configuration → Total Investment

## AI Assistant Configuration

### Enabling AI Features

**Requirements:**
- Google Gemini API key
- Valid Binance API credentials

**Features:**
- Market analysis
- Trading pair recommendations
- Grid parameter suggestions
- Volatility assessment

### Using AI Recommendations

**How It Works:**
1. Click "Find Best Opportunity"
2. AI analyzes top trading pairs
3. Evaluates volatility and trends
4. Recommends optimal parameters
5. You review and accept/modify

**What AI Considers:**
- 24h trading volume
- Price volatility
- Recent trends
- Technical indicators
- Market conditions

**AI Recommendation Output:**
- Recommended trading pair
- Suggested price boundaries
- Optimal grid count
- Investment advice

**Best Practices:**
- Always review AI suggestions
- Don't blindly follow recommendations
- Verify parameters make sense
- Start with smaller amounts
- Monitor performance

## Advanced Configuration (Future Features)

### Configuration File (Coming Soon)

Create a `config.json`:

```json
{
  "binance": {
    "api_key": "your_api_key",
    "api_secret": "your_api_secret",
    "testnet": true
  },
  "gemini": {
    "api_key": "your_gemini_key"
  },
  "trading": {
    "pair": "BTCUSDT",
    "lower_bound": 38000,
    "upper_bound": 45000,
    "grids": 20,
    "investment": 1000
  },
  "risk_management": {
    "max_investment_per_bot": 5000,
    "stop_loss_percentage": 10,
    "take_profit_percentage": 20
  }
}
```

**Note:** This feature is planned for future releases.

### Environment Variables

For automation and security:

```bash
# Linux/macOS
export BINANCE_API_KEY="your_key"
export BINANCE_API_SECRET="your_secret"
export GEMINI_API_KEY="your_gemini_key"

# Windows
set BINANCE_API_KEY=your_key
set BINANCE_API_SECRET=your_secret
set GEMINI_API_KEY=your_gemini_key
```

**Note:** This feature is planned for future releases.

## Configuration Best Practices

### Security

1. **Never hardcode credentials**
2. **Use environment variables or config files**
3. **Add config files to .gitignore**
4. **Rotate keys regularly**
5. **Use testnet for development**

### Risk Management

1. **Start with demo mode**
2. **Use small amounts initially**
3. **Don't invest more than you can afford to lose**
4. **Set appropriate boundaries**
5. **Monitor regularly**

### Performance

1. **Choose liquid pairs**
2. **Set realistic boundaries**
3. **Consider trading fees**
4. **Adjust grid count based on volatility**
5. **Review and optimize periodically**

## Configuration Checklist

Before starting the bot:

- [ ] API keys configured (Binance)
- [ ] API keys tested in demo mode
- [ ] Environment selected (Demo/Live)
- [ ] Trading pair chosen
- [ ] Price boundaries set
- [ ] Number of grids determined
- [ ] Investment amount set
- [ ] Risk tolerance assessed
- [ ] Monitoring plan in place
- [ ] Emergency stop plan ready

## Troubleshooting Configuration

### API Connection Issues

**Problem:** Cannot connect to Binance API

**Solutions:**
1. Verify API key and secret are correct
2. Check API key permissions
3. Ensure API key is not restricted by IP
4. Verify internet connection
5. Check Binance API status

### Invalid Parameters

**Problem:** Bot rejects trading parameters

**Solutions:**
1. Ensure lower < upper boundary
2. Verify pair exists on Binance
3. Check minimum trading amounts
4. Ensure sufficient balance
5. Verify grid count is positive

### AI Features Not Working

**Problem:** AI assistant fails

**Solutions:**
1. Verify Gemini API key is valid
2. Check internet connection
3. Ensure API quota not exceeded
4. Try again (may be temporary)
5. Use manual configuration instead

## Next Steps

After configuration:

1. **Test in Demo Mode**: Verify everything works
2. **Review Documentation**: Read the [User Guide](user-guide.md)
3. **Start Small**: Begin with minimal investment
4. **Monitor**: Watch the bot's activity
5. **Optimize**: Adjust parameters based on results

## Getting Help

Need help with configuration?

- Check [FAQ](faq.md)
- Review [User Guide](user-guide.md)
- Search [GitHub Issues](https://github.com/GizzZmo/crypto_trader/issues)
- Ask in [Discussions](https://github.com/GizzZmo/crypto_trader/discussions)

---

**Next:** Continue to [User Guide](user-guide.md) to learn how to operate the bot.
