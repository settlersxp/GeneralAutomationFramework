import time

import docker
from selenium import webdriver

import dataBroker as Data
from Drivers.base import Base

# start a selenium server using docker
client = docker.from_env()
container = None
try:
    # pull the image from the repo and wait
    client.images.pull(Base.CHROME)

    container = client.containers.run(Base.CHROME,
                          command='shm-size="2g"',
                          ports={Base.CONNECTION_PORT: 4444},
                          remove=True,
                          detach=True)

    # assign the browser to the dataBroker
    Data.BROWSER = webdriver.Remote(command_executor=f'http://localhost:{Base.CONNECTION_PORT}/wd/hub')
except Exception as e:
    client.containers.close()
    print(e)
    Data.BROWSER.quit()
    raise e
finally:
    if container.id in client.containers.list():
        client.containers.close()
        time.sleep(5)
    Data.BROWSER.quit()