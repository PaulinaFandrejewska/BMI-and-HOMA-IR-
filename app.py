from shiny import App, render, ui, reactive

app_ui = ui.page_fluid(

    ui.navset_pill(
        
        ui.nav_panel("BMI",

            ui.layout_columns(
                ui.card(

                    ui.card_header("Personal data"),

                    ui.input_numeric(
                        id="numeric", 
                        label="Your weight (in kg)", 
                        value = 0,
                        min=1,
                        max=250), 

                    ui.input_numeric(
                        id="numeric2", 
                        label="Your height (in cm)", 
                        value = 0, 
                        min=1,
                        max=250), 

            ),


                ui.card(

                    ui.card_header("Your result"),

                    ui.output_text(id="bodymass"),  

                    ui.output_text(id="bodymass2"),              

                ),
            ),
        ),

   ui.nav_panel("HOMA-IR",

            ui.layout_columns(
                ui.card(

                    ui.card_header("Personal data"),

                    ui.input_numeric(
                        id="numeric3", 
                        label="Your glucose level (in mg/dL)", 
                        value = 0,
                        min=1,
                        max=250), 

                    ui.input_numeric(
                        id="numeric4", 
                        label="Your insulin level (in microU/mL)", 
                        value = 0, 
                        min=1,
                        max=50), 

            ),


                ui.card(

                    ui.card_header("Your result"),

                    ui.output_text(id="homa"),  

                    ui.output_text(id="homa2"),              

                ),
            ),
        ),

    ),

) 

def server(input, output, session):

    @reactive.calc
    def bmi():
        w = float(input.numeric())
        h = float(input.numeric2())

        if w == 0 or h == 0:
            return None

        return w / ((h/100) * (h/100))
    
    @output
    @render.text
    def bodymass():

        B = bmi()

        if B is None:
            return "Fill all data"
        else:
            return f"Your BMI is: {round(B, 1)}"

    @output
    @render.text
    def bodymass2():

        B = bmi()

        if B is None:
            return "Fill all data"
        
        else:
            if B < 18.5:
                return "Your BMI category is underweight."
        
            elif B <= 25:
                return "Your BMI category is healthy."

            elif B <30:
                return "Your BMI category is overweight."

            elif B <40:
                return "Your BMI category is obese."
        
            else:
                return "Your BMI category is extreme obesity."

    @reactive.calc
    def ir():
        g = float(input.numeric3())
        i = float(input.numeric4())

        if g == 0 or i == 0:
            return None

        return (g * i) / 405
    
    @output
    @render.text
    def homa():

        H = ir()

        if H is None:
            return "Fill all data"
        else:
            return f"Your HOMA-IR index is: {round(H, 1)}"

    @output
    @render.text
    def homa2():

        H = ir()

        if H is None:
            return "Fill all data"
        
        else:
            if H <= 1:
                return "Your HOMA-IR score indicates optimal insulin sensitivity."
        
            elif H < 3:
                return "Your HOMA-IR score indicates moderate insulin sensitivity."
        
            else:
                return "Your HOMA-IR score indicates significant insulin sensitivity. You should contact your doctor."

    pass


app = App(app_ui, server=server)

