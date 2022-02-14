#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration"""

    ############## Azure Bot Service ###############
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "") 
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    ############## LUIS Service ###############
    LUIS_APP_ID = os.environ.get("LuisAppId", "14445580-ac63-4dee-8408-71d066f97912")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "78583ade4d3d41efad110cdbb7018d52")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://francecentral.api.cognitive.microsoft.com/")

    ############## App Insights Service ###############
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "59f6eb7d-ae5f-4f72-80c4-c3fd8f7c05e1")