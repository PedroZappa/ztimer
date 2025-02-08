"""
A Stopwatch App.
"""

from textual.app import App, ComposeResult
from textual.widgets import Digits


class StopwatchApp(App):
    CSS = """
    Screen { align: center middle; }
    Digits { width: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Digits("")

    def on_ready(self) -> None:
        self.seconds = 0
        self.update_stopwatch()
        self.set_interval(1, self.update_stopwatch)

    def update_stopwatch(self) -> None:
        hrs = self.seconds // 3600
        mins = (self.seconds % 3600) // 60
        secs = self.seconds % 60
        self.query_one(Digits).update(f"{hrs:02}:{mins:02}:{secs:02}")
        self.seconds += 1


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()

