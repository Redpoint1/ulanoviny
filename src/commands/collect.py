import click
from common.logger import LOGGER
from plugin.meeting import MeetingPlugin
from plugin.announcement import AnnouncementPlugin
from plugin.newsletter import NewsletterPlugin
from plugin.budget import BudgetPlugin
from plugin.procurement import ProcurementPlugin
from plugin.report import ReportPlugin
from plugin.order import OrderPlugin


@click.command()
def cli():
    return_code = 0
    LOGGER.info('Start')

    MeetingPlugin().run()
    AnnouncementPlugin().run()
    NewsletterPlugin().run()
    BudgetPlugin().run()
    ProcurementPlugin().run()
    ReportPlugin().run()
    OrderPlugin().run()

    LOGGER.info('Done')
    return return_code
