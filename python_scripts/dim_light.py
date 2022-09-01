entity_id  = data.get('entity_id')
sleep_delay = float(data.get('sleep_delay',1))
start_level_pct = int(data.get('start_level_pct',0))
end_level_pct = int(data.get('end_level_pct',100))
step  = int(data.get('step_in_level',1))


new_level = int((start_level_pct / 100) * 255)
end_level = int((end_level_pct / 100) * 255)
logger.info(f"new {start_level_pct}, end {end_level_pct}")
while new_level < end_level :
	states = hass.states.get(entity_id)
	current_level = states.attributes.get('brightness') or 0
	logger.info(f"current {current_level}")
	if (current_level > end_level) :
		logger.info('Exiting Fade In')
		break;
	else :
		logger.info('Setting brightness of ' + str(entity_id) + ' from ' + str(current_level) + ' to ' + str(new_level))
		data = { "entity_id" : entity_id, "brightness" : new_level }
		hass.services.call('light', 'turn_on', data)
		new_level = new_level + step
		time.sleep(sleep_delay)


