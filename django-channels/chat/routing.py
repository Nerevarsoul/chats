from channels.routing import route

channel_routing = [
    route("http.request", "chat.consumer.http_consumer"),
]

