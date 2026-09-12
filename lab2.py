class Song:
    def __init__(self, song_id, song_title, artist, duration):
        self.song_id = song_id
        self.song_title = song_title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return (f"Song ID: {self.song_id} | Title: {self.song_title} | "
                f"Artist: {self.artist} | Duration: {self.duration}")

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        print(f"\n'{song.song_title}' added at the beginning of the playlist.")

    def insert_last(self, song):
        new_node = Node(song)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.count += 1
        print(f"\n'{song.song_title}' added at the end of the playlist.")

    def insert_at(self, song, position):
        if position < 1 or position > self.count + 1:
            print(f"\nInvalid position. Valid range is 1 to {self.count + 1}.")
            return

        if position == 1:
            self.insert_first(song)
            return

        new_node = Node(song)
        current = self.head
        prev = None
        index = 1

        while index < position:
            prev = current
            current = current.next
            index += 1

        prev.next = new_node
        new_node.next = current
        self.count += 1
        print(f"\n'{song.song_title}' inserted at position {position}.")

    def display(self):
        print("\n================================")
        print("        CURRENT PLAYLIST")
        print("================================")
        if self.is_empty():
            print("The playlist is empty.")
            return

        current = self.head
        position = 1
        while current is not None:
            print(f"{position}. {current.song}")
            current = current.next
            position += 1

        print(f"\nTotal number of songs: {self.count}")

    def search(self, song_id):
        current = self.head
        position = 1
        while current is not None:
            if current.song.song_id.lower() == song_id.lower():
                print(f"\nSong found at position {position}:")
                print(current.song)
                return current.song
            current = current.next
            position += 1

        print(f"\nNo song found with Song ID '{song_id}'.")
        return None

    def delete(self, song_id):
        if self.is_empty():
            print("\nThe playlist is empty. Nothing to remove.")
            return

        current = self.head
        prev = None

        while current is not None:
            if current.song.song_id.lower() == song_id.lower():
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.count -= 1
                print(f"\n'{current.song.song_title}' (ID: {song_id}) "
                      f"removed from the playlist.")
                return
            prev = current
            current = current.next

        print(f"\nNo song found with Song ID '{song_id}'. Nothing removed.")

    def size(self):
        print(f"\nTotal number of songs in the playlist: {self.count}")
        return self.count


def get_song_details():
    print("\nEnter Song Details")
    song_id = input("Song ID: ").strip()
    song_title = input("Song Title: ").strip()
    artist = input("Artist: ").strip()
    duration = input("Duration (e.g., 4:23): ").strip()
    return Song(song_id, song_title, artist, duration)


def get_valid_integer(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        print("Invalid input. Please enter a positive whole number.")

def main():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print("     MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            song = get_song_details()
            playlist.insert_first(song)

        elif choice == "2":
            song = get_song_details()
            playlist.insert_last(song)

        elif choice == "3":
            song = get_song_details()
            position = get_valid_integer("Enter position to insert at: ")
            playlist.insert_at(song, position)

        elif choice == "4":
            playlist.display()

        elif choice == "5":
            song_id = input("\nEnter Song ID to search: ").strip()
            playlist.search(song_id)

        elif choice == "6":
            song_id = input("\nEnter Song ID to remove: ").strip()
            playlist.delete(song_id)

        elif choice == "7":
            playlist.size()

        elif choice == "8":
            print("\nExiting Music Playlist Manager. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()
