from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from styles import Styles
from libs.formulas import Formulas


Builder.load_string("""
                    
#: import CLabel CustomWidgets
#: import TextParameter CustomWidgets
#: import TitleLabel CustomWidgets
#: import CTextInput CustomWidgets 
                    
<GraphicPage>:
    name: "graphicPage"
    BoxLayout:
        orientation: "vertical"
        # Parte superiore
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            size_hint_y: None
            height: dp(60)
            Label:
                text: "Queue System M/M/Y/Y Graphic"
                font_name: "DMSans.ttf"
                font_size: "20sp"
            AnchorLayout:
                anchor_x: "right"
                padding: [0,0,dp(30),0]
                Button:
                    canvas.before:
                        Rectangle:
                            pos: self.pos
                            size: self.size
                            source: "back.png"
                    size_hint: None, None
                    size: dp(35), dp(35)
                    background_normal: ""
                    background_color: 0,0,0,0
                    on_press: root.goToData()
        
        # Dati + grafico
        BoxLayout:
            canvas.before:
                Color:
                    rgba: root.bg_color
                Rectangle:
                    pos: self.pos
                    size: self.size
            # Sinistra -> Dati
            BoxLayout:
                orientation: "vertical"
                # input
                BoxLayout:
                    orientation: "vertical"
                    CLabel:
                        text: "Input"
                    BoxLayout:
                        padding: [dp(20), dp(20)]
                        CTextInput:
                            id: arrival
                            hint_text: "lambda"
                        CTextInput:
                            id: mu
                            hint_text: "mu"
                        CTextInput:
                            id: y
                            hint_text: "y"
                        CTextInput:
                            id: state
                            hint_text: "K"
                    BoxLayout:
                        padding: [dp(20), dp(20)]
                        Button:
                            id: start
                            text: "Start"
                            size_hint_y: None
                            height: dp(50)
                            on_press: root.inputStart()
                        Button:
                            id: reset
                            text: "Reset"
                            size_hint_y: None
                            height: dp(50)
                # output
                BoxLayout:
                    orientation: "vertical"
                    BoxLayout:
                        CLabel:
                            text: "Output"
                    # Pk
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Pk: "
                        TextParameter:
                            id: Pk
                    # Py
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Py: "
                        TextParameter:
                            id: Py
                    # Ls
                    BoxLayout:
                        size_hint_x: None
                        TitleLabel:
                            text: "Ls: "
                        TextParameter:
                            id: Ls
                    # Ws
                    BoxLayout:
                        size_hint_x: None
                        width: self.minimum_width
                        TitleLabel:
                            text: "Ws: "
                        TextParameter:
                            id: Ws
            
            # Destra -> Grafico
            AnchorLayout:
                anchor_x: "right"
                #padding: [0,0,dp(30),0]
                canvas.before:
                    #Color:
                    #    rgba: root.bg_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "img/testGraph.jpg"
            
""")

class GraphicPage(Screen):
    bg_color = Styles.primary_color
    secondary_color = Styles.secondary_color
    text_color_1 = Styles.light_1_color

    def inputStart(self):
        formulas = Formulas(0,0,0,0)
        formulas.arrivalRate = float(self.ids.arrival.text)
        formulas.serviceRate = float(self.ids.mu.text)
        formulas.Y = int(self.ids.y.text)
        formulas.state = int(self.ids.state.text)




        self.ids.Pk.text = str(Formulas.getProbabilityAtState(formulas, formulas.state))
        self.ids.Py.text = str(Formulas.getProbabilityAtStateY(formulas))
        self.ids.Ls.text = str(Formulas.getServerLength(formulas))
        self.ids.Ws.text = str(Formulas.getServerWait(formulas))  


    def goToData(self):
        self.manager.current = "dataPage"
