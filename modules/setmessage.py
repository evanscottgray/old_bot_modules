# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import willie.module
import telnetlib

HOST = ''
PORT = ''
PASS = ''


def login(tn):
    tn.read_until('Password?', 3)
    tn.write(PASS + '\n\r')
    tn.read_until('\r\nTPMC-4SM>', 10)


def message(tn, msg):
    tn.write('message %s' % msg)
    tn.read_until('\r\n', 1)
    tn.write('\n\r')
    tn.read_until('\r\nTPMC-4SM>', 10)


def logout(tn):
    tn.write('bye\n\r')
    tn.read_until('\r\n', 1)
    tn.write('\n\r')
    tn.close()


def set_message(msg):
    tn = telnetlib.Telnet(HOST, PORT)
    tn.set_debuglevel(10)
    login(tn)
    str_msg = str(msg)
    message(tn, str_msg)
    logout(tn)


@willie.module.commands('setmessage', 'message')
def setdisplay(bot, trigger):
    msg = trigger.group(2)
    set_message(msg)
    bot.say('Display message set to: %s' % msg)
