# Tool - Backup with restic

## Information
The idea is to have a way ton backup servers with the same script and to keep the same tree folders.
The couple `restic` and `rclone` is a good way to backup, and this script can automate and send email reports.

_The project is not maintained, but feel free to contribute and improve it !_

### Tree folder
```bash
# Locate where your rclone is configured
/BUCKET_NAME
|__ CLIENT_NAME
    |__ SERVER_NAME
        |__ REPO_NAME
```


### Dependencies
- restic
- rclone
- python3


## Installations
```bash
$ git clone git@github.com:KeisukeFD/backup_script.git /home/scripts/backup
$ cd /home/scripts/backup
$ virtualenv -p $(which python3) venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

#### Restic
```bash
# Get the lastest release from GitHub (https://github.com/restic/restic/releases)

Example:
$ curl -L https://github.com/restic/restic/releases/download/v0.9.6/restic_0.9.6_linux_amd64.bz2 -o /tmp/restic_0.9.6_linux_amd64.bz2
$ bzip2 -d /tmp/restic_0.9.6_linux_amd64.bz2
$ mv /tmp/restic_0.9.6_linux_amd64 /usr/bin/restic
```


#### Rclone
```bash
$ curl https://rclone.org/install.sh | bash
```

#### Backup script
```bash
$ mkdir -p /home/scripts

# Get this repo
$ git clone git@github.com:KeisukeFD/backup_script.git /home/scripts/backup
```

## Configuration
#### rclone
Two ways:

1. Use the command `rclone config` and follow the steps (https://rclone.org/commands/rclone_config/)
2. If you already have a configuration file, put in `~/.config/rclone/rclone.conf`

Note: The name of the connexion used by rclone will be use in the configuration file `config.yml` as `rclone_connection_name`

#### Configuration file

```yaml
information:
    client_name: ""
    server_name: ""
    rclone_connection_name: ""
    bucket_name: ""
    exclusion_file: "exclude-files"
    keep_daily: "90" # 90 days by default

binaries:
    restic: "/usr/bin/restic"

email:
    enable: false
    sender: "backups@local.dev"
    to: ""
    host: "127.0.0.1"
    port: "1025"
    max_try: "5"
    timeout: "600" # seconds
```

## Launch
```bash
# Example:
RESTIC_PASSWORD="Encryption password" /home/scripts/backup/backup -r Data /Backups /tomcat/conf /tomcat/lib
# Will backup into *Data* repository, all folders: /Backups, /tomcat/conf, /tomcat/lib
```

### First launch
At the first launch, you must initialize the `restic` repo. Then you will be able to put your command into `cron` to automate your backups.

## Help to use `restic`
[Official Documentation](https://restic.readthedocs.io/en/stable/)

## Restic Helper

We've added a helper, to avoid to repeat the command, and parameters, and keep organized your folders.
The helper reads the configuration file to know all your information, then you can use it like the following:

```bash
./restic_helper -r Data snapshots
```
