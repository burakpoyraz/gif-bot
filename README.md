# 🎬 Daily Random GIF Bot (Python + Giphy API)

This project is a lightweight automation bot that fetches a random GIF from Giphy every day and logs it to a file. It’s built using Python, scheduled with `schedule`, and keeps your feed (or logs) fun and fresh every morning.

## ✨ Features

- Fetches a random GIF from Giphy
- Runs automatically every day at 10:00 AM
- Logs the selected GIF URL to `gif_bot.log`
- Secure `.env` configuration (API key hidden)
- Simple and extendable structure (can be integrated with Telegram, Twitter, etc.)

---

## 🔧 Technologies Used

- Python 3.13+
- [Giphy API](https://developers.giphy.com/)
- `requests`
- `schedule`
- `logging`
- `python-dotenv`

---

## 🚀 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/burakpoyraz/gif-bot.git
cd gif-bot
