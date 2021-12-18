# docker SDK for python
# https://docker-py.readthedocs.io/en/stable/index.html
# pip install docker (not docker-py)

import os.path
import docker
import time
from utils.containers.containers_conf import *
from utils.containers import db_setup
import logging

client = docker.from_env()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('infrastructure')


class Containers:

    containers = []

    def setup():
        logger.info('setup start')

        container_mock = client.containers.run(
            MOCK_IMAGE, name=MOCK_CONTAINER_NAME, detach=True, ports=MOCK_PORT_MAP)

        container_db = client.containers.run(DB_IMAGE, name=DB_CONTAINER_NAME, detach=True,
                                             ports=DB_PORT_MAP,
                                             environment=[f"MYSQL_ROOT_PASSWORD={DB_ROOT_PASS}"])
        i = 0
        while i < 200 and not db_setup.ready():
            i += 1
            time.sleep(0.1)
        db_setup.setup()

        logger.info('starting app')

        cfg_path = os.path.abspath(APP_VOLUME)

        logger.info(f'volume: {cfg_path}')
        volume_bindings = {
            cfg_path: {
                'bind': '/shared',
                'mode': 'rw',
            },
        }

        container_app = client.containers.run(APP_IMAGE, name=APP_CONTAINER_NAME,
                                              command='/app/myapp --config=/shared/config.config',
                                              detach=True, ports=APP_PORT_MAP,
                                              links={MOCK_CONTAINER_NAME: MOCK_ALIAS,
                                                     DB_CONTAINER_NAME: DB_ALIAS},
                                              volumes=volume_bindings)

        logger.info('setup done')
        Containers.containers = [
            (container_mock, True), (container_db, True), (container_app, True)]

    def teardown():
        logger.info('teardown start')
        i = 0
        for x in Containers.containers:
            i += 1
            logger.info(f"stopping container n{i}")
            x[0].stop()
            if x[1]:
                x[0].remove(force=True)
        logger.info('teardown done')

