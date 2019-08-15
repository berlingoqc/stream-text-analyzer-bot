#! /bin/python

import sys
from twitch_recorder import findVideoStreamURL, readTwitchStream
from bot import startBotThread, CHAN, NICK, PASS
from image_text import startImageToTextThread

if __name__ == '__main__':
    CHAN = '#' + sys.argv[1]
    NICK = sys.argv[2]
    PASS = sys.argv[3]
    quality = 'best'

    startImageToTextThread()
    startBotThread()

    urlStream = findVideoStreamURL(sys.argv[1], quality)

    readTwitchStream(urlStream)
