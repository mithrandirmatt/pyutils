import configparser


def read_ini(path: str) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg


def get_section(cfg: configparser.ConfigParser, section: str) -> dict:
    if not cfg.has_section(section):
        raise KeyError(f"Section [{section}] not found in ini file")
    return dict(cfg[section])
