# Basic Firewall Configuration with UFW

## Objective

The objective of this task is to configure a basic firewall using UFW (Uncomplicated Firewall) on a Linux system.

## Tools Used

* Kali Linux
* UFW (Uncomplicated Firewall)

## Configuration Steps

### Check Firewall Status

```bash
sudo ufw status verbose
```

### Set Default Policies

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Allow SSH Traffic

```bash
sudo ufw allow ssh
```

### Deny HTTP Traffic

```bash
sudo ufw deny 80/tcp
```

### Enable UFW

```bash
sudo ufw enable
```

### Verify Rules

```bash
sudo ufw status numbered
```

## Active Rules

* Allow SSH connections on port 22
* Deny HTTP traffic on port 80

## Security Benefits

* Reduces the attack surface
* Restricts unauthorized access
* Controls incoming network traffic
* Improves system security

## Conclusion

UFW was successfully configured to allow SSH access while blocking HTTP traffic. This task demonstrated basic firewall management and network access control using UFW.

