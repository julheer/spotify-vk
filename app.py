import vk_api
import config

from time import sleep
from spotiapi import SpotifyAPI
from sys import exit


def captcha_worker(captcha):
    key = input('[LOG] Requires solving captcha ({0}): '.format(captcha.get_url())).strip()
    return captcha.try_again(key)


session = vk_api.VkApi(token=config.vk_token, captcha_handler=captcha_worker)
vk = session.get_api()
spotify = SpotifyAPI(config.spotify_api_token)


def start_polling():
    while True:
        user_listening_now = spotify.getUserCurrentTrack()
        if user_listening_now is None or not user_listening_now[0]:
            vk.status.set(text=config.replace_status)

            if config.enable_logger:
                print('[LOG] Now the music is not playing, I set the standard status.')

            # Lower this value if you used all the VK quota.
            sleep(15)
            continue

        author_default_text = ''

        i = 0
        for author in user_listening_now[1]:
            i += 1

            if i + 1 <= len(user_listening_now[1]):
                author_default_text += author + ' & '
            else:
                author_default_text += author + ' '

        vk.status.set(text=config.listening_status.replace('{song}',
                                                           user_listening_now[2]).replace('{author}',
                                                                                          author_default_text))

        if config.enable_logger:
            print('[LOG] The user\'s status has been updated.')

        sleep(5)


if __name__ == '__main__':
    try:
        start_polling()
    except KeyboardInterrupt:
        vk.status.set(text=config.replace_status)
        print('[LOG] Exit...')
        exit(0)
