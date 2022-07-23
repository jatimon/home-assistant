logger.info("***********************************************")
logger.info("Python script triggered from automation")
logger.info("***********************************************")

message = data.get("message", "I am speachless")
title = data.get("title", "service without a title")
alexa_device = data.get("device", "kitchen")

service_data = { 
"message": message,
"target": f"media_player.{alexa_device}",
"data": {"type": "tts"}
}

logger.info("service data: %s, alexa media device: %s", service_data, alexa_device)

hass.services.call("notify", f"alexa_media", service_data, False)