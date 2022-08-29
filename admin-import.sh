#!/bin/bash

export JAVA_OPTS='-server -Xms20g -Xmx20g'

./neo4j-admin import --database=dev-demo --force --delimiter="," --skip-duplicate-nodes --skip-bad-relationships --ignore-empty-strings=true \
--nodes=Customer=/home/neo4j/neo4j-enterprise-4.4.9/import/header/cusinfo.txt,/home/neo4j/neo4j-enterprise-4.4.9/import/data/202104/cusinfo/cusinfo_202104_final.txt \
--nodes=Account=/home/neo4j/neo4j-enterprise-4.4.9/import/header/dpk_final.txt,/home/neo4j/neo4j-enterprise-4.4.9/import/data/202104/dpk_final/dpk_final_20210430_final.txt \
--relationships=HAS_ACCOUNT=/home/neo4j/neo4j-enterprise-4.4.9/import/header/rel_has_account_dpk_final.txt,/home/neo4j/neo4j-enterprise-4.4.9/import/data/202104/dpk_final/dpk_final_20210430_final.txt \
--relationships=HAS_ACCOUNT=/home/neo4j/neo4j-enterprise-4.4.9/import/header/rel_has_account_kredit_final.txt,/home/neo4j/neo4j-enterprise-4.4.9/import/data/202104/kredit_final/kredit_final_202104_final.txt \