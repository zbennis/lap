#!/bin/sh

sudo kill -9 $(sudo lsof -t -i:1883)1