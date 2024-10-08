{{ top_buttons() }}

# Working with benchmark categories

Benchmark categories are collections of benchmark tasks and profiles. Within a category, each task may be used with any of the profiles defined for that category. The profiles are collections of datasets, grouped by shared technical characteristics (e.g., stream type, whether RDF-star is used or not).

## Creating a benchmark category

- Pick a name for the category – it **must** be a single word, lowercase, without hyphens or underscores.
- [Create a new issue](https://github.com/RiverBench/RiverBench/issues/new/choose) (unless already present) in the issue tracker. In the issue specify what datasets and tasks will the category entail.
- [Create a new repository](https://github.com/new?template_name=category-template&template_owner=RiverBench) for the category named `category-[IDENTIFIER]`, using the [category-template](https://github.com/RiverBench/category-template) repo as the template.
- Fill out the `metadata.ttl` file for the category, apply any other changes and push them.
- Go to the admin's Personal Access Token settings.
    - Edit the "Dispatch: dataset-to-category update" token.
    - For the token, add access to the new category repo.
- Go to the [organization secret settings](https://github.com/organizations/RiverBench/settings/secrets/actions). For secrets `PAT_DOC_REPO_HOOKS` and `PAT_MAIN_REPO_HOOKS` add repository access for the new category repository.
- In the main repository:
    - Create a new branch for the proposal issue.
    - In the new branch run `git submodule add ../category-[ID] categories/[ID]`
    - Commit, push, and merge the branch to main.
- Re-run the CI in the category repo to check if it passes correctly.

## See also

- [Creating a new benchmark task](creating-new-task.md)
- [Editing the documentation](editing-docs.md)
- [Reporting benchmark results](reporting-results.md)
