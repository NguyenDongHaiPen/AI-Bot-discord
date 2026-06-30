# 🧪 Rick Sanchez AI — Discord Bot

> *"Wubba Lubba Dub-Dub!"* — A Discord chatbot that talks exactly like Rick Sanchez from Rick and Morty, powered by Google Gemini AI.

![Rick](Rick.jpg)

---

## ✨ Features

- 🧠 **Conversation Memory** — Rick remembers what you said earlier in the channel for natural multi-turn conversations.
- ⚡ **Powered by Gemini 3.5 Flash** — Fast, intelligent responses with deep character understanding.
- 🎭 **Accurate Personality** — Stutters, burps, uses catchphrases, and is appropriately cynical and condescending.
- 🔄 **Memory Reset** — Use `!reset` to wipe Rick's memory if things get too chaotic.
- 💬 **Flexible Triggering** — Mention the bot, reply to it, or just say "Rick" anywhere in your message.

---

## 📁 Project Structure

```
AI_Bot_Discord/
├── bot/
│   ├── .env.example      # Template for environment variables
│   ├── config.py          # Loads environment variables securely
│   ├── rick_ai.py         # Gemini AI integration + Rick's system prompt
│   └── main.py            # Discord bot logic (events, commands)
├── Rick.csv               # Original Rick dialogue dataset (1900+ lines)
├── RickAndMortyScripts.csv # Full show scripts dataset
├── .gitignore             # Protects secrets from being committed
└── README.md              # You are here
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** installed on your machine
- A **Discord Bot Token** ([Get one here](https://discord.com/developers/applications))
- A **Google Gemini API Key** ([Get one here — free](https://aistudio.google.com))

### 1. Clone the repository
```bash
git clone https://github.com/NguyenDongHaiPen/AI-Bot-discord.git
cd AI-Bot-discord
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r bot/requirements.txt
```

### 4. Set up environment variables
```bash
cp bot/.env.example bot/.env
```
Now open `bot/.env` in your editor and fill in your keys:
```env
DISCORD_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

> [!IMPORTANT]
> **Discord Bot Setup**: Go to [Discord Developer Portal](https://discord.com/developers/applications) → Your App → **Bot** tab → scroll down to **Privileged Gateway Intents** → enable **Message Content Intent**. Without this, the bot cannot read messages.

### 5. Run the bot
```bash
python -m bot.main
```
You should see:
```
Wubba Lubba Dub-Dub! The bot is online.
```

---

## 💬 Usage

| Method | Example |
|--------|---------|
| **@Mention** | `@RickBot What is the meaning of life?` |
| **Say "Rick"** | `Hey Rick, what do you think about school?` |
| **Reply** | Reply directly to any of Rick's messages |
| **Reset memory** | `!reset` |

---

## 🔒 Security Notes

- **Never commit your `.env` file** — it contains your API keys and tokens.
- The `.gitignore` file is already configured to exclude `.env`, `APIkey.md`, `kaggle.json`, and other sensitive files.
- If you accidentally leak a token, go to [Discord Developer Portal](https://discord.com/developers/applications) → Bot → **Reset Token** immediately.

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Bot Framework | [discord.py](https://discordpy.readthedocs.io/) v2.7+ |
| AI Model | [Google Gemini 3.5 Flash](https://ai.google.dev/) |
| Language | Python 3.9+ |
| Config | python-dotenv |

---

## 📜 License

This project is for educational purposes. Rick and Morty is property of Adult Swim / Warner Bros.
