from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Tamaño de la ventana
Window.size = (300, 500)


class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Fondo azul
        with self.canvas.before:
            Color(0, 0, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.actualizar_fondo, size=self.actualizar_fondo)

        # Pantalla
        self.resultado = TextInput(
            text="",
            font_size=32,
            multiline=False,
            readonly=True,
            halign="right",
            size_hint=(1, 0.2)
        )
        self.add_widget(self.resultado)

        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "%", "+"],
            ["C", "", "", "="]
        ]

        grid = GridLayout(cols=4)

        for fila in botones:
            for btn in fila:

                if btn == "":
                    grid.add_widget(Button(text="", disabled=True))
                    continue

                boton = Button(
                    text=btn,
                    font_size=24,
                    on_press=self.presionar
                )

                # Botones de operaciones en rojo
                if btn in ["+", "-", "*", "/", "%"]:
                    boton.background_normal = ""
                    boton.background_color = (1, 0, 0, 1)

                # Botón igual en verde
                elif btn == "=":
                    boton.background_normal = ""
                    boton.background_color = (0, 1, 0, 1)

                # Botón borrar en naranja
                elif btn == "C":
                    boton.background_normal = ""
                    boton.background_color = (1, 0.5, 0, 1)

                grid.add_widget(boton)

        self.add_widget(grid)

    def actualizar_fondo(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def presionar(self, instancia):
        texto = instancia.text

        if texto == "C":
            self.resultado.text = ""

        elif texto == "=":
            try:
                expresion = self.resultado.text.replace("%", "/100")
                self.resultado.text = str(eval(expresion))
            except:
                self.resultado.text = "Error"

        else:
            self.resultado.text += texto


class AppCalculadora(App):
    def build(self):
        return Calculadora()
        
AppCalculadora().run()
