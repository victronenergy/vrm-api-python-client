import unittest
import os

# What we are testing
from vrm import VRM_API

# Helpers
from datetime import datetime, timedelta, date

client = VRM_API(access_token='your access token', user_id='your user id')
print(client.get_user_sites())