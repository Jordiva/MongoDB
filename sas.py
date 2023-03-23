import calendar
import tkinter as tk

def highlight_day(year, month, day):
    root = tk.Tk()
    root.title("Calendar")

    cal = calendar.monthcalendar(year, month)

    def on_day_clicked(selected_day):
        selected_date = f"{year}-{month:02d}-{selected_day:02d}"
        date_label.config(text=selected_date)

    for week_idx, week in enumerate(cal):
        for day_idx, d in enumerate(week):
            if d == day:
                label = tk.Label(root, text=d, bg="yellow")
            else:
                label = tk.Label(root, text=d)
            label.grid(row=week_idx+1, column=day_idx, padx=5, pady=5)
            label.bind("<Button-1>", lambda event, day=d: on_day_clicked(day))

    date_label = tk.Label(root, text="")
    date_label.pack(pady=10)

    root.mainloop()

# Example usage
highlight_day(2023, 3, 15) # highlights March 15, 2023 and allows user to select a day
