from this import d
from flask import Flask, render_template,request, redirect, url_for

from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route("/validation")
def validation():
    
    f = open ('run.sh', 'r')
    a = f.read()

    f.close()
    
    return a

@app.route("/config", methods=["GET","POST"])
def configuration():
    if request.method == "POST":
        ram = request.form.get("ram")
        db_name = request.form.get("db_name")
        sep = request.form.get("sep")
        
        ######################################################
        skip_duplicate_nodes = request.form.get("skip_duplicate_nodes")
        skip_bad_relationships = request.form.get("skip_bad_relationships")
        ignore_empty_strings = request.form.get("ignore_empty_strings")
        chache_on_heap = request.form.get("chache_on_heap")
        high_io = request.form.get("high_io")

        if skip_duplicate_nodes is not None:
            skip_duplicate_nodes=' --skip-duplicate-nodes'
        else:
            skip_duplicate_nodes=''

        if skip_bad_relationships is not None:
            skip_bad_relationships=' --skip-bad-relationships'
        else:
            skip_bad_relationships=''

        if ignore_empty_strings is not None:
            ignore_empty_strings=' --ignore-empty-strings'
        else:
            ignore_empty_strings=''

        if chache_on_heap is not None:
            chache_on_heap=' --cache-on-heap'
        else:
            chache_on_heap=''

        if high_io is not None:
            high_io=' --high-io'
        else:
            high_io=''
        

        f = open('run.sh', 'w')
        script = f'''
#! /bin/bash

export JAVA_OPTS='-server -Xms{ram}g -Xmx{ram}g'

./neo4j-admin import --database={db_name} --force --delimiter="{sep}" {skip_duplicate_nodes} {skip_bad_relationships} {ignore_empty_strings} {chache_on_heap} {high_io}
'''
        f.write(script)
        f.close()

        # Node
        node_label = request.form.getlist("node_label[]")
        node_data_dir = request.form.getlist("node_data_dir[]")
        node_header_dir = request.form.getlist("node_header_dir[]")

        # Relationship
        rel_type = request.form.getlist("rel_type[]")
        rel_data_dir = request.form.getlist("rel_data_dir[]")
        rel_header_dir = request.form.getlist("rel_header_dir[]")


        node_data_dir_var = []
        rel_data_dir_var = []
        for i in range(0, len(node_data_dir)):
            node_data_dir_file = [f for f in listdir(node_data_dir[i]) if isfile(join(node_data_dir[i], f))]
            rel_data_dir_file = [f for f in listdir(rel_data_dir[i]) if isfile(join(rel_data_dir[i], f))]

            node_data_dir_var_list = []
            for j in node_data_dir_file:
                node_data_dir_var_list.append(node_data_dir[i] + '/' + j)
            
            node_data_dir_var.append(node_data_dir_var_list)
            
            rel_data_dir_var_list = []
            for k in rel_data_dir_file:
                rel_data_dir_var_list.append(rel_data_dir[i] + '/' + k)
            
            rel_data_dir_var.append(rel_data_dir_var_list)

        node = []
        for i in range(0, len(node_label)):
            
            for j in node_data_dir_var[i]:
                node_str = f'''
--nodes={node_label[i]}={node_header_dir[i]},{j}
                '''
                node.append(node_str)
                
        f_node = open("run.sh","a")
        for i in range(0, len(node)):
            f_node.write(node[i])
        
        f_node.close()

        rel = []
        for i in range(0, len(rel_type)):
            
            for j in rel_data_dir_var[i]:
                rel_str = f'''
--relationships={rel_type[i]}={rel_header_dir[i]},{j}
                '''
                rel.append(rel_str)
        
        
        f_rel = open("run.sh","a")
        for i in range(0, len(rel)):
            f_rel.write(rel[i])
        
        f_rel.close()
            
        return redirect(url_for("validation"))
    else:
        return render_template("layout.html")
    
if __name__ == "__main__":
    app.run(debug=True)