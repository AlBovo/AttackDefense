# Attack Defense
![Cyberchallenge](https://cyberchallenge.it/_next/image?url=%2Fmedia%2Fpublic%2Fpress-kit%2FCCIT_Logo_White.png&w=3840&q=75)<br>
This repository contains some setups for useful tools for [CTF A/D](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity)). <br>
Thanks to suggestions from the [Ulisse](https://ctf.ulis.se) team at the University of Bologna, it was possible to modify or create tools in order to make them easily accessible and configurable during the national finals of **Cyberchallenge 2024**.

## TODOs
- [x] Create a script to exploit a *misconfiguration* of Tulip (no authentication set).
- [x] Write an exploit template that can retrieve the flag-ids and submit flags to [`Destructive Farm`](https://github.com/DestructiveVoice/DestructiveFarm).
- [ ] Setup a Docker for [`Tulip`](https://github.com/OpenAttackDefenseTools/tulip) with authorization and pcap-broker.

## Credits
- **Tulips**
🌷 [`Tulip`](https://github.com/OpenAttackDefenseTools/tulip) is a flow analyzer meant for use during Attack / Defence CTF competitions. It allows players to easily find some traffic related to their service and automatically generates python snippets to replicate attacks.

- **Destructive Farm**
[`Destructive Farm`](https://github.com/DestructiveVoice/DestructiveFarm) is an exploit farm for attack-defense CTF competitions.
