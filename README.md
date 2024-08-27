# GeneralAutomationFramework

## Intended to be:
1) A general automation framework for any type of automation project.
2) Set up as a multi-repo for translations, mocks and other resources.
3) A project which implements most things from scratch to explain the underlying principles and how some things work in other tools.

## Decisions:
1) Intentionally not using https://docs.pytest.org/en/stable/ due to licencing costs for commercial use until approved

## Structure:
1) Write the API tests into `Backend/API/` folder
2) Write the Mocks into `Mocks/API/` folder
3) Write the Translations into `Translations/` folder or set up this folder to get the translations from a different repo
4) Split the frontend into components and write their functionality in the `Frontend/Components/` folder
5) Compose the components into pages and write their functionality in the `Frontend/Pages/` folder
6) Database and websocket connections go into the `Connections/` folder
7) Write the tests into the `Tests/` folder and reuse components, pages, connections, translations, mocks and APIs as needed

## Notes:
- In Utils there are classe which usually help us with the code completion and the code readability.
- The components have the selectors inside their classes, so we can easily change and track them if needed. They can also be exported into a file and loaded all at once but I prefer this approach.
- Sending data between everything is done through the `data` attribute by importing the dataBroker as such `import dataBroker as Data`.
- If you want auto-complete for the attributes of the dataBroker add all the keys there as well else enjoy of getting the keys from the dictionary.
- Can be tested on https://magento.softwaretestingboard.com/ and https://www.saucedemo.com/ for the moment.

## Requests:
Open a new bug with your request. The discussion will happen on that bug. I will try to implement it as soon as possible.

## How to run:
1) Install the requirements with `pip install -r requirements.txt`
2) Run the `runner.py` file with `python runner.py` or `python3 runner.py` depending on your python version

## Contact:
For any questions or suggestions please contact me at [gabriel.cliseru@gmail.com](mailto:gabriel.cliseru@gmail.com?subject=[GitHub]%20General%20Automation%20Framework). 
I am open for work and collaborations. My linkedin is https://www.linkedin.com/in/gabriel-cliseru/ .