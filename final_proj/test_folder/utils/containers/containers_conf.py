MOCK_IMAGE = 'mock_image'
MOCK_CONTAINER_NAME = 'mock_docker'
MOCK_ALIAS = 'mock'

DB_IMAGE = 'percona'
DB_CONTAINER_NAME = 'percona_docker'
DB_HOST = '127.0.0.1'
DB_HOST_PORT = 8888
DB_PORT_MAP = {'3306/tcp': 8888}
DB_ROOT_PASS = 'pass'
DB_NAME = 'test_db'
DB_ALIAS = 'percona'

DB_APP_USER = 'test_qa'
DB_APP_PASS = 'qa_test'

APP_IMAGE = 'myapp'
APP_PORT_MAP = {'8080/tcp': 8080}
APP_VOLUME = '/tmp/shared'
APP_CONTAINER_NAME = 'app_docker'

MOCK_PORT_MAP = {'5000/tcp': 5000}