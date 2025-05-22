#!/usr/bin/env python3

import argparse
import json
import os

from datetime import datetime
from tabulate import tabulate

from lib.log import *
from lib.i18n import *


def parse_arguments():
    """Get commandline arguments."""
    parser = argparse.ArgumentParser('read nuScore reports and show details')
    parser.add_argument('filename', help='Name of the file to analyze')
    parser.add_argument('--language', '-l', help='Translate strings')
    parser.add_argument('--info', '-i', action='store_true', help='Show match info only')
    parser.add_argument('--events', '-e', action='store_true', help='Show events only')
    return parser.parse_args()


def show_info(data):
    """Show general match details."""
    table = []
    print(_t('Game Details'))
    keys = ('meetingNr', 'championship', 'league', 'groupName', 'startTime',
            'endTime', 'teamSize', 'timeoutCount', 'halftimeLength')
    for key in keys:
        table.append((_t(key), data[key]))
    table.append((_t('Arena'), data['location']['name']))
    for team in ('teamHome', 'teamGuest'):
        table.append((_t(team), data[team]['name']))
    table.append((_t('Result'), f"{data['pointsHome']}:{data['pointsGuest']} ({data['pointsHomeHalftime']}:{data['pointsGuestHalftime']})"))
    for official in ('refereeA', 'refereeB', 'secretary', 'timekeeper'):
        fullname = '{} {}'.format(
            data['federationOfficials'][official]['firstname'],
            data['federationOfficials'][official]['lastname'],
        )
        table.append((_t(official), fullname))
    print(tabulate(table, [], tablefmt='simple_outline'))


def format_event(event):
    """Format a single event."""
    idx = event.get('idx')
    format = '%Y-%m-%dT%H:%M:%S.%fZ'
    format_fallback = '%Y-%m-%dT%H:%M:%S.%f%z'
    try:
        timestamp = datetime.strptime(
            event.get('dateTime'), format).strftime('%H:%M:%S')
    except ValueError:
        timestamp = datetime.strptime(
            event.get('dateTime'), format_fallback).strftime('%H:%M:%S')
    second = event.get('second')
    team = '-'*max(len(_t('Home')), len(_t('Guest')))
    if 'teamHome' in event:
        if event.get('teamHome'):
            team = 'Home'
        else:
            team = 'Guest'
    timecode = f'{int(second / 60):02d}:{int(second % 60):02d}'
    points_home = event.get('pointsHome')
    points_guest = event.get('pointsGuest')
    score = f'{points_home}:{points_guest}'
    event_type = event.get('eventType')
    rows = [
        _t(idx),
        _t(timestamp),
        _t(team),
        _t(timecode),
        _t(score),
        _t(event_type),
    ]
    return rows


def show_events(data):
    """Show events stats."""
    print(_t('Events'))
    events = data.get('events', [])
    headers = [
        _t('ID'),
        _t('Clock Time'),
        _t('Team'),
        _t('Game Time'),
        _t('Score'),
        _t('Event'),
    ]
    # i = 1
    table = []
    for event in events:
        table.append(format_event(event))
    print(tabulate(table, headers, tablefmt='simple_outline'))


def read_file(filename):
    """Read the file."""
    try:
        with open(filename) as fd:
            content = json.load(fd)
            return content
    except:
        error()


def main():
    global _t
    args = parse_arguments()
    show = ('info', 'events')
    if args.info:
        show = ('info',)
    if args.events:
        show = ('events', )

    data = read_file(args.filename)

    language = args.language
    if not language:
        language = os.environ['LANG'].split('_')[0]
    dictionary = Dictionary(language)
    _t = dictionary.translate

    if 'info' in show:
        show_info(data)
    if 'events' in show:
        show_events(data)


if __name__ == '__main__':
    main()
