from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# Tamaño de la ventana (solo afecta en PC para pruebas)
Window.size = (360, 640)


class Calculadora(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Fondo azul oscuro elegante uniforme
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self.actualizar_fondo, size=self.actualizar_fondo)

        # Pantalla de resultados (Ocupa el 25% superior de la pantalla)
        self.resultado = TextInput(
            text="",
            font_size=40,
            multiline=False,
            readonly=True,
            halign="right",
            size_hint=(1, 0.25),
            background_color=(0.1, 0.1, 0.18, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[10, 40, 10, 10]
        )
        self.add_widget(self.resultado)

        # Contenedor de Botones (Ocupa el 75% restante de la pantalla de forma expandida)
        grid = GridLayout(cols=4, size_hint=(1, 0.75), spacing=2, padding=2)

        # Distribución balanceada de los botones
        botones = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", ".", "%", "+",
            "0", "="
        ]

        for btn in botones:
            # El botón de '0' y '=' ocuparán más espacio en la última fila para rellenar
            if btn in ["0", "="]:
                boton = Button(
                    text=btn,
                    font_size=28,
                    on_press=self.presionar,
                    size_hint_x=2  # Expande estos botones horizontalmente
                )
            else:
                boton = Button(
                    text=btn,
                    font_size=28,
                    on_press=self.presionar
                )

            # Estilizado de colores
            if btn in ["+", "-", "*", "/", "%"]:
                boton.background_normal = ""
                boton.background_color = (0.8, 0.2, 0.2, 1)  # Operadores en rojo
            elif btn == "=":
                boton.background_normal = ""
                boton.background_color = (0.2, 0.7, 0.3, 1)  # Igual en verde
            elif btn == "C":
                boton.background_normal = ""
                boton.background_color = (0.9, 0.5, 0.1, 1)  # Borrar en naranja
            else:
                boton.background_normal = ""
                boton.background_color = (0.2, 0.2, 0.28, 1)  # Números en azul grisáceo

            grid.add_widget(boton)

        self.add_widget(grid)

    def actualizar_fondo(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def presionar(self, instancia):
        texto = instancia.text

        if self.resultado.text == "Error":
            self.resultado.text = ""

        if texto == "C":
            self.resultado.text = ""

        elif texto == "=":
            if not self.resultado.text:
                return
            try:
                expresion = self.resultado.text.replace("%", "/100")
                self.resultado.text = str(eval(expresion))
            except Exception:
                self.resultado.text = "Error"
        else:
            self.resultado.text += texto


class AppCalculadora(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Calculadora()


if __name__ == "__main__":
    AppCalculadora().run()