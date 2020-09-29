"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

from click_didyoumean import DYMGroup


class CustomMultiGroup(DYMGroup):
    def group(self, *args, **kwargs):
        """Behaves the same as `click.Group.group()` except if passed
        a list of names, all after the first will be aliases for the first.
        """
        def decorator(f):
            aliased_group = []
            if isinstance(args[0], list):
                _args = [args[0][0]] + list(args[1:])
                for alias in args[0][1:]:
                    grp = super(CustomMultiGroup, self).group(
                        alias, *args[1:], **kwargs)(f)
                    grp.short_help = '[DEPRECATED: Use \'{}\']'.format(_args[0])
                    aliased_group.append(grp)
            else:
                _args = args
            grp = super(CustomMultiGroup, self).group(*_args, **kwargs)(f)
            for aliased in aliased_group:
                aliased.commands = grp.commands
            return grp
        return decorator
