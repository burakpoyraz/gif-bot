import requests
import logging
import schedule
import time
from dotenv import load_dotenv
import os


load_dotenv()
# Giphy API anahtarını .env dosyasından al
API_KEY = os.getenv('GIPHY_API_KEY')


GIPHY_URL = f"https://api.giphy.com/v1/gifs/random?api_key={API_KEY}&rating=g"

def fetch_random_gif():
    try:
        response = requests.get(GIPHY_URL)
        data = response.json()
        gif_url = data['data']['images']['original']['url']
        print(f"🎬 Bugünün GIF'i: {gif_url}")
        logging.info(f"GIF gönderildi: {gif_url}")
    except Exception as e:
        logging.error(f"Hata oluştu: {e}")

# Log ayarları
logging.basicConfig(filename='gif_bot.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Her gün saat 10:00'da çalıştır
fetch_random_gif()
schedule.every().day.at("10:00").do(fetch_random_gif)

print("Bot başlatıldı. Her gün 10:00'da çalışacak.")

# Sürekli çalışması için döngü
while True:
    schedule.run_pending()
    time.sleep(1)
