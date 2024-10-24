{{ top_buttons() }}

# Creating a new benchmark task

This guide explains how to propose a new benchmark task to be included in RiverBench.

## Step 0: What is a benchmark task?

A benchmark task is a description of a concrete benchmarking procedure, for example: measuring deserialization throughput. Each task can be associated with several metrics, for example average throughput, 95th percentile throughput, and memory usage.

Each task belongs to one [benchmark category](categories.md). A benchmark category is a group of tasks that share the same requirements for datasets. For example, the `stream` category contains tasks that require a [grouped RDF stream](https://w3id.org/stax/dev/taxonomy/#grouped-rdf-stream) as input. Have a look at the [list of benchmark categories](https://w3id.org/riverbench/category) to see the existing categories.

## Step 1: Create a task proposal

Open a new task proposal in the RiverBench repository: <a href="https://github.com/RiverBench/RiverBench/issues/new?assignees=Ostrzyciel&labels=new+task&projects=&template=task-proposal.yml&title=Task+proposal%3A+%5BIDENTIFIER+HERE%5D" target="_blank" class="md-button md-button--primary rb-small-button" markdown>**:material-invoice-text-plus: New task proposal**</a>

Fill in the fields with the required information, using the instructions embedded in the form.

!!! note

    If you have trouble filling in any of the fields, you can leave them blank and ask [a maintainer](maintainers.md) for help.

!!! question "Does your task require more than just RDF data? SPARQL, anyone?"

    Attaching SPARQL queries, RML mappings, or other additional files to datasets is not supported yet. However, there are plans to implement this feature in the future. If you need this functionality, please **[leave a comment on this issue](https://github.com/RiverBench/RiverBench/issues/128)** to let us know.

## Step 2: Wait for approval

[RiverBench curators](maintainers.md) will be notified your request and will review the form and the task description. The curators may ask for additional information or clarifications.

## Step 3: Create a pull request

Once the task proposal is approved, you will be able to create a pull request to add the task to the category repository. The pull request should:

- Create a new subfolder under the `tasks` folder of the category repository. The name of the folder must match the task's identifier.
- Create a `metadata.ttl` file using [this template](https://github.com/RiverBench/category-template/blob/main/tasks/metadata.ttl) to the task's folder.
- Fill out the metadata in the `metadata.ttl` file using the information from the task proposal.
  - The description of the task in `dcterms:description` should be only enough to understand what the task is about. The details about metrics, specific procedures, etc., should be included in the task's documentation (see below).
  - Example of a completed `metadata.ttl` file: [stream-latency-end-to-end](https://github.com/RiverBench/category-stream/blob/main/tasks/stream-latency-end-to-end/metadata.ttl).
- Create a `index.md` file that will contain the task's elaborated description. Example: [stream-latency-end-to-end](https://github.com/RiverBench/category-stream/blob/main/tasks/stream-latency-end-to-end/index.md).
- (optional) Create any number of additional documentation pages for the task, for example, a page with the task's results. You can also include images in the task's folder.

## Step 4: Wait for merge

The admin will review your pull request (if they don't – remind them in the your task proposal with a comment). Once the pull request is approved, the task will be added to the category repository and will be available on the RiverBench website. :tada:

## See also

- [Creating a new dataset](creating-new-dataset.md)
- [Benchmark categories](categories.md)
- [Editing the documentation](editing-docs.md)
