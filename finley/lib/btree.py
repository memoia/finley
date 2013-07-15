import collections

from lists import first, rest
from const import DIT, DAH


class Node(collections.MutableMapping):

    def __init__(self, *args, **kwargs):
        self._keys = ('data', 'value', 'left', 'right')
        self._struct = dict((k, None) for k in self._keys)
        if args and isinstance(args[0], basestring):
            kwargs['data'] = args[0]
            self.update(dict(**kwargs))
        else:
            self.update(dict(*args, **kwargs))

    @property
    def left(self):
        return self['left']

    @left.setter
    def left(self, val):
        self['left'] = val

    @left.deleter
    def left(self):
        del self['left']

    @property
    def right(self):
        return self['right']

    @right.setter
    def right(self, val):
        self['right'] = val

    @right.deleter
    def right(self):
        del self['right']

    @property
    def value(self):
        return self['value']

    @value.setter
    def value(self, val):
        self['value'] = val

    @value.deleter
    def value(self):
        del self['value']

    @property
    def data(self):
        return self['data']

    @data.setter
    def data(self, val):
        self['data'] = val

    @data.deleter
    def data(self):
        del self['data']

    def __unicode__(self):
        return unicode(self.value)

    __str__ = __unicode__

    def __repr__(self):
        return unicode('<{0}/{1} "{2}" ({3}, {4})>'.format(
                        self.__class__.__name__,
                        self.get('value'),
                        self.get('data'),
                        self.get('left'),
                        self.get('right')))

    def __getitem__(self, key):
        return self._struct[key]

    def __delitem__(self, key):
        self._struct[key] = None

    def __setitem__(self, key, val):
        if key not in self._keys:
            raise KeyError('{0} not allowed'.format(key))
        if (key in ('left', 'right') and
                not (val is None or isinstance(val, self.__class__))):
            raise ValueError('{0} not allowed'.format(val))
        elif key in ('data', 'value'):
            val = unicode(val)
        self._struct[key] = val

    def __iter__(self):
        return iter(self._struct)

    def __len__(self):
        return len(self._struct)

    def find(self, code_seq):
        step = first(code_seq)
        if not step:
            return self.data
        elif step == DAH and self.left:
            return self.left.find(rest(code_seq))
        elif step == DIT and self.right:
            return self.right.find(rest(code_seq))
        return None
