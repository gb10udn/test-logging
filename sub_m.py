import logging

def test():
    logger = logging.getLogger(__name__)
    logger.info('呼び出したよ！')  # TODO: 240420 jupyter-notebook から呼び出した場合に、適切に処理できるようにする？