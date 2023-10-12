from cassandra.cqlengine import columns, models


class Owners(models.Model):
    __keyspace__ = "output_marts"

    owner_id = columns.UUID(partition_key=True)
    identity_number = columns.Text(primary_key=True)
    name = columns.Text()
    email = columns.Text()
    phone = columns.Text()
    address = columns.Text()
    village = columns.Text()
    district = columns.Text()
    city = columns.Text()
    province = columns.Text(index=True, clustering_order="ASC")
    owner_type = columns.Text()


class Applicants(models.Model):
    __keyspace__ = "output_marts"

    applicant_id = columns.UUID(partition_key=True)
    identity_number = columns.Text(primary_key=True)
    name = columns.Text()
    email = columns.Text()
    phone = columns.Text()
    address = columns.Text()
    village = columns.Text()
    district = columns.Text()
    city = columns.Text()
    province = columns.Text(index=True, clustering_order="ASC")


class Permits(models.Model):
    __keyspace__ = "output_marts"

    permit_id = columns.UUID(primary_key=True, partition_key=True)
    jakevo_permit_code = columns.Text()
    oss_permit_id = columns.Text()
    oss_permit_name = columns.Text()
    name = columns.Text()
    sector = columns.Text(index=True, clustering_order="ASC")


class Outputs(models.Model):
    __keyspace__ = "output_marts"

    output_id = columns.UUID(partition_key=True)
    decree_number = columns.Text(primary_key=True)
    owner_identity_number = columns.Text(primary_key=True)
    owner_name = columns.Text()
    applicant_identity_number = columns.Text()
    applicant_name = columns.Text()
    applicant_email = columns.Text()
    application_date = columns.Date()
    issued_date = columns.Date()
    expired_date = columns.Date()
    permit_type = columns.Text()
    application_type = columns.Text()
    permit_id = columns.Text()
    permit_name = columns.Text()
    permit_sector = columns.Text()
    authority = columns.Text()
    jurisdiction = columns.Text(index=True)
    data_source = columns.Text(index=True, clustering_order="ASC")


class Output_Files(models.Model):
    __keyspace__ = "output_marts"

    file_id = columns.UUID(primary_key=True, partition_key=True)
    output_id = columns.UUID(primary_key=True)
    decree_number = columns.Text(primary_key=True)
    owner_identity_number = columns.Text(primary_key=True)
    issued_date = columns.Date(index=True)
    expired_date = columns.Date()
    file_location = columns.Text(),
    data_source = columns.Text(index=True, clustering_order="ASC")


class Request_Logs(models.Model):
    __keyspace__ = "output_marts"

    log_id = columns.UUID(primary_key=True, partition_key=True)
    request_body = columns.Text()
    request_date = columns.DateTime(index=True)
    request_by = columns.UUID(primary_key=True)


class Clients(models.Model):
    __keyspace__ = "output_marts"

    client_id = columns.UUID(primary_key=True, partition_key=True)
    name = columns.Text()
    nick = columns.Text(primary_key=True)
    pic_name = columns.Text()
    pic_email = columns.Text()
    pic_phone = columns.Text()


class User(models.Model):
    __keyspace__ = "ks"

    id = columns.UUID(primary_key=True, partition_key=True)
    name = columns.Text()
    email = columns.Text(primary_key=True)
    registered_at = columns.DateTime()


# Materialized View Models


class Owner_By_Identitynumber(models.Model):
    __keyspace__ = "output_marts"

    owner_id = columns.UUID()
    identity_number = columns.Text(primary_key=True)
    name = columns.Text()
    email = columns.Text(primary_key=True)
    phone = columns.Text()
    address = columns.Text()
    village = columns.Text()
    district = columns.Text()
    city = columns.Text()
    province = columns.Text(index=True, clustering_order="ASC")
    owner_type = columns.Text()


class Applicant_By_Identitynumber(models.Model):
    __keyspace__ = "output_marts"

    applicant_id = columns.UUID()
    identity_number = columns.Text(primary_key=True)
    name = columns.Text()
    email = columns.Text(primary_key=True)
    phone = columns.Text()
    address = columns.Text()
    village = columns.Text()
    district = columns.Text()
    city = columns.Text()
    province = columns.Text(index=True, clustering_order="ASC")


class Permit_By_Jakevocode(models.Model):
    __keyspace__ = "output_marts"

    permit_id = columns.UUID()
    jakevo_permit_code = columns.Text(primary_key=True)
    oss_permit_id = columns.Text()
    oss_permit_name = columns.Text()
    name = columns.Text()
    sector = columns.Text(index=True, clustering_order="ASC")


class Output_By_Decreeidentity(models.Model):
    __keyspace__ = "output_marts"

    output_id = columns.UUID()
    decree_number = columns.Text(primary_key=True)
    owner_identity_number = columns.Text(primary_key=True)
    owner_name = columns.Text()
    applicant_identity_number = columns.Text()
    applicant_name = columns.Text()
    applicant_email = columns.Text(primary_key=True)
    application_date = columns.Date()
    issued_date = columns.Date()
    expired_date = columns.Date()
    permit_type = columns.Text()
    application_type = columns.Text()
    permit_id = columns.Text()
    permit_name = columns.Text()
    permit_sector = columns.Text()
    authority = columns.Text()
    jurisdiction = columns.Text(index=True)
    data_source = columns.Text(index=True, clustering_order="ASC")


class Output_File_By_Decreeidentity(models.Model):
    __keyspace__ = "output_marts"

    file_id = columns.UUID()
    output_id = columns.UUID()
    decree_number = columns.Text(primary_key=True)
    owner_identity_number = columns.Text(primary_key=True)
    issued_date = columns.Date(index=True)
    expired_date = columns.Date()
    file_location = columns.Text(),
    data_source = columns.Text(index=True, clustering_order="ASC")


class Client_By_Nickmail(models.Model):
    __keyspace__ = "output_marts"

    client_id = columns.UUID()
    name = columns.Text()
    nick = columns.Text(primary_key=True)
    pic_name = columns.Text()
    pic_email = columns.Text(primary_key=True)
    pic_phone = columns.Text()


class User_By_Identitynumber(models.Model):
    __keyspace__ = "ks"

    identity_number = columns.Text(primary_key=True, index=True)
    name = columns.Text()
    email = columns.Text(primary_key=True, index=True)
    registered_at = columns.DateTime()
    id = columns.UUID()
