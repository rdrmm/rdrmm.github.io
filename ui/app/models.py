from datetime import datetime
import uuid
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Text,
    Index,
    JSON,
)
from sqlalchemy.orm import relationship, declarative_base


def gen_uuid():
    return str(uuid.uuid4())


Base = declarative_base()


class Organization(Base):
    __tablename__ = "organizations"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    name = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    active = Column(Boolean, default=True)
    users = relationship("User", back_populates="organization")
    groups = relationship("Group", back_populates="organization")
    devices = relationship("Device", back_populates="organization")


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False)
    email = Column(String(320), nullable=False)
    full_name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    organization = relationship("Organization", back_populates="users")
    memberships = relationship("Membership", back_populates="user")
    logs = relationship("Log", back_populates="user")
    __table_args__ = (Index("ix_users_org_email", "organization_id", "email", unique=True),)


class Group(Base):
    __tablename__ = "groups"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    organization = relationship("Organization", back_populates="groups")
    memberships = relationship("Membership", back_populates="group")
    devices = relationship("Device", back_populates="group")
    __table_args__ = (Index("ix_groups_org_name", "organization_id", "name", unique=True),)


class Membership(Base):
    __tablename__ = "memberships"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    group_id = Column(String(36), ForeignKey("groups.id"), nullable=True)
    role = Column(String(50), default="member")
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="memberships")
    group = relationship("Group", back_populates="memberships")
    __table_args__ = (Index("ix_memberships_user_group", "user_id", "group_id", unique=True),)


class Device(Base):
    __tablename__ = "devices"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False)
    group_id = Column(String(36), ForeignKey("groups.id"), nullable=True)
    name = Column(String(255))
    metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)
    organization = relationship("Organization", back_populates="devices")
    group = relationship("Group", back_populates="devices")
    logs = relationship("Log", back_populates="device")
    __table_args__ = (Index("ix_devices_org_name", "organization_id", "name"),)


class Log(Base):
    __tablename__ = "logs"
    id = Column(String(36), primary_key=True, default=gen_uuid)
    organization_id = Column(String(36), ForeignKey("organizations.id"), nullable=False)
    device_id = Column(String(36), ForeignKey("devices.id"), nullable=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=True)
    level = Column(String(20), default="info")
    message = Column(Text)
    payload = Column(JSON, default={})
    timestamp = Column(DateTime, default=datetime.utcnow)
    organization = relationship("Organization")
    device = relationship("Device", back_populates="logs")
    user = relationship("User", back_populates="logs")
    __table_args__ = (Index("ix_logs_org_timestamp", "organization_id", "timestamp"),)
