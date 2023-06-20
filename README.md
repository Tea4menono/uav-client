# uav-client

## service config file

```
sudo nano /etc/systemd/system/test.service
```

## start service

```
sudo systemctl start test.service
```

## stop service

```
sudo systemctl stop test.service
```

## check service status

```
sudo systemctl status test.service
```

## install timestamp log tool

### use apt-get

```
sudo apt-get install moreutils
```

### use homebrew

```
brew install moreutils
```

## execute script

```
python3 test.py 2>&1 | ts '%Y-%m-%d %H:%M:%S' >> logfile.log
```
