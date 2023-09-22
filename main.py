from bot import Bot

if __name__ == '__main__':
    url = "https://www.tickertape.in/market-mood-index"
    client_emails = ["xxx@gmail.com", "xxxx@gmail.com"]
    notifier_email = "notifiermmi@gmail.com"
    notifier_email_app_pswd = ""

    mmi_bot = Bot(url, notifier_email, notifier_email_app_pswd, client_emails)
    # mmi_bot.check_market_mood()
    mmi_bot.send_weekly_market_mood()
