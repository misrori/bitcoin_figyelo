import requests
import os

# Környezeti változók beolvasása (Secrets-ből jönnek majd)
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Bitcoin és Ethereum ár lekérése
url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
valasz = requests.get(url, params=params)
adat = valasz.json()

btc = adat["bitcoin"]["usd"]
eth = adat["ethereum"]["usd"]

# Telegram üzenet összeállítása
uzenet = (
    f"📊 Kripto árfolyamok\n"
    f"━━━━━━━━━━━━━━━━━\n"
    f"₿ Bitcoin:  ${btc:,.0f}\n"
    f"Ξ Ethereum: ${eth:,.0f}\n"
    f"━━━━━━━━━━━━━━━━━\n"
    f"🕐 Automatikus értesítés"
)

# Üzenet küldése Telegram bot API-val
telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
requests.post(telegram_url, json={
    "chat_id": CHAT_ID,
    "text": uzenet
})

print("Üzenet elküldve!")
