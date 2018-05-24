#!/usr/bin/env python2.7


import json


def _escape(text):
    return text.replace('.', r'\.')


def _route(obj, key_so_far, items):
    if isinstance(obj, list):
        return _parse_list(obj, key_so_far, items)
    elif isinstance(obj, dict):
        return _parse_dict(obj, key_so_far, items)
    items.append((str(obj), key_so_far))


def _make_key(a, b):
    key = '.'.join([a, _escape(str(b))])
    return key[1:] if key.startswith('.') else key


def _parse_list(obj, key_so_far, items):
    assert isinstance(obj, list)
    for idx, item in enumerate(obj):
        _route(item, _make_key(key_so_far, idx), items)


def _parse_dict(obj, key_so_far, items):
    assert isinstance(obj, dict)
    for k, v in obj.iteritems():
        _route(v, _make_key(key_so_far, k), items)


def flatten_json(json_string):
    items = []
    _route(json.loads(json_string), key_so_far='', items=items)
    return {key: v for v, key in items}
