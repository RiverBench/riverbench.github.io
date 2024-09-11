import logging, re
import mkdocs.plugins
from mkdocs.structure.pages import Page


log = logging.getLogger('mkdocs')


re_title = re.compile(r'^# (.+)$', re.MULTILINE)


# Resolves: https://github.com/RiverBench/RiverBench/issues/117
def on_page_markdown(markdown: str, page: Page, config, files) -> str:
    if page.file.src_path.endswith('index.md'):
        match = re_title.search(markdown)
        if match:
            title = match.group(1)
            # Don't fix dataset titles, they are fine as-is
            if not title.startswith('Dataset: '):
                log.info(f'Fixing title of {page.file.src_path} to "{title}"')
                page.title = title
        else:
            log.warning(f'Could not find title in {page.file.src_path}')
        
    return markdown
