import click
from common.logger import LOGGER
from plugin.meeting import MeetingPlugin
from plugin.announcement import AnnouncementPlugin
from plugin.newsletter import NewsletterPlugin
from plugin.budget import BudgetPlugin


@click.command()
def cli():
    return_code = 0
    LOGGER.info('Start')
    try:
        MeetingPlugin().run()
        AnnouncementPlugin().run()
        NewsletterPlugin().run()
        BudgetPlugin().run()
    except:
        return_code = 1

    LOGGER.info('Done')
    return return_code
