from enum import Enum


class Category(Enum):
    MEETING = 'zasadnutia'
    ANNOUNCEMENT = 'oznamy'
    NEWSLETTER = 'obecne-noviny'
    BUDGET = 'rozpocet'
    PROCUREMENT = 'verejne-obstaravanie'
    REPORT = 'hlasenie'
