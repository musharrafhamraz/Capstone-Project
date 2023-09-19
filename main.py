from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.uix.camera import Camera
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomsheet import MDBottomSheet
import helper
# from PIL import Image as PILImage
# import numpy as np
# from keras.preprocessing.image import load_img, img_to_array

# model  = ""
print(kivymd. __version__)

class DemoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        screen = Screen()
        self.label = MDLabel(text = "Identity Please!!", font_style="H5", theme_text_color="Custom", text_color = (1,1,1,1), pos_hint= {'center_x': 0.5,'center_y': 0.9}, halign="center")
        self.label1 = MDLabel(text = "Help Vegetables to grow healthy", font_style="Body1", theme_text_color="Custom", text_color = (1,1,1,1), pos_hint= {'center_x': 0.5,'center_y': 0.2}, halign="center")

        # self.icon1 = MDIcon(icon="login-variant", pos_hint= {'center_x': 0.5,'center_y': 0.8}, size_hint= (0.5, 0.5))
        self.username = Builder.load_string(helper.username_input)
        self.password = Builder.load_string(helper.password_input)
        button = MDFloatingActionButton(icon='login',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        
        screen.add_widget(self.label)
        screen.add_widget(self.label1)
        screen.add_widget(self.username)
        screen.add_widget(self.password)
        # screen.add_widget(self.camera)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text != "":
            user_error = self.username.text + " user does not exist."
        else:
            user_error = "Please enter a username"
        self.dialog = MDDialog(title='Username check',
                               text=user_error, size_hint=(0.8, 1),
                               buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                                        MDFlatButton(text='More')]
                               )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog

class HomePage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        screen = Screen()
        
        layout = MDBoxLayout(orientation='vertical')
        
        # Create an MDCamera widget
        self.camera = Camera(play=True, resolution=(640, 600))
        
        # Create a floating action button for camera
        self.btn = MDFloatingActionButton(
            icon="camera",
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            on_release=self.capture_image  # Define a function to capture the image
        )
        
        # Add camera and button to the layout
        layout.add_widget(self.camera)
        layout.add_widget(self.btn)
        
        # Add the layout to the screen
        screen.add_widget(layout)
        
        return screen

# Captures the image from the camera and convert it to the form that our model can process.

    # def capture(self, obj):
    #     img_texture = self.camera.texture
    
    #     if img_texture:
    #         pil_image = PILImage.frombytes('RGBA', img_texture.size, img_texture.pixels)
    #         pil_image = pil_image.convert('RGB')
    #         pil_image = pil_image.resize((224, 224))  # Resize the image to the desired input size
    #         image_array = img_to_array(pil_image)
    #         image_array = image_array / 255.0
    #         # image_array = np.expand_dims(image_array, axis=0)
    #         # prediction = model.predict(image_array)

    #         prediction = model.predict(np.expand_dims(image_array, axis=0))
    #         predicted_class = np.argmax(prediction, axis=1)

    #         class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    #         predicted_class_name = class_names[predicted_class[0]]

    #         self.label.text = f"Prediction: {predicted_class_name}"







if __name__ == "__main__":
    HomePage().run()
