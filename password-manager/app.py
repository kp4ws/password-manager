from models import IndexModel, HomeModel, CreatePasswordModel, ModifyPasswordModel
from views import IndexView, HomeView, CreatePasswordView, ModifyPasswordView
from controllers import IndexController, HomeController, CreatePasswordController, ModifyPasswordController
from events import EventSystem
from root import Root
from PIL import Image, ImageTk
import traceback
import os
import tkinter as tk

def _main() -> None:
    '''
    Main entry point of the application.
    :arg no arguments required by this function
    :except no exceptions thrown by this function
    :return None
    '''
    try:
        #Root Window
        root = Root()
        #Event System
        event_system = EventSystem()

        # Icon set up

        #Make the path to icon
        icon_dir = os.path.abspath("./icon")
        icon_path = os.path.join(icon_dir, "icon.png")

        #Load the icon
        icon_image_pil = Image.open(icon_path)

        #Convert and resize to 32 px by 32 px
        icon_image_pil = icon_image_pil.resize((16, 16))

        #Convert to PhotoImage
        icon_image = ImageTk.PhotoImage(icon_image_pil)

        #Set the window icon
        root.tk.call('wm', 'iconphoto', root._w, '-default', icon_image)

        #Models
        index_model = IndexModel()
        home_model = HomeModel()
        create_password_model = CreatePasswordModel()
        modify_password_model = ModifyPasswordModel()

        #Views
        index_view = IndexView(root)
        home_view = HomeView(root)
        create_password_view = CreatePasswordView(root)
        modify_password_view = ModifyPasswordView(root)

        #Controllers
        index_controller = IndexController(index_view, index_model, event_system)
        home_controller = HomeController(home_view, home_model, event_system)
        create_password_controller = CreatePasswordController(create_password_view, create_password_model, event_system)
        modify_password_controller = ModifyPasswordController(modify_password_view, modify_password_model, event_system)

        #Initial View is the IndexView
        index_controller.show_view()
        
        #Begin the main loop of the application
        root.begin_loop()
    except Exception as e:
        print(traceback.format_exc())

if __name__ == '__main__':
    _main()