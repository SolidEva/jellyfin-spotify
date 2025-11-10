# jelly-spotify

A docker image to automatically import newly saved spotify songs into jellyfin

Roughly it works like this:
- Move all newly saved songs to a user created "new-songs" playlist. see `tool_scripts/spotify_update_playlist.py`
- Use tsar https://github.com/SolidEva/tsar to get all songs in the playlist, then empties the playlist
- Copy the song files into the jellyfin library in the proper `artist/album/song.mp3` organization, then add all the songs to a monthly playlist named `Month Year`. see `tool_scripts/jelly_import.py`

## requirements
- spotify premium, required to use the api
- an jellyfin server or similar

## setup

### build the docker image

```
docker build -t solideva/jellyfin-spotify .
```

### generate a spotipy authentication cache token

get the required SPOTIPY api values: https://www.youtube.com/watch?v=3RGm4jALukM

```
export SPOTIPY_CLIENT_ID=""
export SPOTIPY_CLIENT_SECRET=""
export SPOTIPY_REDIRECT_URI="http://www.somesite.com"
./tool_scripts/generate_spotipy_cache.py --username "username"
```
this will give you a `.cache-<username>` file that you need to map into the docker image

### Manually create a "new-songs" playlist
create a playlist in spotify for the tool to work in
set the playlist description with a timestamp in the format `2022-07-08 00:46:19.285023+00:00`
this timestamp is how the tool will know what saved songs are new, and should be added to the playlist

### Generate a credential.json for librespot
get librespot and run
```
librespot --enable-oauth --system-cache cache_dir
```
go through the login process
once done, there will be a credendials.json file in the cache_dir
copy that to your librespot_cache_dir

## run example

```
docker run \
-v /home/user/.cache-username:/.cache-username \
-v /home/user/librespot_cache_dir:/librespot_cache_dir \
-v /home/user/jellyfin/music_library:/jellyfin \
-e SPOTIPY_CLIENT_ID="" \
-e SPOTIPY_CLIENT_SECRET="" \
-e SPOTIPY_REDIRECT_URI="http://www.somesite.com" \
-e SPOTIFY_USERNAME="" \
-e SPOTIFY_PASSWORD="" \
-e SPOTIFY_PLAYLIST_URI="spotify:playlist:<blah>" \
-e JELLYFIN_USERNAME="" \
-e JELLYFIN_PASSWORD="" \
-e JELLYFIN_SERVER="http://192.168.10.10" \
-e PUID="1000" \
-e PGID="1000" \
solideva/jellyfin-spotify
```
