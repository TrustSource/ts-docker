[![Gitter](https://badges.gitter.im/TrustSource/community.svg)](https://gitter.im/TrustSource/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
![Supported Versions](https://img.shields.io/badge/Python-3.7,%203.8-blue)

# TrustSource Docker scanner

This is a wrapper for Syft, allowing to decompose a docker image - pulled from default registry - and transferring the results to TrustSource or writing it into a local JSON.

# Prerequisites

**Syft** - a tool for generating a Software Bill of Materials (SBOM) from container images and filesystems. 
For the installation instruction, please, refer to https://github.com/anchore/syft . ts-docker will use the default path set during the installation to find syft and handle it. You may specify a path, in case this is required. See below for more information.

# Installation

To install, please clone the repo and install from there:

- Clone repository
```shell
git clone https://github.com/TrustSource/ts-docker.git
```

- Install using PIP from the base directory (where you have cloned the repo in)
```shell
pip3 install ./ts-docker 
```

# Usage

You may execute the utility without any further connection to TrustSource. However, to transfer data into TrustSource, you require a valid API key and a projectname to associate transfered data with. To retrieve a valid API key, please contact your project manager or see 

## Execute Help

ts-docker has a CLI. To learn more, run `--help`
```shell
ts-docker --help
```
This will display the different options available:
```shell
Usage: ts-docker [OPTIONS] IMAGE

Options:
  --syft-path TEXT     Path to the Syft executable.
  --apiKey TEXT        API Key for data transfer to TrustSource.
  --projectName TEXT   Project name to associate data with.
  --skipTransfer       Skip transfer of results to TrustSource (local use only).
  --settingsFile TEXT  Path to a settings file, e.g. containing the API key
  --outputFile TEXT    Path to an output file, to store upload data locally (will be JSON).
  --help               Show this message and exit. 
```

## Examples

### Prepare data without transfering 

```shell
ts-docker --skipTransfer <local Docker image name> 
```
Will execute the scan and write scan result to stdout.

### Prepare data and transfer to TrustSource  

```shell
ts-docker --apiKey <KEY> --projectName <NAME> <local Docker image name> 
```
Will execute the scan, upload data to TrustSource and associate it with project <NAME>.

# Questions & Support

Please find further information at our [knowledgebase](https://support.trustsource.io) or contact [TrustSource Support](mailto:support@trustsource.io) for more questions.

Feel free to star, fork and improve. We are looking forward to get your feedback!
