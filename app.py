"""
zTimer - A Stopwatch App.

This application is a simple stopwatch that displays the elapsed time in hours, minutes, and seconds.
It uses the Textual library to create a text-based user interface.
"""

from textual.app import App, ComposeResult
from textual.widgets import Digits


class zTimer(App):
  """
  A simple stopwatch application using the Textual library.
  """

  CSS = """
    Screen { align: center middle; }
    Digits { 
      width: auto;
      color: green;
    }
    """

  def compose(self) -> ComposeResult:
    """
    Compose the UI elements of the application.

    Yields:
        Digits: A widget to display the elapsed time.
    """
    yield Digits("")

  def on_ready(self) -> None:
    """
    Initialize the stopwatch and start the update interval.

    This method is called when the application is ready.
    It initializes the seconds counter and sets up a recurring
    interval to update the stopwatch display every second.
    """
    self.seconds = 0
    self.update_stopwatch()
    self.set_interval(1, self.update_stopwatch)

  def update_stopwatch(self) -> None:
    """
    Update the stopwatch display with the elapsed time.

    This method calculates the hours, minutes, and seconds
    from the total elapsed seconds and updates the Digits
    widget with the formatted time. It also increments the
    seconds counter by one.
    """
    hrs = self.seconds // 3600
    mins = (self.seconds % 3600) // 60
    secs = self.seconds % 60
    # Update the Digits widget with the formatted time
    self.query_one(Digits).update(f"{hrs:02}:{mins:02}:{secs:02}")
    self.seconds += 1


if __name__ == "__main__":
  # Create an instance of the zTimer and run it
  app = zTimer()
  app.run()
