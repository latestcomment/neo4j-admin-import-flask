
#! /bin/bash

export JAVA_OPTS='-server -Xms20g -Xmx20g'

./neo4j-admin import --database=Raka --force --delimiter=","  --skip-duplicate-nodes  --skip-bad-relationships  --ignore-empty-strings  --cache-on-heap  --high-io

--nodes=Customer=header1,/home/k/Documents/script/python_admin_import/customer/3.txt
                
--nodes=Customer=header1,/home/k/Documents/script/python_admin_import/customer/1.txt
                
--nodes=Customer=header1,/home/k/Documents/script/python_admin_import/customer/2.txt
                
--relationships=Rel1=rel_header1,/home/k/Documents/script/python_admin_import/header/3.txt
                
--relationships=Rel1=rel_header1,/home/k/Documents/script/python_admin_import/header/1.txt
                
--relationships=Rel1=rel_header1,/home/k/Documents/script/python_admin_import/header/2.txt
                