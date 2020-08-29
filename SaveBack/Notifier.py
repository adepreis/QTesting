from os.path import join, dirname, realpath

import random

from plyer import notification
from plyer.utils import platform


title = "Posture reminder"
messages = ["Don't forget to keep your body in perfect alignment, maintaining the spine's natural curvature, with your neck straight and shoulders parallel with the hips.",
            "Don't forget to keep your shoulders back and relax your abdomen. Keep your feet about hip distance, try not to tilt your head forward, backwards or sideways.",
            "Pretend you’re standing against a wall to measure your height. Hold your head straight and tuck in your chin.",
            "Straighten up so you feel like your head stretches toward the sky. Your ears should be over the middle of your shoulders.",
            "Sit all the way back in your chair. Bend your knees at a right angle and keep them the same height, or a bit higher, than your hips.",
            "Please take a minute to stretch your neck and place your feet flat on the floor."]
 
def postureHelper():
    message = random.choice(messages)

    ticker = ''
    kwargs = {'title': title, 'message': message, 'ticker': ticker}

    # modes : 'fancy' (notification w/ icon), 'toast' (without icon) ? => (simple Android message instead of full notification)
    mode = 'fancy'

    if mode == 'fancy':
        kwargs['app_name'] = "SaveBack Notification"
        if platform == "win":
            # Windows requires a .ico :
            kwargs['app_icon'] = 'save-back-icon.ico'   # join(dirname(realpath(__file__)), 'plyer-icon.ico')
            kwargs['timeout'] = 10
        else:
            kwargs['app_icon'] = 'save-back-icon.png'   # join(dirname(realpath(__file__)), 'plyer-icon.png')
    elif mode == 'toast':
        kwargs['toast'] = True
    
    notification.notify(**kwargs)
