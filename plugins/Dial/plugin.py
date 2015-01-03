import re
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Dial')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x


def normalize_number(text):
    return re.sub("[+\- ]", "", text)


class Dial(callbacks.Plugin):
    """Each instance represents one load of the supybot plugin.
    """
    def __init__(self, irc):
        super(Dial, self).__init__(irc)

    def dial(self, irc, msg, args):
        """
        """
        arg = " ".join(args).strip()
        arg = normalize_number(arg)
        if not arg:
            formatted = "Give a phone number to dial"
        elif not re.match("^\d{10,11}\Z", arg):
            formatted = "Give a valid phone number to dial (10-11 digits)"
        else:
            formatted = "Would queue a dial to {0}".format(arg)
        irc.reply(formatted)


Class = Dial
