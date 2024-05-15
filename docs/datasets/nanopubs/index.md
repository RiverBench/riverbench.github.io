# nanopubs (development version)

Nanopublications are small units of publishable information, used for scientific results and more. This dataset is based on a subset of [a dump of all available nanopublications](https://zenodo.org/record/1213293) as of April 5, 2018. Only the first 5M of freely-licensed nanopubs were included. Each nanopub consists of several RDF graphs and thus is an RDF dataset. The included data is primarily from the biomedical domain. More information: [paper](https://arxiv.org/abs/1809.06532), [website](https://nanopub.net/).

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/nanopubs/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/nanopubs/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/nanopubs/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/datasets/nanopubs/dev.jelly)**
    <br>Source repository: **[nanopubs](https://github.com/RiverBench/dataset-nanopubs)**

??? example "Stream preview (click to expand)"

    === "Element 0"

        ```turtle title="0000000000.trig"
        --8<-- "docs/datasets/nanopubs/dev/data/sample_0000000000.trig"
        ```


    === "Element 10"

        ```turtle title="0000000010.trig"
        --8<-- "docs/datasets/nanopubs/dev/data/sample_0000000010.trig"
        ```


    === "Element 100"

        ```turtle title="0000000100.trig"
        --8<-- "docs/datasets/nanopubs/dev/data/sample_0000000100.trig"
        ```


    === "Element 1000"

        ```turtle title="0000001000.trig"
        --8<-- "docs/datasets/nanopubs/dev/data/sample_0000001000.trig"
        ```


    === "Element 10000"

        ```turtle title="0000010000.trig"
        --8<-- "docs/datasets/nanopubs/dev/data/sample_0000010000.trig"
        ```


## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Nanopublications _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `nanopubs`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - Metadata ([eurovoc:c_40f54e0c](http://eurovoc.europa.eu/c_40f54e0c))
    - Open data ([eurovoc:c_5ea6e5c4](http://eurovoc.europa.eu/c_5ea6e5c4))
    - Open science ([eurovoc:c_99a79cea](http://eurovoc.europa.eu/c_99a79cea))
    - Research results ([eurovoc:6306](http://eurovoc.europa.eu/6306))
    - Scientific research ([eurovoc:2924](http://eurovoc.europa.eu/2924))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Authors of the included nanopublications (cited within the dataset) (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Authors of the included nanopublications (cited within the dataset)
    - **Tobias Kuhn (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Tobias Kuhn
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://orcid.org/0000-0002-1267-0234](https://orcid.org/0000-0002-1267-0234)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Author of the [nanopublications dump](https://zenodo.org/record/1213293) _(<abbr title="English">en</abbr>)_
    - **Piotr Sowiński (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-SA-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: [https://doi.org/10.5281/zenodo.1213293](https://doi.org/10.5281/zenodo.1213293)
- **<abbr title="Information about rights held in and over the resource.">Rights</abbr>**: This dataset only includes freely-licensed publications (CC BY, CC BY-SA, or ODbL licenses). Each nanopublication includes information about its original authors and is self-citing. The dataset is marked as under CC BY-SA, as this is the most restrictive license in the dataset. _(<abbr title="English">en</abbr>)_
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-04-30
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2024-05-15
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element is one nanopublication. _(<abbr title="English">en</abbr>)_
- **<abbr title="A vocabulary that is used in the dataset.">Uses vocabulary</abbr>**: 
    - [http://purl.org/dc/terms/](http://purl.org/dc/terms/)
    - [http://www.nanopub.org/nschema#](http://www.nanopub.org/nschema#)
    - [https://www.w3.org/ns/prov-o](https://www.w3.org/ns/prov-o)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="stream-full"></a> Full stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.02 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `656df171ec214b97a657d6e76b6c7f0e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `97c21c99db303cac63653f9067e0c52e684bf110`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="jelly-full"></a> Full Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.56 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3db7b87b4a72588090cd02bcfdcaa7dd`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c714d666de1e60a5265c6678b1aceb0888b8bd26`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_full.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.68 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `387dc1e1adc92f2fd91b6c315fdf9436`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `110d9c128ca0d9e48f806086a373ea3639cf94f4`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="stream-1m"></a> 1M elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 277.18 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `bdcba2c5a45f726700b3f38df96ddeef`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `366bc8559339b05340731f429c36445e3716e58c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="jelly-1m"></a> 1M elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_1M.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 347.02 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7bef12e45e3bd835b0780f68944397ad`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5e1e65282c65897ac11965b416732b5eed0e4ab7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 384.61 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1e2dec57fc8ceb1c212c994d0c8ea04c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9171cabf2cca60d5180de3ddfb0438115b65121f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="stream-100k"></a> 100K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 25.59 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `89f5fa5a760803dbdf80b12cf64f3ac7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ce18a4f833432a02b2fab832cf1a5e65bb7d25b0`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="jelly-100k"></a> 100K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 30.89 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `eb217d88aa6560b61a778769238b3bcc`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `458a8afe9e64342519035fa7081dd09855494ed1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 35.73 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7180fd388408b9e48075afa559dacf89`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b38c9d95416a30a353ac46192f6ab18accc77084`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="stream-10k"></a> 10K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.55 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `4fc62b7a853bc3f706b03baf2395a88e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7eee0c297d04cd37fb4e9fd73b9c3efae74a456e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="jelly-10k"></a> 10K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets. Each RDF dataset corresponds to one nanopublication. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF dataset stream is a grouped RDF stream whose elements are RDF datasets.">RDF dataset stream</abbr> ([stax:datasetStream](https://w3id.org/stax/ontology#datasetStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.01 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6c035201b16269f39bb4e7c57a8b4f3c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ddb2220252f67ed8ff4127fadf80efa64b25951c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is an RDF stream whose elements are quad statements.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.47 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6d6e1ec6871a259250b61bab84d0d810`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e2415dd8ec272c94922beb79f2a025146d2db319`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 236,997,015 | 47,162,247 | 47.40 | 5.68 | 25 | 142 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 20,000,000 | _N/A_ | 4.00 | 0.00 | 4 | 4 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 171,885,662 | _N/A_ | 34.38 | 9.93 | 16 | 196 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 35,643,551 | 3,277,169 | 7.13 | 0.60 | 3 | 34 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 18,591,732 | 2,222,348 | 3.72 | 2.05 | 1 | 20 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 8,423,981 | 21,459 | 1.68 | 0.59 | 0 | 4 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 8,627,838 | 1,033,269 | 1.73 | 1.48 | 0 | 32 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 46,588,350 | _N/A_ | 9.32 | 4.43 | 3 | 68 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 97,782,581 | _N/A_ | 19.56 | 1.81 | 11 | 22 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 159,866,280 | _N/A_ | 31.97 | 6.03 | 14 | 157 |

### <a name="statistics-1m"></a> Statistics for 1M distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 1M distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 48,861,863 | 7,017,131 | 48.86 | 3.03 | 40 | 100 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 4,000,000 | _N/A_ | 4.00 | 0.00 | 4 | 4 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 33,423,542 | _N/A_ | 33.42 | 4.64 | 28 | 135 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 7,030,328 | 620,603 | 7.03 | 0.24 | 7 | 22 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 2,321,606 | 86,968 | 2.32 | 1.11 | 2 | 20 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 1,944,837 | 2,895 | 1.94 | 0.27 | 1 | 3 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 2,763,885 | 530,740 | 2.76 | 0.81 | 0 | 3 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 9,350,387 | _N/A_ | 9.35 | 2.33 | 6 | 52 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 20,738,344 | _N/A_ | 20.74 | 0.94 | 17 | 22 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 32,151,723 | _N/A_ | 32.15 | 3.09 | 27 | 89 |

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 4,907,266 | 671,463 | 49.07 | 1.94 | 44 | 50 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 400,000 | _N/A_ | 4.00 | 0.00 | 4 | 4 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 3,307,350 | _N/A_ | 33.07 | 1.94 | 29 | 34 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 700,000 | 60,262 | 7.00 | 0.00 | 7 | 7 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 200,000 | 4 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 200,000 | 154 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 300,000 | 60,104 | 3.00 | 0.00 | 3 | 3 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 925,880 | _N/A_ | 9.26 | 1.55 | 6 | 10 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 2,100,000 | _N/A_ | 21.00 | 0.00 | 21 | 21 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 3,207,266 | _N/A_ | 32.07 | 1.94 | 27 | 33 |

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 500,000 | 73,219 | 50.00 | 0.00 | 50 | 50 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 40,000 | _N/A_ | 4.00 | 0.00 | 4 | 4 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 340,000 | _N/A_ | 34.00 | 0.00 | 34 | 34 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 70,000 | 6,874 | 7.00 | 0.00 | 7 | 7 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 20,000 | 2 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 20,000 | 15 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 30,000 | 6,857 | 3.00 | 0.00 | 3 | 3 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 100,000 | _N/A_ | 10.00 | 0.00 | 10 | 10 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 210,000 | _N/A_ | 21.00 | 0.00 | 21 | 21 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 330,000 | _N/A_ | 33.00 | 0.00 | 33 | 33 |

