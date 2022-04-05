import click

from distutils.spawn import find_executable

from . import success
from .scanner import DockerScanner
from ts_python_client.client import Client



@click.command()
@click.option('--syft-path', default=None, help='Path to the Syft executable.')
@click.option('--apiKey', default='', help='API Key.')
@click.option('--projectName', default='', help='Project name.')
@click.option('--skipTransfer', default=False, is_flag=True, help='Skip transfer of results to the application.')
@click.option('--settingsFile', default='', help='Path to a settings file.')
@click.option('--outputFile', default='', help='Path to an output file.')
@click.argument('image', required=True)
def main(syft_path, apikey, projectname, skiptransfer, settingsfile, outputfile, image):
    sbom_tool = find_executable('syft', syft_path)

    if not sbom_tool:
        print('Cannot find Syft executable. Please ensure that the Syft tool is installed on your system or specify the path using \'--swift-path\' option.')
        print('For the installation instructions please refer to: https://github.com/anchore/syft#installation')
        exit(2)
    else:
        success('Found Syft: {}'.format(sbom_tool))

    scanner = DockerScanner(image, sbom_tool)
    tool = Client('ts-docker', scanner)

    tool.run(apiKey=apikey,
             projectName=projectname,
             skipTransfer=skiptransfer,
             settingsFile=settingsfile,
             outputFile=outputfile)