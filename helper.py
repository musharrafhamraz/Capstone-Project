username_input = """
MDTextField:
    hint_text: "Email"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "gmail"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.7}
    size_hint_x:0.8
    width:300
"""
camera = """
Camera:
    pos_hint:{'top': 1}
    play=True
    resolution = (640, 480)
"""
password_input = """
MDTextField:
    hint_text: "Password"
    helper_text: "Must be 8 letters"
    helper_text_mode: "on_focus"
    icon_right: "eye"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
    size_hint_x:0.8
    width:300
"""
bottom_sheet = """
MDScreen:

    MDBoxLayout:
        orientation: "vertical"
        padding: "12dp"
        adaptive_height: True
        pos_hint: {"top": 1}

        MDSmartTile:
            id: smart_tile
            source: "https://picsum.photos/id/70/3011/2000"
            radius: 16
            box_radius: [0, 0, 16, 16]
            size_hint_y: None
            height: "240dp"
            on_release:
                bottom_sheet.open() \
                if bottom_sheet.state == "close" else \
                bottom_sheet.dismiss()

            MDLabel:
                bold: True
                color: 1, 1, 1, 1
                text:
                    "Tap to open the bottom sheet" \
                    if bottom_sheet.state == "close" else \
                    "Tap to close the bottom sheet"

    MDBottomSheet:
        id: bottom_sheet
        type: "standard"
        bg_color: "grey"
        default_opening_height: smart_tile.y - dp(12)
        size_hint_y: None
        height: root.height - (smart_tile.height + dp(24))
"""
