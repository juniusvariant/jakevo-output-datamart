from contextlib import asynccontextmanager
from typing import Any
from db.dataModels import Owners, Applicants, Permits, Outputs, Output_Files, Request_Logs, Clients

from cassandra.cluster import Cluster
from cassandra.cqlengine import connection, management


@asynccontextmanager
async def lifespan(_: Any) -> None:
    session = Cluster(
        [
            "localhost",
        ]
    ).connect()

    ddl = "CREATE KEYSPACE IF NOT EXISTS output_marts WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }"
    session.execute(ddl)

    connection.register_connection("cluster1", session=session, default=True)

    management.sync_table(model=Owners, keyspaces=("output_marts",))
    management.sync_table(model=Applicants, keyspaces=("output_marts",))
    management.sync_table(model=Permits, keyspaces=("output_marts",))
    management.sync_table(model=Outputs, keyspaces=("output_marts",))
    management.sync_table(model=Output_Files, keyspaces=("output_marts",))
    management.sync_table(model=Request_Logs, keyspaces=("output_marts",))
    management.sync_table(model=Clients, keyspaces=("output_marts",))

    yield
