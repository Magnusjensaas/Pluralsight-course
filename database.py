#!/usr/bin/env python

class Database:

    def __init__(self, path):
        with open(path, "r") as handle:
            import json
            self.data = json.load(handle)

            # import yaml
            # self.data = yaml.safe_load(handle)

            # import xmltodict
            # self.data = xmltodict.parse(handle.read())["root"]

    def balance(self, acct_id):
        acct = self.data.get(acct_id)
        if acct:
            bal = float(acct["due"]) - float(acct["paid"])
            return f"US$ {bal:.2f}"
        return None
