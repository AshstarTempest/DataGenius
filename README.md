# DataGen

`datagen` is a Python class designed to generate random data for a table. This class provides methods to create random column headings and populate rows with corresponding random data. The generated data includes various fields such as ID, phone number, date of birth, sports, hobbies, age, college, and name.

## Class Attributes

- `headings`: A list of strings representing the column headings of the table.
- `data`: A list of lists representing the data in the table.
- `last_id`: A string representing the last generated ID.

## Methods

### `__init__(self) -> None`

Constructor method to initialize the class attributes.

### `tablehead(n: int = 5) -> list`

Generates a list of `n` random column headings from the `headings` attribute.

### `generate_data(no_of_rows: int = 10) -> list`

Generates `no_of_rows` rows of random data for the table.

### `generate_random_dob(start_date: str, end_date: str) -> str`

Generates a random date of birth between `start_date` and `end_date`.

### `randphonegen(n: int) -> str`

Generates a random phone number of `n` digits.

### `IDgen(No_of_letters: int, randomstate: bool = False, const_char: str = "E") -> str`

Generates a random ID of length `No_of_letters`, with an optional constant character and random state.

### `random_name_gen(split_names: bool = True) -> str or list`

Generates a random name, with an optional flag to split the name into first and last names.

### `generate_institute_name() -> str`

Generates a random institute name.

### `agegen() -> int`

Generates a random age between 18 and 45.

### `generate_random_dob(start_date: str, end_date: str) -> str`

Generates a random date of birth between `start_date` and `end_date`.

## Dependencies

- The class depends on external data provided in the `data` module.

## Example

```python
# Import the datagen class
from your_module import datagen

# Instantiate the class
obj = datagen()

# Generate random data
data = obj.generate_data(no_of_rows=10)

# Display the generated data
print(data)
