import logging

DB_VERSION="1.2.0"

if __name__ == "__main__":

    # Start the Kivy app
    import kivysome
    from screens.main_screen import IPASApp

    kivysome.enable(source='5.14.0', group=kivysome.FontGroup.REGULAR, font_folder="./assets/fonts/fontsawesome")
    kivysome.enable(source='5.14.0', group=kivysome.FontGroup.REGULAR, font_folder="./assets/fonts/fontsawesome")
    
    IPASApp(db=None, warn_processor=None).run()
