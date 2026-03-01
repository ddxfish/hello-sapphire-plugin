# Hello Sapphire — test plugin tool
"""A simple tool that returns what Sapphire is, based on the user's setting."""

import logging

logger = logging.getLogger(__name__)

ENABLED = True
EMOJI = '\U0001f48e'
AVAILABLE_FUNCTIONS = ['sapphire_test_plugin']

TOOLS = [
    {
        "type": "function",
        "is_local": True,
        "function": {
            "name": "sapphire_test_plugin",
            "description": "Returns what Sapphire is. Call this when someone asks 'what is Sapphire?' or wants to test the hello plugin.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
]


def _get_setting():
    try:
        from core.plugin_loader import plugin_loader
        return plugin_loader.get_plugin_settings('hello-sapphire').get('sapphire_is', 'beautiful')
    except Exception:
        return 'beautiful'


def execute(function_name, arguments, config):
    if function_name == "sapphire_test_plugin":
        value = _get_setting()
        return f"Sapphire is {value}.", True
    return f"Unknown function: {function_name}", False
