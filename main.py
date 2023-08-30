from bot import Bot

if __name__ == '__main__':
    url = "https://www.tickertape.in/market-mood-index"
    client_email = ""
    notifier_email = ""
    notifier_email_app_pswd = ""

    mmi_bot = Bot(url, notifier_email, notifier_email_app_pswd, client_email)
    mmi_bot.check_market_mood()
