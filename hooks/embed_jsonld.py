import logging, os
import mkdocs.plugins
from mkdocs.structure.pages import Page


log = logging.getLogger('mkdocs')


# Embeds a JSON-LD snippet into the head of a page
# Issue: https://github.com/RiverBench/RiverBench/issues/148
def on_post_page(html: str, page: Page, config) -> str:
    embed_path = 'docs/' + page.file.src_path.replace('.md', '_embed.jsonld')
    if os.path.exists(embed_path):
        log.info(f'Embedding {embed_path} into {page.file.src_path}')
        with open(embed_path) as f:
            embed = f.read()
            html = html.replace('</head>', f'<script type="application/ld+json">{embed}</script></head>')
    return html
