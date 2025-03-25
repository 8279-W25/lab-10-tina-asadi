from adafruit_circuitplayground import cp
import time


def create_morse_dictionary():
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
        'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', ' ': '/' 
    }
    return morse_dict

def clean_input(sentence, morse_dict):
    cleaned = ''
    for char in sentence:
        if char in morse_dict:
            cleaned += char
    return cleaned

def convert_to_morse(cleaned_sentence, morse_dict):
    morse_list = []
    for char in cleaned_sentence:
        if char == ' ':
            morse_list.append('/')
        else:
            morse_list.append(morse_dict[char])
    return morse_list

def turn_on_leds(pixels, color):
    for i in range(10):
        pixels[i] = color

def turn_off_leds(pixels):
    for i in range(10):
        pixels[i] = (0, 0, 0)

def display_morse(pixels, morse_list, unit_time, color):
    for code in morse_list:
        if code == '/':
            turn_off_leds(pixels)
            time.sleep(unit_time * 7)
        else:
            for symbol in code:
                if symbol == '.':
                    turn_on_leds(pixels, color)
                    time.sleep(unit_time)
                    turn_off_leds(pixels)
                    time.sleep(unit_time)
                elif symbol == '-':
                    turn_on_leds(pixels, color)
                    time.sleep(unit_time * 3)
                    turn_off_leds(pixels)
                    time.sleep(unit_time)
            time.sleep(unit_time * 3)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2)
morse_dict = create_morse_dictionary()

unit_time = float(input("Enter unit time (0-1 second): "))
if unit_time < 0 or unit_time > 1:
    unit_time = 0.5

color_choice = input("Enter LED color (r for red, g for green, b for blue): ")
if color_choice == 'r':
    color = (255, 0, 0)
elif color_choice == 'g':
    color = (0, 255, 0)
elif color_choice == 'b':
    color = (0, 0, 255)
else:
    color = (255, 255, 255)

user_input = input("Enter a sentence to convert to Morse code: ")
cleaned_sentence = clean_input(user_input.lower(), morse_dict)
morse_code = convert_to_morse(cleaned_sentence, morse_dict)
display_morse(pixels, morse_code, unit_time, color)