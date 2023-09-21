# dbpedia-live (development version)

[DBpedia Live](https://www.dbpedia.org/resources/live/) was a real-time service that monitored edits on Wikipedia and published a stream of changes to the DBpedia knowledge graph. This dataset contains only the "added" triples in the stream, so it does not include deletes or other types of changes. Only one month (January 2014) is covered at the moment, but the dataset can be easily expanded in the future (the service stopped functioning in 2021). The stream's elements are irregular in size, depending on the volume of traffic on Wikipedia at a given moment and how the DBpedia Live service was able to cope with it. See also the [paper](http://jens-lehmann.org/files/2012/program_el_dbpedia_live.pdf).
    
The dataset was extensively cleaned to fix or remove bad IRIs, bad Unicode, and invalid literals.

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/dbpedia-live/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/dbpedia-live/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/dbpedia-live/dev.rdf)**
    <br>Source repository: **[dbpedia-live](https://github.com/RiverBench/dataset-dbpedia-live)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: DBpedia Live
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `dbpedia-live`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with encyclopedic information.">Encyclopedic</abbr> ([rbt:encyclopedic](https://w3id.org/riverbench/schema/theme#encyclopedic))
    - <abbr title="Datasets with temporal information.">Temporal</abbr> ([rbt:temporal](https://w3id.org/riverbench/schema/theme#temporal))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Wikipedia contributors (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Wikipedia contributors
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://www.wikipedia.org/](https://www.wikipedia.org/)
    - **Piotr Sowiński (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Processing the dataset
    - **DBpedia Association (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: DBpedia Association
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://www.dbpedia.org/contact/](https://www.dbpedia.org/contact/)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-SA-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: 
    - [https://doi.org/10.1108/00330331211221828](https://doi.org/10.1108/00330331211221828)
    - [https://www.dbpedia.org/resources/live/](https://www.dbpedia.org/resources/live/)
- **<abbr title="Information about rights held in and over the resource.">Rights</abbr>**: The dataset contains attributions of the original source of the data (links to Wikipedia).
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-09
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-09-21
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [dbpedia-live (dev)](https://w3id.org/riverbench/datasets/dbpedia-live/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 166,204
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different instants or intervals of time.">Stream elements split by time</abbr> ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://dbpedia.org/ontology/wikiPageExtracted](http://dbpedia.org/ontology/wikiPageExtracted)
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each element corresponds to a batch of recent changes from Wikipedia. The size of the batch may have been influenced by the traffic on Wikipedia, the load on the system, and other factors, so the element sizes are irregular.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: [http://dbpedia.org/ontology/](http://dbpedia.org/ontology/)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="stream-full"></a> Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 166,204
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 256.91 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8b9155ff9cd3efa4a0a91f7aa3bc4d64`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `bec97b830058fe037b72345f2c5f34dfd6567728`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_full.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="jelly-full"></a> Full triple stream distribution (Jelly)

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution (Jelly)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 166,204
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 358.08 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e722d84a8e4675cf130615fb6cf311d2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b40424dbc6da9a9fc7556812ea0564373c8a4eb1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_full.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_full.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 166,204
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 282.16 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `38bf01cf3ce7d89f726b5bf45eb92c62`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e52475aa78bc883b9b16e4a91e9577d1bef03a30`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_full.nt.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="stream-100k"></a> 100K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 209.48 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9c3dfc6ed8423e37756878b1353bc490`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1d0a358ea474b130fd560135a282a7b530d32fa7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_100K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="jelly-100k"></a> 100K elements triple stream distribution (Jelly)

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution (Jelly)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 294.25 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `18fd5afbf9387fad09367afa70f3fb2a`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e45b4b6a64c3e5e60fcf6a5799a66e33844e2d4b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_100K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 230.12 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e91c8d42594ed9605184b917fe5daf5e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6f911037a3bbc40f6707d4c34e4d731da40aca91`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_100K.nt.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="stream-10k"></a> 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 66.88 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `31aed9710dadb47308a525a089a3b2db`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `213e44560c4425a523ee4282dd9c5c4921053311`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/stream_10K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="jelly-10k"></a> 10K elements triple stream distribution (Jelly)

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution (Jelly)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 93.04 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d08a7865f5e3a99250d6c9d77a5551d5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `75e4bef13b8c52e0153e340b5fde489c2a0aa7bf`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/jelly_10K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 73.69 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `391365b45846ad156e60a0ca668848e7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c98ebf535c727f27eef53da5bbf210fc586119fe`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/dbpedia-live/dev/files/flat_10K.nt.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions
- **<abbr title="Has a dataset statistics object">Has statistics</abbr>**: 
    - **IRI count statistics (1)**    
        - **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 16,654,403
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 11,540,684
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 100.20
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 205.40
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3,727
    - **Blank node count statistics (2)**    
        - **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Literal count statistics (3)**    
        - **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,911,441
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 3,597,388
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 35.57
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 120.44
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6,077
    - **Simple literal count statistics (4)**    
        - **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Datatype literal count statistics (5)**    
        - **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,958,152
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2,729,961
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.82
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 80.44
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3,455
    - **Language string count statistics (6)**    
        - **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,953,289
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 866,665
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.75
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 44.75
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,622
    - **Quoted triple count statistics (7)**    
        - **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Subject count statistics (8)**    
        - **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 11,290,262
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.93
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 130.41
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,961
    - **Predicate count statistics (9)**    
        - **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,881,262
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.32
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 26.04
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 436
    - **Object count statistics (10)**    
        - **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10,060,633
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 60.53
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 194.28
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6,658
    - **Graph count statistics (11)**    
        - **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Statement count statistics (12)**    
        - **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,831,109
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 131.35
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 319.79
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8,275

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions
- **<abbr title="Has a dataset statistics object">Has statistics</abbr>**: 
    - **IRI count statistics (1)**    
        - **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 13,631,942
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 9,703,320
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 136.32
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 224.18
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,681
    - **Blank node count statistics (2)**    
        - **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Literal count statistics (3)**    
        - **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,561,835
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2,808,084
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 45.62
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 128.93
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6,077
    - **Simple literal count statistics (4)**    
        - **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Datatype literal count statistics (5)**    
        - **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,997,501
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2,056,214
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 29.98
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 85.08
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3,455
    - **Language string count statistics (6)**    
        - **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,564,334
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 751,830
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 15.64
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 49.61
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,622
    - **Quoted triple count statistics (7)**    
        - **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Subject count statistics (8)**    
        - **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,361,620
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 93.62
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 144.77
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,961
    - **Predicate count statistics (9)**    
        - **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,471,621
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 14.72
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 28.34
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 436
    - **Object count statistics (10)**    
        - **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,860,478
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 78.60
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 206.43
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6,658
    - **Graph count statistics (11)**    
        - **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Statement count statistics (12)**    
        - **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 17,814,033
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 178.14
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 347.79
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8,275

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions
- **<abbr title="Has a dataset statistics object">Has statistics</abbr>**: 
    - **IRI count statistics (1)**    
        - **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,227,641
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 3,163,701
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 422.76
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 279.53
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,031
    - **Blank node count statistics (2)**    
        - **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Literal count statistics (3)**    
        - **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,566,963
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,068,951
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 156.70
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 256.16
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,120
    - **Simple literal count statistics (4)**    
        - **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Datatype literal count statistics (5)**    
        - **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,080,669
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 798,768
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 108.07
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 181.60
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,708
    - **Language string count statistics (6)**    
        - **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 486,294
        - **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 270,141
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 48.63
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 79.92
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,333
    - **Quoted triple count statistics (7)**    
        - **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Subject count statistics (8)**    
        - **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,928,996
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 292.90
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 121.33
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,449
    - **Predicate count statistics (9)**    
        - **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 430,909
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 43.09
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 49.27
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 436
    - **Object count statistics (10)**    
        - **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,622,682
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 262.27
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 416.36
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2,750
    - **Graph count statistics (11)**    
        - **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
    - **Statement count statistics (12)**    
        - **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
        - **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,575,053
        - **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 557.51
        - **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 529.45
        - **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
        - **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 4,905
