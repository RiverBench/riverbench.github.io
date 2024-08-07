# Creating a new dataset

This guide explains step-by-step how to propose a new dataset for inclusion in RiverBench. You only need to prepare the dataset and its metadata – the rest of the process will be carried out by a RiverBench admin and automated scripts.

## Step 0: Check the requirements

Before you start, have a look at the [requirements for new datasets](contribute.md#contributing-datasets). If your dataset does not meet these requirements, it will not be accepted.

## Step 1: Create a dataset proposal

1. Open a new dataset proposal in the RiverBench repository: **[click HERE](https://github.com/RiverBench/RiverBench/issues/new?assignees=Ostrzyciel&labels=new+dataset&projects=&template=dataset-proposal.md&title=Dataset+proposal%3A+%5BIDENTIFIER+HERE%5D)**.
2. Fill in the form with the required information (see below).

!!! note

    If you have trouble filling in any of the fields, you can leave them blank and ask the maintainer for help.

### General information

- **Description of the dataset:** Provide a brief and informative description of the dataset, including its content, structure, and purpose.
- **Value brought by the dataset:** Explain the significance of the dataset and why it should be included in RiverBench. For example, the dataset might cover a new domain, or it may introduce technical features not found in other datasets.
- **Proposed identifier:** Suggest a unique identifier for the dataset using only lowercase latin letters, digits, and dashes (-).
- **Link to the source of the dataset:** Provide a link to the dataset's source or repository.
- **License of the dataset:** Specify the dataset's license by providing an SPDX license link from [this list](https://spdx.org/licenses/). Ensure that the chosen license allows for free use and does not prohibit commercial usage or modification. Examples of accepted licenses include [CC Zero](https://spdx.org/licenses/CC0-1.0.html), [CC BY](https://spdx.org/licenses/CC-BY-4.0.html), [CC BY-SA](https://spdx.org/licenses/CC-BY-SA-4.0.html), and [ODbL](https://spdx.org/licenses/ODbL-1.0.html).
- **Additional licensing notes (if any):** Mention any licensing irregularities or special clauses related to the dataset, such as a different license for a part of the dataset or restrictions on its use.
- **Creator(s):** List the names of the dataset's original creators.

### Technical information

- **Stream type:** Specify the type of the RDF stream in the dataset, using the [RDF Stream Taxonomy (RDF-STaX)](https://w3id.org/stax).
- **Stream element count:** Provide the total number of stream elements in the dataset (stream length). This corresponds to the number of files in the dataset's source archive (see below).
- **How were the stream elements split:** Explain the method used to split the stream into elements, e.g., by time, by topic, other.
- **Uses RDF-star:** Specify if the dataset uses RDF-star (yes or no).
- **Uses generalized triples:** Indicate if the dataset employs generalized triples (yes or no).
- **Uses generalized datasets:** State if the dataset utilizes generalized RDF datasets (yes or no).
- **Other technical notes (if any):** Include any additional technical information or notes relevant to the dataset.

## Step 2: Wait for approval

An administrator will be notified your request and will review the form and the dataset. The administrator may ask for additional information or clarifications. Once reviewed, the admin will create a new repository for you and give you access to it.

## Step 3: Upload the dataset sources

1. Create a source archive by following the [guide on preparing a source archive](dataset-source-format.md).
2. Access the repository created for your dataset and click on "Releases" in the right sidebar.
3. Click on the "Create a new release" button to start the process of creating a new release for your dataset.
4. Fill in the following fields for the new release:
    - Input "source" as the tag for the release.
    - Enter "Source" as the release name.
    - Check the "Set as a pre-release" option (it's below the large text field).
    - Leave other options unchanged.
5. Upload the prepared source archive (`source.tar.gz`) by dragging and dropping the file into the designated area.
6. Once the source archive is attached, click on the "Publish release" button to finalize the upload.

## Step 4: Fill out the metadata

1. Open the `metadata.ttl` file in your new dataset repository.
2. Use the information from the issue template you filled out earlier to complete the required fields in the `metadata.ttl` file. Replace the placeholder text with the appropriate information from the template.
    - You can have a look at the metadata of [other datasets](../datasets/index.md) for reference.
    - In the `dcterms:description` field and other free-text fields you can use Markdown formatting.
    - For `dcat:theme` use concepts from the [EuroVoc thesaurus](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://eurovoc.europa.eu/100141). Use only elements of type "Concept" (without a number in their name), not "Concept scheme" or "Domain concept".
3. Open the `LICENSE` file and replace the placeholder text with the license of the dataset. You can find commonly used templates [here](https://github.com/licenses/license-templates/tree/master/templates).
4. Save your changes and commit to the main branch.
5. Inform the administrator in your issue that you have completed the metadata for your dataset. The admin will then finalize adding the dataset to the suite and provide any necessary assistance.

----

## Instructions for admins

- Review the issue template – make sure all required information is provided.
- [Create a new repository](https://github.com/organizations/RiverBench/repositories/new) for the dataset with name `dataset-[IDENTIFIER]`. In the repository settings:
  - Use the `RiverBench/dataset-template` repository as the template.
  - Mark the repo as public.
- Add the dataset maintainer as a collaborator to the repository in repo settings.
- Reply in the issue to the maintainer with the link to the repository and a link to step 3 of this guide.
- After the maintainer completes steps 3 and 4, check if the CI passes correctly up to the dataset and documentation update steps (these should fail). If not, try to fix the issue.
- Go to the [organization secret settings](https://github.com/organizations/RiverBench/settings/secrets/actions). For secrets `PAT_DOC_REPO_HOOKS`, `PAT_MAIN_REPO_HOOKS`, and `PAT_DATASET_CAT_REPO_HOOKS` add repository access for the new dataset repository.
- In [Zenodo settings](https://zenodo.org/account/settings/github/) enable the new repository.
- Create a new branch in the main repo (RiverBench/RiverBench) for the proposal issue.
- In the new branch, run `git submodule add ../dataset-[ID] datasets/[ID]`.
- Commit and push changes to GitHub.
- Create a pull request for the branch and merge it to main.
- Re-run the CI in the dataset repo and check if the dataset and documentation update steps pass correctly.
- After all CI finishes check if the [dataset list](../datasets/index.md) and profiles were updated correctly. Check the dataset's documentation page for any obvious issues.

## See also

- [Creating a new benchmark task](creating-new-task.md)
- [Editing the documentation](editing-docs.md)
