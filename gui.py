import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("Nikk AI Assistant")
app.geometry("900x600")

# Title
title_label = ctk.CTkLabel(
    app,
    text="🤖 NIKK AI ASSISTANT",
    font=("Arial", 28, "bold")
)
title_label.pack(pady=20)

# Chat Area
chat_box = ctk.CTkTextbox(
    app,
    width=800,
    height=350,
    font=("Arial", 15)
)
chat_box.pack(pady=10)

chat_box.insert("end", "Nikk : Hello Nikunj! How can I help you?\n")

# Button Frame
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=20)

# Start Button
start_button = ctk.CTkButton(
    button_frame,
    text="🎤 Start Listening",
    width=180
)
start_button.grid(row=0, column=0, padx=10)

# Stop Button
stop_button = ctk.CTkButton(
    button_frame,
    text="🛑 Stop Assistant",
    width=180
)
stop_button.grid(row=0, column=1, padx=10)

# Clear Button
clear_button = ctk.CTkButton(
    button_frame,
    text="🧹 Clear Chat",
    width=180
)
clear_button.grid(row=0, column=2, padx=10)

# Status Label
status_label = ctk.CTkLabel(
    app,
    text="Status : Ready",
    font=("Arial", 15)
)
status_label.pack(pady=15)

# Run App
app.mainloop()