

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_FIXEDASSETSINVEST(Base):
    __tablename__ = "MAC_FIXEDASSETSINVEST"

    DECLAREDATE = Column(DateTime)
    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True)
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    CAPITALCONSTRUCT = Column(Numeric(18, 4))
    TRANSPORTPURCHASE = Column(Numeric(18, 4))
    INNOVATE = Column(Numeric(18, 4))
    REALESTATE = Column(Numeric(18, 4))
    OTHERINVEST = Column(Numeric(18, 4))
    STATEOWNED = Column(Numeric(18, 4))
    RESIDENTINVEST = Column(Numeric(18, 4))
    PRIMARY = Column(Numeric(18, 4))
    SECONDARY = Column(Numeric(18, 4))
    TERTIARY = Column(Numeric(18, 4))
    CENTREPROJECT = Column(Numeric(18, 4))
    LOCALPROJECT = Column(Numeric(18, 4))
    NEWCONSTRUCT = Column(Numeric(18, 4))
    EXPAND = Column(Numeric(18, 4))
    RECONSTRUCT = Column(Numeric(18, 4))
    CONSTRUCTINSTALL = Column(Numeric(18, 4))
    EQUIPMENTPURCHASE = Column(Numeric(18, 4))
    OTHEREXPENSE = Column(Numeric(18, 4))
    TOTALSOURCE = Column(Numeric(18, 4))
    STATEBUDGET = Column(Numeric(18, 4))
    DOMESTICLOAN = Column(Numeric(18, 4))
    BOND = Column(Numeric(18, 4))
    FOREIGNINVEST = Column(Numeric(18, 4))
    FDI = Column(Numeric(18, 4))
    SELFRAISEDFUND = Column(Numeric(18, 4))
    ENTERPRISEFUND = Column(Numeric(18, 4))
    ISSUESHARE = Column(Numeric(18, 4))
    OTHERFUND = Column(Numeric(18, 4))
    VARIOUSDUE = Column(Numeric(18, 4))
    PROJECTFUND = Column(Numeric(18, 4))
    CONSTRUCTAREA = Column(Numeric(18, 4))
    RESIDENTCONSTRUCTAREA = Column(Numeric(18, 4))
    COMPLETEAREA = Column(Numeric(18, 4))
    RESIDENTCOMPLETEAREA = Column(Numeric(18, 4))
    NEWFIXEDASSETS = Column(Numeric(18, 4))
    FIXEDASSETSINVESTYOY = Column(Numeric(10, 4))
    CAPITALCONSTRUCTYOY = Column(Numeric(10, 4))
    TRANSPORTPURCHASEYOY = Column(Numeric(10, 4))
    INNOVATEYOY = Column(Numeric(10, 4))
    REALESTATEYOY = Column(Numeric(10, 4))
    OTHERINVESTYOY = Column(Numeric(10, 4))
    STATEOWNEDYOY = Column(Numeric(10, 4))
    RESIDENTINVESTYOY = Column(Numeric(10, 4))
    PRIMARYYOY = Column(Numeric(10, 4))
    SECONDARYYOY = Column(Numeric(10, 4))
    TERTIARYYOY = Column(Numeric(10, 4))
    CENTREPROJECTYOY = Column(Numeric(10, 4))
    LOCALPROJECTYOY = Column(Numeric(10, 4))
    NEWCONSTRUCTYOY = Column(Numeric(10, 4))
    EXPANDYOY = Column(Numeric(10, 4))
    RECONSTRUCTYOY = Column(Numeric(10, 4))
    CONSTRUCTINSTALLYOY = Column(Numeric(10, 4))
    EQUIPMENTPURCHASEYOY = Column(Numeric(10, 4))
    OTHEREXPENSEYOY = Column(Numeric(10, 4))
    TOTALSOURCEYOY = Column(Numeric(10, 4))
    STATEBUDGETYOY = Column(Numeric(10, 4))
    DOMESTICLOANYOY = Column(Numeric(10, 4))
    BONDYOY = Column(Numeric(10, 4))
    FOREIGNINVESTYOY = Column(Numeric(10, 4))
    FDIYOY = Column(Numeric(10, 4))
    SELFRAISEDFUNDYOY = Column(Numeric(10, 4))
    ENTERPRISEFUNDYOY = Column(Numeric(10, 4))
    ISSUESHAREYOY = Column(Numeric(10, 4))
    OTHERFUNDYOY = Column(Numeric(10, 4))
    VARIOUSDUEYOY = Column(Numeric(10, 4))
    PROJECTFUNDYOY = Column(Numeric(10, 4))
    CONSTRUCTAREAYOY = Column(Numeric(10, 4))
    RESIDENTCONSTRUCTAREAYOY = Column(Numeric(10, 4))
    COMPLETEAREAYOY = Column(Numeric(10, 4))
    RESIDENTCOMPLETEAREAYOY = Column(Numeric(10, 4))
    NEWFIXEDASSETSYOY = Column(Numeric(10, 4))
    FIXEDASSETSINVESTMOM = Column(Numeric(10, 4))