
import time
from datetime import datetime, timedelta
'''
def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        print(f"Task time : {end_time - start_time} seconds")
        return result
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f"Brewing {tea_type} Tea!")
    time.sleep(steep_time)
    print("Tea is Ready!")
 

@timer_dec
def make_matcha():
    print("Making Matcha...")
    time.sleep(1)
    print("Matcha is Ready!")
    return f"Drink Matcha by {datetime.now() + timedelta(minutes=30)}"



brew_tea(tea_type='Green',steep_time= 1)
print(make_matcha())
'''


# practise ===================================================================================================================


def mission_timer(base_fn):
    def enhanced_fn(*args, **kargs):
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        start_time = time.time()
        result = base_fn(*args, **kargs)
        end_time = time.time()
        print(f"Mission duration: {end_time - start_time} seconds")
        return result
    return enhanced_fn



@mission_timer
def launch_probe(planet):
    print(f"Launching probe towards {planet}...")
    time.sleep(1)



@mission_timer
def deploy_satellite(orbit_type, altitude_km):
    print(f"Deploying satellite into {orbit_type} at {altitude_km} km ...")
    time.sleep(2)

result = launch_probe("Europa")
print("Stored mission result:", result)
