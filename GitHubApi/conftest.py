from typing import Generator, List

import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect

from config import GITHUB_ACCESS_TOKEN
from config import GITHUB_USERNAME
from config import GITHUB_PROJECT_NUMBER



@pytest.fixture(scope="session")
def gh_context(
        playwright: Playwright
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}"
    }
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def gh_project_id(gh_context: APIRequestContext) -> str:
    data = {"query": "query{user(login: "
                     f"\"{GITHUB_USERNAME}\")"
                     " {projectV2(number: "f"{GITHUB_PROJECT_NUMBER}""){id}}}"}

    finding_project_id = gh_context.post("/graphql", data=data, )
    assert finding_project_id.ok

    project_id = finding_project_id.json()["data"]["user"]["projectV2"]["id"]

    return project_id
