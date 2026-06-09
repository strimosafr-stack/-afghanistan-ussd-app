from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform

KV = '''
MDBoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "کدهای USSD افغانستان"
        anchor_title: "center"
        elevation: 4
        md_bg_color: 0.1, 0.1, 0.1, 1

    MDTabs:
        id: android_tabs
        background_color: 0.15, 0.15, 0.15, 1
        indicator_color: 1, 0.84, 0, 1

<TabContent>:
    MDScrollView:
        MDBoxLayout:
            orientation: 'vertical'
            padding: "24dp"
            spacing: "16dp"
            adaptive_height: True

            MDLabel:
                text: root.operator_title
                font_style: "H6"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 0.84, 0, 1
                bold: True

            MDFillRoundFlatButton:
                text: "📱 بررسی بیلانس (اعتبار)"
                font_size: "16sp"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.9
                md_bg_color: 0.2, 0.2, 0.2, 1
                on_release: app.dial_ussd(root.operator_key, "balance")

            MDFillRoundFlatButton:
                text: "🌐 بسته اینترنت ۱ جی‌بی"
                font_size: "16sp"
                pos_hint: {"center_x": .5}
                size_hint_x: 0.9
