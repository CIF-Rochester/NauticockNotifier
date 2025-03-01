Nauticock Notifier
------------------
Updated 2025.

# Quick Start
- install Python >= 3.8
- **(Recommended)** Create a virtual environment with `python3 -m venv .venv` and activate it with `source .venv/bin/activate`
- run `python3 -m pip install -r requirements.txt` (this command occasionally has difficulty installing nextcord.  If so, install nextcord manually using `python3 -m pip install nextcord`)
- copy `config.example.cfg` to `config.cfg` and adjust the configuration
- run `python3 app.py`

For compatibility with the CIF Discord bot, also download print-server-logviewer found [here](https://github.com/CIF-Rochester/print-server-logviewer).
Copy `config.example.cfg` to `config.cfg` and ensure that the `key` parameter in this project's config matches the one found
in Nauticock.  The  `channel` parameter should also match the channel id you wish to send notifications to.

# Command Line Arguments
```
usage: app.py [-h] [--config CONFIG]

Print server for remotely printing to CIF lab printer

options:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG
                        Path to print server config file.
```
