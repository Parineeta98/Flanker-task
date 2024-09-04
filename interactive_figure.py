# Author: Teun Mathijssen
# https://github.com/teuncm
#
# This file provides functions to create and interact with a Matplotlib figure.
# The figure registers mouse presses, keyboard input and the location of the mouse.
# The interactive figure requires system focus to work, and therefore it must
# be the only active figure at all times.

import matplotlib.pyplot as plt

# The identifier of the interactive figure.
_FIGURE_ID = 0


# PRESS STATE VARIABLES: press information is stored in the variables below.


# After any key press or mouse click:
# - this variable contains the last key that
#   was pressed.
last_keypress = None
# - this variable contains the last mouse button
#   that was pressed.
last_mousepress = None
# - these variables contain the last mouse coordinates.
last_mouse_x = None
last_mouse_y = None


# INTERACTIVE METHODS: use the methods below if you need to control the figure.


def create(hide_toolbar=False, **kwargs):
    """Create the interactive figure. Optionally hide the toolbar.
    Remaining arguments will be passed to the figure on creation.

    Returns:
    - A reference to the interactive figure.

    Raises:
    - RuntimeError if two interactive figures are created."""
    if not _exists():
        if hide_toolbar:
            plt.rcParams["toolbar"] = "None"

        # Create figure and assign a specific identifier.
        fig = plt.figure(num=_FIGURE_ID, figsize=(6, 6), **kwargs)
        fig.canvas.manager.set_window_title("Interactive Figure")
        # Create drawable axis.
        plt.gca()

        # Show figure but allow the main thread to continue.
        plt.show(block=False)

        # Reset plot state and draw to obtain focus.
        clear()
        _reset_press()
        draw()

        # Add our custom event handlers. For handlers, see:
        # https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.mpl_connect
        # For general interaction handling, see:
        # https://matplotlib.org/stable/users/explain/figure/interactive_guide.html
        # For mouse buttons, see:
        # https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.MouseButton
        fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
        fig.canvas.mpl_disconnect(fig.canvas.manager.button_press_handler_id)
        fig.canvas.mpl_connect("key_press_event", _key_press_handler)
        fig.canvas.mpl_connect("button_press_event", _button_press_handler)

        print("Successfully created interactive figure.")

        return fig
    else:
        raise RuntimeError("Error: you cannot create multiple interactive figures.")


def fullscreen():
    """Make the interactive figure fullscreen."""
    _check_focus()

    plt.get_current_fig_manager().full_screen_toggle()


def clear():
    """Reset the contents and layout of the interactive figure."""
    _check_focus()

    ax = plt.gca()

    ax.clear()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([35, 65])
    ax.set_ylim([49, 51]) # the limits are changed to fit our program's setting


def wait(interval):
    """Timeout for the given number of seconds. During this period it is
    not possible to interact with the figure."""
    _check_focus()

    # Draw now for consistent behavior across OSes.
    draw()

    plt.pause(interval)
    _reset_press()


def wait_for_interaction(interval=-1):
    """Wait for interaction with the interactive figure. Optionally
    use a timeout interval in seconds.

    Returns:
    - True if a key was pressed.
    - False if a mouse button was pressed.
    - None if no input was given within the time interval.
    """
    _check_focus()

    # Draw now for consistent behavior across OSes.
    draw()

    interaction_type = plt.waitforbuttonpress(interval)
    if interaction_type is None:
        # No button was pressed.
        _reset_press()

    return interaction_type


def draw():
    """Draw the figure. Only draw if the figure was changed since the
    last time it was drawn."""
    _check_focus()

    canvas = plt.gcf().canvas
    # Only draw if objects changed.
    canvas.draw_idle()
    # Force update the figure window.
    canvas.flush_events()


def close():
    """Close the interactive figure."""
    _check_focus()

    plt.close()
    print("Successfully closed interactive figure.")


# HIDDEN METHODS: you shouldn't use the methods below.


def _exists():
    """Check whether the interactive figure exists.

    Returns:
    - True if the figure exists.
    - False if the figure does not exist."""
    return plt.fignum_exists(_FIGURE_ID)


def _check_focus():
    """Check focus of the interactive figure.

    Raises:
    - RuntimeError if the figure is not in focus."""
    if not _exists():
        raise RuntimeError("Error: the interactive figure is not available.")
    elif len(plt.get_fignums()) > 1:
        raise RuntimeError("Error: the interactive figure must be the only figure.")


def _reset_press():
    """Reset the last registered press information."""
    global last_keypress, last_mousepress, last_mouse_x, last_mouse_y

    last_keypress = None
    last_mousepress = None
    last_mouse_x = None
    last_mouse_y = None


def _key_press_handler(event):
    """Register key and mouse coordinates on press."""
    global last_keypress, last_mousepress, last_mouse_x, last_mouse_y

    last_keypress = event.key
    last_mousepress = None
    last_mouse_x = event.xdata
    last_mouse_y = event.ydata


def _button_press_handler(event):
    """Register key, mouse button and mouse coordinates on press."""
    global last_keypress, last_mousepress, last_mouse_x, last_mouse_y

    last_keypress = event.key
    last_mousepress = event.button.value
    last_mouse_x = event.xdata
    last_mouse_y = event.ydata


def _print_press_info():
    """Debug print all press info."""
    print("Current press state info:")
    print("Last keypress:", last_keypress)
    print("Last mousepress:", last_mousepress)
    print("Last mouse x:", last_mouse_x)
    print("Last mouse y:", last_mouse_y)
