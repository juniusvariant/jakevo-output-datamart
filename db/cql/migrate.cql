CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.owners_by_identitynumber AS
    SELECT * FROM owners
    WHERE owner_id IS NOT NULL AND identity_number IS NOT NULL AND name IS NOT NULL
    PRIMARY KEY (identity_number, name, owner_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.applicants_by_identitynumber AS
    SELECT * FROM applicants
    WHERE applicant_id IS NOT NULL AND identity_number IS NOT NULL AND name IS NOT NULL
    PRIMARY KEY (identity_number, name, applicant_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.permits_by_jakevocode AS
    SELECT * FROM permits
    WHERE permit_id IS NOT NULL AND jakevo_permit_code IS NOT NULL AND oss_permit_id IS NOT NULL
    PRIMARY KEY (jakevo_permit_code,sector, permit_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.outputs_by_decreeowner AS
    SELECT * FROM outputs
    WHERE output_id IS NOT NULL AND decree_number IS NOT NULL AND owner_identity_number IS NOT NULL AND applicant_identity_number IS NOT NULL
    PRIMARY KEY (decree_number, owner_identity_number, output_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.output_files_by_decreeidentity AS
    SELECT * FROM output_files
    WHERE file_id IS NOT NULL AND output_id IS NOT NULL AND decree_number IS NOT NULL AND owner_identity_number IS NOT NULL
    PRIMARY KEY (decree_number, owner_identity_number, file_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.request_logs_by_requestbydate AS
    SELECT * FROM request_logs
    WHERE log_id IS NOT NULL AND request_body IS NOT NULL AND request_date IS NOT NULL AND request_by IS NOT NULL
    PRIMARY KEY (request_by, request_date, log_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS output_marts.clients_by_nicmail AS
    SELECT * FROM clients
    WHERE client_id IS NOT NULL AND name IS NOT NULL AND nick IS NOT NULL AND pic_name IS NOT NULL
    PRIMARY KEY (nick, pic_email, client_id)
;

CREATE MATERIALIZED VIEW IF NOT EXISTS ks.user_by_identitynumber AS
    SELECT * FROM user
    WHERE id IS NOT NULL AND identity_number IS NOT NULL AND name IS NOT NULL AND email IS NOT NULL AND registered_at IS NOT NULL
    PRIMARY KEY (identity_number, email, id)
;