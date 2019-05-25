
# openstack-python-sdk-tutorial
Openstack Python SDK tutorial using Flask

## Assumptions:
* You have an existing openstack installation up and running.
* You have already downloaded the openrc.sh from Horizon for your project.

## Clone this repo and setup Flask virtualenv
```
$ git clone https://github.com/mayankkapoor/openstack-python-sdk-tutorial.git
$ cd openstack-python-sdk-tutorial
$ python3 -m venv venv # Create a virtualenv under directory venv
$ . venv/bin/activate # Activate virtualenv
(venv)$ pip install -r requirements.txt # Install necessary dependencies for the Flask app
```

## Source Openstack openrc.sh file
This repo has a file `flaskr/app.py` that runs a flask server on port 8080. It assumes the appropriate Openstack environment variables are already set in order for it to talk to Openstack. Therefore, download your openrc.sh file from your project in Horizon and source it. Assuming the openrc file is called demo-openrc.sh:
```
(venv)$ source demo-openrc.sh
Please enter your OpenStack Password for project demo as user demo:
<Enter your openstack password for user demo>
(venv)$ python flaskr/app.py
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 302-433-515
```

## Test if the app is working in your browser
Open http://localhost:8080/ in your browser, it should print "Hello from Flask!".

## Generate a list of resources in openstack.
Open http://localhost:8080/list in your browser. This will print a list of current resources in your openstack on the terminal where you started the Flask app.

```
...
* Debugger PIN: 283-629-770
49.36.1.41 - - [25/May/2019 14:22:33] "GET / HTTP/1.1" 200 -
conn:  <openstack.connection.Connection object at 0x7fc49a235198>
[{'access_ipv4': '',
 'access_ipv6': '',
 'addresses': {'private': [{'OS-EXT-IPS-MAC:mac_addr': 'fa:16:3e:1a:d3:63',
                            'OS-EXT-IPS:type': 'fixed',
                            'addr': '10.0.0.19',
                            'version': 4},
                           {'OS-EXT-IPS-MAC:mac_addr': 'fa:16:3e:1a:d3:63',
                            'OS-EXT-IPS:type': 'fixed',
                            'addr': 'fd0d:1d87:b84d:0:f816:3eff:fe1a:d363',
                            'version': 6}]},
 'admin_password': None,
 'attached_volumes': [{'id': 'cefdec32-abbd-4ad6-bd52-3b457d1e42be'}],
 'availability_zone': 'nova',
 'block_device_mapping': None,
 'compute_host': 'ip-172-31-7-51',
 'config_drive': '',
 'created_at': '2019-05-25T11:06:31Z',
 'description': None,
 'disk_config': 'AUTO',
 'flavor': {'id': '84',
            'links': [{'href': 'http://172.31.7.51/compute/flavors/84',
                       'rel': 'bookmark'}]},
 'flavor_id': None,
 'id': '0649ea9e-b4da-4d1e-a82c-7bfa33a0470d',
 'instance_name': 'instance-00000001',
 'is_locked': None,
 'kernel_id': None,
 'key_name': 'mayank-public-key',
 'name': 'first-instance',
 'networks': None,
...
```

Congratulations, you've connected to openstack using the Openstack SDK. Now, let's try to create and delete a virtual machine (server).
