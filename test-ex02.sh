#!/bin/bash

jq -c . test-data/ex02.json | python json2.py
