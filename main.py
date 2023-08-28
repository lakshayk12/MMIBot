from bot import Bot

if __name__ == '__main__':
    # replace URL-Text with product that should be checked on Amazon
    # replase EMAIL-Text where the notification should be sent
    url = "https://www.tickertape.in/market-mood-index"
    client_email = "imcoollakshay02@gmail.com"

    mmi_bot = Bot(url, client_email)
    mmi_bot.check_market_mood()
