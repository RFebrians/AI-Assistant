from exp import Experiment

if __name__=='__main__':
    shield = Experiment()
    shield.change_state_led('green', True)
    shield.send_message_lcd('Test Message')

    while True:
        #shield.move_feet()
        distance_cm = str(shield.read_distance())
        shield.send_message_lcd(distance_cm, 2)