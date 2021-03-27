import vk_api
import config

from asyncio import sleep, ensure_future, get_event_loop
from spotiapi import SpotifyAPI
from sys import exit


def captcha_worker(captcha):
    key = input('[LOG] Requires solving captcha ({0}): '.format(captcha.get_url())).strip()
    return captcha.try_again(key)

session = vk_api.VkApi(token=config.vk_token, captcha_handler=captcha_worker)
vk = session.get_api()
spotify = SpotifyAPI(config.spotify_api_token)

async def start_polling():
    user_listening_now = spotify.get_user_player()
    if user_listening_now is None or not user_listening_now[0]:
        vk.status.set(text=config.replace_status)
            
        # Lower this value if you used all the VK quota.
        await sleep(15)
        pass

    author_default_text = ''

    i = 0
    for author in user_listening_now[1]:
        i += 1

        if i + 1 <= len(user_listening_now[1]):
            author_default_text += author + ' & '
        else:
            author_default_text += author + ' '

    vk.status.set(text=config.listening_status.replace('{song}',user_listening_now[2]).replace('{author}', author_default_text))
    await sleep(5)


async def main():
    print('Successfull start. Listening for updates...')
    ensure_future(main())
    await start_polling()


if __name__ == '__main__':
    try:
        loop = get_event_loop()
        ensure_future(main())
        loop.run_forever()
    except KeyboardInterrupt:
        vk.status.set(text=config.replace_status)
        print('[LOG] Exit...')
        exit(0)
