[![Gitter](https://badges.gitter.im/TrustSource/community.svg)](https://gitter.im/TrustSource/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

# TrustSource Docker scanner

# Prerequisites

**Syft** - a tool for generating a Software Bill of Materials (SBOM) from container images and filesystems. 
For the installation instruction, please, refer to https://github.com/anchore/syft .  

# Installation

- Clone repository
```shell
git clone https://github.com/TrustSource/ts-docker.git
```

- Install using PIP from the local directory
```shell
pip3 install ./ts-docker 
```

# Usage

## Help

```shell
ts-docker --help
```
```shell
Usage: ts-docker [OPTIONS] IMAGE

Options:
  --syft-path TEXT     Path to the Syft executable.
  --apiKey TEXT        API Key.
  --projectName TEXT   Project name.
  --skipTransfer       Skip transfer of results to the application.
  --settingsFile TEXT  Path to a settings file.
  --outputFile TEXT    Path to an output file.
  --help               Show this message and exit. 
```

## Prepare data without transfering 

```shell
ts-docker --skipTransfer <local Docker image name> 
```

## Prepare data and transfer to the TrustSource application  

```shell
ts-docker --apiKey <KEY> --projectName <NAME> <local Docker image name> 
```

# Questions & Support
Please see our [support offering](https://www.trustsource.io/support) or checkout the [knowledgebase](https://support.trustsource.io) for more information.
