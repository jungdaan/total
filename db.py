from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///result.db', echo=True)

Base = declarative_base()


class DNS(Base):
    __tablename__ = 'dns'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ttl = Column(Integer, nullable=False)
    type = Column(String(100), nullable=False)
    data = Column(String(100), nullable=False)

    def __init__(self, name, ttl, typ, data):
        self.name = name
        self.ttl = ttl
        self.type = typ
        self.data = data

    def __repr__(self):
        return "<DNS %s>" % self.name


class Kakao(Base):
    __tablename__ = 'kakao'
    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return "<Kakao %s>" % self.url


class MailList(Base):
    __tablename__ = 'maillist'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    title = Column(String(100), nullable=False)
    sender = Column(String(50), nullable=False)
    receiver = Column(String(50), nullable=False)

    def __init__(self, username, title, sender, receiver):
        self.username = username
        self.title = title
        self.sender = sender
        self.receiver = receiver

    def __repr__(self):
        return "<MailList %s>" % self.username


class MailSize(Base):
    __tablename__ = 'mailsize'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    title = Column(String(100), nullable=False)
    size = Column(String(50), nullable=False)
    folderName = Column(String(50), nullable=False)
    unreadCount = Column(String(100), nullable=False)
    totalCount = Column(String(50), nullable=False)

    def __init__(self, username, title, size, folderName, unreadCount, totalCount):
        self.username = username
        self.title = title
        self.size = size
        self.folderName = folderName
        self.unreadCount = unreadCount
        self.totalCount = totalCount

    def __repr__(self):
        return "<MailSize %s>" % self.username


Session = sessionmaker()
Session.configure(bind=engine)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    session = Session()
    session.add(Kakao("testurl"))
    session.commit()
