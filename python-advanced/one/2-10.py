def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

is_not_empty = filter(lambda s: s and len(s.strip()) > 0 ,['test', None, '', 'str', '  ', 'END'])

print is_not_empty