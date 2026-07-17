import trafilatura


def extract_article(url: str) -> str:
    """
    Download and extract the main article content.
    """

    try:

        downloaded = trafilatura.fetch_url(url)

        if not downloaded:
            return ""

        content = trafilatura.extract(
            downloaded,
            include_comments=False,
            include_tables=False,
        )

        return content or ""

    except Exception:

        return ""