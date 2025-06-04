import asyncio
import logging
from _agents import LeadScraperAgent
from _types import AppConfig, ScrapeLeadsRequest
from _utils import load_config
from autogen_core import TypeSubscription
from autogen_ext.runtimes.grpc import GrpcWorkerAgentRuntime


async def main(config: AppConfig) -> None:
    runtime = GrpcWorkerAgentRuntime(host_address=config.host.address)
    await runtime.start()
    agent_type = await LeadScraperAgent.register(
        runtime,
        config.lead_scraper.topic_type,
        lambda: LeadScraperAgent(config.lead_scraper.description),
    )
    await runtime.add_subscription(
        TypeSubscription(topic_type=config.lead_scraper.topic_type, agent_type=agent_type.type)
    )
    await runtime.stop_when_signal()


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    asyncio.run(main(load_config()))
