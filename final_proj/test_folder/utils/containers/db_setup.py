import pymysql
from utils.containers.containers_conf import *
from pymysql.constants import CLIENT
import logging

logger = logging.getLogger('infrastructure')

def ready():
    try:
        connection = pymysql.connect(host=DB_HOST,
                                    port=DB_HOST_PORT,
                                    user='root',
                                    password=DB_ROOT_PASS,
                                    cursorclass=pymysql.cursors.DictCursor,
                                    autocommit=True)
        return True
    except Exception:
        return False

    
def setup():
    logger.info('DB setup start')
    connection = pymysql.connect(host=DB_HOST,
                                port=DB_HOST_PORT,
                                user='root',
                                password=DB_ROOT_PASS,
                                cursorclass=pymysql.cursors.DictCursor,
                                autocommit=True)
    try:
        with connection:
            with connection.cursor() as cursor:
                sql = f'CREATE DATABASE {DB_NAME};'
                cursor.execute(sql)
                logger.info('DB created')
    except Exception as e:
        logger.info(e)

    connection = pymysql.connect(host=DB_HOST,
                                 port=DB_HOST_PORT,
                                 user='root',
                                 database='test_db',
                                 password=DB_ROOT_PASS,
                                 client_flag=CLIENT.MULTI_STATEMENTS,
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True)
    with connection:
        with connection.cursor() as cursor:
            try:
                sql = '''CREATE TABLE `test_users` (
                    `id` int NOT NULL AUTO_INCREMENT,
                    `username` varchar(16) DEFAULT NULL,
                    `password` varchar(255) NOT NULL,
                    `email` varchar(64) NOT NULL,
                    `access` smallint DEFAULT NULL,
                    `active` smallint DEFAULT NULL,
                    `start_active_time` datetime DEFAULT NULL,
                    PRIMARY KEY (`id`),
                    UNIQUE KEY `email` (`email`),
                    UNIQUE KEY `ix_test_users_username` (`username`)
                    );
                    '''
                cursor.execute(sql)
            except Exception as e:
                logger.info(e)

            try:
                sql = f'''DROP USER '{DB_APP_USER}'@'localhost';
                DROP USER '{DB_APP_USER}'@'%';
                '''
                cursor.execute(sql)
                logger.info('DB user erased')
            except Exception:
                logger.info('DB user already exists')
                pass

            try:
                sql = f'''CREATE USER '{DB_APP_USER}'@'localhost' IDENTIFIED BY '{DB_APP_PASS}';
                CREATE USER '{DB_APP_USER}'@'%' IDENTIFIED BY '{DB_APP_PASS}';
                GRANT ALL ON *.* TO '{DB_APP_USER}'@'localhost';
                GRANT ALL ON *.* TO '{DB_APP_USER}'@'%';
                FLUSH PRIVILEGES;
                '''
                cursor.execute(sql)
                logger.info('DB user inited')
            except Exception as e:
                logger.info(e)
                pass