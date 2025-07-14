import random #for random selection of words
import tkinter as tk #GUI lib
from tkinter import messagebox #to show popups
from tkcalendar import DateEntry  # Calendar support
from PIL import ImageGrab #to capture the Ui as image
import time #to pause execution

# Creating subjects, actions, places and random words necesaary for the news generation
subjects = [
    "Shahrukh Khan", "Priyanka Chopra", "Virat Kohli", "Narendra Modi", 
    "Nirmala Sitaramana", "An Indian band", "A Delhi Cat", "2 Men in their 20s", 
    "A group of monkeys", "An auto driver from Bengaluru", 
    "Ranveer Singh in neon pants", "A lost Amazon package", "Kangana Ranaut on Twitter", 
    "A confused Google Maps car", "A hyperactive street dog", "Elon Musk's clone", 
    "A sleeping security guard", "Your neighborhood uncle", "An alien spotted in Mumbai", 
    "A tea stall owner", "A haunted Alexa speaker", "The last Nokia phone alive", 
    "A random Zomato delivery guy", "The CEO of Chai Point", "An angry traffic cop", 
    "A mysterious WhatsApp forward", "A dancing toddler", "A runaway cow", 
    "An Indian auntie with a stick", "The ghost of a Bollywood actor"
]

actions = [
    "launches", "cancels", "wins", "dances with", "was found in",
    "hospitalized", "got a cardiac arrest", "killed", "eats", "declares war on",
    "celebrates", "buys Twitter again", "starts a food blog", "hacks NASA", 
    "throws a samosa party", "gets lost in Chandni Chowk", "starts stand-up comedy", 
    "accidentally invents AI", "wins Bigg Boss", "hosts KBC", "runs away from paparazzi", 
    "sings at India Gate", "becomes a meme", "joins a rock band", "loses WiFi connection", 
    "invests in crypto", "launches flying autos", "steals mangoes", "learns bhangra", 
    "meditates on the Metro roof"
]

places_or_things = [
    "at Red Fort", "in Delhi Fort", "a plate of samosa", "at Ganga Ghat",
    "banana", "during rain", "at Indian household", "on Mars", "at a dhaba near Jaipur", 
    "inside a washing machine", "in Bengaluru traffic", "at India Gate", "on a moving train roof", 
    "inside Big Bazaar", "at a secret Goa rave", "on top of Qutub Minar", "under a banyan tree", 
    "at Mumbai local station", "in a haunted mansion", "while skydiving", "on a Zoom call", 
    "inside Parliament canteen", "in the middle of IPL stadium", "while eating pani puri", 
    "at a tech startup", "inside a temple bell", "on a scooter with 5 people", "during a sandstorm", 
    "at Sarojini market", "on a banana leaf"
]

random_words = [
    "breaking", "exclusive", "mystery", "revealed", "unexpected",
    "chaos", "shockwave", "sensation", "viral", "spotted", "leaked",
    "controversy", "exposed", "outrage", "bizarre", "unbelievable", 
    "surreal", "trending", "insane", "hilarious", "epic fail", 
    "hidden truth", "wild", "spectacle", "jaw-dropping", "craziness", 
    "frenzy", "chaotic", "rumor mill", "utter madness", "what just happened?"
]


#generates a random ffake news headline and updates the UI
def generate_headline():
    global current_headline, current_filler
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    filler_text = " ".join(random.choices(random_words, k=10)).capitalize()

    current_headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    current_filler = filler_text
    headline_label.config(text=current_headline)
    content_label.config(text=current_filler)

    date_picker.pack_forget()
    confirm_button.pack_forget()

    save_button.pack(pady=5)

#saves the selected date and updates UI
def confirm_date():
    global selected_date
    selected_date = date_picker.get_date().strftime("%d %B %Y")
    date_label.config(text=f"📅 Date: {selected_date}")
    date_picker.pack_forget()
    confirm_button.pack_forget()

#resets the headline, content and date also makes the picker available again
def clear_headline():
    headline_label.config(text="Click 'Generate' to get your headline!")
    content_label.config(text="")
    date_label.config(text="")  # Clear date text

    date_picker.pack(pady=10)
    confirm_button.pack(pady=5)

    save_button.pack_forget() #hides save until the next generation

#captures the UI area and saves it as a PNG image
def save_ui_area():
    # Hide buttons for clean screenshot
    button_frame.pack_forget()
    save_button.pack_forget()

    # Wait for UI to redraw without buttons
    root.update()
    time.sleep(0.2)

    # Get window coordinates
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()

    # Capture only the window area
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))

    # Save as PNG
    filename = f"headline_{selected_date.replace(' ', '_')}.png"
    img.save(filename)

    messagebox.showinfo("Saved", f"UI saved as {filename}")

    # Show buttons back
    button_frame.pack(pady=20)
    save_button.pack(pady=5)


# Tkinter window
root = tk.Tk()
root.title("Vintage Fake News Generator")
root.geometry("700x550")
root.configure(bg="#f5f0e1")

# Styling
title_font = ("Georgia", 28, "bold")
headline_font = ("Times New Roman", 20, "bold")
content_font = ("Courier", 16, "italic")

current_headline = ""
current_filler = ""
selected_date = ""

# Widgets
title_label = tk.Label(root, text="📰 Vintage Fake News Generator 📰",
                       font=title_font, bg="#f5f0e1", fg="#5e503f")
title_label.pack(pady=20)

date_label = tk.Label(root, text="", font=("Georgia", 14),
                      bg="#f5f0e1", fg="#5e503f")
date_label.pack()

date_picker = DateEntry(root, width=12, background='darkblue',
                        foreground='white', borderwidth=2, font=("Georgia", 12))
date_picker.pack(pady=10)

confirm_button = tk.Button(root, text="✅ OK",
                           font=("Georgia", 12), bg="#c5a880",
                           fg="#3b3021", command=confirm_date)
confirm_button.pack(pady=5)

headline_label = tk.Label(root, text="Click 'Generate' to get your headline!",
                          font=headline_font, bg="#f5f0e1", fg="#3b3021",
                          wraplength=600, justify="center")
headline_label.pack(pady=30)

content_label = tk.Label(root, text="", font=content_font,
                         bg="#f5f0e1", fg="#3b3021", wraplength=600,
                         justify="center")
content_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root, bg="#f5f0e1")
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="🖋 Generate Headline",
                            font=("Georgia", 14), bg="#d8c3a5",
                            fg="#3b3021", command=generate_headline)
generate_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="🗑 Clear",
                         font=("Georgia", 14), bg="#e6b89c",
                         fg="#3b3021", command=clear_headline)
clear_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(root, text="💾 Save Poster as PNG",
                        font=("Georgia", 14), bg="#c5e1a5",
                        fg="#3b3021", command=save_ui_area)
save_button.pack_forget()

root.mainloop()
