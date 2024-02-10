# crypto-price-bot
this repository contains a simple example of telegram bot using aiogram v3

this is a simple Python Telegram bot designed to provide cryptocurrency prices using the Binance API. Users can interact with the bot by starting a conversation and utilizing buttons to inquire about the prices of popular cryptocurrencies.

## Getting Started

1. **Create a Telegram Bot:**
   - Obtain a Telegram Bot Token from [@BotFather](https://t.me/BotFather) on Telegram.

2. **Install Dependencies:**
   - Make sure to install the necessary Python packages using the following command:
     ```bash
     pip install aiogram requests
     ```

3. **Configure the Bot:**
   - Replace the placeholder 'YOUR_API_TOKEN' with the actual token received from [@BotFather] in the `API_TOKEN` variable in the code.

4. **Run the Bot:**
   - Execute the script to start the bot.
     ```bash
     python main.py
     ```

## Bot Features

### Start Command
- Upon starting a conversation with the bot, users receive a welcome message along with a button to check cryptocurrency prices.

### Check Cryptocurrency Prices
- Users can click the "Узнать цену криптовалюты💰" button to view a list of popular cryptocurrencies.
- The bot provides inline buttons for cryptocurrencies such as Bitcoin, Ethereum, Litecoin, and others.

### Inline Buttons
- Users can select a specific cryptocurrency to receive its current price in both USD and RUB.

## Dependencies
- **aiogram:** A Python framework for building Telegram bots.
- **requests:** Used to make HTTP requests to the Binance API for cryptocurrency prices.

## Binance API Integration
- The bot fetches cryptocurrency prices from the Binance API in both USDT and RUB.

## Notes
- Ensure that your Binance API has the necessary permissions to access price information.
- The bot utilizes the asyncio library for asynchronous programming and aiogram for Telegram bot development.
