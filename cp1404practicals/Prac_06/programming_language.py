

class ProgrammingLanguage:

    def  __init__(self):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, reflection ={}, First appeared in {}".format(self.name, self.reflection, self.typing, self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"


    def run_tests():
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        visual_basic = ProgrammingLanguage("Visual_basic", "Static", False, 1991)
        cplusplus = ProgrammingLanguage("C++", "static", False, 1983)


        languages = [ruby, python, visual_basic, cplusplus]
        print(python)

        print ("Dynamically typed languages include")
        for language in languages:
            if language.is_dynamic():
                print(language.name)

    if __name__=="__main__":
        run_tests()


