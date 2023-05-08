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
* There must be exactly one source file per dataset (either `triples.tar.gz`, `graphs.tar.gz`, or `quads.tar.gz`).
* The source file must be a `.tar.gz` archive, with a structure, as outlined below.
* The archive can contain only directories (nesting is allowed) and stream element files.
* The file extension of the stream elements depends on the stream type. See subsections below for more details.
* The files must be named starting from `0000000000.Y`, and sequentially up to `X.Y`, where `X + 1` is the number of stream elements in the dataset, and Y is the file extension. All numbers must be zero-padded to exactly ten digits.
* **Important!** All files must be stored in the tar **sequentially in lexicographic order**. This is different to what the tar command usually does on Linux (order of files is random). See the [creating a source archive](#creating-source-archive) section below for more details.
* There are no special rules for grouping files into directories – but examples of what would work are presented below. It is recommended to have at most ~1000 files per directory to avoid issues with filesystems and file browsers.

**Example 1: flat file structure, graph stream, 431256 elements:**

```
- 0000000000.trig
- 0000000001.trig
- 0000000002.trig
- ...
- 0000431255.trig
```

**Example 2: files in directories, triple stream, 201900 elements:**

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

**Example 3: files in nested directories, triple stream, 201900 elements:**

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
find dataset -type f | sort | tar -T - -czf triples.tar.gz
```

You can then verify that the files were stored sequentially in the tar by running:
``` sh
tar -tzvf triples.tar.gz
```

You should see a list of files in the archive, in lexicographic order.

### Graph stream format

In the graph stream format, every stream element is an RDF dataset, and every RDF dataset corresponds to exactly one file. In the dataset there must be exactly one named RDF graph pair `<n, G>`, where `G` is an RDF graph, and `n` is the graph name. Apart from graph `G`, the RDF dataset may contain any number of triples in the default graph. If the stream is a timestamped stream, then the default graph must include exactly one timestamp triple `<n, p, t>`, where `p` is the designated timestamp property, as specified in metadata.

!!! note
    The above format specification is meant to be compatible with the draft [RSP Data model](https://streamreasoning.org/RSP-QL/Abstract%20Syntax%20and%20Semantics%20Document/), when the stream is timestamped.*

The files must be in the RDF 1.1 TriG format, or in the TriG-star format, if the dataset uses RDF-star. The extensions of the files must be `.trig`. The files must be encoded in UTF-8.

**Example graphs dataset:** [citypulse-traffic-graphs](https://github.com/RiverBench/dataset-citypulse-traffic-graphs)

### Quad stream format

In the quad stream format, every stream element is an RDF dataset, and every RDF dataset corresponds to exactly one file. In the dataset there can be zero or more named RDF graphs, and the default graph (which may be empty).

!!! note
    The above format specification is meant to cover all valid [RDF 1.1 datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset). Because of this, a completely empty file is also a valid stream element.*

The files must be in the RDF 1.1 TriG format, or in the TriG-star format, if the dataset uses RDF-star. The extensions of the files must be `.trig`. The files must be encoded in UTF-8.

**Example quads dataset:** [nanopubs](https://github.com/RiverBench/dataset-nanopubs)

### Triple stream format

In the triple stream format, every stream element is an unnamed (default) RDF graph, and every RDF graph corresponds to exactly one file.

!!! note
    The above format specification is meant to cover all valid [RDF 1.1 graphs](https://www.w3.org/TR/rdf11-concepts/#dfn-rdf-graph). Because of this, a completely empty file is also a valid stream element.*

The files must be in the RDF 1.1 Turtle format, or in the Turtle-star format, if the dataset uses RDF-star. The extensions of the files must be `.ttl`. The files must be encoded in UTF-8.

**Example triples dataset:** [yago-annotated-facts](https://github.com/RiverBench/dataset-yago-annotated-facts)

## See also

- [Creating a new dataset](creating-new-dataset.md)
- [Dataset release format](dataset-release-format.md)
