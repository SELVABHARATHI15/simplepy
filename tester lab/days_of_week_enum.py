from enum import Enum

# Creating an enum class for days of the week
class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# Examples of using the enum
def main():
    # Accessing enum members
    print(f"First day is: {DaysOfWeek.MONDAY}")
    print(f"First day name: {DaysOfWeek.MONDAY.name}")
    print(f"First day value: {DaysOfWeek.MONDAY.value}")
    
    # Iterating through enum members
    print("\nAll days of the week:")
    for day in DaysOfWeek:
        print(f"{day.name} = {day.value}")
    
    # Checking if a day is a weekend
    def is_weekend(day):
        return day in (DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY)
    
    # Testing the weekend function
    day = DaysOfWeek.SATURDAY
    print(f"\nIs {day.name} a weekend? {is_weekend(day)}")
    day = DaysOfWeek.MONDAY
    print(f"Is {day.name} a weekend? {is_weekend(day)}")

if __name__ == "__main__":
    main()