import os
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
    #
    # # assign the browser to the dataBroker
    Data.BROWSER = webdriver.Remote(command_executor=f'http://localhost:{Base.CONNECTION_PORT}/wd/hub')
    Data.BROWSER.maximize_window()

    # list of keywords received as input to the program.
    # "login" is here to prove that nothing is run and nothing crashes if the feature has no method with this name
    keywords = ['product', 'buy', 'login']

    # load the method names from `/Tests/Web` that contain the keywords
    technology_folders = os.listdir('Tests/')
    for technology_folder in technology_folders:
        for feature_file in os.listdir(f'Tests/{technology_folder}/Features/'):
            if not feature_file.endswith('.py') or feature_file == '__init__.py':
                continue

            # import the class from the file
            class_module = __import__(f'Tests.{technology_folder}.Features.{feature_file[:-3]}', fromlist=[''])
            class_name = class_module.__dir__()[-1]
            class_instance = getattr(class_module, class_name)()
            class_methods = class_instance.__dir__()
            # get the class from the module
            for method_name in class_methods:
                # our methods are prefixed with `test_` everything else is either unittest or helper methods
                if not method_name.startswith('test_'):
                    continue

                # exclude the method if it doesn't contain any of the keywords
                found = False
                for keyword in keywords:
                    if keyword in method_name:
                        found = True
                        break
                if not found:
                    continue

                method = getattr(class_instance, method_name)
                # run the method and not crash if it fails because the next test has to run
                try:
                    method()
                except:
                    pass

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
