# Dataset source format

This page describes the source format of datasets in RiverBench. This format is used only internally and is **different** to the [release format](dataset-release-format.md).

## Overall file structure

This file structure will be created for you when your repository is created by an admin using the [template](https://github.com/RiverBench/dataset-template).

* `.github/` – the directory with CI configuration needed to package and publish your dataset. You don't need to change anything there.
* `LICENSE` – specifies the license for the dataset.
* `metadata.ttl` – describes the dataset in a machine-readable manner. See the [metadata documentation](metadata.md) for more details.
* `README.md` – auto-generated from metadata.ttl. You don't need to touch it.

You can also add more files and directories (like `.gitignore`, etc.) to the repository.

## Source files

* Source files must be uploaded as a GitHub release to your repository, following [this guide](creating-new-dataset.md#step-3-upload-the-dataset-sources).
* There must be exactly one source file per dataset (either `source.tar.gz`).
* The source file must be a `.tar.gz` archive, with a structure, as outlined below.
* The archive can contain only directories (nesting is allowed) and stream element files.
* The file extension of the stream elements depends on the stream type. See subsections below for more details.
* The files must be named starting from `0000000000.Y`, and sequentially up to `X.Y`, where `X + 1` is the number of stream elements in the dataset, and Y is the file extension. All numbers must be zero-padded to exactly ten digits.
* **Important!** All files must be stored in the tar **sequentially in lexicographic order**. This is different to what the tar command usually does on Linux (order of files is random). See the [creating a source archive](#creating-source-archive) section below for more details.
* There are no special rules for grouping files into directories – but examples of what would work are presented below. It is recommended to have at most ~1000 files per directory to avoid issues with filesystems and file browsers.

**Example 1: flat file structure, [RDF dataset stream](https://w3id.org/stax/dev/taxonomy#rdf-dataset-stream), 431256 elements:**

```
- 0000000000.trig
- 0000000001.trig
- 0000000002.trig
- ...
- 0000431255.trig
```

**Example 2: files in directories, [RDF graph stream](https://w3id.org/stax/dev/taxonomy#rdf-graph-stream), 201900 elements:**

```
- 0000/
    - 0000000000.ttl
    - 0000000001.ttl
    - ...
    - 0000000999.ttl
- ...
- 0201/
    - 0000201000.ttl
    - 0000201001.ttl
    - ...
    - 0000201899.ttl
```

**Example 3: files in nested directories, [RDF graph stream](https://w3id.org/stax/dev/taxonomy#rdf-graph-stream), 201900 elements:**

```
- 00/
    - 00/
        - 0000000000.ttl
        - ...
        - 0000000099.ttl
    - 99/
        - 0000009900.ttl
        - ...
        - 0000009999.ttl
- ...
- 20/
    - ...
    - 18/
        - 0000201800.ttl
        - ...
        - 0000201899.ttl
```

### Creating a source archive

The stream element files must be stored in the source archive sequentially, so that the archive can be processed by the CI jobs in a streaming manner, speeding up packaging and validation.

Let's say you have a directory named "dataset" with .ttl files (possibly in nested directories) that you want to add to the archive. On Linux you can run:

``` sh
find dataset -type f | sort | tar -T - -czf source.tar.gz
```

You can then verify that the files were stored sequentially in the tar by running:

``` sh
tar -tzvf source.tar.gz
```

You should see a list of files in the archive, in lexicographic order.

### RDF dataset stream format

This format corresponds to the **[RDF dataset stream](https://w3id.org/stax/dev/taxonomy#rdf-dataset-stream)**, **[RDF named graph stream](https://w3id.org/stax/dev/taxonomy#rdf-named-graph-stream)**, and **[timestamped RDF named graph stream](https://w3id.org/stax/dev/taxonomy#timestamped-rdf-named-graph-stream)** stream types from [RDF-STaX](https://w3id.org/stax/dev/taxonomy/).

In the dataset stream format, every stream element is an RDF dataset, and every RDF dataset corresponds to exactly one file. The files must be in the RDF 1.1 TriG format, or in the TriG-star format, if the dataset uses RDF-star. The extensions of the files must be `.trig`. The files must be encoded in UTF-8.

!!! note

    The above format specification is meant to cover all valid [RDF 1.1 datasets](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-dataset). Because of this, a completely empty file is also a valid stream element.

**Example timestamped RDF named graph stream:** [citypulse-traffic-graphs](https://github.com/RiverBench/dataset-citypulse-traffic-graphs)

**Example RDF dataset stream:** [nanopubs](https://github.com/RiverBench/dataset-nanopubs)

### RDF graph stream format

This format corresponds to the **[RDF graph stream](https://w3id.org/stax/dev/taxonomy#rdf-graph-stream)** and **[RDF subject graph stream](https://w3id.org/stax/dev/taxonomy#rdf-subject-graph-stream)** stream types from [RDF-STaX](https://w3id.org/stax/dev/taxonomy/).

In the graph stream format, every stream element is an unnamed (default) RDF graph, and every RDF graph corresponds to exactly one file. The files must be in the RDF 1.1 Turtle format, or in the Turtle-star format, if the dataset uses RDF-star. The extensions of the files must be `.ttl`. The files must be encoded in UTF-8.

!!! note

    The above format specification is meant to cover all valid [RDF 1.1 graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). Because of this, a completely empty file is also a valid stream element.


**Example RDF subject graph stream:** [yago-annotated-facts](https://github.com/RiverBench/dataset-yago-annotated-facts)

**Example RDF graph stream:** [citypulse-traffic](https://github.com/RiverBench/dataset-citypulse-traffic)

## See also

- [Creating a new dataset](creating-new-dataset.md)
- [Dataset release format](dataset-release-format.md)
