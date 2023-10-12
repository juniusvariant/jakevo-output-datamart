import argparse
from contextlib import asynccontextmanager
from typing import Any

from cassandra.cluster import Cluster
from cassandra.cqlengine import connection


def argument_parser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--hosts",
                        help="ScyllaDB node address",
                        required=True, default="localhost")
    parser.add_argument("-u", "--username",
                        help="Password based authentication username")
    parser.add_argument("-p", "--password",
                        help="Password based authentication password")
    parser.add_argument("-d", "--datacenter",
                        help="Local data center")
    return parser


@asynccontextmanager
async def lifespan(_: Any) -> None:
    # ddl = "CREATE KEYSPACE IF NOT EXISTS ks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}"
    # session.execute(ddl)
    session = Cluster(
        [
            "localhost",
        ]
    ).connect()

    connection.register_connection("cluster1", session=session, default=True)
    # management.sync_table(model=User, keyspaces=("ks",))

    # users = [User(id=uuid.uuid4(), name=faker.name(), email=faker.email())
    #          for _ in range(100)]
    # for user in users:
    #     user.save()
    yield
