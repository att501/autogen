import asyncio
from _types import HostConfig
from _utils import load_config
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntimeHost
from rich.console import Console
from rich.markdown import Markdown


async def main(cfg: HostConfig) -> None:
    host = GrpcWorkerAgentRuntimeHost(address=cfg.address)
    host.start()
    Console().print(Markdown(f"`CRM Host` running at **{cfg.address}**"))
    await host.stop_when_signal()


if __name__ == "__main__":
    asyncio.run(main(load_config().host))
