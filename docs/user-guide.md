# User Guide

Complete guide to using the AI-Powered Binance Grid Trading Bot.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Understanding the Interface](#understanding-the-interface)
3. [Using AI Assistant](#using-ai-assistant)
4. [Manual Trading Setup](#manual-trading-setup)
5. [Monitoring Your Bot](#monitoring-your-bot)
6. [Stopping the Bot](#stopping-the-bot)
7. [Best Practices](#best-practices)
8. [Common Scenarios](#common-scenarios)

---

## Getting Started

### First Launch

1. **Start the bot:**
   ```bash
   cd crypto_trader
   python bot.py
   ```

2. **The GUI will appear** with two main sections:
   - Left panel: Controls and configuration
   - Right panel: Activity dashboard

### Initial Setup Checklist

Before your first trade:

- [ ] API keys configured ([API Setup Guide](api-setup.md))
- [ ] Environment selected (Demo recommended)
- [ ] Bot configuration understood
- [ ] Trading strategy planned
- [ ] Risk tolerance assessed

---

## Understanding the Interface

### Left Panel: Bot Configuration

#### 1. Binance Credentials Section

**API Key Input:**
- Enter your Binance API key
- Will show as plain text
- Can be pasted from clipboard

**API Secret Input:**
- Enter your Binance API secret
- Displayed as dots (••••) for security
- Paste carefully (no extra spaces)

#### 2. Environment Selection

**Two Modes Available:**

**Demo (Testnet):**
- Use for testing
- Fake money
- No risk
- Recommended for beginners

**Live Trading:**
- Real money
- Real trades
- Full risk
- Use with caution

**How to Switch:**
- Click on your preferred mode
- Blue highlight indicates selected mode

#### 3. AI Strategy Assistant

**Gemini API Key:**
- Enter your Google Gemini API key
- Displayed as dots for security
- Required for AI features

**Find Best Opportunity Button:**
- Triggers AI market analysis
- Takes 10-30 seconds
- Results appear below button

**AI Recommendation Display:**
- Shows AI's analysis
- Recommended trading pair
- Suggested parameters
- Can be accepted or modified

#### 4. Manual Configuration

**Trading Pair:**
- Enter symbol (e.g., BTCUSDT)
- Must be valid Binance pair
- Case-sensitive

**Lower Price Boundary:**
- Minimum grid price
- Must be below current price
- Numeric value only

**Upper Price Boundary:**
- Maximum grid price
- Must be above current price
- Must be higher than lower bound

**Number of Grids:**
- Integer between 5-50
- More grids = tighter spacing
- Consider fees and volatility

**Total Investment:**
- Amount in quote currency (USDT)
- Will be distributed across grids
- Start small for testing

#### 5. Bot Controls

**Start Bot Button:**
- Green when ready
- Begins trading
- Validates parameters first

**Stop Bot Button:**
- Red when bot is running
- Stops all trading
- Disabled when bot is off

### Right Panel: Dashboard

**Activity Log:**
- Real-time bot activity
- Timestamped messages
- Scrollable view
- Auto-scrolls to latest

**Log Types:**
- Info: General activity
- Success: Trades executed
- Warning: Issues detected
- Error: Problems encountered

---

## Using AI Assistant

### Step-by-Step AI Trading

#### Step 1: Enter Gemini API Key

1. Find "AI Strategy Assistant" section
2. Click in the Gemini API Key field
3. Paste your API key
4. Key will be hidden (shown as dots)

#### Step 2: Click "Find Best Opportunity"

1. Click the blue button
2. Button changes to "Analyzing..."
3. Button becomes disabled during analysis
4. Wait 10-30 seconds

#### Step 3: Review AI Analysis

**Dashboard Shows:**
```
AI Assistant: Starting market analysis...
AI Assistant: Fetching all market tickers from Binance...
AI Assistant: Analyzing pairs: BTCUSDT, ETHUSDT, BNBUSDT...
AI Assistant: Analysis complete. Found an opportunity!
```

**AI Recommendation Example:**
```
Recommended Pair: BTCUSDT
Lower Boundary: $40,500
Upper Boundary: $43,500
Grids: 15
Reasoning: High volatility and volume detected...
```

#### Step 4: Accept or Modify

**To Accept:**
1. Parameters auto-fill in manual section
2. Review each parameter
3. Click "Start Bot"

**To Modify:**
1. Adjust any parameter as needed
2. Consider AI reasoning
3. Apply your own judgment
4. Click "Start Bot"

### AI Analysis Process

**What the AI Does:**

1. **Fetches Top Pairs:**
   - Gets high-volume USDT pairs
   - Filters out leveraged tokens
   - Sorts by 24h trading volume

2. **Analyzes Market Data:**
   - Current price
   - 24h high/low
   - Price change percentage
   - Trading volume
   - Volatility metrics

3. **Generates Recommendation:**
   - Evaluates all pairs
   - Considers risk/reward
   - Suggests optimal parameters
   - Provides reasoning

### When to Use AI vs Manual

**Use AI When:**
- You're new to crypto trading
- Market conditions are unclear
- You want data-driven decisions
- You're testing different pairs
- You need quick setup

**Use Manual When:**
- You have a specific strategy
- You know the market well
- AI recommendations seem off
- You want full control
- Testing specific parameters

---

## Manual Trading Setup

### Step-by-Step Manual Configuration

#### Step 1: Choose Trading Pair

**Research First:**
1. Visit Binance and check pairs
2. Look for high volume
3. Check price charts
4. Understand the asset

**Enter Pair:**
1. Click "Trading Pair" field
2. Type the symbol (e.g., BTCUSDT)
3. Ensure it's spelled correctly
4. Must match Binance exactly

#### Step 2: Set Price Boundaries

**Determine Range:**

1. **Check Current Price:**
   - View on Binance
   - Note recent highs/lows
   - Consider trend direction

2. **Set Lower Bound:**
   - Below current price
   - Near recent support
   - Leave margin for drops
   - Example: If BTC is $42,000, try $39,000

3. **Set Upper Bound:**
   - Above current price
   - Near recent resistance
   - Consider upside potential
   - Example: If BTC is $42,000, try $45,000

**Enter Values:**
1. Click "Lower Price Boundary"
2. Enter your lower price
3. Click "Upper Price Boundary"
4. Enter your upper price

#### Step 3: Choose Number of Grids

**Calculate Grid Spacing:**
```
Spacing = (Upper - Lower) / Grids
Example: ($45,000 - $39,000) / 20 = $300 per grid
```

**Factors to Consider:**
- **Market Volatility:** High volatility = fewer grids
- **Trading Fees:** More grids = more fees
- **Capital:** More capital allows more grids
- **Price Range:** Larger range = more grids

**Recommendations:**
- **Narrow Range (<5%):** 10-15 grids
- **Medium Range (5-10%):** 15-25 grids
- **Wide Range (>10%):** 25-40 grids

**Enter Value:**
1. Click "Number of Grids"
2. Enter your chosen number
3. Typically 10-30 for most strategies

#### Step 4: Set Investment Amount

**Determine Amount:**

**First Time Users:**
- Testnet: Any amount (it's fake)
- Live: $50-$100 minimum

**After Testing:**
- Based on success in testnet
- Percentage of portfolio (5-10% max)
- Amount you can afford to lose

**Per-Grid Calculation:**
```
Per Grid = Total Investment / Number of Grids
Example: $1000 / 20 = $50 per grid
```

**Enter Value:**
1. Click "Total Investment"
2. Enter amount (e.g., 1000)
3. Currency is quote asset (usually USDT)

#### Step 5: Verify Configuration

**Pre-Start Checklist:**
- [ ] Trading pair is correct
- [ ] Lower < Current Price < Upper
- [ ] Grid count is reasonable
- [ ] Investment amount is acceptable
- [ ] You understand the risks
- [ ] You're ready to monitor

---

## Monitoring Your Bot

### During Operation

**What to Watch:**

1. **Dashboard Activity:**
   - New orders placed
   - Orders filled
   - Price movements
   - Errors or warnings

2. **Binance Account:**
   - Open orders
   - Recent trades
   - Account balance
   - Profit/loss

3. **Market Conditions:**
   - Price staying in range?
   - Unusual volatility?
   - News or events?
   - Trend changes?

### Dashboard Messages

**Normal Operation:**
```
Bot started successfully
Placing grid orders...
Buy order filled at $41,500
Sell order filled at $42,000
Profit realized: $25.00
```

**Warning Signs:**
```
Warning: Price approaching lower boundary
Warning: High volatility detected
Warning: API rate limit approaching
```

**Errors:**
```
Error: Insufficient balance
Error: API connection lost
Error: Invalid order parameters
```

### When to Intervene

**Stop the Bot If:**
- Price breaks out of range significantly
- Major market news/events
- Technical errors occur repeatedly
- You need to adjust strategy
- Account balance issues

**Let It Run If:**
- Normal price fluctuations
- Grid orders executing as expected
- Minor warnings (rate limits, etc.)
- Profit is being generated

---

## Stopping the Bot

### Normal Stop Procedure

**Step 1: Click "Stop Bot"**
1. Locate red "Stop Bot" button
2. Click once
3. Wait for confirmation

**Step 2: Verify Stoppage**
- Dashboard shows "Bot stopped"
- "Start Bot" button re-enabled
- "Stop Bot" button disabled

**Step 3: Check Open Orders**
1. Log in to Binance
2. View open orders
3. Manually cancel if needed
4. Review executed trades

### Emergency Stop

**If Bot Malfunctions:**
1. Click "Stop Bot" immediately
2. Close the application
3. Log in to Binance
4. Cancel all open orders manually
5. Review account status

**Manual Order Cancellation:**
1. Binance → Orders → Open Orders
2. Select trading pair
3. Click "Cancel All"
4. Confirm cancellation

### Post-Stop Actions

**Review Performance:**
1. Calculate profit/loss
2. Review trade history
3. Analyze what worked
4. Identify improvements

**Export Data:**
- Binance trade history
- Bot log messages
- Performance metrics

---

## Best Practices

### Before Trading

1. **Test Thoroughly:**
   - Use testnet first
   - Run for several hours
   - Test various scenarios
   - Verify all features

2. **Start Small:**
   - Minimum investment
   - Single trading pair
   - Conservative parameters
   - Short time frame initially

3. **Educate Yourself:**
   - Understand grid trading
   - Learn about your chosen pair
   - Study market analysis
   - Know the risks

### During Trading

1. **Monitor Regularly:**
   - Check every few hours
   - Review before sleeping
   - Watch for market news
   - Track performance

2. **Be Patient:**
   - Grid trading needs time
   - Don't panic on dips
   - Trust the strategy
   - Avoid emotional decisions

3. **Keep Records:**
   - Screenshot configurations
   - Note start/stop times
   - Track profit/loss
   - Document lessons learned

### After Trading

1. **Analyze Results:**
   - Calculate returns
   - Review efficiency
   - Identify patterns
   - Learn from mistakes

2. **Optimize Strategy:**
   - Adjust parameters
   - Try different pairs
   - Refine grid counts
   - Improve timing

3. **Manage Risk:**
   - Don't over-invest
   - Diversify strategies
   - Set loss limits
   - Take profits regularly

---

## Common Scenarios

### Scenario 1: First Test Trade

**Goal:** Learn the system risk-free

**Steps:**
1. Use testnet API keys
2. Select "Demo (Testnet)" mode
3. Use AI assistant for recommendations
4. Start with default parameters
5. Run for 2-4 hours
6. Monitor and learn
7. Stop and review

**Expected Outcome:**
- Understand interface
- See how grid trading works
- Gain confidence
- No real money at risk

### Scenario 2: First Live Trade

**Goal:** Real trading with minimal risk

**Steps:**
1. Use production API keys
2. Select "Live Trading" mode
3. Choose high-liquidity pair (BTCUSDT)
4. Set tight range (current price ±2%)
5. Use 10-15 grids
6. Invest minimum amount ($50-100)
7. Monitor closely for first hour
8. Review after 24 hours

**Expected Outcome:**
- Real trading experience
- Small profits or losses
- Confidence building
- Strategy validation

### Scenario 3: Range-Bound Market

**Goal:** Profit from sideways price action

**Best Setup:**
- More grids (25-40)
- Tight range (±3-5%)
- Medium investment
- Popular pairs

**Strategy:**
- Price oscillates within range
- Frequent buy-sell cycles
- Accumulate small profits
- Compound gains

### Scenario 4: Trending Market

**Goal:** Adapt to directional movement

**Uptrend Setup:**
- Bias upper boundary higher
- Fewer grids (10-20)
- Take profits on way up

**Downtrend Setup:**
- Consider not grid trading
- Or set lower boundaries
- Reduce investment

### Scenario 5: High Volatility

**Goal:** Manage risk during volatile periods

**Strategy:**
- Fewer grids (10-15)
- Wider spacing
- Smaller investment
- Tighter stop-loss

**Monitoring:**
- Watch more frequently
- Be ready to stop
- Adjust quickly

---

## Keyboard Shortcuts & Tips

**None currently**, but future versions may include:
- Ctrl+S: Stop bot
- Ctrl+R: Restart bot
- Ctrl+L: Clear logs
- Ctrl+E: Export logs

## Troubleshooting

See [Configuration Guide](configuration.md#troubleshooting-configuration) for common issues and solutions.

---

## Next Steps

**After Mastering Basic Usage:**
1. Explore advanced strategies
2. Try multiple pairs
3. Optimize parameters
4. Share your experience
5. Contribute improvements

## Getting Help

- [FAQ](faq.md) - Common questions
- [GitHub Issues](https://github.com/GizzZmo/crypto_trader/issues) - Report bugs
- [Discussions](https://github.com/GizzZmo/crypto_trader/discussions) - Community help

---

**Happy Trading! 📈**

Remember: Never invest more than you can afford to lose.
