# See: https://mkdocs-macros-plugin.readthedocs.io/en/latest

import os, logging


log = logging.getLogger('mkdocs')


def define_env(env):
    tag = os.environ.get('RELEASE_TAG', '')
    if not tag:
        log.warning('RELEASE_TAG environment variable not set. Defaulting to "dev".')
        tag = 'dev'


    @env.macro
    def nanopub_template_url():
        # URL to the latest version of the nanopublication template
        return 'https://w3id.org/np/RAuH8cdAJiFYj8WgiflflK8xwt0T6r4c791KFE2aEnI9o'
    

    @env.macro
    def report_results_url():
        return 'https://nanodash.petapico.org/publish?template=' + nanopub_template_url()


    @env.macro
    def top_buttons(edit_override = None):
        split = [s for s in env.page.url.split('/') if s]
        buttons = []
        version = tag.lstrip('v')
        purl = f'https://w3id.org/riverbench/v/{version}/{"/".join(split)}'
        buttons.append(
            f'[:material-link-variant: Permanent URL]({purl} "Link to the permanent URL of this resource.")'
        )
        if tag == 'dev':
            if edit_override:
                edit_url = edit_override
            else:
                edit_url = f'https://github.com/RiverBench/riverbench.github.io/edit/main/docs/{env.page.file.src_path}'
            buttons.append(
                f'**[:material-file-edit: Edit this page]({edit_url} "Edit this page\'s source in Markdown on GitHub.")**'
            )
            file_split = env.page.file.src_path.split('/')
            if file_split[0] == 'documentation':
                dir_part = ''
            else:
                dir_part = ('../' * (len(file_split) - 1)) + 'documentation/'
            buttons.append(
                f'[:material-help-circle:]({dir_part}editing-docs.md "Need help with editing?")'
            )
        else:
            buttons.append(
                f'<div markdown><abbr title="This page corresponds to a stable release of RiverBench, so it cannot ' +
                f"be edited. If you want to edit this page, go to the development version by selecting 'dev' from the " +
                f'version selector in the top navigation bar.">' +
                f':material-lock-check: Stable: {version}</abbr></div>'
            )

        buttons = [f'<div markdown>{b}</div>' for b in buttons]
        return f'<div markdown class="rb-top-buttons">{"".join(buttons)}</div>'
