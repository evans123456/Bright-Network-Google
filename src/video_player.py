"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.PLAYING = 0
        self.PAUSE = False
        self.FLAGGED_VIDEOS = []
        self.PLAYLISTS = {}
        # f"{self.PLAYING.title} ({self.PLAYING.video_id}) [{self.PLAYING.tags}]"

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos: ")

        for i in self._video_library.get_all_videos():
            print(f"{i.title} ({i.video_id}) {i.tags}")

        
        # struct = self._video_library.get_all_videos()[0]
        # print("This: ",struct)
        # print(dir(struct) )

        return 

        

    def play_video(self, video_id):
        """Plays the respective video.
        
        # PLAY funny_dogs_video_id

        Args:
            video_id: The video_id to be played.


        """
        self.PLAYING = self._video_library.get_video(video_id)


        print(f"Playing video: {self.PLAYING.title}")


    def stop_video(self):
        """Stops the current video."""
        temp = self.PLAYING
        self.PLAYING = 0
        # temp = self._video_library.get_video(video_id)
        if temp == 0:
            print("No video is currently playing")
        else:
            print("Stopping video: ",temp.title)

        return

    def play_random_video(self):
        """Plays a random video from the video library."""
        num = len(self._video_library.get_all_videos())
        video = random.randint(0, num-1)
        if self.PLAYING != 0:
            self.stop_video()
        self.PLAYING = self._video_library.get_all_videos()[video]
        print("Playing video: ",self.PLAYING.title)
        return


    def pause_video(self):
        """Pauses the current video."""
        if self.PLAYING != 0:
            if self.PAUSE == False:

                self.PAUSE = True
                print("Pausing video: ",self.PLAYING.title)
            else:
                print("Video already paused: ",self.PLAYING.title)
        else:
            print("Cannot pause video: No video is currently playing")
        return




    def continue_video(self):
        """Resumes playing the current video."""

        if self.PLAYING != 0: #if a video is playing
            if self.PAUSE == False:
                print("Cannot continue video: Video is not Paused")
            else: #if paused is true

                self.PAUSE = False
                print("Continuing video: ",self.PLAYING.title)
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        # PLAY funny_dogs_video_id
        if self.PLAYING == 0:
            print("No video is currently playing")
        else:

            print(f"Currently playing:  {self.PLAYING.title} ({self.PLAYING.video_id}) [{self.PLAYING.tags}]")

        return

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for key, value in self.PLAYLISTS.items():

            if key.lower() == playlist_name.lower():
                print("Cannot create playlist: A playlist with the same name already exists")
                return
        
        self.PLAYLISTS[playlist_name] = []
        print(f"Successfully created new playlist: {playlist_name}")
        return

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        CREATE_PLAYLIST foo
        ADD_TO_PLAYLIST foo funny_dogs_video_id

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        for key, value in self.PLAYLISTS.items():
            if key.lower() == playlist_name.lower():
                video_obj = self._video_library.get_video(video_id)
                if video_obj == None:
                    print(f"Cannot add video to {playlist_name}: Video does not exist")
                    return
                if video_obj not in value:
                    value.append(video_obj)
                    print(f"Added video to {playlist_name}: {video_obj.title}")
                    return
                else:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                    return
        return

    def show_all_playlists(self):
        """Display all playlists."""
        if len(self.PLAYLISTS) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for key, value in self.PLAYLISTS.items():
                print(f" {key}")


        return

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        CREATE_PLAYLIST foo
        ADD_TO_PLAYLIST foo funny_dogs_video_id

        Args:
            playlist_name: The playlist name.
        """
        
        for key, value in self.PLAYLISTS.items():
            if key.lower() == playlist_name.lower():#check if playlist exists
                print(f"Showing playlist: {playlist_name}")
                if len(value) == 0:
                    print(" No videos here yet")
                    return
                else:
                    for i in value: #the videos
                        print(f" {i.title} ({i.video_id}) {i.tags} ")
                    return
        
        print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        return


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        CREATE_PLAYLIST foo
        ADD_TO_PLAYLIST foo funny_dogs_video_id
        REMOVE_FROM_PLAYLIST foo funny_dogs_video_id
        REMOVE_FROM_PLAYLIST fosd funny_dogs_video_id

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        video_obj = self._video_library.get_video(video_id)
        for key, value in self.PLAYLISTS.items():
            if key.lower() == playlist_name.lower():#check if playlist exists
                if video_obj in value:
                    value.remove(video_obj)
                    print(f"Removed video from {playlist_name}: {video_obj.title}")
                    return
                else:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
                    return

        print(f"Cannot remove video from {playlist_name}: Playlist does not exist ")
        return

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        CREATE_PLAYLIST foo
        ADD_TO_PLAYLIST foo funny_dogs_video_id
        CLEAR_PLAYLIST foo
        SHOW_PLAYLIST foo

        Args:
            playlist_name: The playlist name.
        """
        for key, value in self.PLAYLISTS.items():
            if key.lower() == playlist_name.lower():#check if playlist exists
                self.PLAYLISTS[key] = []
                # value = []
                print(f"Successfully removed all videos from {playlist_name}")
                return

        print(f"Cannot clear playlist {playlist_name}: Playlist does not exist ")
        return

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        CREATE_PLAYLIST foo
        ADD_TO_PLAYLIST foo funny_dogs_video_id
        DELETE_PLAYLIST foo

        Args:
            playlist_name: The playlist name.
        """
        for key, value in self.PLAYLISTS.items():
            if key.lower() == playlist_name.lower():#check if playlist exists
                del self.PLAYLISTS[key]
                print(f"Deleted playlist: {playlist_name}")
                return
        
        print(f"Cannot delete playlist {playlist_name}: Playlist does not exist ")
        return




    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        indices=[]
        print(f"Here are the results for {search_term}: ")
        for idx,i in enumerate(self._video_library.get_all_videos()):
            if search_term.lower() in i.title.lower():
                indices.append(idx)
                print(f"{idx}) {i.title} ({i.video_id}) {i.tags}")

        if len(indices) == 0:
            print(f"No search results for {search_term}")
            return

        res = input("Would you like to play any of the above?If yes, specify the number of the video.\n If your answer is not a valid number, we will assume its a no.\n")
        #check if res is an int
        try:
            if len(indices) >= int(res):
                self.PLAYING = self._video_library.get_all_videos()[res-1]
                print(f"Playing video: {self.PLAYING.title}")
                return
        except:
            pass

            

        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.
        FLAG_VIDEO funny_dogs_video_id booo
        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        temp = self._video_library.get_video(video_id)


        self.stop_video()
        self.FLAGGED_VIDEOS.append({video_id,flag_reason})
        print(f"Successfully flaged video: {temp.title} ({temp.video_id}) [{temp.tags}]")

    def allow_video(self, video_id):
        """Removes a flag from a video.
        FLAG_VIDEO funny_dogs_video_id booo
        ALLOW_VIDEO funny_dogs_video_id

        Args:
            video_id: The video_id to be allowed again.
        """
        temp = 0
        for index,flagged_item in enumerate(self.FLAGGED_VIDEOS):
            print("Flagged item: ",flagged_item)
            print("Flagged item: ",type(flagged_item))
            if flagged_item["video_id"] == video_id:
                temp = self._video_library.get_video(video_id)
                del self.FLAGGED_VIDEOS[index]
        
        print(f"Successfully removed flag from video: {temp.title}")
