import logging
from colorama import Fore, init

init(autoreset=True)


def setup_logging():
    logging.addLevelName(25, "SUCCESS")

    def success(self, message, *args, **kws):
        if self.isEnabledFor(25):
            self._log(25, message, args, **kws)

    logging.Logger.success = success

    class ColorFormatter(logging.Formatter):
        """Formatter de logs pour ajouter des couleurs aux messages de log."""

        def format(self, record):
            if record.levelno == logging.INFO and "found in cache" in record.getMessage():
                # Messages contenant "found in cache" en vert
                record.msg = f"{Fore.GREEN}{record.msg}{Fore.RESET}"
            elif record.levelno == logging.ERROR:
                # Messages d'erreur en rouge
                record.msg = f"{Fore.RED}{record.msg}{Fore.RESET}"
            else:
                # Autres messages en gris
                record.msg = f"{Fore.LIGHTBLACK_EX}{record.msg}{Fore.RESET}"
            return logging.Formatter.format(self, record)

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
