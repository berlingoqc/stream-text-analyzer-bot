#!/usr/bin/env python

import sys

from streamlink import Streamlink, NoPluginError, PluginError
from image_text import addImageToParse, startImageToTextThread
from bot import startBotThread
import cv2

twitchURL = "https://www.twitch.tv/"


def exit(msg):
    print(msg)
    sys.exit(1)


def findVideoStreamURL(channel, quality):
    streamlink = Streamlink()

    url = twitchURL + channel

    # Attempt to fetch streams
    try:
        streams = streamlink.streams(url)
    except NoPluginError:
        exit("Streamlink is unable to handle the URL '{0}'".format(url))
    except PluginError as err:
        exit("Plugin error: {0}".format(err))

    if not streams:
        exit("No streams found on URL '{0}'".format(url))

    # Look for specified stream
    if quality not in streams:
        exit("Unable to find '{0}' stream on URL '{1}'".format(quality, url))
    return streams[quality].url


def readTwitchStream(url):

    cap = cv2.VideoCapture(url)

    nbrIteration = 0

    while(True):
        ret, frame = cap.read()
        if nbrIteration == 60:
            addImageToParse(frame)
            cv2.imshow('frame', frame)
            nbrIteration = 0
        nbrIteration += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
