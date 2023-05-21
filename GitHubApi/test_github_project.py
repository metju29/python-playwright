import json

from playwright.sync_api import APIRequestContext, expect
from typing import List


def test_add_draft_issue(
        gh_context: APIRequestContext,
        gh_project_id: List[str]) -> None:

    data = {"query": "mutation {addProjectV2DraftIssue(input: {projectId: "
                     f"\"{gh_project_id}\""
                     " title: \"New issue\" body: \"Body of new issue\"}) {projectItem {id}}}"}

    add_draft_issue = gh_context.post("/graphql", data=data)
    expect(add_draft_issue).to_be_ok()

    # with open('add_draft_issue.json', 'w', encoding='utf-8') as f:
    #     json.dump(add_draft_issue.json(), f, ensure_ascii=False, indent=4)






