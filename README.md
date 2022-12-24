# yulu-learning

Flow : 
* Scan yulu's in current area
* get details of every one (get-bike-details.py)
* Select one with can_unlock_from_server param set to false
* get ble_id
* send unlock command to omnilockkey (check if can be achieved by yulu's intervention) (omnilock.py)
* send ignition_on to yulu (check if can be achieved by yulu's intervention)
  
Other ideas :
* Record and spoof gatt of yulu bike? and send malformed output?
* some good way to block yulu's connection to server if can_unlock_from_server is true (`s/ride-request-unlock` outputs with SIM details of the bike?)
* if ignition_on without yulu's intervention is possible then can I forcefully turn off someone else's yulu?
* if omnilock unlock command without ......... is possible then can I forcefully lock a yulu at any given time?
* What if I relay bluetooth responses from bike and change crucial details in mid?
