# Telegram Bot for BgRemover

[![python](https://img.shields.io/badge/python-3.11-blue?style=flat-square)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=flat-square)](https://github.com/python-telegram-bot/python-telegram-bot)

Telegram Bot for BgRemover is a Python project aimed at building a server-side service for Telegram users. This project utilizes the TeleBot library to create a Telegram bot with various functionalities tailored for user interaction.

## Overview

The project consists of two main modules: `COUNT_MANAGER.PY` and `MAIN.PY`. `COUNT_MANAGER.PY` handles the management of processing counts, while `MAIN.PY` serves as the main server implementation for the Telegram bot. The bot interacts with users through text and image messages, providing responses and performing image processing tasks.

## Features

- **Processing Count Management**: The `COUNT_MANAGER.PY` module manages the processing count for image processing tasks. It includes functions to load and save the processing count from a file, ensuring continuity across bot sessions.

- **Telegram Bot Server**: The `MAIN.PY` module implements a Telegram bot server using the TeleBot library. It handles various commands from users, such as `/start`, `/help`, `/website`, `/button`, and `/removebg`. Additionally, it supports image processing tasks by removing the background from uploaded images.

- **Interactive Commands**: Users can interact with the bot by sending text commands, such as requesting help (`/help`), opening a website (`/website`), or triggering specific actions (`/button`). The bot provides prompt responses to user commands and inquiries.

- **Image Processing**: The bot supports image processing functionalities, allowing users to upload images for background removal. Upon receiving an image, the bot processes it and sends back the result to the user.

## Usage

1. Navigate into the cloned directory: `git clone https://github.com/SaidisIam/BgRemover-Bot.git`
2. Navigate into the cloned directory: `cd BgRemover-Bot`
2. Create an environment file by running the following command: `python -m venv env` 
3. Run this command to activate your virtual environment: `source ./env/bin/activate`
3. Create the necessary folders: `mkdir media`, `mkdir media/inputs`, `mkdir media/outputs`
4. Create the `conf.py` file with your Telegram bot token: `touch conf.py`, Add the following line to `conf.py` and replace `"YOUR_TOKEN"` with your actual Telegram bot token: TOKEN = "YOUR_TOKEN"
4. To install the required dependencies, simply execute: `pip install -r requirements.txt`
5. Run the Telegram bot server using the appropriate wiht command`python main.py`
6. Interact with the Telegram bot using your Telegram client, and utilize various commands provided by the bot.

## Contribution

Contributions to Telegram Bot for BgRemover are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.
