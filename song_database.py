import glob

image_paths = [file for file in glob.glob(r'C:\Users\Tyler\Desktop\Gui_images\Album Art/*')]

def cover_finder(album_name: str):
    for i in range(len(image_paths)):
        image_path = image_paths[i]
        condition = album_name in image_path
        if condition == True:
            return image_path
            
song_info = []    
def insert_song_info(png_path: str, artist: str, song: str):
    tuples = (png_path, artist, song)
    song_info.append(tuples)
    
    
insert_song_info(cover_finder('Parachutes'), 'Coldplay', 'Yellow')
insert_song_info(cover_finder('Parachutes'), 'Coldplay', 'Speed of Sound')    
insert_song_info(cover_finder('A Rush Of Blood To the Head'), 'Coldplay', 'Clocks')    
insert_song_info(cover_finder('A Rush Of Blood To the Head'), 'Coldplay', 'The Scientist')    
insert_song_info(cover_finder('Beautiful Day'), 'U2', 'Beautiful Day')    
insert_song_info(cover_finder('Songs of Innocence'), 'U2', 'Song for Someone')    
insert_song_info(cover_finder('The Joshua Tree'), 'U2', 'With or Without you')    
insert_song_info(cover_finder('The Joshua Tree'), 'U2', "I Still Haven't found what I'm Looking For")    
insert_song_info(cover_finder('Carter IV'), 'Lil Wayne', 'How to Love')
insert_song_info(cover_finder('Battle Studies'), 'John Mayer', ' Half of my Heart')
insert_song_info(cover_finder('Battle Studies'), 'John Mayer', 'Heartbreak Warfare')
insert_song_info(cover_finder('Continuum'), 'John Mayer', 'Slow Dancing in a Burning Room')
