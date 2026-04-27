# =============================================================================
# utils.py -- color-print helpers
#
# Mirrors the label/color convention from build/makefiles/utils.mk.
# Each function has a primary variant and a sub-variant (4-space indent).
#
# Primary:  pb  pd  pi  pe  pw  pok
# Sub:      psb psd psi pse psw psok
# =============================================================================

_RESET  = "\033[0m"
_YELLOW = "\033[1;33m"   # bold yellow  -- build
_PURPLE = "\033[1;35m"   # bold magenta -- debug
_CYAN   = "\033[1;36m"   # bold cyan    -- info
_RED    = "\033[1;31m"   # bold red     -- error
_ORANGE = "\033[0;33m"   # dim yellow   -- warning
_GREEN  = "\033[1;32m"   # bold green   -- ok

_SUB = "    "            # 4-space indent for sub-variants


def _p(color: str, label: str, msg: str, indent: str = "") -> None:
    print(f"{color}{indent}{label}  {msg}{_RESET}")


# -- build --------------------------------------------------------------------
def pb(msg: str)  -> None: _p(_YELLOW, "[BUILD]  ", msg)
def psb(msg: str) -> None: _p(_YELLOW, "[BUILD]  ", msg, _SUB)

# -- debug --------------------------------------------------------------------
def pd(msg: str)  -> None: _p(_PURPLE, "[DEBUG]  ", msg)
def psd(msg: str) -> None: _p(_PURPLE, "[DEBUG]  ", msg, _SUB)

# -- info ---------------------------------------------------------------------
def pi(msg: str)  -> None: _p(_CYAN,   "[INFO]   ", msg)
def psi(msg: str) -> None: _p(_CYAN,   "[INFO]   ", msg, _SUB)

# -- error --------------------------------------------------------------------
def pe(msg: str)  -> None: _p(_RED,    "[ERROR]  ", msg)
def pse(msg: str) -> None: _p(_RED,    "[ERROR]  ", msg, _SUB)

# -- warning ------------------------------------------------------------------
def pw(msg: str)  -> None: _p(_ORANGE, "[WARNING]", msg)
def psw(msg: str) -> None: _p(_ORANGE, "[WARNING]", msg, _SUB)

# -- ok -----------------------------------------------------------------------
def pok(msg: str)  -> None: _p(_GREEN, "[OK]     ", msg)
def psok(msg: str) -> None: _p(_GREEN, "[OK]     ", msg, _SUB)
