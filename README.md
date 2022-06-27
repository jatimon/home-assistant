# Home Assistant

## My Smart Home Philosophy

* Convenience 
  * My home should make smart decisions without me having to hit a button or say a command
* Control
  * Where possible always have a physical override, i.e. a light switch.
  * Have simple voice activated or phone activated controls when the first principle is not possible

## Naming Conventions

### Devices
Devices will be named according to their manufacturer
i.e. **Shelly** 

Renaming newly added devices this way, will have the side effect of changing the entity ids of each of the device entities to match the beginning of the proposed entity naming convention.

### Entities

I am adopting a concept I found in a [post](https://community.home-assistant.io/t/recommended-ways-to-manage-devices-and-entities-names/243815/13) which advocates using custom attributes for entity metadata.

The core ideas are:
* short and simple names for entity ids.
* grouping of similar devices is easy
* Metadata will contain the fields that I might want to search on in a template using the `selectattr` 

Entity naming conventions will follow:

< domain >.< manufacturer >_< type >_< location >_< number *optional* >

### Examples
```
binary_sensor.aqara_contact_entryway:
  integration: zigbee
  location: front door
  security_zone: entry point
```
```
binary_sensor.aqara_contact_office:
  integration: zigbee
  location: office door
  security_zone: interior
```
```
light.sengled_level_on_off_downstairs_bathroom_5:
  integration: zwave
  location: above vanity
  ```

## Security Zones
I will use meta data to define an entity's security zone.  This way I can have an automation that ensures all entities in say security zone **entry point**  are locked/closed when the house goes to sleep or becomes unoccupied. 

### Proposed Zones
* entry point -- who saw that coming?
* exterior 
* interior
* none

This should allow straightforward simple filtering of devices for various automations/alerts


## Automation Ideas

### Unlock the front door
* When a trusted person is recognized, unlock the front door

### Party Time
* when the back yard disco ball is on, make the pool, landscape, and bar lights cycle color changes to compliment the disco ball

### Blind Control
* at a specified time lower blinds in the living room
    * also maybe adjust for if the TV gets turned on

### detect when we are not at home and put the home in Away Mode
* In away mode, lights come on at dark and go off and some time around 'Bedtime'

## Intergrations to add?
* presence detection; owntrack, gps logger, icloud platform 
* geolocation triggering
