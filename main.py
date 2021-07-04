###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################
# Importing Libraries
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

# Import image.kv file
Builder.load_file("image.kv")

# Create a class
class MyLayout(Widget):
    pass


# Create main app class 
class MyApp(App):
    # Set background color to White
    Window.clearcolor = (1, 1, 1, 1)
    def build(self):
        return MyLayout()


# Run App
if __name__ == "__main__":
    MyApp().run()   
########################### END ###########################
