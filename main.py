class datagen :
    """
    A class used to generate random data for a table.

    ...

    Attributes
    ----------
    headings : list
        a list of strings representing the column headings of the table
    data : list
        a list of lists representing the data in the table
    last_id : str
        a string representing the last generated ID

    Methods
    -------
    tablehead(n: int = 5)
        generates a list of n random column headings from the headings attribute
    generate_data(no_of_rows: int = 10)
        generates no_of_rows rows of random data for the table
    generate_random_dob(start_date: str, end_date: str)
        generates a random date of birth between start_date and end_date
    randphonegen(n: int)
        generates a random phone number of n digits
    IDgen(No_of_letters: int, randomstate: bool = False, const_char: str = "E")
        generates a random ID of No_of_letters length, with an optional constant character and random state
    random_name_gen(split_names: bool = True)
        generates a random name, with an optional flag to split the name into first and last names
    generate_institute_name()
        generates a random institute name
    agegen()
        generates a random age between 18 and 45
    """
    def __init__(self) -> None:
        self.headings = ["ID" , "Phone-no" ,"DOB" , "Sports" , "hobbies" , "age" ,  "college","name" ]
        self.data = []
        self.tablehead()
        self.last_id = None
        
    
    #n is no of fields in the table
    def tablehead(self ,n : int = 5):
        """
        Generates a list of n random column headings from the headings attribute.

        Parameters
        ----------
        n : int, optional
            the number of column headings to generate (default is 5)

        Returns
        -------
        list
            a list of n random column headings from the headings attribute
        """
        import random
        temp = []
        # n is the no of table heading its gonna have 
        random_numbers = random.sample(range(0, 7), n)

        for i in random_numbers: 
            temp.append(self.headings[i])

        self.data.append(temp)
        
    def generate_data(self,no_of_rows:int = 10):
        """
        Generates no_of_rows rows of random data for the table.

        Parameters
        ----------
        no_of_rows : int, optional
            the number of rows to generate (default is 10)

        Returns
        -------
        list
            a list of lists representing the data in the table
        """
        import data
        import random
        while no_of_rows > 0:
            temp = []
            for i in self.data[0]:
                if i == "ID":
                    temp.append(self.IDgen(5))
                elif i == "Phone-no":
                    temp.append(self.randphonegen(10))
                elif i == "DOB":
                    temp.append(self.generate_random_dob("2000-01-01", "2016-12-31"))
                elif i == "Sports":
                    temp.append(data.sports_list[random.randrange(0,len(data.sports_list))])
                elif i == "hobbies":
                    temp.append(data.hobbies_list[random.randrange(0,len(data.hobbies_list))])
                elif i == "age":
                    temp.append(self.agegen())
                elif i == "college":
                    temp.append(self.generate_institute_name())
                elif i == "name":
                    temp.append(self.random_name_gen())
            no_of_rows-=1
            self.data.append(temp)
                
        return self.data

    def generate_random_dob(self, start_date, end_date):
        """
        Generates a random date of birth between start_date and end_date.

        Parameters
        ----------
        start_date : str
            the start date in the format "YYYY-MM-DD"
        end_date : str
            the end date in the format "YYYY-MM-DD"

        Returns
        -------
        str
            a random date of birth between start_date and end_date in the format "YYYY-MM-DD"
        """
        import random
        from datetime import datetime, timedelta


        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        random_days = random.randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)
        return random_date.strftime("%Y-%m-%d")

    def randphonegen(self,n):
        """
        Generates a random phone number of n digits.

        Parameters
        ----------
        n : int
            the number of digits in the phone number

        Returns
        -------
        str
            a random phone number of n digits
        """
        india_phone = "+91"
        import random 
        for i in range(n):
            if i ==0:
                india_phone+=str(random.randrange(1, 10))
            india_phone+=str(random.randrange(0,10))
        return india_phone

    def IDgen(self,No_of_letters:int,randomstate:bool=False,const_char:str= "E"):
        """
        Generates a random ID of No_of_letters length, with an optional constant character and random state.

        Parameters
        ----------
        No_of_letters : int
            the length of the ID
        randomstate : bool, optional
            a flag indicating whether the ID should be totally random (default is False)
        const_char : str, optional
            a constant character to include in the ID (default is "E")

        Returns
        -------
        str
            a random ID of No_of_letters length, with an optional constant character and random state
        """
        import random
        import string 
        id = []
        
        const_id = []
        alphabets = list(string.ascii_letters)
        if randomstate == True:
            for i in range(No_of_letters):
                id.append(random.choice(alphabets))
            return "".join(id)
        if randomstate == False :
            if self.last_id != None:
                temp_id = int("1" + self.last_id[1:])
                self.last_id = const_char + str(temp_id+1)[1:]
                return self.last_id

                
                
                pass
            else:
                pass
            for i in range(No_of_letters-1):
                if i < No_of_letters -2:
                    const_id.append('0')
                else:
                    const_id.append('1')
            #print(f"-------{const_id}-----------")
            self.last_id =const_char+  "".join(const_id)
            
            return self.last_id

    def random_name_gen(self,split_names:bool = True):
        """
        Generates a random name, with an optional flag to split the name into first and last names.

        Parameters
        ----------
        split_names : bool, optional
            a flag indicating whether to split the name into first and last names (default is True)

        Returns
        -------
        str or list
            a random name, with an optional flag to split the name into first and last names
        """
        import data
        import random
        if split_names == True:
            first_names = data.indian_student_first_names
            last_names = data.indian_student_last_names
            names = [random.choice(first_names),random.choice(last_names)]
            return names
        first_names = data.indian_student_first_names
      #  print(first_names)
        last_names = data.indian_student_last_names
        name = random.choice(first_names) + " " + random.choice(last_names)

        return name
    
    def generate_institute_name(self):
        """
        Generates a random institute name.

        Returns
        -------
        str
            a random institute name
        """
        import random
        import data
        prefixes = data.prefixes
        nouns = data.nouns
        adjectives = data.adjectives
        prefix = random.choice(prefixes)
        noun = random.choice(nouns)
        adjective = random.choice(adjectives)
        
        # Randomly select the order of words
        order = random.choice(["prefix-noun", "noun-prefix", "adjective-noun", "noun-adjective"])
        
        if order == "prefix-noun":
            name = f"{prefix} {noun}"
        elif order == "noun-prefix":
            name = f"{noun} {prefix}"
        elif order == "adjective-noun":
            name = f"{adjective} {noun} college"
        elif order == "noun-adjective":
            name = f"{noun} {adjective} college"
    
        return name

    def agegen(self):
        """
        Generates a random age between 18 and 45.

        Returns
        -------
        int
            a random age between 18 and 45
        """
        import random
        age = random.randrange(18, 45)
        return age
    
# obj = datagen()
# print(obj.generate_data())
