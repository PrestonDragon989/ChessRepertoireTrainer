import logging

FORMATTER = logging.Formatter("%(asctime)s |:| LEVEL: %(levelname)s |:| %(name)s = %(message)s",
                              "%y-%b-%d -- %H:%M:%S")


def get_chess_logger(log_file_path) -> logging.Logger:
    """
    Generates the logger object for chess related messages.
    :param log_file_path: File path for the log file used.
    :return: Logger object.
    """
    chess_logger = logging.getLogger("CHESS")

    handler = logging.StreamHandler()

    handler.setFormatter(FORMATTER)
    handler.setLevel(logging.DEBUG)

    handler.setStream(open(log_file_path, 'a'))

    chess_logger.addHandler(handler)
    chess_logger.setLevel(handler.level)

    return chess_logger
