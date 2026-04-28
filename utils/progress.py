# =============================================================================
# progress.py -- in-place terminal progress bar
# =============================================================================

import sys

_RESET  = "\033[0m"
_CYAN   = "\033[1;36m"   # label
_GREEN  = "\033[1;32m"   # filled bar
_DIM    = "\033[0;37m"   # task text
_BOLD   = "\033[1m"      # percentage / counts
_ERASE  = "\033[K"       # erase to end of line

_BAR_WIDTH = 25


class ProgressBar:
    """
    In-place terminal progress bar.

    Usage:
        bar = ProgressBar(label='Set 1', min=0, max=365, units='cards')
        bar.update(current=180, task='lotr01089')
        bar.done()
    """

    def __init__(self, label: str, min: int = 0, max: int = 100, units: str = ''):
        self._label = label
        self._min   = min
        self._max   = max
        self._units = units
        self._tty   = sys.stdout.isatty()

    def update(self, current: int, task: str = '') -> None:
        if not self._tty:
            return
        sys.stdout.write('\r' + self._render(current, task) + _ERASE)
        sys.stdout.flush()

    def done(self, task: str = '') -> None:
        if not self._tty:
            return
        sys.stdout.write('\r' + self._render(self._max, task) + _ERASE + '\n')
        sys.stdout.flush()

    def _render(self, current: int, task: str) -> str:
        span = self._max - self._min
        pct  = (current - self._min) / span if span > 0 else 1.0
        pct  = max(0.0, min(1.0, pct))

        filled = int(pct * _BAR_WIDTH)
        empty  = _BAR_WIDTH - filled - (1 if filled < _BAR_WIDTH else 0)

        bar_fill = '=' * filled
        if filled < _BAR_WIDTH:
            bar_body = f"{_GREEN}{bar_fill}>{_RESET}" + ' ' * empty
        else:
            bar_body = f"{_GREEN}{bar_fill}{_RESET}"

        pct_str    = f"{_BOLD}{int(pct * 100):>3}%{_RESET}"
        counts_str = f"{_BOLD}{current}/{self._max}{_RESET}"
        units_str  = f" {self._units}" if self._units else ''
        task_str   = f"  {_DIM}{task}{_RESET}" if task else ''

        return (
            f"  {_CYAN}{self._label}{_RESET}"
            f"  [{bar_body}]"
            f"  {pct_str}"
            f"  {counts_str}{units_str}"
            f"{task_str}"
        )
