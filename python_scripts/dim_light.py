entity_id  = data.get('entity_id')
sleep_delay = float(data.get('sleep_delay',1))
start_level_pct = int(data.get('start_level_pct',0))
end_level_pct = int(data.get('end_level_pct',100))
step  = int(data.get('step_in_level',1))


new_level_pct = start_level_pct
while new_level_pct < end_level_pct :
	logger.info(f"new {new_level_pct}, end {end_level_pct}")
	states = hass.states.get(entity_id)
	current_level_pct = states.attributes.get('brightness_pct') or 0
	logger.info(f"current {current_level_pct}")
	if (current_level_pct > end_level_pct) :
		logger.info('Exiting Fade In')
		break;
	else :
		logger.info('Setting brightness of ' + str(entity_id) + ' from ' + str(current_level_pct) + ' to ' + str(new_level_pct))
		data = { "entity_id" : entity_id, "brightness_pct" : new_level_pct }
		hass.services.call('light', 'turn_on', data)
		new_level_pct = new_level_pct + step
		time.sleep(sleep_delay)