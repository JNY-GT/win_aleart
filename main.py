import time

from weather import get_weather, is_thunderstorm
from notifier import send_notification
from config import CHECK_INTERVAL


last_thunder_state = False


while True:

    try:

        data = get_weather()
        
        print(data)

        thunder = is_thunderstorm(data)

        print("雷状態:", thunder)

        if thunder and not last_thunder_state:

            send_notification(
                "雷雲接近",
                "雷雨の可能性があります"
            )

        last_thunder_state = thunder

    except Exception as e:

        print("エラー:", e)

    time.sleep(CHECK_INTERVAL)