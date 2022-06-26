## channel-copier
A simple script for copying telegram channels

### Installing dependencies
```
 pip3 install -r requirements.txt  
```
### Configuring the config:

1. Enter your API_ID and API_HASH (you can take it on the website my.telegram.org)
2. Specify INTERVAL - the period of publication of posts (in seconds)
3. In CHANNEL1, specify the channels from which we will take posts (you can specify one)
4. In CHANNEL2, specify the target channel (where we will copy posts)

### Launch
```
python3 main.py
```
