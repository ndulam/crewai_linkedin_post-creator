from bs4 import BeautifulSoup


def parse_html_content(page_source: str):
    """
    Parses the HTML from the LinkedIn's profile and returns a collection of LinkedIn posts. We don't need
    all of them, just a few, since we can get the "writing-style" very easily.

    Args:
        page_source (str): The HTML content

    Returns:
        list: A list of div containers representing a collection of LinkedIn posts
    """
    linkedin_soup = BeautifulSoup(page_source.encode("utf-8"), "lxml")

    containers = linkedin_soup.find_all("div", {"class": "feed-shared-update-v2"})
    containers = [container for container in containers if 'activity' in container.get('data-urn', '')]
    return containers


def get_post_content(container, selector, attributes):
    """
    Gets the content of a LinkedIn post container.

    Args:
        container (Tag): The div container
        selector (str): The selector
        attributes (dict): Attributes to be fetched

    Returns:
        str: The post content
    """
    try:
        element = container.find(selector, attributes)
        if element:
            return element.text.strip()
    except Exception as e:
        print(e)
    return ""


def get_linkedin_posts(page_source: str):
    """
    Extracts LinkedIn posts from the HTML content.

    Args:
        page_source (str): The HTML content

    Returns:
        list: A list of post contents
    """
    containers = parse_html_content(page_source)
    posts = []

    for container in containers:
        post_content = get_post_content(container, "div", {"class": "update-components-text"})
        posts.append(post_content)

    return posts