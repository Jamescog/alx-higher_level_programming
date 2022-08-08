"""

This is the base class for this project

"""
import json
import csv


class Base:
    """
    This is the "base" of all other class in the project.

    Attributes:
        __nb_objects (int) : Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Manages the id attribute in all classes and keep the code DRY
        Args:
            id (int): The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of (list_dictionaries)"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A classmethod that  writes
           the JSON string representation of list_objs to a file
        Args:
            list_objs (list): List object as input to the method
        """
        file_name = str(cls.__name__) + ".json"
        with open(file_name, "w", encoding="utf-8") as wf:
            if list_objs is None:
                wf.wirte("[]")
            else:
                list_objs = [obj.to_dictionary() for obj in list_objs]
                wf.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """A staticmethod that returns the list of
           JSON string representation
           Args:
                json_string (str): A JSON str
                representation of a list of dicts.
            Returns:
                If json_string is None or empty - an empty list.
                Otherwise - the Python list represented by json_string.
            """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
            Returns an instance with all the attributes already set
        '''
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            r2 = cls(9, 7)
        elif cls.__name__ == "Square":
            r2 = cls(6)
        r2.update(**dictionary)
        return (r2)

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters for
            and instance and from that creating instances
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except Exception:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
            Opens a window and draws all the squares and rectangles
        '''
        import turtle

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
            this is my method
        '''
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as fd:
            write_this = csv.writer(fd, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

            if cls.__name__ == "Square":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

    @classmethod
    def load_from_file_csv(cls):
        '''
            this is my method
        '''
        return ([])
