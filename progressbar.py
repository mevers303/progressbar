# Mark Evers
# <mark@regstechnology.com>
# 5/8/19
# progress_bar.py
# Module that can print a progress bar

import sys
import time



_progress_bar_last_time = 0
def progress_bar(done, total, text="", resolution=0.333):
    """
    Prints a progress bar to sys.stdout.
    :param done: Number of items complete
    :param total: Total number if items
    :param resolution: How often to update the progress bar (in seconds).
    :param text: Text to be displayed below the progress bar every update.
    :param clear_when_done: Clear the progress bar or leave it when completed?
    :return: None
    """

    global _progress_bar_last_time

    time_now = time.time()
    if time_now - _progress_bar_last_time < resolution and done < total:
        return

    # so we don't divide by 0
    if not total:
        i = 100
    else:
        # percentage done
        i = (done * 100) // total

    # go to beginning of our output
    if text and done > 0:
        sys.stdout.write("\r")
        sys.stdout.write("\033[F")
    else:
        sys.stdout.write("\r")

    # print the progress bar
    sys.stdout.write( "[" + (("-" * (i // 2)) +  (">" if i < 100 else "")).ljust(50) + "]" )
    # print the percentage
    sys.stdout.write(str(i).rjust(4) + "%")
    # print the text progress
    sys.stdout.write(" ({}/{})".format(done, total))
    # print the text below (if any)
    if text:
        sys.stdout.write("\n" + (' ' * 80) + "\r")
        sys.stdout.write(text)

    if i >= 100:
        sys.stdout.write("\n")

    sys.stdout.flush()
    _progress_bar_last_time = time_now
