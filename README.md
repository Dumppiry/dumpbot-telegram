# DumpBot-Telegram

This is a bot for Dumppi Ry Telegram group. Main purpose for this bot at the moment is to automatically delete system messages from Telegram.

## Development

First you need to create `.env` file.

```bash
# Linux
cp .env.example .env
```

After you have an .env file, you need bot token of the bot. Please create a development bot for you. You can reference this [guide](https://core.telegram.org/bots/tutorial) on how to get started with @BotFather. Use the token that you will get from @BotFather and put it in to the `.env` file.

### Requirements

Here is a list of requirements. This might differ depending on your operating system. Main thing is that you can either install the pip packages straigth to your pc (not recommended) or you can use venv to install the packages.

- Python3.12
- python3-venv
- Packages from `requirements.txt`

### Virtual Environment

It is recommended to install the pip packages to a venv. For Ubuntu/Debian:

```bash
# Create the venv to a folder 'venv'
python3 -m venv venv

# Activate the venv
source venv/bin/activate

# Install requirements.txt
pip3 install -r requirements.txt
```

You might need to restart your IDE after you have installed the requirements.

### Run the bot

Now you are ready to run the bot.

```bash
python3 src/main.py
```

## Deployment

Currently this bot is hosted by webmaster. When there is a need to deploy a new version, please contact current webmaster of Dumppi Ry.
