from mypy.plugin import Plugin
from typing import Type


class MailJetPlugin(Plugin):
    def get_type_analyze_hook(self, fullname: str):
        # see explanation below
        pass


def plugin(version: str) -> Type[MailJetPlugin]:
    # ignore version argument if the plugin works with all mypy versions.
    return MailJetPlugin
