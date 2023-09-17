# Dataset release format

This page explains the formats in which [RiverBench's datasets](../datasets/index.md) are distributed.

Each dataset has two types of distributions: flat and streaming. Flat distributions are simply compressed files with a sequence of RDF statements. Streaming distributions are compressed archives with a sequence of files, with each file corresponding to one stream element.

There always a few size variants of each distribution to choose from, starting from 10K stream elements, with 10x increases up to the full dataset. The full distribution is the longest available distribution of the dataset.

!!! tip
    Choose the size-limited distributions, if your work does not require the full dataset. They are much easier to work with. You can also want to choose them to have all datasets of the same size.

## Flat distributions

Flat distributions are serialized in the [N-Triples](https://www.w3.org/TR/n-triples/) or [N-Quads](https://www.w3.org/TR/n-quads/) format, depending on stream type. In case RDF-star is used in the dataset, the used formats are [N-Triples-star](https://www.w3.org/2021/12/rdf-star.html#n-triples-star) or [N-Quads-star](https://www.w3.org/2021/12/rdf-star.html#n-quads-star). The files are compressed with [gzip](https://en.wikipedia.org/wiki/Gzip). This format is streamable, as you can decompress gzip-compressed files on-the-fly and read the statements line-by-line.

The flat distribution files are named `flat_{size}.nt.gz` or `flat_{size}.nq.gz`, where `{size}` is the number of stream elements in the file. For example, `flat_10K.nt.gz` is a flat distribution file of a triple stream with 10,000 stream elements. The full distribution is denoted by `flat_full.nt.gz` or `flat_full.nq.gz`.

## Streaming distributions

In streaming distributions each stream element is represented by a separate file. The files are compressed in a `.tar.gz` archive. The files are sequentially named starting from `0000000000.Y`, and sequentially up to `X.Y`, where `X + 1` is the number of stream elements in the dataset, and Y is the file extension. All numbers are zero-padded to exactly ten digits. The files are in nested directories with at most 1000 files per directory, to avoid issues with some file systems and file browsers. The number of levels of directories depends on the size of the distribution, with 10K–1M distributions having one level of directories and larger distributions having two.

The file names are sequentially numbered, and the files are stored in nested directories with at most 1000 files per directory, to avoid issues with some file systems and file browsers. The files are laid out in the archive sequentially, that is, physically the bytes files `X` and `X+1` are next to each other. This allows the package to be processed one element at a time without decompressing the entire archive. To do that, you will need a streaming decompressor / untar utility like the one in Pekko Streams ([tarReader](https://pekko.apache.org/docs/pekko-connectors/current/file.html#tar-archive), [gunzip](https://pekko.staged.apache.org/docs/pekko/current/stream/operators/Compression/gunzip.html)) or [Apache Commons Compress](https://commons.apache.org/proper/commons-compress/).

Each element is serialized in either the [Turtle](https://www.w3.org/TR/turtle/) or the [TriG](https://www.w3.org/TR/trig/) format, depending on the stream type. In case RDF-star is used in the dataset, the used formats are [Turtle-star](https://www.w3.org/2021/12/rdf-star.html#turtle-star) or [TriG-star](https://www.w3.org/2021/12/rdf-star.html#trig-star).

The streaming distribution files are named `stream_{size}.tar.gz`, where `{size}` is the number of stream elements in the file. For example, `stream_10K.tar.gz` is a streaming distribution file with 10,000 stream elements. The full distribution is denoted by `stream_full.tar.gz`.

### Example – triple stream, `stream_10K.tar.gz`

```
- 000/
    - 0000000000.ttl
    - 0000000001.ttl
    - ...
    - 0000000999.ttl
...
- 009/
    - 0000009000.ttl
    - 0000009001.ttl
    - ...
    - 0000009999.ttl
```

### Example – graph stream, `stream_10M.tar.gz`

```
- 000/
    - 000/
        - 0000000000.trig
        - 0000000001.trig
        - ...
        - 0000000999.trig
    - 001/
        - 0000001000.trig
        - 0000001001.trig
        - ...
        - 0000001999.trig
    - ...
    - 999/
        - 0000099000.trig
        - 0000099001.trig
        - ...
        - 0000099999.trig
...
- 999/
    - 000/
        - 0009990000.trig
        - 0009990001.trig
        - ...
        - 0009990999.trig
    - ...
    - 999/
        - 0009999000.trig
        - 0009999001.trig
        - ...
        - 0009999999.trig
```

## See also

- [Metadata](metadata.md)
- [Dataset source format](dataset-source-format.md)
