# nanopubs (development version)

Nanopublications are small units of publishable information, used for scientific results and more. This dataset is based on a subset of [a dump of all available nanopublications](https://zenodo.org/record/1213293) as of April 5, 2018. Only the first 5M of freely-licensed nanopubs were included. Each nanopub consists of several RDF graphs and thus is an RDF dataset. The included data is primarily from the biomedical domain. More information: [paper](https://arxiv.org/abs/1809.06532), [website](https://nanopub.net/).

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Nanopublications
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: nanopubs
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with bibliographical information.">Bibliographical</abbr> ([rbt:bibliographical](https://w3id.org/riverbench/schema/theme#bibliographical))
    - <abbr title="Datasets with biomedical information.">Biomedical</abbr> ([rbt:biomedical](https://w3id.org/riverbench/schema/theme#biomedical))
    - <abbr title="Datasets with scientific information.">Scientific</abbr> ([rbt:scientific](https://w3id.org/riverbench/schema/theme#scientific))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Authors of the included nanopublications (cited within the dataset) (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Authors of the included nanopublications (cited within the dataset)
    - **Piotr Sowiński (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            - [https://github.com/Ostrzyciel](https://github.com/Ostrzyciel)
            - [https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)
    - **Tobias Kuhn (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Tobias Kuhn
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://orcid.org/0000-0002-1267-0234](https://orcid.org/0000-0002-1267-0234)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Author of the [nanopublications dump](https://zenodo.org/record/1213293)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-SA-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-04-30
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-01
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Quad streams consist of elements, where each element is an RDF dataset.">Quads</abbr> ([rb:quads](https://w3id.org/riverbench/schema/metadata#quads))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5000000
- **Has stream element split**: 
    - **Type**: Stream elements split by topic ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element is one nanopublication.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: 
    - [http://purl.org/dc/terms/](http://purl.org/dc/terms/)
    - [http://www.nanopub.org/nschema#](http://www.nanopub.org/nschema#)
    - [https://www.w3.org/ns/prov-o](https://www.w3.org/ns/prov-o)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 42041430
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b3db88b6419b2ccee97918b2afa5ddeeb936e2fa`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b07dc5606b4119873186a18b445c1ccf`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 158
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 671463
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9446800570788878
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4907266
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 44
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 49.07266

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60104
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 300000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60262
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 700000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9446800570788294
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3207266
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.07266

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9427037216209224
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3307350
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 29
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.0735

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.5541629772967769
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 925880
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.2588

### <a name="stream-100k"></a> 100K elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 33180359
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9d67294cd03e041caeefefd8366a7186`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ebd080fec09f7b327a812d4ccfdc8dc2ee117237`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 158
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 400000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 671463
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9446800570788878
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4907266
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 44
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 49.07266

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60104
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 300000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60262
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 700000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9446800570788294
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3207266
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.07266

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.9427037216209224
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3307350
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 29
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.0735

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.5541629772967769
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 925880
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.2588

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 4088399
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3b35daa0466c2bc34b28c524497935e7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1f3b2bb6b1da9488322d917a432dccae80707cfa`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 17
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 73219
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 50
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 50.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6857
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6874
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 70000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 330000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 33
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.0

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 210000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 340000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 34
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.0

### <a name="stream-10k"></a> 10K elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3307035
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `01cec44e7482f8380901435698335770918d27d2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c5c1bfd524c9950fae4b784deb6c00c2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 17
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 40000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 73219
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 50
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 50
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 50.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6857
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6874
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 70000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 330000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 33
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.0

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 210000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 21
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 340000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 34
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.0

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 449755193
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f70531ea354cf93d8818329776f12aeb`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f66f663ec2b4b41ad397a759c19abe0d17a51afb`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 89864
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.9363691193920275
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4266443
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.266443

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 7017131
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 100
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.029570129445959
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48861863
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 40
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 48.861863

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 530740
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.8078333409652018
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2763885
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.763885

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 620603
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.23779447515870109
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7030328
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.030328

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 89
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.09442129182036
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 32151723
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.151723

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.938818479613572
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20738344
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 17
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.738344

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 135
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.639066950824928
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33423542
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 28
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.423542

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 52
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.334196210739579
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9350387
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.350387

### <a name="stream-1m"></a> 1M elements quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 354370553
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `bd4f144fafd128634071aacc14a875b2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1bdf519b197b9931788c4b66ce82757e9bf00b6d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_1M.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 89864
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.9363691193920275
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4266443
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.266443

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 7017131
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 100
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.029570129445959
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48861863
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 40
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 48.861863

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 530740
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.8078333409652018
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2763885
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.763885

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 620603
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.23779447515870109
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7030328
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 7
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.030328

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 89
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.09442129182036
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 32151723
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 27
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 32.151723

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.938818479613572
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20738344
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 17
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.738344

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 135
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.639066950824928
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33423542
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 28
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 33.423542

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 52
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.334196210739579
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9350387
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.350387

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nq.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2029120097
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `45982375450d2df554c0ec1f54fe893e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `4615d6c1f2d54524a3f289c17553d023b6773d6f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 2243795
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.7362842636115896
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 27015713
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.4031426

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 47162247
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 142
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.676726895279631
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 236997015
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 25
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 47.399403

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 1033269
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 32
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.4829012299645046
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8627838
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.7255676

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 3277169
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6004447388527527
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35643551
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.1287102

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 157
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.030255878357412
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159866280
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 14
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.973256

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.811598277526649
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 97782581
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.5565162

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 196
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.931873295248486
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 171885662
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 16
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.3771324

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 68
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.4253618350480695
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46588350
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.31767

### <a name="stream-full"></a> Full quad stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full quad stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1373020178
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a99695ad8e6465888830b9756d4e8ef690d4f810`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `eadc660aa32c31d189b131c12f06f953`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/nanopubs/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 2243795
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.7362842636115896
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 27015713
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.4031426

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 47162247
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 142
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.676726895279631
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 236997015
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 25
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 47.399403

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 1033269
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 32
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.4829012299645046
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8627838
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.7255676

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 3277169
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 34
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6004447388527527
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35643551
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.1287102

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 157
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.030255878357412
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159866280
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 14
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.973256

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.811598277526649
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 97782581
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.5565162

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 196
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.931873295248486
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 171885662
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 16
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 34.3771324

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 68
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.4253618350480695
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46588350
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.31767

