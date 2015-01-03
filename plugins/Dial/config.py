import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Dial')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified themself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Dial', True)


Dial = conf.registerPlugin('Dial')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Dial, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
