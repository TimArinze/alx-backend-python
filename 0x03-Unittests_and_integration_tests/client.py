#!/usr/bin/env python3
"""A github org client
"""

from typing import (
        List,
        Dict,
        )
from utils import (
        get_json,
        access_nested_map,
        memoize,
        )


class GithubOrgClient:
    """A Github org client"""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Init method of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Public repos URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Memoize repos
