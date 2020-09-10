---
title: 'api'
date: 2019-02-11T19:27:37+10:00
weight: 20
---

There is only one API route:  
https://charlesjlee.github.io/bitcoin-beacon/api/v1/random.json

and it returns data formatted like this:
```json
{
  "block_hash": "0000000000000000000ae92414a5d908254927edd7663cd1c52ddd66d503a024",
  "timestamp": "2020-09-10 15:10:47",
  "random_binary": "01101111100011101100110111111110",
  "random_int": 1871629822,
  "block": 647617
}
```

<br>
<!--
## future improvements
- add voting for requested features
- ability to query for historical numbers
- ability to set a future time or block and recieve a notification when that time or block occurs
- random numbers from other blockchains
- ability to specify a desired number range, e.g. want integer in [1,10]
- ability to map number ranges into categories
-->