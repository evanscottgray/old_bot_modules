import requests
import willie.module


def get_tft():
    base_url = 'http://itsthisforthat.com'
    path = '/api.php?text'
    url = base_url + path
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        r.raise_for_status()


@willie.module.commands('tft', 'itsthisforthat', 'itft', 'itisthisforthat')
def tft(bot, trigger):
    msg = get_tft()
    bot.say(msg)
