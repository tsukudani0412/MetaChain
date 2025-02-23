from metachain.util import run_command_in_container
from .docker_env import DockerEnv
from metachain.io_utils import print_stream
def setup_metachain(workplace_name: str, env: DockerEnv):
    cmd = "pip list | grep metachain"
    response = env.run_command(cmd, print_stream)
    if response['status'] == 0:
        print("Metachain is already installed.")
        return
    cmd = f"cd /{workplace_name}/MetaChain && pip install -e ."
    response = env.run_command(cmd, print_stream)
    if response['status'] == 0:
        print("Metachain is installed.")
        return
    else:
        raise Exception(f"Failed to install metachain. {response['result']}")
