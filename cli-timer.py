#! usr/bin/env python3

# @author: N Rogers

import argparse
import subprocess
import sys
import time


def handle_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("time", type=int, help="specify a starting time in seconds")
    parser.add_argument("-n", "--name", dest="name", help="Name the timer")
    parser.add_argument("-q", "--quiet", action="store_true", default=False, dest="quiet", help="Do not show countdown")

    return parser.parse_args()


def alarm(name=''):
    subprocess.Popen("say 'Ding, ding. {} timer is done.'".format(name), shell=True)


def cycle_timer():
    sys.stdout.flush()
    time.sleep(1.0)


def timer_print_to_terminal(sec, name=False):
    if name:
        while sec > 0:
            sys.stdout.write("\r{} {}".format(sec, name))
            cycle_timer()
            sec -= 1
        alarm(name)
    else:
        while sec > 0:
            sys.stdout.write("\r{}".format(sec))
            cycle_timer()
            sec -= 1
        alarm()


def main():
    args = handle_args()
    if args.quiet:
        time.sleep(args.time)
        if args.name:
            alarm(name=args.name)
        else:
            alarm()
    else:
        timer_print_to_terminal(args.time, args.name)


if __name__ == "__main__":
    main()
