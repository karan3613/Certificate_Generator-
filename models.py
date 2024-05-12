from PIL import Image, ImageDraw, ImageFont


class Ceterficate:

    def __init__(self):
        self.basicfnt = ImageFont.truetype("arial.ttf", size=35)
        self.normal_text_color = "grey"
        self.width = 3500
        self.height = 2200
        self.img = Image.new(mode="RGB", size=(self.width, self.height), color="white")
        self.draw = ImageDraw.Draw(self.img)

    def ShowImage(self):
        self.img.show("ceterficate_Coursera")

    def BasicImages(self):
        courserimg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\courseraTemplate.jpg")
        self.img.paste(im=courserimg.resize((750, 1700)), box=(2300, 0))
        self.draw.rectangle(xy=[70, 70, self.width - 70, self.height - 70], width=5, fill=None,
                            outline=self.normal_text_color)
        self.draw.rectangle(xy=[0, 0, self.width, self.height], width=35, fill=None, outline=self.normal_text_color)

    def institute_selected(self, univ_name):
        basictxt = f"an online non-credit course authorized by {univ_name} and offered through\nCoursera"
        self.draw.text(xy=(400, 1300), text=basictxt, size=40, font=self.basicfnt, fill=self.normal_text_color,
                       spacing=5)
        if(univ_name == "University of Michigan"):
            univimg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_logo\\michigan.png")
            signImg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_sign\\michigan_sign.png")
            self.img.paste(im = signImg.resize((600 , 300)) , box=(400 , 1500))
            self.img.paste(im=univimg.resize((1500, 500)), box=(400, 300))

        if(univ_name == "Duke University"):
            univimg = Image.open(
                "C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_logo\\duke.png")
            signImg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_sign\\duke_sign.png")
            self.img.paste(im = signImg.resize((600 , 300)) , box=(400 , 1500))

            self.img.paste(im = univimg.resize((1000 , 500)) , box= (400 , 300))
        if (univ_name == "Yale University"):
            univimg = Image.open(
                "C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_logo\\yale.jpg")
            signImg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_sign\\yale_sign.jpg")
            self.img.paste(im = signImg.resize((600 , 300)) , box=(400 , 1500))
            self.img.paste(im=univimg.resize((900, 400)), box=(400, 300))
        if (univ_name == "Google"):
            univimg = Image.open(
                "C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_logo\\google.jpg")
            signImg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_sign\\google_sign.jpg")
            self.img.paste(im = signImg.resize((600 , 300)) , box=(400 , 1500))

            self.img.paste(im=univimg.resize((1500, 500)), box=(400, 300))
        if (univ_name == "Coursera"):
            univimg = Image.open(
                "C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_logo\\coursera.jpg")
            signImg = Image.open("C:\\Users\\karan\\PycharmProjects\\CourseraCeterficateGenerator\\institute_sign\\coursera_sign.jpg")
            self.img.paste(im = signImg.resize((600 , 300)) , box=(400 , 1500))

            self.img.paste(im=univimg.resize((1300, 500)), box=(400, 300))








    def BasicText(self):
        verify_course_text = "Verify at coursera.org/verify/N6DEUQV6FRRX"
        confiramtion_txt1 = "Coursera has confirmed the identity of this individual and their"
        confiramtion_txt2 = "participation in their course"

        self.draw.text(xy=(2200, 1900), text=verify_course_text, size=40, font=self.basicfnt,
                       fill=self.normal_text_color,
                       stroke_width=1)
        self.draw.text(xy=(2200, 1950), text=confiramtion_txt1, size=40, font=self.basicfnt,
                       fill=self.normal_text_color)
        self.draw.text(xy=(2200, 2000), text=confiramtion_txt2, align="right", size=40, font=self.basicfnt,
                       fill=self.normal_text_color)
        self.draw.text(xy=(400, 1100), text="has successfully completed", size=40, font=self.basicfnt,
                       fill=self.normal_text_color, spacing=5)

    def Name(self, name_of_user):
        name = name_of_user
        namefnt = ImageFont.truetype("lucon.ttf", size=100)
        self.draw.text(xy=(400, 950), text=name, size=40, font=namefnt, fill="black", stroke_width=2, spacing=5)

    def Course(self, course_of_user):
        course = course_of_user
        coursefnt = ImageFont.truetype("arial.ttf", size=60)
        self.draw.text(xy=(400, 1200), text=course, size=40, font=coursefnt, fill="black", stroke_width=1, spacing=4)

    def Date(self, date_of_user):
        date = date_of_user
        self.draw.text(xy=(400, 850), text=date, size=40, font=self.basicfnt, fill=self.normal_text_color)

    def Professor(self, univ_name):


        if univ_name == "University of Michigan":
            professor = "Charles Severance\nClinical Professor,School of Information\nUniversity of Michigan"
            self.draw.text(xy=(400, 1850), text=professor, size=40, font=self.basicfnt, fill=self.normal_text_color,
                           spacing=5)
        if univ_name == "Coursera":
            professor = "Betty Vandenbosch\n Chief Content Officer"
            self.draw.text(xy=(400, 1850), text=professor, size=40, font=self.basicfnt, fill=self.normal_text_color,
                           spacing=5)
        if univ_name == "Duke University":
            professor = "Genevieve M. Lipp\nDavid Carlson\nLawrence Carin"
            self.draw.text(xy=(400, 1850), text=professor, size=40, font=self.basicfnt, fill=self.normal_text_color,
                           spacing=5)
        if univ_name == "Google":
            professor = "Google"
            self.draw.text(xy=(400, 1850), text=professor, size=40, font=self.basicfnt, fill=self.normal_text_color,
                           spacing=5)
        if univ_name == "Yale University":
            professor = "Paul Bloom\nBrooks and Suzanne Ragen Professor of Psychology\nYale University"
            self.draw.text(xy=(400, 1850), text=professor, size=40, font=self.basicfnt, fill=self.normal_text_color,
                           spacing=5)


