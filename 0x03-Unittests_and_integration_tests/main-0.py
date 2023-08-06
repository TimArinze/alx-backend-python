#!/usr/bin/env python3
"""
checking client and how it works
"""
GithubOrgClient = __import__('client').GithubOrgClient
OrgClient = GithubOrgClient("TimArinze")

org = OrgClient.org
print(org)
