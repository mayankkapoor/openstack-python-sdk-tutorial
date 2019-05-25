from flask import Flask
from openstack import connection
from pprint import pprint
import os

app = Flask(__name__)
# Source the openstack project rc file before running this app, to create the
# environment variables needed
conn = connection.Connection(auth_url=os.environ['OS_AUTH_URL'],
                             project_name="demo", username="admin",
                             password="mayank@123",
                             user_domain_id="default",
                             project_domain_id="default")


@app.route("/")
def hello():
    return "Hello from Flask!"


@app.route("/list")
def list_openstack_resources():
    # Check if connection is established
    print("conn: ", conn)

    # Print list of servers, images, flavors, endpoints, projects, users
    for server in conn.compute.servers():
        print("server.name: ", server.name)
    for image in conn.compute.images():
        print("image.name: ", image.name)
    for flavor in conn.compute.flavors():
        print("flavor.name: ", flavor.name)
    for endpoint in conn.identity.endpoints():
        print("endpoint: ", endpoint)
    for project in conn.identity.projects():
        print("project: ", project)
    for user in conn.identity.users():
        print("user: ", user)

    return "List printed to stdout"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
