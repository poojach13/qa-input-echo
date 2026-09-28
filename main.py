"""QA fixture for PLT-4621: read the run's input and report it.

Logs what it received (so the test works even if step output is not displayed, PLT-4786),
then returns it. No network, no model, no third-party dependencies.
"""
import logging

from trase_os_sdk.sandbox import NoInputError, read_input

log = logging.getLogger("qa-input-echo")


def run():
    try:
        data = read_input()
    except NoInputError:
        data = None
    log.info("QA_INPUT_RECEIVED %r", data)
    text = ""
    if isinstance(data, dict):
        text = data.get("text") or data.get("user_message") or ""
    elif isinstance(data, str):
        text = data
    result = {"shout": str(text).upper(), "received": data}
    log.info("QA_RESULT %s", result)
    return result
