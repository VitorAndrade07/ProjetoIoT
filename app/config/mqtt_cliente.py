import json
import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from app.controllers.data_controller import save_to_db

# Carrega as variáveis do .env
load_dotenv("./camila-IoT/.env")

MQTT_BROKER = os.getenv("MQTT_BROKER")
try:
    MQTT_PORT= int(os.getenv("MQTT_PORT")) 
except (TypeError, ValueError):
    raise ValueError("MQTT_PORT não está configurada corretamente no .env")

MQTT_TOPIC = os.getenv("MQTT_TOPIC")
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT com sucesso.")
        client.subscribe(MQTT_TOPIC)
        print(f"Inscrito no tópico: {MQTT_TOPIC}")
    else:
        print(f"Falha na conexão, código de retorno: {rc}")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        save_to_db(payload) # Chama a função que agora usa .get()
        print("Mensagem recebida e salva:", payload)
    except json.JSONDecodeError:
        print("Erro: Mensagem MQTT não é um JSON válido.")
    except Exception as e:
        # Se um erro ocorrer agora, ele será um erro do MySQL, não do KeyError!
        print("Erro ao processar MQTT:", e)


def start_mqtt():
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
        client.on_connect = on_connect
        client.on_message = on_message
        
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        client.tls_set() 

        print(f"Tentando conectar a {MQTT_BROKER}:{MQTT_PORT}...")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        client.loop_start() 
        
    except Exception as e:
        print(f"❌ ERRO FATAL AO INICIAR MQTT: {e}")
        raise