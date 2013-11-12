# -*- encoding: utf-8 -*-
from abjad.tools import stringtools
from abjad.tools.lilypondproxytools.LilyPondGrobProxy import LilyPondGrobProxy


class LilyPondGrobProxyContextWrapper(object):
    r'''Context wrapper for LilyPond grob overrides.
    '''

    ### SPECIAL METHODS ###

    def __getattr__(self, name):
        from abjad import ly
        try:
            return vars(self)[name]
        except KeyError:
            cased_name = stringtools.snake_case_to_upper_camel_case(name)
            if cased_name in ly.grob_interfaces:
                vars(self)[name] = LilyPondGrobProxy()
                return vars(self)[name]
            else:
                message = 'object can have only'
                message += ' LilyPond grob attributes: {!r}.'
                message = message.format(type(self).__name__)
                raise AttributeError(message)

    def __repr__(self):
        return '{}()'.format(type(self).__name__)
