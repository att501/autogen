import asyncio
from autogen_core import DefaultTopicId, MessageContext, RoutedAgent, message_handler, type_subscription
from _types import (
    ScrapeLeadsRequest,
    LeadDiscovered,
    SendEmail,
    OrderRequest,
)


@type_subscription("crm.leads.scrape")
class LeadScraperAgent(RoutedAgent):
    def __init__(self, description: str) -> None:
        super().__init__(description)

    @message_handler
    async def handle_scrape(self, message: ScrapeLeadsRequest, ctx: MessageContext) -> None:
        print(f"Scraping leads from: {message.page}")
        await asyncio.sleep(0.1)
        # Emit a dummy lead discovered event
        await self.publish_message(
            LeadDiscovered(name="Jane Doe", title="Estimator"),
            topic_id=DefaultTopicId(type="crm.leads.discovered"),
        )


@type_subscription("crm.email.send")
class EmailAgent(RoutedAgent):
    def __init__(self, description: str) -> None:
        super().__init__(description)

    @message_handler
    async def handle_email(self, message: SendEmail, ctx: MessageContext) -> None:
        print(f"EmailAgent sending email to {message.recipient}: {message.subject}")


@type_subscription("crm.order.new")
class OrderAgent(RoutedAgent):
    def __init__(self, description: str) -> None:
        super().__init__(description)

    @message_handler
    async def handle_order(self, message: OrderRequest, ctx: MessageContext) -> None:
        print(f"OrderAgent received order for {message.quantity} x {message.item}")


@type_subscription("crm.manager")
class ManagerAgent(RoutedAgent):
    def __init__(self, description: str) -> None:
        super().__init__(description)

    @message_handler
    async def handle_lead(self, message: LeadDiscovered, ctx: MessageContext) -> None:
        print(f"Manager received new lead: {message.name} - {message.title}")
        # respond by sending an email
        await self.publish_message(
            SendEmail(
                recipient="sales@example.com",
                subject="New Lead",
                body=f"Contact {message.name}"
            ),
            DefaultTopicId(type="crm.email.send"),
        )
