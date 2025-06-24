# 📈 Telegram Investment ETF Bot

A Telegram bot that fetches ETF recommendations from an external investment API and displays them in chat. Built with Python and `python-telegram-bot`, and deployed on Heroku.

---

## 🚀 Features

- `/start` — Greet the user
- `/portfolio` — Fetch and display ETF allocation recommendations
- Handles dynamic API responses (e.g. "allocation" or "% allocation")
- Secure deployment using environment variables on Heroku

---

## 🛠 Tech Stack

- Python 3.12+
- [python-telegram-bot](https://python-telegram-bot.org/)
- Heroku (worker dyno)
- `requests` for HTTP API calls

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/etf-telegram-bot.git
   cd etf-telegram-bot
