import subprocess
import webbrowser

import willie.module

STRING = 'HANGOUTS_URL'


@willie.module.commands('hstart')
def hangout_start(bot, trigger):
    pid = check_status()
    if pid:
        bot.say('I think hangouts is already running with pid %s' % pid)
    else:
        webbrowser.open(STRING)
        bot.say('Starting hangouts')


@willie.module.commands('hkill')
def hangout_kill(bot, trigger):
    bot.say('Attempting to kill hangouts')
    subprocess.call(['pkill', '-of', STRING])
    subprocess.call(['pkill', '-of', STRING])


@willie.module.commands('hstatus')
def hangout_status(bot, trigger):
    pid = check_status()
    if pid:
        bot.say('Looks like hangouts are already running with pid %s' % pid)
    else:
        bot.say('Hangout does not appear to be running')


def check_status():
    p = subprocess.Popen(['pgrep', '-of', STRING], stdout=subprocess.PIPE)
    pid = p.communicate()[0].rstrip()

    return pid
