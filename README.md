# 🤖 AI-Powered Binance Grid Trading Bot

An intelligent cryptocurrency trading bot that combines grid trading strategies with AI-powered market analysis using Google's Gemini AI. This bot features a modern GUI built with CustomTkinter and supports both testnet and live trading on Binance.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## ✨ Features

- **AI-Powered Market Analysis**: Utilizes Google's Gemini AI to analyze market data and recommend optimal trading opportunities
- **Grid Trading Strategy**: Automated grid trading with customizable price ranges and grid levels
- **Modern GUI**: User-friendly interface built with CustomTkinter
- **Dual Mode Support**: 
  - Demo Mode (Testnet) for risk-free testing
  - Live Trading Mode for real market execution
- **Real-Time Monitoring**: Live dashboard displaying bot activity and trading status
- **High-Volume Pair Detection**: Automatically identifies top trading pairs by volume
- **Risk Management**: Configurable investment amounts and grid parameters
- **Comprehensive Logging**: Detailed activity logs for monitoring and debugging

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Binance API credentials (for testnet or live trading)
- Google Gemini API key (for AI features)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GizzZmo/crypto_trader.git
   cd crypto_trader
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the bot**
   ```bash
   python bot.py
   ```

## 📖 Usage

### Basic Configuration

1. **Launch the application**
   ```bash
   python bot.py
   ```

2. **Enter your API credentials**
   - Binance API Key
   - Binance API Secret
   - Google Gemini API Key (for AI features)

3. **Select trading environment**
   - Demo (Testnet): Risk-free testing environment
   - Live Trading: Real market trading (use with caution)

### AI-Assisted Trading

1. Click **"Find Best Opportunity"** to let the AI analyze the market
2. The AI will:
   - Fetch high-volume trading pairs
   - Analyze market trends and volatility
   - Recommend optimal grid trading parameters
3. Review the AI recommendation
4. Click **"Start Bot"** to begin automated trading

### Manual Configuration

Alternatively, you can manually configure the bot:
- **Trading Pair**: e.g., BTCUSDT, ETHUSDT
- **Lower Price Boundary**: Minimum grid price
- **Upper Price Boundary**: Maximum grid price
- **Number of Grids**: Grid levels between boundaries
- **Total Investment**: Amount to invest (in quote currency)

## 🔧 API Setup

### Binance API

1. Visit [Binance API Management](https://www.binance.com/en/my/settings/api-management)
2. Create a new API key
3. Enable spot trading permissions
4. Save your API key and secret securely

**For Testnet:**
1. Visit [Binance Testnet](https://testnet.binance.vision/)
2. Create a testnet API key
3. Use testnet credentials in Demo mode

### Google Gemini API

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key for use in the bot

## 🏗️ Architecture

The bot consists of several key components:

- **GUI Layer**: CustomTkinter-based user interface
- **Trading Engine**: Grid trading logic and order management
- **AI Integration**: Gemini AI for market analysis
- **Binance Client**: API integration for trading operations
- **Logger**: Activity monitoring and error tracking

## ⚙️ Configuration

### Grid Trading Parameters

- **Lower Bound**: Minimum price for grid placement
- **Upper Bound**: Maximum price for grid placement
- **Grid Count**: Number of price levels in the grid
- **Investment**: Total capital allocated to the strategy

### Safety Features

- Order tracking to prevent duplicates
- Error handling for API failures
- State management for bot operations
- Thread-safe GUI updates

## 📊 How Grid Trading Works

Grid trading is a quantitative trading strategy that:

1. Divides a price range into equal intervals (grids)
2. Places buy orders at lower grid levels
3. Places sell orders at higher grid levels
4. Profits from market volatility within the range

**Example:**
- Range: $40,000 - $50,000
- Grids: 10
- Grid spacing: $1,000
- The bot buys when price drops and sells when price rises

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 🗺️ Roadmap

See [ROADMAP.md](ROADMAP.md) for planned features and development milestones.

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**IMPORTANT**: Cryptocurrency trading carries significant risk. This bot is provided for educational purposes. Always:
- Start with testnet/demo mode
- Never invest more than you can afford to lose
- Understand the risks of automated trading
- Monitor your bot regularly
- Use appropriate risk management

The developers are not responsible for any financial losses incurred through the use of this software.

## 🙏 Acknowledgments

- [python-binance](https://github.com/sammchardy/python-binance) - Binance API wrapper
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern GUI framework
- [Google Generative AI](https://ai.google.dev/) - AI-powered market analysis

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/GizzZmo/crypto_trader/issues)
- **Discussions**: [GitHub Discussions](https://github.com/GizzZmo/crypto_trader/discussions)

## 🔐 Security

Please report security vulnerabilities to the project maintainers. See [SECURITY.md](SECURITY.md) for details.

---

**Happy Trading! 📈**
