import logging

def test():
    logger = logging.getLogger(__name__)  # INFO: 240420 パッケージ構造の場合、name -> sub_p.hoge と出た。問題無し。
    logger.debug('hoge debug')
    logger.info('hoge info')
    logger.warning('hoge warning')
    logger.error('hoge error')