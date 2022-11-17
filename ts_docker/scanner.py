import tempfile
import subprocess

from typing import Tuple
from typing import List

from pathlib import Path
from docker.client import DockerClient
from docker.models.images import Image
from docker.errors import ImageNotFound, DockerException

from ts_python_client import Scan, Dependency, Scanner
from ts_spdx_import.importer import SPDXImporter

from . import info, success, fail


class DockerScanner(Scanner):
    def __init__(self, image: str, sbom_tool: str):
        """
        some comment
        """
        super().__init__()

        self.image = image
        self.sbom_tool = sbom_tool

    @property
    def is_folder_scanner(self):
        return False

    def run(self) -> Scan:
        scan = Scan(module=self.image, ns='docker')
        scan.type = 'docker'

        with tempfile.TemporaryDirectory() as tmpdir:
            scan.dependencies = self.scan(tmpdir)

        return scan

    def scan(self, tmpdir: str) -> [Dependency]:
        """
        scan action
        """
        image_data = None

        try:
            dockerApi = DockerClient()
            image_data = dockerApi.images.get(self.image)

        except DockerException as err:
            fail('Docker error: {}'.format(err))
            exit(2)

        except ImageNotFound:
            fail('Image not found: {}'.format(self.image))
            exit(2)

        success('Found image: {}'.format(image_data.short_id))
        info('Scanning image: {}'.format(image_data.short_id))

        image_scan = self.scan_image(tmpdir, self.image)

        name, vers = DockerScanner.parse_tag(image_data)

        dep = Dependency(key='docker:{}'.format(
            name), name=name, versions=vers)
        dep.meta = DockerScanner.build_metadata(image_data)
        dep.dependencies = image_scan.dependencies

        return [dep]

    def scan_image(self, tmpdir: str, image: str) -> Scan:
        output = Path('{}/{}.spdx.json'.format(tmpdir, image))
        cmd = [self.sbom_tool, image, '-o', 'spdx-json={}'.format(output)]

        subprocess.call(cmd, cwd=self.client.path)

        info('Parsing packages SPDX')

        return SPDXImporter.parse_doc(output)

    @staticmethod
    def parse_tag(image_data: Image) -> Tuple[str, List[str]]:
        name = ''
        versions = []

        for tag in image_data.tags:
            tag = tag.split(':')

            if not name:
                name = tag[0]

            if len(tag) == 2:
                versions.append(tag[1])

        return name, versions

    @staticmethod
    def build_metadata(image_data: Image) -> dict:
        attrs = image_data.attrs
        metadata = {
            'Id': attrs.get('Id'),
            'RepoTags': attrs.get('RepoTags'),
            'RepoDigests': attrs.get('RepoDigests'),
            'Architecture': attrs.get('Architecture'),
            'Os': attrs.get('Os'),
            'RootFS': attrs.get('RootFS')
        }

        return metadata
