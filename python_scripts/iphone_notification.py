message = data.get("message")
title = data.get("title")
device = data.get("device")

if not any([message, title, device]):
    logging.info(
        "Missing data for iphone notification: message: %s, title: %s, device: %s",
        message, title, device
    )


service_data = { 
"message": message,
"title": title,
}

logger.info("service data: %s, device: %s", service_data, device)

hass.services.call("notify", f"mobile_app_{device}", service_data, False)