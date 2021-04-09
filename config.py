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
