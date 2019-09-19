TOKEN = '869700453:AAFYPaaF_zCeIocVcdYiDNCLp4PkcpJi7t4'
HEROKU_URL = 'https://norin-telegram-bot.herokuapp.com/'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(HEROKU_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'