#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration"""
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "7875854f-5d46-4aa8-b9bd-4b4cad15ec10") 
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "2:Q98]wT&&3*&DtDg=/U^GSK[?")
    APP_ID = os.environ.get("MicrosoftAppId", "") 
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    
    LUIS_APP_ID = os.environ.get("LuisAppId", "14445580-ac63-4dee-8408-71d066f97912")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "78583ade4d3d41efad110cdbb7018d52")
    #LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "francecentral.api.cognitive.microsoft.com")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "https://francecentral.api.cognitive.microsoft.com/")

    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "59f6eb7d-ae5f-4f72-80c4-c3fd8f7c05e1")
