# spotify-vk

A repository that can broadcast the current track from Spotify to the VK status.

### Dependencies
This repository is based on two third-party libraries:
* **[vk-api](https://github.com/python273/vk_api)** (**^11.9.1**)
* **[spotiapi](https://github.com/julheer/spotiapi)** (^**1.1.2**)

By using this program, you agree to the terms of use of these libraries.

### Program configuration:
In order to use the program, you need to get Spotify and [VK](https://vkhost.github.io) tokens.
```python
# Key for using spotiapi.
spotify_api_token = ''

# Similarly for VK.
vk_token = ''

# Turn on/Disable logging (default: False)
enable_logger = True

# The status that will be set when you are not listening to anything.
replace_status = 'Example status'

# The status that will be set when listening to the track.
listening_status = 'Spotify | Listening {song} by {author}'
```

### Todos and future plans
This repository plans to actively develop, we will make our plans below:
- [ ] Switch all methods to asynchronous processing
- [ ] Rewrite the code so that it can be scaled to a larger quota limit
- [ ] Reduce the number of requests, while leaving the instant setting of the status when listening.

© [Julheer](https://github.com/julheer), 2021. Developed with ❤.