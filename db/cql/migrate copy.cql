CREATE TABLE IF NOT EXISTS output_marts.owners
(
    owner_id          UUID,
    identity_number   TEXT,
    name              TEXT,
    email             TEXT,
    phone             TEXT,
    address           TEXT,
    village           TEXT,
    district          TEXT,
    city              TEXT,
    province          TEXT,
    owner_type        TEXT,
    PRIMARY KEY ((owner_id, identity_number), province)
);

CREATE TABLE IF NOT EXISTS output_marts.applicants
(
    applicant_id      UUID,
    identity_number   TEXT,
    name              TEXT,
    email             TEXT,
    phone             TEXT,
    address           TEXT,
    village           TEXT,
    district          TEXT,
    city              TEXT,
    province          TEXT,
    PRIMARY KEY ((applicant_id, identity_number), province)
);

CREATE TABLE IF NOT EXISTS output_marts.permits
(
    permit_id           UUID,
    jakevo_permit_code  TEXT,
    oss_permit_id       TEXT,
    oss_permit_name     TEXT,
    name                TEXT,
    sector              TEXT,
    PRIMARY KEY ((permit_id), sector)
);

CREATE TABLE IF NOT EXISTS output_marts.outputs
(
    output_id                     UUID,
    decree_number                 TEXT,
    owner_identity_number         TEXT,
    owner_name                    TEXT,
    applicant_identity_number     TEXT,
    applicant_name                TEXT,
    applicant_email               TEXT,
    application_date              DATE,
    issued_date                   DATE,
    expired_date                  DATE,
    permit_type                   TEXT,
    application_type              TEXT,
    permit_id                     TEXT,
    permit_name                   TEXT,
    permit_sector                 TEXT,
    authority                     TEXT,
    jurisdiction                  TEXT,
    data_source                   TEXT,
    PRIMARY KEY ((output_id, decree_number, owner_identity_number), jurisdiction, data_source)
);

CREATE TABLE IF NOT EXISTS output_marts.output_files
(
    file_id         UUID,
    output_id       UUID,
    decree_number   TEXT,
    identity_number TEXT,
    issued_date     TEXT,
    expired_date    TEXT,
    file_location   TEXT,
    data_source     TEXT,
    PRIMARY KEY ((file_id, output_id, decree_number, identity_number), issued_date, data_source)
);

CREATE TABLE IF NOT EXISTS output_marts.request_logs
(
    log_id       UUID,
    request_body TEXT,
    request_date TIMESTAMP,
    request_by   UUID,
    PRIMARY KEY ((log_id,request_by), request_date)
);

CREATE TABLE IF NOT EXISTS output_marts.clients
(
    client_id   UUID,
    name        TEXT,
    nick        TEXT,
    pic_name    TEXT,
    pic_email   TEXT,
    pic_phone   TEXT,
    PRIMARY KEY (client_id, nick)
);