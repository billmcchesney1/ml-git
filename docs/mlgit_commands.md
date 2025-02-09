# ml-git commands #

<details>
<summary><code> ml-git --help </code></summary>
<br>

```
Usage: ml-git [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clone       Clone a ml-git repository ML_GIT_REPOSITORY_URL
  dataset     management of datasets within this ml-git repository
  labels      management of labels sets within this ml-git repository
  login       login command generates new Aws credential.
  model       management of models within this ml-git repository
  repository  Management of this ml-git repository
```

Example:
```
$ ml-git --help
```

</details>

<details>
<summary><code> ml-git --version </code></summary>

Displays the installed version of ml-git.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; add </code></summary>
<br>

```
Usage: ml-git dataset add [OPTIONS] ML_ENTITY_NAME [FILE_PATH]...

Add dataset change set ML_ENTITY_NAME to the local ml-git staging area.

Options:
--bumpversion  Increment the version number when adding more files.
--fsck         Run fsck after command execution.
--help         Show this message and exit.
```

Example:
```
$ ml-git dataset add dataset-ex --bumpversion
```

ml-git expects datasets to be managed under _dataset_ directory.
\<ml-entity-name\> is also expected to be a repository under the tree structure and ml-git will search for it in the tree.
Under that repository, it is also expected to have a \<ml-entity-name\>.spec file, defining the ML entity to be added.
Optionally, one can add a README.md which will describe the dataset and be what will be shown in the github repository for that specific dataset.

Internally, the _ml-git add_ will add all the files under the \<ml-entity\> directory into the ml-git index / staging area.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; branch </code></summary>
<br>

```
Usage: ml-git dataset branch [OPTIONS] ML_ENTITY_NAME

  This command allows to check which tag is checked out in the ml-git
  workspace.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset branch imagenet8
('vision-computing__images__imagenet8__1', '48ba1e994a1e39e1b508bff4a3302a5c1bb9063e')
```

That information is equal to the HEAD reference from a git concept. ml-git keeps that information on a per \<ml-entity-name\> basis. which enables independent checkout of each of these \<ml-entity-name\>.

The output is a tuple:
1) the tag auto-generated by ml-git based on the \<ml-entity-name\>.spec (composite with categories, \<ml-entity-name\>, version)
2) the sha of the git commit of that \<ml-entity\> version
Both are the same representation. One is human-readable and is also used internally by ml-git to find out the path to the referenced \<ml-entity-name\>.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; checkout </code></summary>
<br>

```
Usage: ml-git model checkout [OPTIONS] ML_ENTITY_TAG|ML_ENTITY

  Checkout the ML_ENTITY_TAG|ML_ENTITY of a model set into user workspace.

Options:
  -l, --with-labels         The checkout associated labels  in user workspace
                            as well.
  -d, --with-dataset        The checkout associated dataset in user workspace
                            as well.
  --retry INTEGER           Number of retries to download the files from the
                            storage [default: 2].
  --force                   Force checkout command to delete
                            untracked/uncommitted files from local repository.
  --bare                    Ability to add/commit/push without having the ml-
                            entity checked out.
  --version INTEGER         Number of artifact version to be downloaded
                            [default: latest].
  --verbose                 Debug mode
```

Examples:
```
$ ml-git dataset checkout computer-vision__images__faces__fddb__1
```
or you can use the name of the entity directly and download the latest available tag
```
$ ml-git dataset checkout fddb
```



Note:

```--d:``` It can only be used in checkout of labels and models to get the entities that are associated with the entity.

```--l:``` It can only be used in checkout of models to get the label entity that are associated with the entity.

```--sample-type, --sampling, --seed:``` These options are available only for dataset. If you use this option ml-git will not allow you to make changes to the entity and create a new tag.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; commit </code></summary>
<br>

```
Usage: ml-git model commit [OPTIONS] ML_ENTITY_NAME

  Commit model change set of ML_ENTITY_NAME locally to this ml-git
  repository.

Options:
  --dataset TEXT                  Link dataset entity name to this model set
                                  version.
  --labels TEXT                   Link labels entity name to this model set
                                  version.
  --tag TEXT                      Ml-git tag to identify a specific version of
                                  a ML entity.
  --version-number, --version INTEGER RANGE
                                  Set the number of artifact version.
                                  [DEPRECATED:--version-number]
  -m, --message TEXT              Use the provided <msg> as the commit
                                  message.
  --fsck TEXT                     Run fsck after command execution.
  --verbose                       Debug mode
```

Example:
```
$ ml-git model commit model-ex --dataset=dataset-ex
```

This command commits the index / staging area to the local repository. It is a 2-step operation in which 1) the actual data (blobs) is copied to the local repository, 2) committing the metadata to the git repository managing the metadata.
Internally, ml-git keeps track of files that have been added to the data store and is storing that information to the metadata management layer to be able to restore any version of each \<ml-entity-name\>.

Another important feature of ml-git is the ability to keep track of the relationship between the ML entities. So when committing a label set, one can (should) provide the option ```--dataset=<dataset-name>```.
Internally, ml-git will inspect the HEAD / ref of the specified \<dataset-name\> checked out in the ml-git repository and will add that information to the specificatino file that is committed to the metadata repository.
With that relationship kept into the metadata repository, it is now possible for anyone to checkout exactly the same versions of labels and dataset.

Same for ML model, one can specify which dataset and label set that have been used to generate that model through ```--dataset=<dataset-name>``` and ```--labels=<labels-name>```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; create </code></summary>
<br>

```
Usage: ml-git dataset create [OPTIONS] ARTIFACT_NAME

  This command will create the workspace structure with data and spec file
  for an entity and set the git and store configurations.

Options:
  --category TEXT                 Artifact's category name.  [required]
  --mutability [strict|flexible|mutable]
                                  Mutability type.  [required]
  --store-type, --storage-type [s3h|azureblobh|gdriveh]
                                  Data storage type [default: s3h].
                                  [DEPRECATED:--store-type]
  --version-number, --version INTEGER RANGE
                                  Number of artifact version.
                                  [DEPRECATED:--version-number]
  --import TEXT                   Path to be imported to the project. NOTE:
                                  Mutually exclusive with argument:
                                  credentials_path, import_url.
  --wizard-config                 If specified, ask interactive questions. at
                                  console for git & store configurations.
  --bucket-name TEXT              Bucket name
  --import-url TEXT               Import data from a google drive url. NOTE:
                                  Mutually exclusive with argument: import.
  --credentials-path TEXT         Directory of credentials.json. NOTE: This
                                  option is required if --import-url is used.
  --unzip                         Unzip imported zipped files. Only available
                                  if --import-url is used.
  --verbose                       Debug mode
```

Examples:
 - To create an entity with s3 as storage and importing files from a path of your computer:
```
ml-git dataset create imagenet8 --storage-type=s3h --category=computer-vision --category=images --version=0 --import='/path/to/dataset' --mutability=strict
```

- To create an entity with s3 as storage and importing files from a google drive URL:
```
ml-git dataset create imagenet8 --storage-type=s3h --category=computer-vision --category=images --import-url='gdrive.url' --credentials-path='/path/to/gdrive/credentials' --mutability=strict --unzip
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; export </code></summary>
<br>

```
Usage: ml-git dataset export [OPTIONS] ML_ENTITY_TAG BUCKET_NAME

  This command allows you to export files from one store (S3|MinIO) to
  another (S3|MinIO).

Options:
  --credentials TEXT  Profile of AWS credentials [default: default].
  --endpoint TEXT     Endpoint where you want to export
  --region TEXT       AWS region name [default: us-east-1].
  --retry INTEGER     Number of retries to upload or download the files from
                      the storage [default: 2].
  --help              Show this message and exit.
```

Example:
```
$ ml-git dataset export computer-vision__images__faces__fddb__1 minio
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; fetch </code></summary>
<br>

```
Usage: ml-git dataset fetch [OPTIONS] ML_ENTITY_TAG

  Allows you to download just the metadata files of an entity.

Options:
  --sample-type [group|range|random]
  --sampling TEXT                 The group: <amount>:<group> The group sample
                                  option consists of amount and group used to
                                  download a sample.
                                  range: <start:stop:step>
                                  The range sample option consists of start,
                                  stop and step used to download a sample. The
                                  start parameter can be equal or greater than
                                  zero.The stop parameter can be 'all', -1 or
                                  any integer above zero.
                                  random:
                                  <amount:frequency> The random sample option
                                  consists of amount and frequency used to
                                  download a sample.
  --seed TEXT                     Seed to be used in random-based samplers.
  --retry INTEGER                 Number of retries to download the files from
                                  the storage [default: 2].
  --help                          Show this message and exit.
```

Example:
```
ml-git dataset fetch computer-vision__images__faces__fddb__1
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; fsck </code></summary>
<br>

```
Usage: ml-git dataset fsck [OPTIONS]

  Perform fsck on dataset in this ml-git repository.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset fsck
```

This command will walk through the internal ml-git directories (index & local repository) and will check the integrity of all blobs under its management.
It will return the list of blobs that are corrupted.

Note: 

```
in the future, fsck should be able to fix some errors of detected corruption.
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; import </code></summary>
<br>

```
Usage: ml-git dataset import [OPTIONS] BUCKET_NAME ENTITY_DIR

  This command allows you to download a file or directory from the S3 bucket or Gdrive
to ENTITY_DIR.

Options:
  --credentials TEXT  Profile of AWS credentials [default: default].
  --region TEXT       AWS region name [default: us-east-1].
  --retry INTEGER     Number of retries to download the files from the storage
                      [default: 2].
  --path TEXT         Bucket folder path.
  --object TEXT       Filename in bucket.
  --store-type, --storage-type [s3|gdrive]
                                  Data storage type [default: s3h].
                                  [DEPRECATED:--store-type]
  --endpoint-url      Storage endpoint url.
  --help              Show this message and exit.
```

Example:
```
$ ml-git dataset import bucket-name dataset/computer-vision/imagenet8/data
```
For google drive store:
```
$ ml-git dataset import gdrive-folder --store-type=gdrive --object=file_to_download --credentials=credentials-path dataset/
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; init </code></summary>
<br>

```
Usage: ml-git dataset init [OPTIONS]

  Init a ml-git dataset repository.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset init
```

This command is mandatory to be executed just after the addition of a remote metadata repository (_ml-git \<ml-entity\> remote add_).
It initializes the metadata by pulling all metadata to the local repository.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; list </code></summary>
<br>

```
Usage: ml-git dataset list [OPTIONS]

  List dataset managed under this ml-git repository.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset list
ML dataset
|-- computer-vision
|   |-- images
|   |   |-- dataset-ex-minio
|   |   |-- imagenet8
|   |   |-- dataset-ex
```

</details>


<details>
<summary><code>ml-git &lt;ml-entity&gt; log </code></summary>
<br>

```
Usage: ml-git dataset log [OPTIONS] ML_ENTITY_NAME

  This command shows ml-entity-name's commit information like author, date,
  commit message.

Options:
  --stat      Show amount of files and size of an ml-entity.
  --fullstat  Show added and deleted files.
  --help      Show this message and exit.
```

Example:
```
ml-git dataset log dataset-ex
```

</details>



<details>
<summary><code> ml-git &lt;ml-entity&gt; push </code></summary>
<br>

```
Usage: ml-git dataset push [OPTIONS] ML_ENTITY_NAME

  Push local commits from ML_ENTITY_NAME to remote ml-git repository &
  store.

Options:
  --retry INTEGER  Number of retries to upload or download the files from the
                   storage [default: 2].
  --clearonfail    Remove the files from the store in case of failure during
                   the push operation.
  --help           Show this message and exit.
```

Example:
```
ml-git dataset push dataset-ex
```

This command will perform a 2-step operations:
1. push all blobs to the configured data store.
2. push all metadata related to the commits to the remote metadata repository.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; remote-fsck </code></summary>
<br>

```
Usage: ml-git dataset remote-fsck [OPTIONS] ML_ENTITY_NAME

  This command will check and repair the remote by uploading lacking
  chunks/blobs.

Options:
  --thorough       Try to download the IPLD if it is not present in the local
                   repository to verify the existence of all contained IPLD
                   links associated.
  --paranoid       Adds an additional step that will download all IPLD and its
                   associated IPLD links to verify the content by computing
                   the multihash of all these.
  --retry INTEGER  Number of retries to download the files from the storage
                   [default: 2].
  --help           Show this message and exit.
```

Example:
```
ml-git dataset remote-fsck dataset-ex
```

This ml-git command will basically try to:

* Detects any chunk/blob lacking in a remote store for a specific ML artefact version
* Repair - if possible - by uploading lacking chunks/blobs
* In paranoid mode, verifies the content of all the blobs

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; reset </code></summary>
<br>

```
Usage: ml-git dataset reset [OPTIONS] ML_ENTITY_NAME

  Reset ml-git state(s) of an ML_ENTITY_NAME

Options:
  --hard                     Remove untracked files from workspace, files to
                             be committed from staging area as well as
                             committed files upto <reference>.
  --mixed                    Revert the committed files and the staged files
                             to 'Untracked Files'. This is the default action.
  --soft                     Revert the committed files to 'Changes to be
                             committed'.
  --reference [head|head~1]  head:Will keep the metadata in the current
                             commit.
                             head~1:Will move the metadata to the last
                             commit.
  --help                     Show this message and exit.
```

Examples:

```
ml-git reset --hard
```

* Undo the committed changes.
* Undo the added/tracked files.
* Reset the workspace to fit with the current HEAD state.

```
ml-git reset --mixed
```
if HEAD:
* nothing happens.
else:
* Undo the committed changes.
* Undo the added/tracked files.

```
ml-git reset --soft
```
if HEAD:
* nothing happens.
else:
* Undo the committed changes.

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; show </code></summary>
<br>

```
Usage: ml-git dataset show [OPTIONS] ML_ENTITY_NAME

  Print the specification file of the entity.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset show dataset-ex
-- dataset : imagenet8 --
categories:
- vision-computing
- images
manifest:
  files: MANIFEST.yaml
  store: s3h://mlgit-datasets
name: imagenet8
version: 1
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; status </code></summary>
<br>

```
Usage: ml-git dataset status [OPTIONS] ML_ENTITY_NAME [STATUS_DIRECTORY]

  Print the files that are tracked or not and the ones that are in the
  index/staging area.

Options:
  --full     Show all contents for each directory.
  --verbose  Debug mode
```

Example:
```
$ ml-git dataset status dataset-ex
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; tag add</code></summary>
<br>

```
Usage: ml-git dataset tag add [OPTIONS] ML_ENTITY_NAME TAG

  Use this command to associate a tag to a commit.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset tag add dataset-ex my_tag
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; tag list </code></summary>
<br>

```
Usage: ml-git dataset tag list [OPTIONS] ML_ENTITY_NAME

  List tags of ML_ENTITY_NAME from this ml-git repository.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset tag list dataset-ex
```

</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; update </code></summary>
<br>

```
Usage: ml-git dataset update [OPTIONS]

  This command will update the metadata repository.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset update
```

This command enables one to have the visibility of what has been shared since the last update (new ML entity, new versions).
</details>

<details>
<summary><code> ml-git &lt;ml-entity&gt; unlock </code></summary>
<br>

```
Usage: ml-git dataset unlock [OPTIONS] ML_ENTITY_NAME FILE

  This command add read and write permissions to file or directory. Note:
  You should only use this command for the flexible mutability option.

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git dataset unlock dataset-ex data/file1.txt
```

Note:

```
You should only use this command for the flexible mutability option.
```
 
</details>


<details>
<summary><code> ml-git clone &lt;repository-url&gt; </code></summary>
<br>

```
Usage: ml-git clone [OPTIONS] REPOSITORY_URL

  Clone a ml-git repository ML_GIT_REPOSITORY_URL

Options:
  --folder TEXT
  --track
  --help         Show this message and exit.
```

Example:
```
$ ml-git clone https://git@github.com/mlgit-repository
```

</details>

<details>
<summary><code> ml-git login </code></summary>
<br>

```
Usage: ml-git login [OPTIONS]

  login command generates new Aws credential.

Options:
  --credentials TEXT  profile name for store credentials [default: default].
  --insecure          use this option when operating in a insecure location.
                      This option prevents storage of a cookie in the folder.
                      Never execute this program without --insecure option in
                      a compute device you do not trust.
  --rolearn TEXT      directly STS to this AWS Role ARN instead of the
                      selecting the option during runtime.
  --help              Show this message and exit.

```

Example:
```
ml-git login
```

Note: 

```

```

</details>

<details>
<summary><code> ml-git repository config </code></summary>
<br>

```
Usage: ml-git repository config [OPTIONS]

  Configuration of this ml-git repository

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git repository config
config:
{'dataset': {'git': 'git@github.com:example/your-mlgit-datasets'},
 'store': {'s3': {'mlgit-datasets': {'aws-credentials': {'profile': 'mlgit'},
                                     'region': 'us-east-1'}}},
 'verbose': 'info'}
```

Use this command if you want to check what configuration ml-git is running with. It is highly likely one will need to 
change the default configuration to adapt for her needs.

</details>

<details>
<summary><code> ml-git repository gc </code></summary>
<br>

```
Usage: ml-git repository gc [OPTIONS]

  Cleanup unnecessary files and optimize the use of the disk space.

Options:
  --verbose  Debug mode
```

This command will remove unnecessary files contained in the cache and objects directories of the ml-git metadata (.ml-git).

</details>

<details>
<summary><code> ml-git repository init </code></summary>
<br>

```
Usage: ml-git repository init [OPTIONS]

  Initialiation of this ml-git repository

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git repository init
```

This is the first command you need to run to initialize a ml-git project. It will bascially create a default .ml-git/config.yaml

</details>

<details>
<summary><code> ml-git repository remote &lt;ml-entity&gt; add </code></summary>
<br>

```
Usage: ml-git repository remote dataset add [OPTIONS] REMOTE_URL

  Add remote dataset metadata REMOTE_URL to this ml-git repository

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git repository remote dataset add https://git@github.com/mlgit-datasets
```

</details>

<details>
<summary><code> ml-git repository remote &lt;ml-entity&gt; del </code></summary>
<br>

```
Usage: ml-git repository remote dataset del

  Remove remote dataset metadata REMOTE_URL from this ml-git repository

Options:
  --help  Show this message and exit.
```

Example:
```
$ ml-git repository remote dataset del
```

</details>

<details>
<summary><code> ml-git repository store add </code> (DEPRECATED)</summary>
<br>

```
Usage: ml-git repository store add [OPTIONS] BUCKET_NAME

  [DEPRECATED]: Add a storage BUCKET_NAME to ml-git

Options:
  --credentials TEXT              Profile name for storage credentials
  --region TEXT                   Aws region name for S3 bucket
  --type [s3h|s3|azureblobh|gdriveh]
                                  Storage type (s3h, s3, azureblobh, gdriveh
                                  ...) [default: s3h]
  --endpoint-url TEXT             Storage endpoint url
  -g, --global                    Use this option to set configuration at
                                  global level
  --verbose                       Debug mode
```

Example:
```
$ ml-git repository store add minio --endpoint-url=<minio-endpoint-url>
```

Use this command to add a data storage to a ml-git project.

**Note: Command deprecated, use storage instead store.**

</details>

<details>
<summary><code> ml-git repository store del </code>(DEPRECATED)</summary>
<br>

```
Usage: ml-git repository store del [OPTIONS] BUCKET_NAME

  [DEPRECATED]: Delete a store BUCKET_NAME from ml-git

Options:
  --type [s3h|s3|azureblobh|gdriveh]  Store type (s3h, s3, azureblobh, gdriveh ...) [default:
                              s3h]
  --help                      Show this message and exit.
```

Example:
```
$ ml-git repository store del minio
```

**Note: Command deprecated, use storage instead store.**

</details>

<details>
<summary><code> ml-git repository storage add </code></summary>
<br>

```
Usage: ml-git repository storage add [OPTIONS] BUCKET_NAME

  Add a storage BUCKET_NAME to ml-git

Options:
  --credentials TEXT              Profile name for storage credentials
  --region TEXT                   Aws region name for S3 bucket
  --type [s3h|s3|azureblobh|gdriveh]
                                  Storage type (s3h, s3, azureblobh, gdriveh
                                  ...) [default: s3h]
  --endpoint-url TEXT             Storage endpoint url
  -g, --global                    Use this option to set configuration at
                                  global level
  --verbose                       Debug mode
```

Example:
```
$ ml-git repository storage add minio --endpoint-url=<minio-endpoint-url>
```

Use this command to add a data storage to a ml-git project.

</details>

<details>
<summary><code> ml-git repository storage del </code></summary>
<br>

```
Usage: ml-git repository storage del [OPTIONS] BUCKET_NAME

  Delete a storage BUCKET_NAME from ml-git

Options:
  --type [s3h|s3|azureblobh|gdriveh]  Storage type (s3h, s3, azureblobh, gdriveh ...) [default:
                              s3h]
  --help                      Show this message and exit.
```

Example:
```
$ ml-git repository storage del minio
```

</details>

<details>
<summary><code> ml-git repository update </code></summary>
<br>

```
Usage: ml-git repository update

  This command updates the metadata for all entities.
```

Example:
```
$ ml-git repository update
```

</details>

