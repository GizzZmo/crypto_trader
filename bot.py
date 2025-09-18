import tkinter
import customtkinter
import threading
import queue
import time
import json
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
import pandas as pd
import numpy as np
import google.generativeai as genai

# --- Basic Configuration ---
# Set the appearance and color theme for the GUI
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BinanceGridBotApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("AI-Powered Binance Grid Trading Bot")
        self.geometry("1100x780")

        self.bot_thread = None
        self.bot_running = False
        self.gui_queue = queue.Queue()

        # --- Main Grid Layout ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Left Frame for Controls ---
        self.left_frame = customtkinter.CTkFrame(self, width=280, corner_radius=10)
        self.left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.left_frame.grid_propagate(False)

        # --- Right Frame for Dashboard ---
        self.right_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.right_frame.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="nsew")
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)

        self.create_controls()
        self.create_dashboard()

        # Start the GUI update loop
        self.after(100, self.process_gui_queue)

    def create_controls(self):
        """Creates all the input fields and buttons in the left control frame."""
        frame = self.left_frame
        
        # --- Title ---
        title_label = customtkinter.CTkLabel(frame, text="Bot Configuration", font=customtkinter.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=20)

        # --- API Configuration ---
        api_frame = customtkinter.CTkFrame(frame)
        api_frame.pack(pady=10, padx=10, fill="x")
        api_label = customtkinter.CTkLabel(api_frame, text="Binance Credentials", font=customtkinter.CTkFont(size=14, weight="bold"))
        api_label.pack(pady=(5,10))

        self.api_key_entry = customtkinter.CTkEntry(api_frame, placeholder_text="API Key")
        self.api_key_entry.pack(pady=5, padx=10, fill="x")
        self.api_secret_entry = customtkinter.CTkEntry(api_frame, placeholder_text="API Secret", show="*")
        self.api_secret_entry.pack(pady=5, padx=10, fill="x")

        # --- Environment Selection ---
        self.env_selection = customtkinter.CTkSegmentedButton(frame, values=["Demo (Testnet)", "Live Trading"])
        self.env_selection.pack(pady=10, padx=10, fill="x")
        self.env_selection.set("Demo (Testnet)")

        # --- AI Strategy Assistant ---
        ai_frame = customtkinter.CTkFrame(frame)
        ai_frame.pack(pady=10, padx=10, fill="x")
        ai_label = customtkinter.CTkLabel(ai_frame, text="AI Strategy Assistant", font=customtkinter.CTkFont(size=14, weight="bold"))
        ai_label.pack(pady=(5,10))

        self.gemini_api_key_entry = customtkinter.CTkEntry(ai_frame, placeholder_text="Google Gemini API Key", show="*")
        self.gemini_api_key_entry.pack(pady=5, padx=10, fill="x")

        self.find_opportunity_button = customtkinter.CTkButton(ai_frame, text="Find Best Opportunity", command=self.find_best_opportunity)
        self.find_opportunity_button.pack(pady=10, padx=10, fill="x")
        self.ai_recommendation_label = customtkinter.CTkLabel(ai_frame, text="Recommendation will appear here...", wraplength=220, justify="left")
        self.ai_recommendation_label.pack(pady=5, padx=10)

        # --- Manual Bot Configuration ---
        manual_frame = customtkinter.CTkFrame(frame)
        manual_frame.pack(pady=10, padx=10, fill="x")
        manual_label = customtkinter.CTkLabel(manual_frame, text="Manual Configuration", font=customtkinter.CTkFont(size=14, weight="bold"))
        manual_label.pack(pady=(5,10))

        self.pair_entry = customtkinter.CTkEntry(manual_frame, placeholder_text="Trading Pair (e.g., BTCUSDT)")
        self.pair_entry.pack(pady=5, padx=10, fill="x")
        self.lower_bound_entry = customtkinter.CTkEntry(manual_frame, placeholder_text="Lower Price Boundary")
        self.lower_bound_entry.pack(pady=5, padx=10, fill="x")
        self.upper_bound_entry = customtkinter.CTkEntry(manual_frame, placeholder_text="Upper Price Boundary")
        self.upper_bound_entry.pack(pady=5, padx=10, fill="x")
        self.grids_entry = customtkinter.CTkEntry(manual_frame, placeholder_text="Number of Grids")
        self.grids_entry.pack(pady=5, padx=10, fill="x")
        self.investment_entry = customtkinter.CTkEntry(manual_frame, placeholder_text="Total Investment (e.g., 1000 USDT)")
        self.investment_entry.pack(pady=5, padx=10, fill="x")

        # --- Bot Controls ---
        self.start_bot_button = customtkinter.CTkButton(frame, text="Start Bot", command=self.start_bot)
        self.start_bot_button.pack(pady=15, padx=10, fill="x")
        self.stop_bot_button = customtkinter.CTkButton(frame, text="Stop Bot", command=self.stop_bot, state="disabled")
        self.stop_bot_button.pack(pady=5, padx=10, fill="x")

    def create_dashboard(self):
        """Creates the text box for logging bot activity."""
        self.dashboard_textbox = customtkinter.CTkTextbox(self.right_frame, state="disabled", corner_radius=10, font=("Courier", 13))
        self.dashboard_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def log_to_dashboard(self, message):
        """Thread-safe method to log messages to the GUI."""
        self.gui_queue.put(message)

    def process_gui_queue(self):
        """Processes messages from the queue to update the GUI."""
        while not self.gui_queue.empty():
            try:
                message = self.gui_queue.get_nowait()
                self.dashboard_textbox.configure(state="normal")
                self.dashboard_textbox.insert("end", message + "\n")
                self.dashboard_textbox.see("end")
                self.dashboard_textbox.configure(state="disabled")
            except queue.Empty:
                pass
        self.after(100, self.process_gui_queue)

    def find_best_opportunity(self):
        """Starts a thread to get the LLM recommendation."""
        self.log_to_dashboard("AI Assistant: Starting market analysis...")
        self.find_opportunity_button.configure(state="disabled", text="Analyzing...")
        
        # Run analysis in a separate thread to not freeze the GUI
        threading.Thread(target=self.run_llm_analysis, daemon=True).start()

    def run_llm_analysis(self):
        """Gathers data, queries the LLM, and updates the GUI."""
        try:
            client = self.get_binance_client() # Use a temporary client for data fetching
            if not client:
                 self.log_to_dashboard("AI Assistant Error: Please enter valid API keys first.")
                 self.find_opportunity_button.configure(state="normal", text="Find Best Opportunity")
                 return
            
            # Dynamically fetch high-volume pairs instead of using a hardcoded list.
            pairs = self.fetch_high_volume_pairs(client, limit=10)
            self.log_to_dashboard(f"AI Assistant: Analyzing pairs: {', '.join(pairs)}")
            
            gemini_api_key = self.gemini_api_key_entry.get()
            if not gemini_api_key:
                self.log_to_dashboard("AI Assistant Error: Please enter your Google Gemini API key.")
                self.after(0, lambda: self.find_opportunity_button.configure(state="normal", text="Find Best Opportunity"))
                return
                 
            market_data = self.gather_market_data(client, pairs)
            
            if market_data:
                recommendation = self.get_gemini_recommendation(market_data, gemini_api_key)
            else:
                recommendation = None
                self.log_to_dashboard("AI Assistant: No market data gathered. Cannot get recommendation.")

            if recommendation:
                self.log_to_dashboard("AI Assistant: Analysis complete. Found an opportunity!")
                # Update GUI from the main thread
                self.after(0, self.update_ui_with_recommendation, recommendation)
            else:
                self.log_to_dashboard("AI Assistant: Could not determine a clear opportunity.")
        
        except Exception as e:
            self.log_to_dashboard(f"AI Assistant Error: {e}")
        finally:
            # Re-enable the button from the main thread
            self.after(0, lambda: self.find_opportunity_button.configure(state="normal", text="Find Best Opportunity"))

    def fetch_high_volume_pairs(self, client, limit=10):
        """Fetches the top N USDT pairs by 24h trading volume."""
        try:
            self.log_to_dashboard("AI Assistant: Fetching all market tickers from Binance...")
            all_tickers = client.get_ticker()
            
            # Filter for USDT pairs and also filter out leveraged tokens (e.g., BTCUP, BTCDOWN)
            usdt_pairs = [
                t for t in all_tickers 
                if t['symbol'].endswith('USDT') and 'UP' not in t['symbol'] and 'DOWN' not in t['symbol']
            ]
            
            # Sort by quote volume (volume in USDT)
            sorted_pairs = sorted(usdt_pairs, key=lambda x: float(x['quoteVolume']), reverse=True)
            
            top_pairs = [p['symbol'] for p in sorted_pairs[:limit]]
            self.log_to_dashboard(f"AI Assistant: Found top {limit} high-volume pairs.")
            return top_pairs
            
        except Exception as e:
            self.log_to_dashboard(f"AI Assistant Error: Could not fetch high-volume pairs: {e}")
            # Fallback to a default list in case of error
            return ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'SOLUSDT', 'XRPUSDT', 'ADAUSDT']

    def gather_market_data(self, client, pairs):
        """Fetches and analyzes historical data for a list of pairs."""
        all_data = []
        for pair in pairs:
            try:
                # Fetch 30 days of 4-hour candles
                klines = client.get_historical_klines(pair, Client.KLINE_INTERVAL_4HOUR, "30 day ago UTC")
                df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
                
                for col in ['open', 'high', 'low', 'close', 'volume']:
                    df[col] = pd.to_numeric(df[col])

                # --- Data Analysis ---
                # 1. Price Range
                support = df['low'].min()
                resistance = df['high'].max()
                current_price = df['close'].iloc[-1]

                # 2. Volatility (ATR)
                df['tr1'] = df['high'] - df['low']
                df['tr2'] = abs(df['high'] - df['close'].shift())
                df['tr3'] = abs(df['low'] - df['close'].shift())
                df['tr'] = df[['tr1', 'tr2', 'tr3']].max(axis=1)
                atr = df['tr'].ewm(span=14, adjust=False).mean().iloc[-1]
                atr_percentage = (atr / current_price) * 100

                # 3. Trend (simple check for ranginess)
                price_range = resistance - support
                is_ranging = (current_price > support + 0.15 * price_range) and \
                             (current_price < resistance - 0.15 * price_range)

                all_data.append({
                    "pair": pair,
                    "current_price": f"{current_price:.4f}",
                    "support": f"{support:.4f}",
                    "resistance": f"{resistance:.4f}",
                    "atr_percentage": f"{atr_percentage:.2f}%",
                    "is_ranging": is_ranging
                })
                self.log_to_dashboard(f"AI Assistant: Analyzed {pair}.")
                time.sleep(0.2) # Avoid hitting API rate limits
            except Exception as e:
                self.log_to_dashboard(f"AI Assistant: Could not analyze {pair}. Reason: {e}")
        return all_data

    def get_gemini_recommendation(self, market_data, api_key):
        """
        Calls the Google Gemini API to get a trading recommendation.
        """
        self.log_to_dashboard("AI Assistant: Contacting Google Gemini for analysis...")

        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # --- Construct the prompt for the LLM ---
            prompt = f"""
            You are an expert crypto market analyst specializing in grid trading strategies. 
            Based on the following market data for several cryptocurrencies, identify the single best candidate for a profitable grid trading bot.
            The ideal candidate is a high-volume asset in a stable, sideways market (where 'is_ranging' is true) with high volatility within its range (high 'atr_percentage').

            Analyze the data and respond ONLY with a valid JSON object containing your top recommendation. Do not include any text or markdown formatting before or after the JSON.

            Market Data:
            {json.dumps(market_data, indent=2)}

            Your Task:
            Respond in a JSON format with your top recommendation. Provide the 'trading_pair', a 'lower_bound' (based on support), an 'upper_bound' (based on resistance), and a recommended 'grid_density' (an integer between 20 and 50). Include a short 'justification' explaining why this pair is the best choice right now.

            Example JSON output format:
            {{
                "trading_pair": "SOLUSDT",
                "lower_bound": "120.5000",
                "upper_bound": "155.7500",
                "grid_density": 30,
                "justification": "SOLUSDT shows high volatility in a clearly defined range, making it ideal for capturing profits from price swings."
            }}
            """

            response = model.generate_content(prompt)
            
            # Clean up the response to ensure it's valid JSON
            cleaned_response_text = response.text.strip().replace('```json', '').replace('```', '').strip()
            
            self.log_to_dashboard("AI Assistant: Received recommendation from Gemini.")
            recommendation = json.loads(cleaned_response_text)
            
            # Basic validation of the received data
            if all(k in recommendation for k in ['trading_pair', 'lower_bound', 'upper_bound', 'grid_density', 'justification']):
                return recommendation
            else:
                self.log_to_dashboard("AI Assistant Error: Gemini response was missing required fields.")
                return None

        except Exception as e:
            self.log_to_dashboard(f"AI Assistant Error during Gemini API call: {e}")
            self.log_to_dashboard("Check your Gemini API key and ensure the model 'gemini-pro' is available.")
            return None

    def update_ui_with_recommendation(self, recommendation):
        """Populates the GUI fields with the AI's suggestion."""
        self.pair_entry.delete(0, "end")
        self.pair_entry.insert(0, recommendation['trading_pair'])
        
        self.lower_bound_entry.delete(0, "end")
        self.lower_bound_entry.insert(0, recommendation['lower_bound'])

        self.upper_bound_entry.delete(0, "end")
        self.upper_bound_entry.insert(0, recommendation['upper_bound'])

        self.grids_entry.delete(0, "end")
        self.grids_entry.insert(0, str(recommendation['grid_density']))

        self.ai_recommendation_label.configure(text=recommendation['justification'])

    def get_binance_client(self):
        """Creates a Binance client based on GUI settings."""
        api_key = self.api_key_entry.get()
        api_secret = self.api_secret_entry.get()
        if not api_key or not api_secret:
            return None
            
        testnet = self.env_selection.get() == "Demo (Testnet)"
        return Client(api_key, api_secret, testnet=testnet)

    def start_bot(self):
        """Validates inputs and starts the bot thread."""
        if self.bot_running:
            self.log_to_dashboard("Bot is already running.")
            return

        try:
            params = {
                "pair": self.pair_entry.get(),
                "lower_bound": float(self.lower_bound_entry.get()),
                "upper_bound": float(self.upper_bound_entry.get()),
                "grids": int(self.grids_entry.get()),
                "investment": float(self.investment_entry.get())
            }
            
            if params['lower_bound'] >= params['upper_bound'] or params['grids'] < 2:
                raise ValueError("Invalid grid parameters.")

        except ValueError as e:
            self.log_to_dashboard(f"Error: Invalid input. Please check your parameters. Details: {e}")
            return

        client = self.get_binance_client()
        if not client:
            self.log_to_dashboard("Error: Binance API keys are required.")
            return

        self.bot_running = True
        self.toggle_controls_state()
        
        self.bot_thread = GridBot(client, params, self.gui_queue)
        self.bot_thread.start()
        
        self.log_to_dashboard("Bot has been started.")

    def stop_bot(self):
        """Signals the bot thread to stop."""
        if not self.bot_running or not self.bot_thread:
            self.log_to_dashboard("Bot is not currently running.")
            return

        self.log_to_dashboard("Stopping bot... Please wait for open orders to be cancelled.")
        self.bot_thread.stop()
        self.bot_thread.join() # Wait for the thread to finish
        self.bot_running = False
        self.toggle_controls_state()
        self.log_to_dashboard("Bot has been stopped.")

    def toggle_controls_state(self):
        """Enables/disables GUI controls based on bot status."""
        state = "disabled" if self.bot_running else "normal"
        self.start_bot_button.configure(state=("disabled" if self.bot_running else "normal"))
        self.stop_bot_button.configure(state=("normal" if self.bot_running else "disabled"))
        
        # Disable all configuration entries when bot is running
        self.api_key_entry.configure(state=state)
        self.api_secret_entry.configure(state=state)
        self.env_selection.configure(state=state)
        self.gemini_api_key_entry.configure(state=state)
        self.find_opportunity_button.configure(state=state)
        self.pair_entry.configure(state=state)
        self.lower_bound_entry.configure(state=state)
        self.upper_bound_entry.configure(state=state)
        self.grids_entry.configure(state=state)
        self.investment_entry.configure(state=state)


class GridBot(threading.Thread):
    def __init__(self, client, params, gui_queue):
        super().__init__(daemon=True)
        self.client = client
        self.params = params
        self.gui_queue = gui_queue
        self._is_running = True
        self.total_pnl = 0.0

    def log(self, message):
        """Send a log message to the main GUI thread."""
        logging.info(message)
        self.gui_queue.put(f"[{self.params['pair']}] {message}")

    def stop(self):
        """Signal the bot to stop."""
        self._is_running = False

    def run(self):
        """The main logic loop for the grid trading bot."""
        try:
            self.log("Initializing bot...")
            # --- Initial Setup ---
            self.cancel_all_orders()
            
            current_price = float(self.client.get_symbol_ticker(symbol=self.params['pair'])['price'])
            self.log(f"Current price of {self.params['pair']} is {current_price}")

            # --- Grid Calculation ---
            grid_lines = np.linspace(self.params['lower_bound'], self.params['upper_bound'], self.params['grids'])
            buy_orders = []
            sell_orders = []
            
            quote_asset = self.get_quote_asset()
            base_asset = self.get_base_asset()

            investment_per_grid = self.params['investment'] / (len(grid_lines) - 1)
            
            # --- Place Initial Orders ---
            for line in grid_lines:
                qty_to_trade = self.calculate_quantity(investment_per_grid, line)
                
                if line < current_price:
                    # Place buy orders below current price
                    order = self.place_order(self.params['pair'], 'BUY', qty_to_trade, line)
                    if order: buy_orders.append(order)
                else:
                    # Place sell orders above current price
                    order = self.place_order(self.params['pair'], 'SELL', qty_to_trade, line)
                    if order: sell_orders.append(order)
            
            self.log(f"Placed {len(buy_orders)} initial buy orders and {len(sell_orders)} initial sell orders.")
            
            # --- Main Loop ---
            while self._is_running:
                time.sleep(10) # Check for filled orders every 10 seconds
                filled_orders = self.check_filled_orders()

                for filled_order in filled_orders:
                    filled_price = float(filled_order['price'])
                    filled_qty = float(filled_order['executedQty'])
                    grid_step = (self.params['upper_bound'] - self.params['lower_bound']) / (self.params['grids'] - 1)

                    if filled_order['side'] == 'BUY':
                        self.log(f"BUY order filled at {filled_price}")
                        # Place a corresponding sell order one grid up
                        sell_price = filled_price + grid_step
                        if sell_price <= self.params['upper_bound']:
                            self.place_order(self.params['pair'], 'SELL', filled_qty, sell_price)
                    
                    elif filled_order['side'] == 'SELL':
                        self.log(f"SELL order filled at {filled_price}")
                        # Calculate profit for this buy-sell pair
                        pnl = (filled_price - (filled_price - grid_step)) * filled_qty
                        self.total_pnl += pnl
                        self.log(f"PROFIT from trade: {pnl:.4f} {quote_asset}. Total P&L: {self.total_pnl:.4f} {quote_asset}")
                        # Place a corresponding buy order one grid down
                        buy_price = filled_price - grid_step
                        if buy_price >= self.params['lower_bound']:
                             self.place_order(self.params['pair'], 'BUY', filled_qty, buy_price)
                
        except Exception as e:
            self.log(f"An error occurred in the bot thread: {e}")
        finally:
            self.log("Bot loop finished. Cleaning up...")
            self.cancel_all_orders()

    def get_quote_asset(self):
        # e.g., for BTCUSDT, returns USDT
        return self.client.get_symbol_info(self.params['pair'])['quoteAsset']

    def get_base_asset(self):
        # e.g., for BTCUSDT, returns BTC
        return self.client.get_symbol_info(self.params['pair'])['baseAsset']
        
    def calculate_quantity(self, investment, price):
        """Calculate trade quantity based on investment and price, respecting lot size rules."""
        info = self.client.get_symbol_info(self.params['pair'])
        lot_size_filter = next(f for f in info['filters'] if f['filterType'] == 'LOT_SIZE')
        step_size = float(lot_size_filter['stepSize'])
        
        raw_qty = investment / price
        # Adjust quantity to conform to step size
        adjusted_qty = (raw_qty // step_size) * step_size
        return f"{adjusted_qty:.8f}".rstrip('0')

    def place_order(self, symbol, side, qty, price):
        """Places a limit order on Binance."""
        try:
            price_str = f"{price:.8f}".rstrip('0')
            self.log(f"Placing {side} order for {qty} {symbol} at {price_str}")
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=Client.ORDER_TYPE_LIMIT,
                timeInForce=Client.TIME_IN_FORCE_GTC,
                quantity=qty,
                price=price_str
            )
            return order
        except BinanceAPIException as e:
            self.log(f"Failed to place order: {e}")
            return None

    def cancel_all_orders(self):
        """Cancels all open orders for the current pair."""
        try:
            open_orders = self.client.get_open_orders(symbol=self.params['pair'])
            if open_orders:
                self.log(f"Cancelling {len(open_orders)} open order(s)...")
                for order in open_orders:
                    self.client.cancel_order(symbol=self.params['pair'], orderId=order['orderId'])
            else:
                self.log("No open orders to cancel.")
        except BinanceAPIException as e:
            self.log(f"Error cancelling orders: {e}")

    def check_filled_orders(self):
        """Checks for recently filled orders."""
        # A more robust solution would use websockets for real-time updates.
        # For simplicity, we poll recent trades.
        try:
            trades = self.client.get_my_trades(symbol=self.params['pair'], limit=50)
            # This is a simplification. A real bot would need to track order IDs
            # to avoid reprocessing the same filled order. We'll just return the
            # most recent ones for this example.
            # Here we just check the very last trade and assume it's new.
            # In a real app, you must maintain a list of processed trade IDs.
            
            # This logic is simplified for the example. It checks the latest trades.
            # A robust implementation would involve tracking order IDs and their status.
            filled_orders = []
            open_orders = self.client.get_open_orders(symbol=self.params['pair'])
            open_order_ids = {str(o['orderId']) for o in open_orders}
            
            all_orders = self.client.get_all_orders(symbol=self.params['pair'], limit=50)
            
            # Placeholder for state: track processed orders to avoid duplication
            if not hasattr(self, 'processed_order_ids'):
                 self.processed_order_ids = set()

            for order in all_orders:
                 if order['status'] == 'FILLED' and str(order['orderId']) not in self.processed_order_ids:
                      filled_orders.append(order)
                      self.processed_order_ids.add(str(order['orderId']))

            return filled_orders

        except BinanceAPIException as e:
            self.log(f"Error checking filled orders: {e}")
            return []


if __name__ == "__main__":
    app = BinanceGridBotApp()
    app.mainloop()
