# spotify-vk

A repository that can broadcast the current track from Spotify to the VK status.

### Dependencies
This repository is based on two third-party libraries:
* **[vk-api](https://github.com/python273/vk_api)** (**^11.9.1**)
* **[spotiapi](https://github.com/julheer/spotiapi)** (^**2.0.3**)

By using this program, you agree to the terms of use of these libraries.

### Program configuration:
In order to use the program, you need to get Spotify and [VK](https://vkhost.github.io) tokens.
```python
# Key for using SpotifyAPI.
# Variable type: string, default value: None.
spotify_api_token = ''


# Similarly for VK.
# Variable type: string, default value: None.
vk_token = ''


# The status that will be set when you are not listening to anything.
# Variable type: string, default value: 'Example status'.
replace_status = 'Example status'


# The status that will be set when listening to the track.
# Variable type: string, default value: 'Spotify | Listening {song} by {author}'.
listening_status = 'Spotify | Listening {song} by {author}'


# This parameter is responsible for the division between the authors of the song.
# Variable type: string, default value: ' & '.
author_separator = ' & '


# This variable is responsible for checking the Spotify
# response time during listening.
# Variable type: integer, default value: 10.
listening_status_update = 10

# This variable is responsible for checking the Spotify response
# time when the user is not listening to anything.
# Variable type: integer, default value: 15.
stopped_checker = 15
```

© [Julheer](https://github.com/julheer), 2021. Developed with ❤.