import logging

def test():
    logger = logging.getLogger(__name__)
    logger.debug('sub_m debug')
    logger.info('sub_m info')
    logger.warning('sub_m warning')
    logger.error('sub_m error')