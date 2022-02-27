from enum import Enum


class Category(Enum):
    MEETING = 'zasadnutia'
    ANNOUNCEMENT = 'oznamy'
    NEWSLETTER = 'obecne-noviny'
    BUDGET = 'rozpocet'
    PROCUREMENT = 'verejne-obstaravanie'
    REPORT = 'hlasenie'
    ORDER = 'objednavky'
    INVOICE = 'faktury'
    CONTRACT = 'zmluvy'
    TABLE = 'dokumenty-uradna-tabula'
    RESOLUTION = 'dokumenty-uznesenia'
    TRANSCRIPT = 'dokumenty-zapisnice'
    VZN = 'dokumenty-vzn'
