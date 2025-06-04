from dataclasses import dataclass
from typing import Dict

from pydantic import BaseModel


@dataclass
class ScrapeLeadsRequest:
    page: str


@dataclass
class LeadDiscovered:
    name: str
    title: str


@dataclass
class SendEmail:
    recipient: str
    subject: str
    body: str


@dataclass
class OrderRequest:
    item: str
    quantity: int


class HostConfig(BaseModel):
    hostname: str
    port: int

    @property
    def address(self) -> str:
        return f"{self.hostname}:{self.port}"


class AgentConfig(BaseModel):
    topic_type: str
    description: str


class AppConfig(BaseModel):
    host: HostConfig
    lead_scraper: AgentConfig
    email_agent: AgentConfig
    order_agent: AgentConfig
    manager_agent: AgentConfig
    client_config: Dict[str, str] | None = None
