#!/usr/bin/env python
# coding=utf-8

import requests
from typing import (
    Dict,
    Tuple
)


class Config(object):
    def __init__(self, version: str = None, api_url: str = None): ...

    def __getitem__(self, key: str) -> Tuple[str, Dict[str, str]]: ...


class Endpoint(object):
    def __init__(self, url: str, headers: Dict[str, str], auth: str, action: str = None) -> None: ...

    def __doc__(self) -> str: ... # type: ignore

    def _get(self, filters: Dict[str, str] = None, action_id: str = None, id: int = None, **kwargs) -> requests.Response: ...

    def get_many(self, filters: Dict[str, str] = None, action_id: str = None, **kwargs) -> requests.Response: ...

    def get(self, id: int = None, filters: Dict[str, str] = None, action_id: str = None, **kwargs) -> requests.Response: ...

    def create(self, data: Dict[str, str] = None, filters: Dict[str, str] = None, id: int = None, action_id: str = None, **kwargs) -> requests.Response: ...

    def update(self, id: int, data: Dict[str, str], filters: Dict[str, str] = None, action_id=None, **kwargs) -> requests.Response: ...

    def delete(self, id: int, **kwargs) -> requests.Response: ...


class Client(object):
    def __init__(self, auth: str = None, **kwargs): ...

    def __getattr__(self, name: str): ...


def api_call(
        auth: str,
        method: str,
        url: str,
        headers: Dict[str, str],
        data: str = None,
        filters: Dict[str, str] = None,
        resource_id: int = None,
        timeout: int = 60,
        debug: bool = False,
        action: str = None,
        action_id: str = None,
        **kwargs
    ) -> requests.Response: ...


def build_headers(resource: str, action: str, extra_headers: Dict[str, str] = None) -> Dict[str, str]: ...


def build_url(url: str, method: str, action: str = None, resource_id: int = None, action_id: str = None) -> str: ...


def parse_response(response: requests.Response, debug: bool = False) -> Dict[str, str]: ...
