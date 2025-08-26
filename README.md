# ucanet-registry
A live registry for ucanet domains
For more info about the project. visit [ucanet.net](https://ucanet.net)

## How to Register
To register a domain, you have to join our Discord server [linked on our website](http://ucanet.net). This is to discourage rule-breaking sites from being registered. You can also [manually register a domain with a pull request](#manual-registration). 

## Full Description and Specification
This repo contains a registry ([ucanet-registry.txt](https://github.com/ucanet/ucanet-registry/blob/main/ucanet-registry.txt)) of domains/subdomains accessible from the [ucanet DNS server](https://github.com/ucanet/ucanet-server), and their respective DNS entries. This file is automatically updated by the [ucanet Discord bot](https://github.com/ucanet/ucanet-server) whenever a domain is registered, or a domain's DNS entry is changed. The ucanet DNS server will automatically refresh its registry every 10 minutes (unless defined otherwise), and DNS propagation usually happens between 10-20 minutes.

Each domain/subdomain DNS entry is contained on one line. Each data field is separated by a space. There must be three data fields minimum per DNS entry.
Field | Description
------|-------
0     | Defines the name or subdomain of the entry.
1     | Discord ID, 1, or 0. If 1, domain is registered by a github user. If 0, domain was registered by repo managers and is used for internal purposes.
2     | The IP address or Neocities subdomain. If equal to "protoweb", sites will pull from Protoweb's proxy.
3     | Extra field. If the second field value is 1, this must a Github username.

## Manual Registration
If you want to avoid registering a domain over discord, you can submit a pull request with your domain. Following the format defined above, please provide a domain name, ip address (or Neocities site), and your Github username. Here is an example of a formatted entry `ucanet.net 1 172.67.219.131 ucanet`. Pull request domain registrations will be reviewed manually.

## ucanet-registry-updater
This repository contains ucanet-registry-updater.py which contains utilities for managing the registry. See the included registry-updater.md readme for more details.

## License
[APGL-3.0 license](https://github.com/ucanet/ucanet-registry/blob/main/LICENSE.md)
