import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

def get_coin_data():
    url = "https://api.coinpaprika.com/v1/coins/rgen-paragen/markets"
    response = requests.get(url)
    data = response.json()
    return data

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the Crypto Bot! Use /price to get cryptocurrency information.")

def price(update: Update, context: CallbackContext):
    coin_data = get_coin_data()

    if coin_data:
        exchange_id = coin_data[0]["exchange_id"]
        exchange_name = coin_data[0]["exchange_name"]
        pair = coin_data[0]["pair"]
        base_currency_id = coin_data[0]["base_currency_id"]
        base_currency_name = coin_data[0]["base_currency_name"]
        quote_currency_id = coin_data[0]["quote_currency_id"]
        quote_currency_name = coin_data[0]["quote_currency_name"]
        fee_type = coin_data[0]["fee_type"]
        adjusted_volume_24h_share = coin_data[0]["adjusted_volume_24h_share"]
        price = coin_data[0]["quotes"]["USD"]["price"]
        volume_24h = coin_data[0]["quotes"]["USD"]["volume_24h"]
        last_updated = coin_data[0]["last_updated"]

        response = "<b><a href='https://paragen.io'>Paragen</a> (Official)</b> 🚀🌙\n\n"

        response += "<b>🎁Marketcap</b>: 200,000,000 RGEN\n\n"

        response += "⌛<b>Launch Date</b>: February 25th 🌙\n\n"

        response += f"🏦<b>Exchange:</b> {exchange_name} ({exchange_id})\n\n"

        response += f"🔁<b>Pair:</b> {pair}\n\n"

        response += f"💱<b>Base Currency:</b> {base_currency_name} ({base_currency_id})\n\n"

        response += f"💲<b>Quote Currency:</b> {quote_currency_name} ({quote_currency_id})\n\n"

        response += f"💸<b>Fee Type:</b> {fee_type}\n\n"

        response += f"📈<b>Adjusted Volume 24h Share:</b> {adjusted_volume_24h_share}%\n\n"

        response += f"💰<b>Price:</b> ${price}\n\n"

        response += f"📊<b>24h Volume:</b> {volume_24h}\n\n"

        response += "🚧<b>Purchase</b>: <a href='https://pancakeswap.finance/swap?outputCurrency=0x25382fb31e4b22e0ea09cb0761863df5ad97ed72'>Pancakeswap</a>🔥\n\n"

        response += "🍅<b>Charts</b>: <a href='https://coinmarketcap.com/dexscan/bsc/0x447ff4dd9cee7f751cf3eb253dbb3c227747b31c/'>CoinMarketCap</a>🎂 | <a href='https://poocoin.app/tokens/0x25382fb31e4b22e0ea09cb0761863df5ad97ed72'>Poocoin</a>🏡\n\n"

        response += "🌶️<b>Socials</b>: <a href='https://paragen.io'>Website</a> | <a href='https://twitter.com/paragenio'>Twitter</a> | <a href='https://discord.gg/C5hJuCS2yC'>Discord</a> | <a href='https://paragen.medium.com/'>Medium</a>\n\n"

        keyboard = [
            [
                InlineKeyboardButton("🌐", url="https://t.me/paragenio"),
                InlineKeyboardButton("💼", url="https://t.me/BullionDOT"),
                InlineKeyboardButton("💰", url="https://pancakeswap.finance/swap?outputCurrency=0x25382fb31e4b22e0ea09cb0761863df5ad97ed72"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(response, parse_mode='HTML', reply_markup=reply_markup, disable_web_page_preview=True)
    else:
        update.message.reply_text("Unable to fetch cryptocurrency data.")

def main():
    bot_token = "6137101636:AAHfjZi7YFO9QAb7wCIUZjZSahRmb4KgD6I"  # Replace with your actual bot token
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("price", price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
