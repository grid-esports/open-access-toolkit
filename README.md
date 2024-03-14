# Open Access Toolkit
A set of scripts and tools for GRID Open Access users.


## Series State Exporter
Gives Open Access users the ability to retrieve and download the state for a series, for usage with data analysis tools and frameworks.

### Prerequisites
To use this script, you will need the following installed:

* Python >= 3.9
Many modern OSes will already have this installed, but you can also install via tools like apt-get, homebrew, or chocolatey.
For more details, see the [Python documentation](https://wiki.python.org/moin/BeginnersGuide/Download).

* gql - Python GraphQL Client
You can install this via pip with the following command:
`pip install "gql[all]"`
For more details, see the [gql documentation](https://gql.readthedocs.io/en/latest/intro.html)

### Setup

You will first need to set your GRID API Key as an environment variable.

ZSH:
`echo "export GRID_API_KEY=yourkeygoeshere" >> ~/.zshrc && source `

BASH:
`echo "export GRID_API_KEY=yourkeygoeshere" >> ~/.bashrc`

You may also need to grant execute permissions on the script.
`chmod +x ./series-state-exporter.py`

### Usage
You should be able to run the script with the following command, where [seriesId] is the ID of the series you would like to export / download.
`./series-state-exporter.py [seriesId]`

All going well, it will download the data and write it to `[seriesId]_series_state.json`.

If you don't have permissions to access the specific series, it should return an exception message & exit.

If you get a bad response back from the Series State API (e.g. system error), it'll let you know in the output, but still write the response to file.
