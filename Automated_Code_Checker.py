import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
import webbrowser
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import timeit

def check_syntax(code):
    try:
        compiled_code = compile(code, filename="<string>", mode="exec")
        exec(compiled_code)
        return True, ""
    except SyntaxError as e:
        return False, f"Syntax Error: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def train_ml_model():
    X = np.random.rand(100, 2)
    y = np.random.randint(0, 2, size=100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy

def time_complexity(code):
    try:
        execution_time = timeit.timeit(code, number=100)
        return True, f"Execution time: {execution_time:.6f} seconds"
    except Exception as e:
        return False, f"Error: {e}"

def automated_code_checker(code):
    output_text.delete('1.0', tk.END)
    
    syntax_passed, syntax_error = check_syntax(code)
    
    accuracy = train_ml_model()
    
    time_passed, time_result = time_complexity(code)
    
    if syntax_passed:
        output_text.insert(tk.END, "Code passed syntax check.\n")
        output_text.insert(tk.END, f"Machine Learning Model Accuracy: {accuracy:.2f}\n")
        if time_passed:
            output_text.insert(tk.END, f"{time_result}\n")
        else:
            output_text.insert(tk.END, f"{time_result}\n")
    else:
        output_text.insert(tk.END, "Code has errors:\n")
        output_text.insert(tk.END, f"{syntax_error}\n")
        google_search_button["state"] = tk.NORMAL
        youtube_search_button["state"] = tk.NORMAL

def reset_output():
    output_text.delete('1.0', tk.END)
    google_search_button["state"] = tk.DISABLED
    youtube_search_button["state"] = tk.DISABLED

def start_check():
    code = code_text.get("1.0", tk.END)
    if not code.strip():
        messagebox.showerror("Error", "Please enter code to check.")
        return
    automated_code_checker(code)

def google_search():
    search_query = output_text.get("1.0", tk.END)
    if search_query.strip():
        webbrowser.open_new("https://www.google.com/search?q=" + "+".join(search_query.split()))
    else:
        messagebox.showinfo("Info", "No error message found to search.")

def youtube_search():
    search_query = output_text.get("1.0", tk.END)
    if search_query.strip():
        webbrowser.open_new("https://www.youtube.com/results?search_query=" + "+".join(search_query.split()))
    else:
        messagebox.showinfo("Info", "No error message found to search.")

def determine_time_complexity():
    code = code_text.get("1.0", tk.END)
    if not code.strip():
        messagebox.showerror("Error", "Please enter code to check time complexity.")
        return
    time_passed, time_result = time_complexity(code)
    if time_passed:
        messagebox.showinfo("Time Complexity", f"Time complexity result: {time_result}")
    else:
        messagebox.showerror("Error", f"Failed to determine time complexity.\n{time_result}")

def show_results():
    result_window = tk.Toplevel(root)
    result_window.title("Results")
    result_text = scrolledtext.ScrolledText(result_window, width=60, height=10)
    result_text.pack(padx=5, pady=5)
    result_text.insert(tk.END, output_text.get("1.0", tk.END))

def toggle_theme():
    current_bg = root.cget("background")
    if current_bg == light_palette['bg']:
        root.tk_setPalette(background=dark_palette['bg'], foreground=dark_palette['fg'])
    else:
        root.tk_setPalette(background=light_palette['bg'], foreground=light_palette['fg'])

light_palette = {
    "bg": "white",
    "fg": "black",
    "button_bg": "#f0f0f0",
    "button_fg": "blue",
    "active_bg": "#dcdcdc",
    "active_fg": "black"
}

dark_palette = {
    "bg": "#1e1e1e",
    "fg": "white",
    "button_bg": "#2d2d2d",
    "button_fg": "blue",
    "active_bg": "#454545",
    "active_fg": "white"
}

root = tk.Tk()
root.title("Automated Code Checker")

root.tk_setPalette(background=light_palette['bg'], foreground=light_palette['fg'])

code_label = tk.Label(root, text="Enter code to check:", bg=light_palette['bg'], fg=light_palette['fg'])
code_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

code_text = scrolledtext.ScrolledText(root, width=60, height=10)
code_text.grid(row=1, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

check_button = tk.Button(root, text="Check Code", command=start_check, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'])
check_button.grid(row=2, column=0, padx=5, pady=5, sticky="we")

reset_button = tk.Button(root, text="Reset", command=reset_output, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'])
reset_button.grid(row=2, column=1, padx=5, pady=5, sticky="we")

output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

theme_button = tk.Button(root, text="Toggle Theme", command=toggle_theme, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'])
theme_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

google_search_button = tk.Button(root, text="Google Search", command=google_search, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'], state=tk.DISABLED)
google_search_button.grid(row=5, column=0, padx=5, pady=5, sticky="we")

youtube_search_button = tk.Button(root, text="YouTube Search", command=youtube_search, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'], state=tk.DISABLED)
youtube_search_button.grid(row=5, column=1, padx=5, pady=5, sticky="we")

time_complexity_button = tk.Button(root, text="Time Complexity", command=determine_time_complexity, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'])
time_complexity_button.grid(row=6, column=0, padx=5, pady=5, sticky="we")
"""
results_button = tk.Button(root, text="Results", command=show_results, bg=light_palette['button_bg'], fg=light_palette['button_fg'], activebackground=light_palette['active_bg'], activeforeground=light_palette['active_fg'])
results_button.grid(row=6, column=1, padx=5, pady=5, sticky="we")
"""

# Allow resizing
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
