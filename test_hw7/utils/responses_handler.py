import logging

class ResponsesHandler:
    def __init__(self, lvl):
        self.logger = logging.getLogger(__name__)
        handler = logging.FileHandler('responses.log')
        self.logger.handlers = [handler]
        self.log_level = lvl
        self.logger.propagate = False

    def log(self, response):
        msg = f'{response.status_code} - {response.headers} - {response.content}'
        self.logger.log(self.log_level, msg)

    def set_log_level(self, lvl):
        self.log_level = lvl
