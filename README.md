# Home Assistant

## My Smart Home Philosophy

* Convenience 
  * My home should make smart decisions without me having to hit a button or say a command
* Control
  * Where possible always have a physical override, i.e. a light switch.
  * Have simple voice activated or phone activated controls when the first principle is not possible

## Naming Conventions

I am adopting a concept I found in a [post](https://community.home-assistant.io/t/recommended-ways-to-manage-devices-and-entities-names/243815/13) which advocates using custom attributes for device metadata.

The core ideas are short and simple names for entity ids.  Metadata will contain the fields that I might want to search on in a template using the `selectattr` search

Entity naming conventions will follow:

< domain >.< type >_< location >

### Example
```
binary_sensor.contact_front_door:
  integration: zigbee
  manufacturer: aqara
  location: top
  security_zone: entry point
```
```
binary_sensor.contact_office_door:
  integration: zigbee
  manufacturer: aqara
  location: top
  security_zone: interior
```
```
sensor.power_front_door:
  integration: zigbee
  manufacturer: aqara
  location: top
  battery: cr1632
```

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
