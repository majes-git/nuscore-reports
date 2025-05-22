# nuscore-reports 

Loads a json file from nuScore and show match information.

## Running the tool

The tool comes as a Python executable:

* **nuscore-reports.pyz**

## Running on macOS/Linux

1. Download the nuscore-reports.pyz
2. Open a Terminal
3. Make the file executable
4. Run the tool and provide json file

```
$ curl -JLO https://github.com/majes-git/nuscore-reports/raw/refs/heads/main/nuscore-reports.pyz
$ chmod +x nuscore-reports.pyz
$ ./nuscore-reports.pyz ddmmyy_test.json
```


## Usage

```
./nuscore-reports.pyz --help
usage: read nuScore reports and show details [-h] [--language LANGUAGE] [--info] [--events] filename

positional arguments:
  filename              Name of the file to analyze

options:
  -h, --help            show this help message and exit
  --language, -l LANGUAGE
                        Translate strings
  --info, -i            Show match info only
  --events, -e          Show events only
```


## Example Output

```
$ ./nuscore-reports.pyz demo.json
Game Details
┌────────────────┬──────────────────────────┐
│ meetingNr      │                          │
│ championship   │                          │
│ league         │                          │
│ groupName      │ HLA Oberes-Play-Off      │
│ startTime      │ 2015-03-14T18:00:00.000Z │
│ endTime        │                          │
│ teamSize       │ 14                       │
│ timeoutCount   │ 3                        │
│ halftimeLength │ 30                       │
│ Arena          │ Sporthalle am See        │
│ teamHome       │ Alpla HC Hard            │
│ teamGuest      │ Bregenz Handball         │
│ Result         │ 3:2 (2:1)                │
│ refereeA       │ Andreas Müller           │
│ refereeB       │ Bertram Schneider        │
│ secretary      │ Detlef Schmidt           │
│ timekeeper     │ Renate Schmidt           │
└────────────────┴──────────────────────────┘
Events
┌──────┬──────────────┬────────┬─────────────┬─────────┬─────────────────┐
│   ID │ Clock Time   │ Team   │ Game Time   │ Score   │ Event           │
├──────┼──────────────┼────────┼─────────────┼─────────┼─────────────────┤
│    1 │ 08:29:08     │ -----  │ 00:00       │ 0:0     │ gameTimeStart   │
│    2 │ 08:29:08     │ -----  │ 00:00       │ 0:0     │ gameStart       │
│    3 │ 08:29:08     │ -----  │ 00:00       │ 0:0     │ gamePeriodStart │
│    5 │ 08:29:18     │ -----  │ 00:10       │ 1:0     │ gameTimeStop    │
│    4 │ 08:29:13     │ Home   │ 00:05       │ 1:0     │ goal            │
│    6 │ 08:29:40     │ Home   │ 00:10       │ 1:0     │ playerWarning   │
│    7 │ 08:29:47     │ -----  │ 00:10       │ 1:0     │ gameTimeStart   │
│    8 │ 08:29:52     │ -----  │ 00:15       │ 1:0     │ gameTimeStop    │
│    9 │ 08:29:56     │ Home   │ 00:15       │ 1:0     │ playerPenalty   │
│   10 │ 08:30:02     │ -----  │ 00:15       │ 1:0     │ gameTimeStart   │
│   11 │ 08:30:09     │ Guest  │ 00:22       │ 1:1     │ goal            │
│   12 │ 08:30:22     │ -----  │ 00:34       │ 1:1     │ gameTimeStop    │
│   13 │ 08:30:38     │ Home   │ 00:34       │ 2:1     │ goal            │
│   14 │ 08:30:51     │ -----  │ 29:59       │ 2:1     │ gameTimeStart   │
│   15 │ 08:30:52     │ -----  │ 30:00       │ 2:1     │ gameTimeStop    │
│   17 │ 08:30:52     │ -----  │ 30:00       │ 2:1     │ gamePeriodStop  │
│   16 │ 08:30:59     │ -----  │ 30:00       │ 2:1     │ gameTimeStart   │
│   18 │ 08:30:59     │ -----  │ 30:00       │ 2:1     │ gamePeriodStart │
│   19 │ 08:31:08     │ Home   │ 30:08       │ 3:1     │ goal            │
│   20 │ 08:31:22     │ Guest  │ 30:23       │ 3:2     │ goal            │
│   21 │ 08:31:26     │ -----  │ 30:27       │ 3:2     │ gameTimeStop    │
│   22 │ 08:31:34     │ -----  │ 59:59       │ 3:2     │ gameTimeStart   │
│   23 │ 08:31:35     │ -----  │ 60:00       │ 3:2     │ gameTimeStop    │
│   24 │ 08:31:35     │ -----  │ 60:00       │ 3:2     │ gamePeriodStop  │
│   25 │ 08:31:37     │ -----  │ 60:00       │ 3:2     │ gameEnd         │
└──────┴──────────────┴────────┴─────────────┴─────────┴─────────────────┘
```