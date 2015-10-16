import requests
import willie.module


def get_in(force=False):
    url_base = 'http://bluetooth.api.wow:1337/api'
    if force:
        path = '/force_in'
    else:
        path = '/in'
    url = url_base + path
    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        r.raise_for_status()


def in_message(peeps):
    p = [x['name'] for x in peeps if x['in']]
    if len(p):
        ps = ', '.join(p)
        msg = 'These people are in or near HH: %s' % ps
        fucking_kevin = ' and not Kevin..'
        msg = msg + fucking_kevin
    else:
        msg = 'Looks like there\'s nobody in HH.. ( ._.)'
    return msg


@willie.module.commands('hh')
def hh(bot, trigger):
    peeps = get_in()
    msg = in_message(peeps['status'])
    bot.say(msg)


@willie.module.commands('hhforce')
def hh_force(bot, trigger):
    bot.say('Forcing bluetooth scan.. be patient..')
    peeps = get_in(force=True)
    msg = in_message(peeps['status'])
    bot.say(msg)
