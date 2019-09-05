from datetime import datetime
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from sqlalchemy.orm.collections import attribute_mapped_collection

from . import db


class SerializableMixin(object):
    def _serialize(self):
        """Jsonify the sql alchemy query result."""
        convert = dict()
        d = dict()
        # noinspection PyUnresolvedReferences
        for c in self.__class__.__table__.columns:
            v = getattr(self, c.name)
            if c.type in convert.keys() and v is not None:
                try:
                    d[c.name] = convert[c.type](v)
                except:
                    d[c.name] = "Error: Failed to covert using ", str(convert[c.type])
            elif v is None:
                if (
                    hasattr(c.type, "__visit_name__")
                    and c.type.__visit_name__ == "JSON"
                ):
                    d[c.name] = None
                elif "INTEGER" == str(c.type) or "NUMERIC" == str(c.type):
                    # print "??"
                    d[c.name] = 0
                elif "DATETIME" == str(c.type):
                    d[c.name] = None
                else:
                    # print c.type
                    d[c.name] = str()
            elif isinstance(v, datetime):
                if v.utcoffset() is not None:
                    v = v - v.utcoffset()
                d[c.name] = v.strftime("%Y-%m-%d %H:%M:%S")
            else:
                d[c.name] = v
        return d

    def json(self):
        raise NotImplementedError()


class User(SerializableMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    twitch_id = db.Column(db.String(100), nullable=False, unique=True)

    def json(self):
        data = self._serialize()
        return data

class TwitchOAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = "twitch_oauth"

class GithubOAuth(OAuthConsumerMixin, db.Model):
    __tablename__ = "github_oauth"