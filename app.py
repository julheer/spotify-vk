from asyncio import sleep, ensure_future, get_event_loop
from sys import exit

from spotiapi import SpotifyAPI
from vk_api import VkApi

import config


# A function for working with a captcha from VKontakte.
def captcha_worker(captcha):
    # If the captcha exists, we request the captcha solutions from the user.
    key = input('Requires solving captcha ({0}): '.format(captcha.get_url())).strip()
    return captcha.try_again(key)


session = VkApi(token=config.vk_token, captcha_handler=captcha_worker)
vk = session.get_api()
spotify = SpotifyAPI(config.spotify_api_token)


async def start_polling():
    user_listening_now = await spotify.get_player()
    if 'error' in user_listening_now:
        print('Stopping program. Founded Spotify API error.')
        return exit(-1)

    # We check whether the user is listening to something at the moment.
    if user_listening_now is None or not user_listening_now['is_playing']:
        vk.status.set(text=config.replace_status)
        await sleep(config.stopped_checker)
        pass

    author_default_text = ''

    i = 0
    for author in user_listening_now['player_artists']:
        i += 1

        if i + 1 <= len(user_listening_now['player_artists']):
            author_default_text += author + config.author_separator
        else:
            author_default_text += author + ' '

    vk.status.set(text=config.listening_status
                  .replace('{song}', user_listening_now['player_name']['name'])
                  .replace('{author}', author_default_text))
    await sleep(config.listening_status_update)


async def main():
    ensure_future(main())
    await start_polling()


if __name__ == '__main__':
    try:
        loop = get_event_loop()
        ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        vk.status.set(text=config.replace_status)
        print('Exit from the program. Goodbye.')
        exit(-1)
