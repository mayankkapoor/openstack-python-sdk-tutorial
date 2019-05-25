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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
