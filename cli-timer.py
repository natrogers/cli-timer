#! usr/bin/env python3

# @author: N Rogers

import sys
import time
import subprocess
import argparse


def handle_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("time", dest="time", type=int, help="specify a starting time in seconds")
    parser.add_argument("-n", "--name", dest="name", type=string, help="Name the timer")
    parser.add_argument("-q", "--quiet", action="store_true", default=False, dest="quiet" help="Do not show countdown")

    return parser.parse_args()


def alarm(name=''):
    subprocess.Popen("say 'Ding, ding. {} timer is done.'".format(name), shell=True)


def quiet_timer(sec):
    # https://www.geeksforgeeks.org/timer-objects-python/
    # https://stackoverflow.com/questions/18406165/creating-a-timer-in-python
    time.sleep(sec)
    alarm()


def timer_print_to_terminal(sec):
    # https://stackoverflow.com/questions/2122385/dynamic-terminal-printing-with-python
    while sec > 0:
        sys.stdout.write("\r{}".format(sec))
        sys.stdout.flush()
        time.sleep(1.0)
        seconds -= 1
    alarm()


def main():
    args = handle_args()
    if args.quiet:
        quiet_timer(args.time)
    else:
        timer_print_to_terminal(args.time)



if __name__ == "__main__":
    main()
