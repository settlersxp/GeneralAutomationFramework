# GeneralAutomationFramework

Intended to be:
1) a general automation framework for any type of automation project.
2) set up as a multi-repo for translations, mocks and other resources.

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