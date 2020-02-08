import musicbox
# CONSTANT VARIALBES
NOTES = [("C", 60), ("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]
MAJOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MINOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
DURATION = 500
OCTAVE_VALUE = 12
my_music = musicbox.MusicBox()

def note_to_int(note):
    # Counter for value of a note
    note_value = 0
    #Loops through the length of parameter
    for i in range(len(note)):
        #Loops through the length of List
        for j in range(len(NOTES)):
            #During the nest for loop if index of i in note == "^"
            if note[i] == "^":
                #if the note has another character after
                if note[i + 1] == "^" or (note[i + 1] == NOTES[j][0]):
                    note_value += OCTAVE_VALUE
                    # breaks the loops so it doesn't constantly add 12
                    break
            #if the note is just one character
            elif note[i] == NOTES[j][0]:
                # adds the default value to for that note from the list
                note_value += NOTES[j][1]
                #If the note has another character after
                if i < len(note) - 1:
                    if note[i + 1] == "b":
                        note_value -= 1
                    elif note[i + 1] == "#":
                        note_value += 1
                    else:
                        note_value = -1
    # returns the note value
    return note_value
def print_menu():
    # Prints the layout of main menu
    print("Main Menu: ")
    print("1. Play Scale")
    print("2. Play Song")
    print("3. Quit")

def menu_choice():
    # If user input is less than 1 or greater than 4. Re enter choice
    user = int(input("Please enter a selection: "))
    while(user < 1 or user > 3):
        user = int(input("Please enter a selection: "))
    # Returns the user choice
    return user

def get_scale():
    # User inputs a scale
    scale = input("Please enter a scale name: ")
    #Sets note to the index of scale from first to " "
    note = scale[:scale.rfind(" ")]
    # Place holder for note
    note_scale = ""
    # Place holder for word
    word_scale = ""
    while scale != "":
        # If note_to_int(note) is invalid
        if note_to_int(note) == -1:
            scale = input("Please enter a scale name: ")
        else:
            #If valid sets the note to place holder and breaks loop
            note_scale = note
            break
    ## If scale cannot find major or minor
    while(scale.find("major") == -1 and scale.find("minor") == -1):
        # User re inputs scale
            scale = input("Please enter a scale name: ")
        # If scale contains major or minor, break loop
            if scale.find("major") != -1 or scale.find("minor") != -1:
                break
    ## If index of " " + 1 to end of scale is major
    if scale[scale.find(" ")+1:] == "major":
        word_scale = "major"
    else:
        word_scale = "minor"
    ## returns tuple of note and word
    return (note_scale, word_scale)

def scale_to_ints(scale):
    #Validates first note of scale
    note_scale= note_to_int(scale[0])
    # Adds notes to a list
    list_scale = [note_scale]
    # First note
    note = note_scale
    # If first note of scale is a minor
    if scale[1] == "minor":
        # Loops through the integers of minor
        for i in MINOR_INTERVALS:
            note = note + i
            # adds minor note to list
            list_scale.append(note)
    else:
        # Loops through major integers if not minor
        for i in MAJOR_INTERVALS:
            note = note + i
            # adds major note to list
            list_scale.append(note)
    # Returns list of 8 integers
    return list_scale

def menu_play_scale():
    # Gets a scale from the user to turn into ints
    scale = scale_to_ints(get_scale())
    ## Loops through the given scale playing each note for duration of 500
    for i in scale:
        # Calls play_note function from musicbox
        my_music.play_note(i,DURATION)

def get_song_file():
    # Asks user to input a song file
    song = input("Please enter a song file name: ")
    # return the file name
    return song

def play_song(file_name):
    # Loops through each line of file
    for line in open(file_name):
        # Determines if line is a comment
        comment = line.find("//")
        ## If not a comment
        if comment == -1:
            #find the given duration after space
            duration = line[line.rfind(" "):]
            #finds the given note before the space
            one_note = line[:line.rfind(" ")]
            # If note starts with I
            if one_note == "I":
                # Calls change_instrument function from music box
                my_music.change_instrument(int(duration))
            # finds the note value calling note_to_int()
            note_value = note_to_int(one_note)
            # If note value is = -1  and has more than one note
            if note_value == -1 and len(one_note) > 1:
                # Create a list of notes
                notes = []
                # Splits each note after the space
                note_line = one_note.split(" ")
                # Loops through the line with more than one note
                for note in note_line:
                    #finds values of the notes in the line
                    notes_in_line = note_to_int(note)
                    #addes the notes to the list
                    notes.append(notes_in_line)
                #Since more than one note calls play_chord function
                my_music.play_chord(notes, int(duration))
            else:
                # If only one note calling play_note function
                my_music.play_note(note_value, int(duration))

def menu_play_song():
    #gets file name and calls play_song function playing the selected file
    play_song(get_song_file())

def main():
    # Default is true so it will create a loop
    while True:
        # Prints main menu
        print_menu()
        # Obtains user choice
        menu = menu_choice()
        # Calls menu_play_scale if 1
        if menu == 1:
            menu_play_scale()
        # Calls menu_play_scale if 2
        if menu == 2:
            menu_play_song()
        # ends loops if 3
        if menu == 3:
            break

main()
my_music.close()

