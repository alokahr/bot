#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "aa50a6bb-a6c1-48e5-8f68-ed925e13c538")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "Bi08Q~9PLNObF2EOWgdWtqXunrsMLnopeUpAqcnd")
