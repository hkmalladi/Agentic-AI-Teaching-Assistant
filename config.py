"""
Configuration for AI Teaching Assistant Tutorial

This file contains all the configuration needed to connect to Azure OpenAI.
You need to update these values with your own Azure OpenAI credentials.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

# ============================================================================
# AZURE OPENAI CONFIGURATION
# ============================================================================

# Your Azure OpenAI endpoint URL
# Example: "https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_ENDPOINT = os.getenv(
    "AZURE_OPENAI_ENDPOINT",
    ""
)

# Your Azure OpenAI API key
# Find this in the Azure Portal under your OpenAI resource
AZURE_OPENAI_API_KEY = os.getenv(
    "AZURE_OPENAI_API_KEY",
    ""
)

# API version to use
# This determines which features are available
AZURE_OPENAI_API_VERSION = os.getenv(
    "AZURE_OPENAI_API_VERSION",
    "2024-12-01-preview"
)

# Your GPT-4 deployment name
# This is the name you gave your deployment in Azure
GPT4_DEPLOYMENT_NAME = os.getenv(
    "GPT4_DEPLOYMENT_NAME",
    ""
)

# ============================================================================
# VALIDATION
# ============================================================================

# Check if credentials are configured
if not AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_ENDPOINT == "your-endpoint-here":
    print("⚠️  WARNING: Azure OpenAI endpoint not configured!")
    print("   Please update AZURE_OPENAI_ENDPOINT in config.py")
    print()

if not AZURE_OPENAI_API_KEY or AZURE_OPENAI_API_KEY == "your-api-key-here":
    print("⚠️  WARNING: Azure OpenAI API key not configured!")
    print("   Please update AZURE_OPENAI_API_KEY in config.py")
    print()

# ============================================================================
# HOW TO GET YOUR CREDENTIALS
# ============================================================================
"""
To get your Azure OpenAI credentials:

1. Go to the Azure Portal (https://portal.azure.com)
2. Navigate to your Azure OpenAI resource
3. Click on "Keys and Endpoint" in the left menu
4. Copy the following:
   - Endpoint URL → AZURE_OPENAI_ENDPOINT
   - Key 1 or Key 2 → AZURE_OPENAI_API_KEY
5. Go to "Model deployments" to find your deployment name
   - Copy the deployment name → GPT4_DEPLOYMENT_NAME

Then update the values above or create a .env file with:
    AZURE_OPENAI_ENDPOINT=your-endpoint
    AZURE_OPENAI_API_KEY=your-key
    GPT4_DEPLOYMENT_NAME=your-deployment-name
"""

