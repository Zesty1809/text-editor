import curses
from curses import wrapper
import time

def main(stdscr):
     # Minimal fix
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    MAGENTA_AND_GREEN = curses.color_pair(1)
    BLACK_AND_CYAN = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 3, 25)

    for i in range(101):
        counter_win.clear()
        color = MAGENTA_AND_GREEN

        if i % 2 == 0:
            color = BLACK_AND_CYAN

        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(0.1)

    stdscr.addstr("Press any key to exit...")
    stdscr.getch()


wrapper(main)