""" Cache.py

This module is a simple cache using a dict.
"""
import datetime


_SIMPLE_CACHE = {}
_DAY = None


def clean_cache():
    _SIMPLE_CACHE.clear()


def set_cache(data: dict):
    _handle_cache_per_day()
    _SIMPLE_CACHE[data['ticket']] = data


def get_item_cached(ticket: str) -> dict:
    _handle_cache_per_day()
    return _SIMPLE_CACHE.get(ticket)


def _handle_cache_per_day():
    global _DAY

    now = datetime.datetime.now()
    if not _DAY:
        _DAY = now.day

    if now.day > _DAY:
        _DAY = now.day
        clean_cache()
