# coding: utf-8

from ..gh_client import GhClient
import sys
import csv


class PrCommentsExporter():
    """
    リポジトリのPRのコメントを出力する
    """

    def __init__(self, repo):
        self.repo = repo
        self.gh = GhClient()

    def print_as_csv(self):
        """
        CSV形式で標準出力に出力する

        @see: https://docs.github.com/en/rest/reference/pulls#review-comments
        """

        fieldnames = ['id', 'url', 'body', 'user_name']
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)

        writer.writeheader()

        for comment in self.gh.fetch_pr_comments(self.repo):
            writer.writerow({
                'id': comment.id,
                'url': comment.html_url,
                'body': comment.body,
                'user_name': comment.user.login
            })
