from github import Github
from os import getenv


class GhClient():

    def __init__(self):
        self.client = Github(getenv('GH_TOKEN'))

    def fetch_pr_comments(self, repo):
        """
        リポジトリへのPRコメントの一覧を取得する
        """
        repo = self.client.get_repo(repo)
        return repo.get_pulls_comments()

    def fetch_pulls(self, repo):
        """
        リポジトリのPRの一覧を取得する
        """
        repo = self.client.get_repo(repo)
        return repo.get_pulls()
