# ansible-deploy-gluon-to-proxmox

Deploy gluon to proxmox nodes ...

Before running, do:
```
apt install python-pip
pip install proxmoxer
```

Variables used in host_vars:
```
proxmox_api_password: ...
```

Some notes:
- Nodes are identified by their hostname.
- Nodes are not recreated if a node with the same hostname exists.
- A bridge `vmbr20106` is created for the vm with id 106. This bridge is used
  for the client interface of the node.
- Ssh is used to configure the nodes and leave config mode.
