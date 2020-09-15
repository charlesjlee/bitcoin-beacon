---
title: 'faq'
date: 2019-02-11T19:27:37+10:00
weight: 10
---

### How are the random bits computed?
By applying an entropy extraction function to the bitwise $OR$ of the block header and the hash of the block header:

$$Beacon(t) = Ext_k(B_t||H(B_t))$$

The hash of the block header is included to make it impossible for malicious miners to exclusively try solutions that produce a certain beacon output. Since the hash of the header is unpredictable, malicious miners must mine normally: finding valid solutions, computing the beacon output, then deciding whether to withhold the block.

### Why 32 bits?
From 68 bits of min-entropy, originating from the current difficulty $d$, we can extract 32 uniform bits. This is summarized in **Table 1** from the paper:

![Table 1](/img/capture.png)

### How much would it cost to attack this beacon?
An attack on the beacon is equivalent to manipulating the block hash of the most recent block. Malicious miners can withhold valid blocks if they would result in an unfavorable beacon output. The paper models a *strong bribing attacker* able to successfully "pay any miner exactly $B$ [the block reward] to suppress a valid block whenever the attacker desires”.

The cost of attack depends on how the beacon is being used. If we let $p$ be the probability that the attacker wins a lottery with value $W$ by doing nothing, then:

$$(earnings\ from\ manipulating\ beacon) > (expected\ earnings\ if\ do\ nothing)$$
$$(lottery\ stake) - (cost\ to\ manipulate\ beacon) > (expected\ earnings\ if\ do\ nothing)$$
$$W - {(1-p) \over p} > pW$$
$$W > {1 \over p}$$

So in the case of a lottery decided by a single bit, i.e. $p=1/2$, the lottery is manipulation-resistant against an attacker who has less than $2B$, currently {{< blockreward >}}, at stake.

### Why not use transactions as sources of entropy?
> for the purposes of a beacon which is unpredictable we care only about entropy conditional on all public information just prior to the moment the block is first announced. This eliminates most of the entropy from transactions, as they are nearly all published in transaction pools prior to being included in a block.

### How is this site built?
The front-end is Hugo on GitHub Pages with GitHub Actions automating the deployment from `master` to `gh-pages`. The back-end is a scheduled GitHub Action that grabs the latest block from [blockchain.info](https://blockchain.info/q/) and re-writes `data/random.json` every 5 minutes.

The underlying code is here:  
https://github.com/charlesjlee/bitcoin-beacon

### Why should I use this instead of random.org, NIST, or drand?
Because you believe in the great dream of liberating the global financial system from the clutches of central banks and want to pump the price of BTC to the moon so we can all retire.

### I don't like your code and don't trust you
I was a Certified Bitcoin Professional back in 2017 and went on to work at a blockchain startup. If you still don't accept my street cred then look [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ).