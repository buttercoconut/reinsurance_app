from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    reinsurer_name = Column(String, nullable=False)
    primary_insurer_name = Column(String, nullable=False)
    effective_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=False)
    premium = Column(Numeric(12, 2), nullable=False)
    risk_limit = Column(Numeric(12, 2), nullable=False)
    status = Column(String, default="active")

    # relationships
    claims = relationship("Claim", back_populates="contract")

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"))
    claim_date = Column(Date, nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    status = Column(String, default="submitted")

    contract = relationship("Contract", back_populates="claims")
