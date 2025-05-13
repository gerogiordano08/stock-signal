from set_signals import compare_trendline_w_data
import json
import requests

tg_token = "7893540413:AAEo_dKZPi6rgGKq6P69z0eEfX0MXHdGwWQ"
geronimo_chat_id = 1699732759

def check_all_trendlines(json_path="data/trendlines.json"):
    with open(json_path, "r") as f:
        trendlines = json.load(f)
    for symbol in trendlines:
        checked = compare_trendline_w_data(symbol, json_path)
        if checked == "tocando-arriba":
            send_telegram_message(tg_token, geronimo_chat_id, f"{symbol} esta tocando una linea de tendencia por arriba." )
        elif checked == "tocando-abajo":
            send_telegram_message(tg_token, geronimo_chat_id, f"{symbol} esta tocando una linea de tendencia por abajo." )
        elif checked == "cruzo-p-arriba":
            send_telegram_message(tg_token, geronimo_chat_id, f"{symbol} ha cruzado una linea de tendencia hacia arriba." )
        elif checked == "cruzo-p-abajo":
            send_telegram_message(tg_token, geronimo_chat_id, f"{symbol} ha cruzado una linea de tendencia hacia abajo." )

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id" :chat_id,
        "text" : message
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent succesfully!")
    else:
        print("Failed to send message.")
        print(response.text)



if __name__ == "__main__":
    check_all_trendlines()