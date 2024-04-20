import logging
import sub_m


def set_logging():  # INFO: 240420 jupyter-notebook から実行する場合等では、この設定処理を別で呼び出して実行する。
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)  # INFO: 240420 (ログファイルより) よく見る箇所なので、不要なものは出さなくて良い気がする。

    file_handler = logging.FileHandler("./misc/example.log", encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # INFO: 240420 このように設定すると、各ハンドラでレベルを分けれる。

    # TODO: 240420 ERROR の場合はメール飛ばす処理を記述する。

    logging.basicConfig(
        handlers=[stream_handler, file_handler],  # INFO: 240420 handlers で設定すると複数のハンドラを設定できる。
        level=logging.DEBUG,                      # INFO: 240420 全体の設定。個別設定の handeler よりも下げる。(Ex. 全体設定が WARNING であれば、個別設定で DEBUG としても表示されない。)
    )  


if __name__ == '__main__':
    set_logging()
    logger = logging.getLogger(__name__)
    
    logger.debug('main debug')
    logger.info('main info')
    logger.warning('main warning')
    logger.error('main error')

    sub_m.test()