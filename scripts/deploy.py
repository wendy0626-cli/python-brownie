#!/usr/bin/python3

import os
from brownie import FooBar, accounts, network, config


def main():
    print("Deploying FooBar")
    print("network.show_active-->", network.show_active())
    dev = accounts.add(config["wallets"]["from_key"])
    print("dev-->", dev)
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False
    # FooBar.deploy({"from": dev, "gas": 63000}, publish_source=publish_source)
    FooBar.deploy({"gas": "0x666f6f", "from": dev}, publish_source=True)
