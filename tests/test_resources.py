from types import GeneratorType

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestResource:
    def test_resource_relation(self, client):
        """Test passing parent object when using get_relation."""
        album = client.get_album(302127)
        tracks = album.get_tracks()
        assert tracks[0].album is album


class TestAlbum:
    def test_album_attributes(self, client):
        album = client.get_album(302127)
        assert hasattr(album, "title")
        assert repr(album) == "<Album: Discovery>"

        artist = album.get_artist()
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_album_tracks(self, client):
        album = client.get_album(302127)
        tracks = album.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"
        assert type(album.iter_tracks()) == GeneratorType
        track = list(album.iter_tracks())[0]
        assert isinstance(track, deezer.resources.Track)

    def test_as_dict(self, client):
        album = client.get_album(302127)
        assert album.asdict()["id"] == 302127


class TestArtist:
    def test_artist_attributes(self, client):
        artist = client.get_artist(27)
        assert hasattr(artist, "name")
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_artist_albums(self, client):
        artist = client.get_artist(27)
        albums = artist.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Random Access Memories>"
        assert type(artist.iter_albums()) == GeneratorType

    def test_artist_top(self, client):
        """
        Test top method of artist resource
        """
        artist = client.get_artist(27)
        tracks = artist.get_top()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Instant Crush>"

    def test_artist_radio(self, client):
        """
        Test radio method of artist resource
        """
        artist = client.get_artist(27)
        tracks = artist.get_radio()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"

    def test_artist_related(self, client):
        """
        Test related method of artist resource
        """
        artist = client.get_artist(27)
        artists = artist.get_related()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Justice>"
        assert type(artist.iter_related()) == GeneratorType


class TestTrack:
    def test_track_attributes(self, client):
        """
        Test track resource
        """
        track = client.get_track(3135556)
        artist = track.get_artist()
        album = track.get_album()
        assert hasattr(track, "title")
        assert isinstance(track, deezer.resources.Track)
        assert isinstance(artist, deezer.resources.Artist)
        assert isinstance(album, deezer.resources.Album)
        assert repr(track) == "<Track: Harder Better Faster Stronger>"
        assert repr(artist) == "<Artist: Daft Punk>"
        assert repr(album) == "<Album: Discovery>"


class TestRadio:
    def test_radio_attributes(self, client):
        """
        Test radio resource
        """
        radio = client.get_radio(23261)
        assert hasattr(radio, "title")
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Telegraph Classical>"

    def test_radio_tracks(self, client):
        """
        Test tracks method of radio resource
        """
        radio = client.get_radio(23261)
        tracks = radio.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[2]
        assert isinstance(track, deezer.resources.Track)
        assert type(radio.iter_tracks()) == GeneratorType


class TestGenre:
    def test_genre_attributes(self, client):
        genre = client.get_genre(106)
        assert hasattr(genre, "name")
        assert isinstance(genre, deezer.resources.Genre)
        assert repr(genre) == "<Genre: Electro>"

    def test_genre_artists(self, client):
        genre = client.get_genre(106)
        artists = genre.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Clean Bandit>"
        assert type(genre.iter_artists()) == GeneratorType

    def test_genre_radios(self, client):
        genre = client.get_genre(106)
        radios = genre.get_radios()
        assert isinstance(radios, list)
        radio = radios[0]
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Electro Swing>"
        assert type(genre.iter_radios()) == GeneratorType


class TestChart:
    def test_chart_tracks(self, client):
        chart = client.get_chart()
        tracks = chart.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Head & Heart (feat. MNEK)>"
        assert type(chart.iter_tracks()) == GeneratorType

    def test_chart_artists(self, client):
        """
        Test artists method of chart resource
        """
        chart = client.get_chart()
        artists = chart.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Juice Wrld>"
        assert type(chart.iter_artists()) == GeneratorType

    def test_chart_albums(self, client):
        """
        Test albums method of chart resource
        """
        chart = client.get_chart()
        albums = chart.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert (
            repr(album)
            == "<Album: The Dark Side Of The Moon [Remastered] (Remastered Version)>"
        )
        assert type(chart.iter_albums()) == GeneratorType

    def test_chart_playlists(self, client):
        """
        Test playlists method of chart resource
        """
        chart = client.get_chart()
        playlists = chart.get_playlists()
        assert isinstance(playlists, list)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Deezer Hits UK>"
        assert type(chart.iter_playlists()) == GeneratorType


class TestUser:
    def test_user_albums(self, client):
        """
        Test albums method of user resource
        """
        user = client.get_user(359622)
        albums = user.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: A Century Of Movie Soundtracks Vol. 2>"
        assert type(user.iter_albums()) == GeneratorType

    def test_user_artists(self, client):
        """
        Test artists method of user resource
        """
        user = client.get_user(359622)
        artists = user.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Wax Tailor>"
        assert type(user.iter_artists()) == GeneratorType

    def test_user_playlists(self, client):
        """
        Test playlists method of user resource
        """
        user = client.get_user(359622)
        playlists = user.get_playlists()
        assert isinstance(playlists, list)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: AC/DC>"
        assert type(user.iter_playlists()) == GeneratorType

    def test_user_tracks(self, client):
        """
        Test tracks method of user resource
        """
        user = client.get_user(353978015)
        tracks = user.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Prélude a l'après-midi d'un faune, L. 86>"
        assert type(user.iter_tracks()) == GeneratorType


class TestPlaylist:
    def test_get_tracks(self, client):
        playlist = client.get_playlist(12345)
        tracks = playlist.get_tracks()
        assert len(tracks) == 4
        for track in tracks:
            assert isinstance(track, deezer.resources.Track)
        assert tracks[0].title == "Skanky Panky"
        assert type(playlist.iter_tracks()) == GeneratorType

    def test_get_fans(self, client):
        playlist = client.get_playlist(6512)
        fans = playlist.get_fans()
        assert len(fans) == 3
        for fan in fans:
            assert isinstance(fan, deezer.resources.User)
        assert fans[0].name == "laurentky"
        assert type(playlist.iter_fans()) == GeneratorType


class TestPodcast:
    def test_get_episodes(self, client):
        """
        Test episodes method of podcast resource
        """
        podcast = client.get_podcast(699612)
        episodes = podcast.get_episodes()
        assert isinstance(episodes, list)
        assert len(episodes) == 12
        for episode in episodes:
            assert isinstance(episode, deezer.resources.Episode)
        assert episodes[0].title == "Episode 9: Follow the money"
        assert type(podcast.iter_episodes()) == GeneratorType
