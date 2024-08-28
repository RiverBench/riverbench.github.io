{{ top_buttons() }}

# Using RiverBench – quick start guide

RiverBench collects three types of resources:

- **Benchmark tasks** – descriptions of benchmark procedures and metrics.
- **[Datasets](../datasets/index.md)** – diverse, real-life datasets that can be used for a variety of tasks.
- **Profiles** – collections of datasets that share common technical characteristics. For example: datasets that contain only RDF triples.

## To perform a benchmark...

1. **Make sure you are using a stable release of RiverBench** – do _not_ use the "dev" version of RiverBench for benchmarking, as it can change at any moment. You can find the version you are viewing in the top navigation bar. By using a stable release, you ensure that your results are reproducible.
    - Go to the [latest stable release of RiverBench](https://w3id.org/riverbench/v/stable/).
    - You can also find the list of all available releases [here](../releases.md).
2. **Find a benchmark task** – see the [list of benchmark categories](../categories/index.md) and browse the available tasks. The task's description will explain how to set up the benchmark and measure the results. You will also find there the list of previously reported results for this task.
    - If someone has already reported the results for this task, they may have published their benchmark code, which may be useful. Check the task's "Results" subpage for more information.
3. **Choose a profile** – within the same category as the task you've picked, you can choose any profile that fits your needs. For example, if you've selected the [`flat-rdf-store-loading`](../tasks/flat-rdf-store-loading/index.md) task, you can use any profile with a name starting with `flat-`, such as [`flat-triples`](../profiles/flat-triples.md).
    - The profiles vary in the type of data they contain (e.g., triples vs quads) and their usage of RDF features (e.g., if they use RDF-star or not).
4. **Download the datasets** – each profile page has a convenient list of download links for all datasets in that profile.
    - You can also view each [dataset's documentation](../datasets/index.md) to learn more about its origin, use cases, size, and other technical characteristics. You can also preview the dataset's contents.
    - The dataset's documentation page also includes useful statistics (e.g., number of subjects/predicates/objects, unique IRIs, etc.) that may be useful for analyzing and discussing your results.
    - Read more about the [available dataset formats](dataset-release-format.md).
5. **Run the benchmark**.
6. **Report your results** – see the dedicated guide below.



## Reporting your benchmark – best practices

Reproducibility is key in benchmarking. Here we've collected a few best practices for reporting your benchmark results, so that others can easily understand and reproduce your work.

Most importantly, **always refer to a stable release of RiverBench** – if you link to the "dev" version of RiverBench, others will have no way of knowing which version of the task or dataset you really used.


### Reporting RiverBench usage in your paper/report

You should at least state the following information: the benchmark task identifier (with version) and the profile identifier (with version).

!!! example
    
    For example, you can write: 
    
    > We used the `flat-rdf-store-loading` task from RiverBench, version 2.1.0, with the `flat-triples` profile, version 2.1.0.

    Feel free to modify the wording to your liking... the only important part are the identifiers and versions.

If you can use links in your text, we recommend you link to the task and profile pages on the RiverBench website. You should only use permanent URLs, which are guaranteed to never change. The permanent URL links can be found in the top-right corner of every page – [read more about them](metadata.md#accessing-metadata).

!!! example

    The permanent URL for the `flat-rdf-store-loading` task, version 2.1.0 is: `https://w3id.org/riverbench/v/2.1.0/tasks/flat-rdf-store-loading`
    <br>For the `flat-triples` profile, version 2.1.0, it is: `https://w3id.org/riverbench/v/2.1.0/profiles/flat-triples`

    You can link to them in LaTeX like this:

    ``` { .latex .rb-wrap-code title="LaTeX" } 
    We used the \href{https://w3id.org/riverbench/v/2.1.0/tasks/flat-rdf-store-loading}{flat-rdf-store-loading} task from RiverBench, version 2.1.0, with the \href{https://w3id.org/riverbench/v/2.1.0/profiles/flat-triples}{flat-triples} profile, version 2.1.0.
    ```

    Which will look like this:

    > We used the [flat-rdf-store-loading](https://w3id.org/riverbench/v/2.1.0/tasks/flat-rdf-store-loading) task from RiverBench, version 2.1.0, with the [flat-triples](https://w3id.org/riverbench/v/2.1.0/profiles/flat-triples) profile, version 2.1.0.
    

You can also optionally link to the individual datasets that you used.

If you use RiverBench in your research, **we kindly ask you to [cite it using the canonical citation](licensing.md#attribution-citation)**.


### Sharing your benchmark run on the RiverBench website

We highly encourage you to share your benchmark results with the community in a structured manner. This way, your benchmark run [will be listed on the RiverBench website](../results/index.md) (along with appropriate citation), and others will be able to easily find your paper/report, benchmark code, and results.

<div style="text-align: center" markdown>[:material-star-plus: Report your benchmark results](../documentation/reporting-results.md){ .md-button }</div>


### Model example

You can use this paper as a model example of how to report your benchmark results: [https://doi.org/10.48550/arXiv.2406.16412](https://doi.org/10.48550/arXiv.2406.16412). Of course, you don't have to go into as much detail as this paper did – just stating the profile and task really is enough.

This paper also reported its results in a structured manner, using the mechanism described **[here](reporting-results.md)**. You can find the original nanopublication with the results [here](https://w3id.org/np/RAyFZlqsYQ_w-j5cah_gI8WBIZxiVSM4ocWHD_tnyjLxs), and the results being rendered on the RiverBench website [here](../tasks/flat-rdf-store-loading/results.md).


## I can't find the task/dataset I need...

You are welcome to contribute new tasks or datasets to RiverBench! You can find more information on how to do that in the **[contributing guide](contribute.md)**.

You can also [propose changes](editing-docs.md) to any of the existing tasks, documentation pages, and metadata files.

## See also

- [Reporting benchmark results](reporting-results.md)
- [Licensing and citation](licensing.md)
- [Dataset release format](dataset-release-format.md)
- [Metadata of datasets, profiles, and more](metadata.md)
- [Contributing to RiverBench](contribute.md)
