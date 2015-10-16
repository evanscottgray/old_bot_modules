# -*- coding: utf-8 -*-
import subprocess

import willie.module


@willie.module.commands('guten', 'gutentag', 'gutentaag', 'gutentaaag',
                        'gutentaaaag')
def gutentag(bot, trigger):
    bot.say('GUETENTAAAAG!')
    subprocess.call(['aplay', '/home/dongs/.sounds/guetentaaaag.wav'])


@willie.module.commands('victory')
def victory(bot, trigger):
    bot.say('Yay!')
    subprocess.call(['aplay', '/home/dongs/.sounds/victory.wav'])


@willie.module.commands('out')
def out(bot, trigger):
    bot.say('Fuck this shit I\'m out')
    subprocess.call(['aplay', '/home/dongs/.sounds/out.wav'])


@willie.module.commands('inception')
def inception(bot, trigger):
    bot.say('BRRRRRRRAAAAAWWWWRWRRRMRMRMMRMRMMMMM!!!')
    subprocess.call(['aplay', '/home/dongs/.sounds/inception.wav'])


@willie.module.commands('nanas')
def nanas(bot, trigger):
    bot.say('B-A-N-G-N-A-N-A-S!')
    subprocess.call(['aplay', '/home/dongs/.sounds/bangnanas.wav'])


@willie.module.commands('zelda', 'secret')
def zelda(bot, trigger):
    bot.say('do do do do do do de do.')
    subprocess.call(['aplay', '/home/dongs/.sounds/zelda_secret.wav'])


@willie.module.commands('in')
def janice(bot, trigger):
    bot.say('Hey Janice!')
    subprocess.call(['aplay', '/home/dongs/.sounds/hey_janice.wav'])


@willie.module.commands('ostrich', 'haha')
def ostrich(bot, trigger):
    bot.say('Ha ha.')
    subprocess.call(['aplay', '/home/dongs/.sounds/ostrich.wav'])


@willie.module.commands('tranny', 'shemale', 'spooky', 'skeleton',
                        'thankyoumrskeletal', 'doot', 'dootdoot',
                        'mr_skeletal', 'dootskootboogy', 'skelatal',
                        'calsiums', 'calcium')
def spooky(bot, trigger):
    bot.say('skeltons')
    subprocess.call(['aplay', '/home/dongs/.sounds/spooky.wav'])


@willie.module.commands('pressure')
def pressure(bot, trigger):
    bot.say('Dun dun dun dun dun.')
    subprocess.call(['aplay', '/home/dongs/.sounds/pressure.wav'])


@willie.module.commands('cd', 'cando', 'caando', 'caandoo', 'can')
def cando(bot, trigger):
    bot.say('Caaaan Doooooo!.')
    subprocess.call(['aplay', '/home/dongs/.sounds/can_doo.wav'])
