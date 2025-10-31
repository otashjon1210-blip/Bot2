import requests
import time
from datetime import datetime

TELEGRAM_TOKEN = "8311496185:AAFVn1e1Bp7H3zCTjDlvhquZEaYSdLA5xEo"
CHANNEL_ID = "@My_rsi_treding_bot."  

class SimpleSignalBot:
    def __init__(self, token, channel_id):
        self.token = token
        self.channel_id = channel_id
        self.api_url = f"https://api.telegram.org/bot{token}/"
    
    def send_message(self, text):
        """Telegramga xabar yuborish"""
        url = self.api_url + "sendMessage"
        data = {
            "chat_id": self.channel_id,
            "text": text,
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print(f"✅ Xabar yuborildi: {datetime.now()}")
            else:
                print(f"❌ Xatolik: {response.text}")
        except Exception as e:
            print(f"❌ Ulanish xatosi: {e}")

def get_gold_price():
    """Oltin narxini olish (test ma'lumot)"""
    # Haqiqiy tradingda bu qism o'zgartiriladi
    import random
    price = 1800 + random.randint(-10, 10)
    rsi = random.randint(20, 80)
    return price, rsi

def check_rsi_signal(rsi):
    """RSI signalini tekshirish"""
    signals = []
    
    # Yuqori breakoutlar
    if rsi >= 75:
        signals.append("SELL - RSI yuqori (75+)")
    if rsi >= 85:
        signals.append("SELL - RSI juda yuqori (85+)")
    if rsi >= 95:
        signals.append("SELL - RSI ekstremal (95+)")
    
    # Quyi breakoutlar
    if rsi <= 25:
        signals.append("BUY - RSI past (25-)")
    if rsi <= 15:
        signals.append("BUY - RSI juda past (15-)")
    if rsi <= 5:
        signals.append("BUY - RSI ekstremal (5-)")
    
    return signals

def main():
    print("🤖 TELEGRAM SIGNAL BOT ISHGA TUSHDI")
    print("=" * 50)
    
    # Botni yaratish
    bot = SimpleSignalBot(TELEGRAM_TOKEN, CHANNEL_ID)
    
    # Test xabar yuborish
    bot.send_message("🚀 Signal Bot ishga tushdi! " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    
    counter = 0
    while True:
        try:
            counter += 1
            print(f"\n🔍 Tekshiruv #{counter} - {datetime.now().strftime('%H:%M:%S')}")
            
            # Oltin narxi va RSI olish (test)
            price, rsi = get_gold_price()
            print(f"💰 XAUUSD: {price} | RSI: {rsi}")
            
            # Signallarni tekshirish
            signals = check_rsi_signal(rsi)
            
            # Signal borligini tekshirish
            if signals:
                for signal in signals:
                    message = f"""
🚨 <b>TRADING SIGNAL</b> 🚨

📊 <b>Instrument:</b> XAUUSD
🎯 <b>Signal:</b> {signal}
💰 <b>Price:</b> {price}
📈 <b>RSI:</b> {rsi}

⚠️ <b>Risk Management:</b>
• Stop Loss: 20-30 pips
• Take Profit: 50-100 pips

⏰ <b>Time:</b> {datetime.now().strftime('%H:%M:%S')}
                    """
                    bot.send_message(message)
                    print(f"📢 Signal yuborildi: {signal}")
            
            # 60 soniya kutish (1 daqiqa)
            print("⏳ Keyingi tekshiruvgacha 60 soniya...")
            time.sleep(60)
            
        except KeyboardInterrupt:
            print("\n⏹️ Bot to'xtatildi")
            break
        except Exception as e:
            print(f"❌ Xatolik: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()