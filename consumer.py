from kafka import KafkaConsumer
import json

# Kafka bootstrap servers
bootstrap_servers = ['localhost:9092']

# topic kafka
topic = 'data-stream'

# Creation d'un consumer kafka
consumer = KafkaConsumer(topic,
                         bootstrap_servers=bootstrap_servers,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    price_data = message.value
    
    # Extraire les valeurs requises
    #HINT : Aller sur l'url "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo" et examiner les champs des données qu'on veut extraire
    timestamp = price_data['timestamp']
    open_price = #fill_here
    high_price = #fill_here
    low_price = #fill_here
    close_price = #fill_here
    volume = #fill_here
    
    print('Timestamp: ' + timestamp)
    print('Open Price: ' + open_price)
    print('High Price: ' + high_price)
    print('Low Price: ' + low_price)
    print('Close Price: ' + close_price)
    print('Volume: ' + volume)
    print('---------------------')
