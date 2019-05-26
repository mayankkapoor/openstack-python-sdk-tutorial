from flask import Flask, request
from openstack import connection
from pprint import pprint
import json
import os

app = Flask(__name__)
# Source the openstack project rc file before running this app, to create the
# environment variables needed
conn = connection.Connection(auth_url=os.environ['OS_AUTH_URL'],
                             project_name=os.environ['OS_PROJECT_NAME'],
                             username=os.environ['OS_USERNAME'],
                             password=os.environ['OS_PASSWORD'],
                             user_domain_id="default",
                             project_domain_id=os.environ['OS_PROJECT_DOMAIN_ID'])


@app.route("/")
def hello():
    return "Hello from Flask!"


@app.route("/list")
def list_openstack_resources():
    # Check if connection is established
    print("conn: ", conn)

    # Print list of servers, images, flavors, endpoints, projects, users
    server_list = list(conn.compute.servers())
    image_list = list(conn.compute.images())
    flavor_list = list(conn.compute.flavors())
    project_list = list(conn.identity.projects())
    user_list = list(conn.identity.users())
    pprint(server_list)
    pprint(image_list)
    pprint(flavor_list)
    pprint(project_list)
    pprint(user_list)

    return "List printed to stdout"


@app.route("/create_server")
def create_server():
    # Check if connection is established
    print("conn: ", conn)

    # Create the volume first
    volume_size = request.args.get('volume_size')
    print("Starting to create volume with size (in GiB): ", volume_size)
    volume = conn.create_volume(size=volume_size,
                                image="cirros-0.4.0-x86_64-disk",
                                wait=True,
                                bootable=True,
                                )
    print("Created volume: ", json.dumps(volume))

    # Create the server using the server_name parameter in the GET request
    server_name = request.args.get('server_name')
    print("Starting to create the server with name: ", server_name)
    server = conn.create_server(name=server_name,
                                flavor="m1.micro",
                                terminate_volume=True,
                                timeout=180,
                                boot_volume=volume.id,
                                key_name="mayank-public-key",
                                )
    print("Created server: ", json.dumps(server))

    return "Server create request sent!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
