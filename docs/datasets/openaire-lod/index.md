<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/datasets/openaire-lod/dev "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/dataset-openaire-lod/edit/main/metadata.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Dataset: openaire-lod (development version)

[OpenAIRE LOD](https://web.archive.org/web/20201230151925/http://lod.openaire.eu/documentation) was a service that exported data from the OpenAIRE information space in RDF format, using Linked Open Data principles. The data was exported to Zenodo, with the [last dump dated at March 3, 2021](https://zenodo.org/records/4587369). This dataset consists of the "result" subset of the OpenAIRE LOD graph, including scientific results such as publications.

Only records that were valid RDF and had the "dateofcollection" property were included here. They were then sorted by the date of collection in ascending order. The first 2 (out of 28) million records that were obtained in this way are a part of this dataset.

See also [the project documentation](https://web.archive.org/web/20201230151925/http://lod.openaire.eu/documentation) and [the used ontology](https://web.archive.org/web/20201230151925/http://lod.openaire.eu/vocab).

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/openaire-lod/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/openaire-lod/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/openaire-lod/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/datasets/openaire-lod/dev.jelly)**
    <br>:material-github: Source repository: **[dataset-openaire-lod](https://github.com/RiverBench/dataset-openaire-lod)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/datasets/openaire-lod/dev`](https://w3id.org/riverbench/datasets/openaire-lod/dev)

    **[:octicons-arrow-down-24: Go to download links](#distributions)**

??? example "Stream preview (click to expand)"

    === "Element 0"

        ```turtle title="0000000000.ttl"
        --8<-- "docs/datasets/openaire-lod/data/sample_0000000000.ttl"
        ```


    === "Element 10"

        ```turtle title="0000000010.ttl"
        --8<-- "docs/datasets/openaire-lod/data/sample_0000000010.ttl"
        ```


    === "Element 100"

        ```turtle title="0000000100.ttl"
        --8<-- "docs/datasets/openaire-lod/data/sample_0000000100.ttl"
        ```


    === "Element 1000"

        ```turtle title="0000001000.ttl"
        --8<-- "docs/datasets/openaire-lod/data/sample_0000001000.ttl"
        ```


    === "Element 10000"

        ```turtle title="0000010000.ttl"
        --8<-- "docs/datasets/openaire-lod/data/sample_0000010000.ttl"
        ```


## General information

<div class="annotate" markdown>

- **<abbr title="A name given to the resource.">Title</abbr>**: OpenAIRE LOD graph _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `openaire-lod`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - Bibliography ([eurovoc:4864](http://eurovoc.europa.eu/4864))
    - Open data ([eurovoc:c_5ea6e5c4](http://eurovoc.europa.eu/c_5ea6e5c4))
    - Open science ([eurovoc:c_99a79cea](http://eurovoc.europa.eu/c_99a79cea))
    - Research report ([eurovoc:2896](http://eurovoc.europa.eu/2896))
    - Research results ([eurovoc:6306](http://eurovoc.europa.eu/6306))
    - Scientific research ([eurovoc:2924](http://eurovoc.europa.eu/2924))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Giorgos Alexiou (​1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Giorgos Alexiou
        - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**: [https://orcid.org/0000-0003-2244-4916](https://orcid.org/0000-0003-2244-4916)
    - **George Papastefanatos (​2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: George Papastefanatos
        - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**: [https://orcid.org/0000-0002-9273-9843](https://orcid.org/0000-0002-9273-9843)
    - **Sahar Vahdati (​3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Sahar Vahdati
    - **Christoph Lange (​4)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Christoph Lange
    - **Piotr Sowiński (​5)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Processing the dataset for RiverBench
        - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC0-1.0](https://spdx.org/licenses/CC0-1.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: 
    - Alexiou, G., Papastefanatos, G., Vahdati, S., &amp; Lange, C. (2021). <i>OpenAIRE LOD Dump</i> (Version 2.0) [Dataset]. Zenodo. [https://doi.org/10.5281/ZENODO.4587369](https://doi.org/10.5281/ZENODO.4587369) :custom-bibtex:{ .rb-bibtex } (1)
    - [https://web.archive.org/web/20201230151925/http://lod.openaire.eu/documentation](https://web.archive.org/web/20201230151925/http://lod.openaire.eu/documentation)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2024-07-12
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2026-06-20
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [openaire-lod (dev)](https://w3id.org/riverbench/datasets/openaire-lod/dev)

</div>

1. BibTeX citation:
    ``` { .bibtex .rb-wrap-code }
    @misc{https://doi.org/10.5281/zenodo.4587369,
      doi = {10.5281/ZENODO.4587369},
      url = {https://zenodo.org/record/4587369},
      author = {Alexiou, Giorgos and Papastefanatos, George and Vahdati, Sahar and Lange, Christoph},
      language = {en},
      title = {OpenAIRE LOD Dump},
      publisher = {Zenodo},
      year = {2021},
      copyright = {Creative Commons Zero v1.0 Universal}
    }
    ```

## Technical metadata

- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (​1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
    - **RDF stream type usage (​2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,000,000
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**:     
        - <abbr title="The elements correspond to different instants or intervals of time.">Stream elements split by time</abbr> ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
        - <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to exactly one scientific result in OpenAIRE, each with an assigned timestamp (time of collection). _(<abbr title="English">en</abbr>)_
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://lod.openaire.eu/vocab/dateofcollection](http://lod.openaire.eu/vocab/dateofcollection)
    - **<abbr title="Indicates the subject node in an RDF subject graph stream, using SHACL. The value of this property should be a SHACL sh:NodeShape with a specified target (e.g., sh:targetSubjectsOf). Only the target will be considered, restrictions on the shape will be ignored.  This property is required for RDF subject graph streams. Only sh:targetClass, sh:targetSubjectsOf, and sh:targetObjectsOf are allowed as the target specification.  This property can be specified multiple times. The different target specifications will then be treated as alternatives.">Has subject shape</abbr>**:     
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Target instances of class ResultEntity. _(<abbr title="English">en</abbr>)_
        - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: [http://lod.openaire.eu/vocab/ResultEntity](http://lod.openaire.eu/vocab/ResultEntity)
- **<abbr title="A vocabulary that is used in the dataset.">Uses vocabulary</abbr>**: [http://lod.openaire.eu/vocab](http://lod.openaire.eu/vocab)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no
- **<abbr title="A language of the resource.">Language</abbr>**: `en`

## Distributions


### Download links

The dataset is published in a few size variants, each containing a specific number of stream elements.
For each size, there are three distribution types available: flat
(an N-Triples/N-Quads file in the [RDF Message Log format](https://w3c-cg.github.io/rsp/spec/messages)),
streaming (a .tar.gz archive with Turtle/TriG files, one file per stream element),
and [Jelly](https://w3id.org/jelly) (a native binary format for streaming RDF).
See the [documentation](../../documentation/dataset-release-format.md) for more details.

Distribution size | Statements | Flat | Streaming | Jelly
--- | --: | --: | --: | --:
<abbr title="10,000 stream elements">10K</abbr> | 193,178 | [:octicons-download-24: 3.4 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_10K.nt.gz) | [:octicons-download-24: 3.0 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_10K.tar.gz) | [:octicons-download-24: 2.9 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_10K.jelly.gz)
<abbr title="100,000 stream elements">100K</abbr> | 2,267,185 | [:octicons-download-24: 48.1 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_100K.nt.gz) | [:octicons-download-24: 42.8 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_100K.tar.gz) | [:octicons-download-24: 42.6 MB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_100K.jelly.gz)
<abbr title="1,000,000 stream elements">1M</abbr> | 42,913,544 | [:octicons-download-24: 1.1 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_1M.nt.gz) | [:octicons-download-24: 1.1 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_1M.tar.gz) | [:octicons-download-24: 1.2 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_1M.jelly.gz)
<abbr title="2,000,000 stream elements">Full</abbr> | 71,810,467 | [:octicons-download-24: 1.7 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_full.nt.gz) | [:octicons-download-24: 1.6 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_full.tar.gz) | [:octicons-download-24: 1.6 GB](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_full.jelly.gz)


The full metadata of all distributions can be found below.

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_full.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file, using the RDF Message Log format.">Flat distribution (RDF Messages)</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.7 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0ee203465246efcafb0363724fb0efde`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0f8ef003456ba4fdbbbd4341aed9da13ec437091`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_full.nt.gz)

### <a name="stream-full"></a> Full stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.6 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3f1e19fce36ba2d9c5833da6d443aca1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `fbbd51300bddd43dc0bbb92ba8bbf087d9d62f3f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_full.tar.gz)

### <a name="jelly-full"></a> Full Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (​1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
    - **RDF stream type usage (​2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.6 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `494a86dd897e5eada6927106f1769c58`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e3902dcaf1f31bb60b918ec71751cf95517c32fc`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_full.jelly.gz)

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file, using the RDF Message Log format.">Flat distribution (RDF Messages)</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.1 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `334c1cbd2dc96873849f5311ef9d131d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `af9b9581bebf92fd065853114b8e483daae9d7c0`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_1M.nt.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_1M.nt.gz)

### <a name="stream-1m"></a> 1M elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.1 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6d79b4dcbb9e4ea24540cf31a641e6f4`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9d9b39aeaed185e985f341a0ed7e25db9978a63f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_1M.tar.gz)

### <a name="jelly-1m"></a> 1M elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_1M.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (​1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
    - **RDF stream type usage (​2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.2 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7dfbc6d0e62f11917e48fc3f7d49f17c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0f47b562d79ebc41dd2b6e5a621c7185eca40e76`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_1M.jelly.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_1M.jelly.gz)

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file, using the RDF Message Log format.">Flat distribution (RDF Messages)</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 48.1 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2133f9b7b8a0a1a44a7cc785a6e26b95`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d8bff2ddb192e1d52456f80f5ab3d5f8b3884ea8`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_100K.nt.gz)

### <a name="stream-100k"></a> 100K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 42.8 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e8748bf855e1ecdc5a5289a8b034e9fa`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `54a09b989cec5cffd275cbae5832a4f81bd51c07`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_100K.tar.gz)

### <a name="jelly-100k"></a> 100K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (​1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
    - **RDF stream type usage (​2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 42.6 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `54f8df813c1fcd6b5e4171dfe6bec87f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0bc6add08fb8fd6e10434c6a4bcaefe5ba251d89`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_100K.jelly.gz)

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file, using the RDF Message Log format.">Flat distribution (RDF Messages)</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.4 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a91442ef557740b79dcda89ae890dd84`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `4c10e4e7f3f159bdcd64488080b9a5057f93dc78`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/flat_10K.nt.gz)

### <a name="stream-10k"></a> 10K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.0 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b4bb22834226e08a46db9605dd8b7b51`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `cc8f01a73eb70a571a19664d19f2ae18da0b6246`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_10K.tar.gz)

### <a name="jelly-10k"></a> 10K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (​1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
    - **RDF stream type usage (​2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs, with each graph corresponding to one scientific result from OpenAIRE. Each graph is uniquely identified by its subject IRI. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.9 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (​1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f442c19161b3c77782eebd90f2fd0ed9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (​2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5d511d1584200722a2196f6f4c35c44c0fc5cf71`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_10K.jelly.gz)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 44,830,559 | <abbr title="Estimated value. Lower bound: 5,872,262, upper bound: 5,949,152 (95% confidence).">~5,910,457</abbr> | 22.42 | 48.04 | 10 | 8,988 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 55,180,959 | <abbr title="Estimated value. Lower bound: 9,513,521, upper bound: 9,638,090 (95% confidence).">~9,575,401</abbr> | 27.59 | 132.67 | 5 | 5,121 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 55,180,959 | <abbr title="Estimated value. Lower bound: 9,585,837, upper bound: 9,711,352 (95% confidence).">~9,648,186</abbr> | 27.59 | 132.67 | 5 | 5,121 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 5,234 | _N/A_ | 0.00 | 0.94 | 0 | 503 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 2,000,000 | <abbr title="Estimated value. Lower bound: 1,988,722, upper bound: 2,014,762 (95% confidence).">~2,001,658</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 28,476,853 | <abbr title="Estimated value. Lower bound: 24, upper bound: 24 (95% confidence).">~24</abbr> | 14.24 | 0.95 | 8 | 19 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 69,535,884 | <abbr title="Estimated value. Lower bound: 14,004,330, upper bound: 14,187,700 (95% confidence).">~14,095,419</abbr> | 34.77 | 141.46 | 7 | 8,985 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 2,000,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 71,810,467 | _N/A_ | 35.91 | 141.51 | 8 | 8,987 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 282.06 | 1,382.31 | 0.28 | 298,514.27 |

### <a name="statistics-1m"></a> Statistics for 1M distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 1M distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 26,480,270 | <abbr title="Estimated value. Lower bound: 4,643,767, upper bound: 4,704,572 (95% confidence).">~4,673,971</abbr> | 26.48 | 67.66 | 10 | 8,988 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 29,668,659 | <abbr title="Estimated value. Lower bound: 4,814,772, upper bound: 4,877,816 (95% confidence).">~4,846,089</abbr> | 29.67 | 187.48 | 5 | 5,121 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 29,668,659 | <abbr title="Estimated value. Lower bound: 4,832,376, upper bound: 4,895,650 (95% confidence).">~4,863,808</abbr> | 29.67 | 187.48 | 5 | 5,121 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 2 | _N/A_ | 0.00 | 0.00 | 0 | 2 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 1,000,000 | <abbr title="Estimated value. Lower bound: 992,711, upper bound: 1,005,709 (95% confidence).">~999,168</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 13,660,885 | <abbr title="Estimated value. Lower bound: 24, upper bound: 24 (95% confidence).">~24</abbr> | 13.66 | 0.93 | 8 | 19 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 41,489,263 | <abbr title="Estimated value. Lower bound: 9,033,665, upper bound: 9,151,950 (95% confidence).">~9,092,423</abbr> | 41.49 | 199.70 | 7 | 8,985 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 1,000,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 42,913,544 | _N/A_ | 42.91 | 199.75 | 8 | 8,987 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 380.97 | 1,949.04 | 0.28 | 298,514.27 |

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 1,700,241 | <abbr title="Estimated value. Lower bound: 209,233, upper bound: 211,973 (95% confidence).">~210,594</abbr> | 17.00 | 3.85 | 12 | 227 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 1,849,721 | <abbr title="Estimated value. Lower bound: 818,570, upper bound: 829,288 (95% confidence).">~823,894</abbr> | 18.50 | 28.73 | 7 | 3,037 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 1,849,721 | <abbr title="Estimated value. Lower bound: 827,464, upper bound: 838,299 (95% confidence).">~832,846</abbr> | 18.50 | 28.73 | 7 | 3,037 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 100,000 | <abbr title="Estimated value. Lower bound: 99,317, upper bound: 100,617 (95% confidence).">~99,963</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 1,284,078 | <abbr title="Estimated value. Lower bound: 22, upper bound: 22 (95% confidence).">~22</abbr> | 12.84 | 1.10 | 10 | 18 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 2,165,891 | <abbr title="Estimated value. Lower bound: 929,554, upper bound: 941,726 (95% confidence).">~935,600</abbr> | 21.66 | 29.45 | 10 | 3,101 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 100,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 2,267,185 | _N/A_ | 22.67 | 29.35 | 10 | 3,101 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 189.88 | 171.91 | 0.95 | 25,737.47 |

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 170,859 | <abbr title="Estimated value. Lower bound: 29,726, upper bound: 30,115 (95% confidence).">~29,919</abbr> | 17.09 | 6.29 | 13 | 207 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 138,454 | <abbr title="Estimated value. Lower bound: 56,594, upper bound: 57,335 (95% confidence).">~56,963</abbr> | 13.85 | 5.07 | 7 | 202 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 138,454 | <abbr title="Estimated value. Lower bound: 56,713, upper bound: 57,455 (95% confidence).">~57,082</abbr> | 13.85 | 5.07 | 7 | 202 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 10,000 | <abbr title="Estimated value. Lower bound: 9,921, upper bound: 10,051 (95% confidence).">~9,985</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 121,432 | <abbr title="Estimated value. Lower bound: 22, upper bound: 22 (95% confidence).">~22</abbr> | 12.14 | 0.71 | 10 | 16 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 177,888 | <abbr title="Estimated value. Lower bound: 76,399, upper bound: 77,399 (95% confidence).">~76,896</abbr> | 17.79 | 8.41 | 10 | 239 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 10,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 193,178 | _N/A_ | 19.32 | 8.53 | 10 | 240 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 185.05 | 103.82 | 1.77 | 2,641.00 |

