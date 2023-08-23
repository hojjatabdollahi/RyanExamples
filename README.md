# Read Me

This workspace contains examples for interacting with Ryan using ROS

## Say
To make Ryan say something you need to publish that to `tts_event_topic`:

```
source ~/ryan-master/cws/devel/setup.bash
rosrun ryan_sample say.py
```

## Listen
If you want to see what Ryan is hearing you should trigger STT on `stt_event_topic` with a `3000` code, when Ryan detects a pause it will publish whatever it has heard on `event_topic` with a `3001` code.

```
source ~/ryan-master/cws/devel/setup.bash
rosrun ryan_sample listen.py
```


## FER
Ryan publishes the emotions that it detects on `fer_event_topic`.
```
source ~/ryan-master/cws/devel/setup.bash
rosrun ryan_sample fer_listener.py
```


