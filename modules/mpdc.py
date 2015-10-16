import contextlib
import willie.module
import mpd


@contextlib.contextmanager
def client(host='/run/mpd/socket', port=None):
    mc = mpd.MPDClient()
    mc.connect(host, port)

    yield mc

    mc.close()
    mc.disconnect()


def play_song(uri):
    with client() as mc:
        mc.clear()
        mc.add(uri)
        mc.play(0)


@willie.module.commands('vol')
def volume(bot, trigger):
    if not trigger.group(2):
        with client() as mc:
            vol = mc.status()['volume']
        bot.say('MPD volume set to: %s' % vol)
        return
    arg = trigger.group(3)
    try:
        amt = int(arg)
    except ValueError:
        bot.say('Invalid argument, yo')
        return
    if str(arg)[0] in ('-', '+') and -100 <= amt <= 100:
        with client() as mc:
            vol = int(mc.status()['volume'])
            mc.setvol(vol + amt)
            vol = int(mc.status()['volume'])
        bot.say('Changed volume by %s to %s' % (arg, vol))
        return
    else:
        with client() as mc:
            mc.setvol(amt)
            vol = mc.status()['volume']
        bot.say('Changed volume to %s' % vol)


@willie.module.commands('stop', 'stahp', 'pause')
def pause(bot, trigger):
    with client() as mc:
        mc.pause(1)
    bot.say('Music paused')


@willie.module.commands('play', 'start')
def play(bot, trigger):
    with client() as mc:
        mc.pause(0)
    bot.say('Starting music')


@willie.module.commands('skip', 'next')
def skip(bot, trigger):
    with client() as mc:
        mc.next()
    now_playing(bot, trigger)


@willie.module.commands('prev', 'back', 'previous')
def prev(bot, trigger):
    with client() as mc:
        mc.previous()
    now_playing(bot, trigger)


@willie.module.commands('np')
def now_playing(bot, trigger):
    data = None

    with client() as mc:
        if mc.status()['state'] == 'play':
            data = mc.currentsong()

    if data:
        album = data['album']
        title = data['title']
        artist = data['artist']
        date = data['date']
        bot.say('Now Playing: %s - %s (%s: %s)' % (artist, title, date[0:4],
                                                   album))
    else:
        bot.say('its oh so quiet... shhhhhh..... shhhhhhh...')


def lev(s, t):
        if s == t:
            return 0
        elif len(s) == 0:
            return len(t)
        elif len(t) == 0:
            return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]

        return v1[len(t)]


def scoremebro(s, artist=None, title=None):
    score = 0
    if artist is not None:
        score += lev(s.get('artist'), artist)
    if title is not None:
        score += lev(s.get('title'), title)*2
    return score


def play_next(s):
    with client() as c:
        song_id = c.addid(s.get('file'))
    with client() as c:
        cs = c.currentsong()
    with client() as c:
        s = c.playlistid(song_id)

    next_pos = int(cs['pos']) + 1

    with client() as c:
        c.moveid(int(song_id), int(next_pos))


def play_a_song(title=None, artist=None):
    with client() as c:
        sr = c.search('title', title)
    ranked = [(scoremebro(r, title=title, artist=artist), r) for r in sr]
    ranked = sorted(ranked)
    try:
        s = ranked[0][-1]
        play_next(s)
    except IndexError:
        s = 'FAIL'
    except KeyError:
        s = 'NOTPLAYING'
    return s


@willie.module.commands('plsplay', 'pp')
def plsplay(bot, trigger):
    print trigger.group(2)
    search = trigger.group(2).split('|')
    if len(search) > 1:
        title = search[0]
        artist = search[1]
        s = play_a_song(title=title, artist=artist)
    else:
        title = search[-1]
        s = play_a_song(title=title)

    if s == 'FAIL':
        bot.say('oops i couldn\'t find that..')
    elif s == 'NOTPLAYING':
        bot.say('cant add to playlist, nothing is playing right now..')
    else:
        bot.say('trying to play %s next..' % s.get('title'))


@willie.module.commands('whatsnext', 'waznext', 'wasnext', 'whatisnext', 'wn')
def what_is_next(bot, trigger):
    with client() as c:
        cs = c.currentsong()
    with client() as c:
        pl = c.playlistinfo()

    # default to 3 songz
    count = 3
    if trigger.group(2):
        try:
            count = int(trigger.group(2))
        except:
            count = 1337
    ns_pos = int(cs.get('pos')) + 1
    cpls = [s.get('title') for s in pl if int(s.get('pos'))
            in xrange(ns_pos, ns_pos + count)]
    songz = ', '.join(cpls)
    if count == 1337:
        msg = 'why do you hate me? please dont try to h4x0r me'
    elif count > 20 or count < 1:
        msg = 'are you trying to break irc..? pls no'
    else:
        msg = 'These are next: %s' % songz
    bot.say(msg)


@willie.module.commands('mix', 'shuffle', 'random', 'rand')
def shuffle_it(bot, trigger):
    with client() as c:
        c.shuffle()
    bot.say('things are mixed up now')
