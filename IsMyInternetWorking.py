import socket
import time
import winsound

def check_internet():
    """
    Checks the internet connection by attempting to connect to a well-known site.
    Returns True if the connection is successful, otherwise False.
    """
    try:
        socket.create_connection(("www.google.com.br", 80))
        return True
    except OSError:
        return False

def play_alert_sound():
    """
    Plays a series of beeps resembling the intro of "The Man Who Sold the World."
    This continues in an infinite loop with a 1-second pause between repetitions.
    """

    while True:
        # The man who sold the world:
        # E |------------------------
        # B |-1--1--1------121-------
        # G |----------4--------4----
        # D |------------------------
        # A |------------------------
        # E |------------------------

        winsound.Beep(415, 300) # G#
        winsound.Beep(415, 300) # G#
        winsound.Beep(415, 300) # G#
        winsound.Beep(369, 500) # F#
        winsound.Beep(415, 200) # G#
        winsound.Beep(440, 200) # A
        winsound.Beep(415, 200) # G#
        winsound.Beep(369, 300) # F#

        time.sleep(1)

def main():
    """
    Main function that continuously checks for an internet connection.
    When the connection is detected, it plays an alert sound and exits.
    """
    while True:
        if check_internet():
            play_alert_sound()
            break
        else:
            print("nothing yet, trying again in 90 seconds")
            time.sleep(90)

if __name__ == '__main__':
    main()
