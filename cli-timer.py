#! usr/bin/env python3

# @author: N Rogers

import sys
import time
import subprocess
import argparse


def handle_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("time", type=int, help="specify a starting time in seconds")
    parser.add_argument("-n", "--name", dest="name", help="Name the timer")
    parser.add_argument("-q", "--quiet", action="store_true", default=False, dest="quiet", help="Do not show countdown")

    return parser.parse_args()


def alarm(name=''):
    subprocess.Popen("say 'Ding, ding. {} timer is done.'".format(name), shell=True)


def timer_print_to_terminal(sec):
    # https://stackoverflow.com/questions/2122385/dynamic-terminal-printing-with-python
    while sec > 0:
        sys.stdout.write("\r{}".format(sec))
        sys.stdout.flush()
        time.sleep(1.0)
        sec -= 1


def main():
    args = handle_args()
    if args.quiet:
        time.sleep(args.time)
        if args.name:
            alarm(args.name)
        else:
            alarm()
    else:
        timer_print_to_terminal(args.time)
        if args.name:
            alarm(args.name)
        else:
            alarm()


if __name__ == "__main__":
    main()
