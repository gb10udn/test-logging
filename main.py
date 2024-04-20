import logging
import sub_m


def set_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR)

    file_handler = logging.FileHandler("./misc/example.log", encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # INFO: 240420 このように設定すると、各ハンドラでレベルを分けれる。

    # TODO: 240420 ERROR の場合はメール飛ばす処理を記述する。

    logging.basicConfig(handlers=[stream_handler, file_handler])  # INFO: 240420 handlers で設定すると処理を同居できる。


if __name__ == '__main__':
    set_logging()
    logger = logging.getLogger(__name__)
    
    logger.debug('This message should go to the log file')
    logger.info('So should this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

    sub_m.test()